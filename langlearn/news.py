from flask import session, flash
from langlearn.models import ClassRole, Class, User, NewsPost
from langlearn.database import db_session
import langlearn
import langlearn.auth
import langlearn.classes

def newsposts_in_class(cid):
    return NewsPost.query.filter(NewsPost.cid == cid).all()[::-1]

def can_create_newspost(cid, uid=None):
    if uid is None:
        uid = session["uid"]
    return langlearn.classes.user_is_teacher(cid, uid)

def create_newspost(cid, title, content):
    post = NewsPost(cid, title, content)
    db_session.add(post)
    db_session.commit()

def delete_newspost(postid):
    db_session.delete(NewsPost.query.filter(NewsPost.postid == postid).first())
    db_session.commit()

@langlearn.app.context_processor
def inject_funcs():
    return dict(newsposts_in_class = newsposts_in_class,
            can_create_newspost = can_create_newspost)
