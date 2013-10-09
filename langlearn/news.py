from flask import session
from langlearn.models import NewsPost
from langlearn.database import db_session
import langlearn
import langlearn.auth
import langlearn.classes


def newsposts_in_class(cid):
    """
    Get the newsposts in a specific class (given a class ID.
    """
    return NewsPost.query.filter(NewsPost.cid == cid).all()[::-1]


def can_create_newspost(cid, uid=None):
    """
    Return whether a user can post in a given class (given a cid and uid). If
    the uid is not specified, use the currently logged in user.
    """
    if uid is None:
        uid = session["uid"]
    return langlearn.classes.user_is_teacher(cid, uid)


def create_newspost(cid, title, content):
    """
    Create a newspost given a cid, title, and content.
    """
    post = NewsPost(cid, title, content)
    db_session.add(post)
    db_session.commit()


def delete_newspost(postid):
    """
    Delete a post given a post ID.
    """
    db_session.delete(NewsPost.query.filter(NewsPost.postid == postid).first())
    db_session.commit()


@langlearn.app.context_processor
def inject_funcs():
    """
    Inject functions for use in templates.
    """
    return dict(newsposts_in_class=newsposts_in_class,
                can_create_newspost=can_create_newspost)
