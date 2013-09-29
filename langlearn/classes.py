from flask import session, flash
from langlearn.models import Class, ClassRole, User
from langlearn.database import db_session
import langlearn
import langlearn.auth

def list_user_classes(uid=None):
    if uid is None:
        uid = session["uid"]
    classes = []
    for role in ClassRole.query.filter(ClassRole.uid == uid).all():
        classes.append(
                Class.query.filter(Class.cid == role.cid).first())
    return classes

def list_class_members(cid):
    return [User.query.filter(User.uid == i.uid).first() for i in \
            ClassRole.query.filter(ClassRole.cid == cid).all()]

def add_class_member(username, cid):
    try: 
        uid = User.query.filter(User.username == username).first().uid
        db_session.add(ClassRole(cid, uid, 0))
        db_session.commit()
        flash("Success!", "success")
    except: flash("User does not exist!", "error")

def rm_class_member(username, cid):
    try:
        uid = User.query.filter(User.username == username).first().uid
        db_session.delete(ClassRole.query.filter(
            ClassRole.cid == cid, ClassRole.uid == uid).first())
        db_session.commit()
        flash("Success!", "success")
    except: flash("An error occured!", "error")

def get_user_role(cid, uid=None):
    if uid is None:
        uid = session["uid"]
    try: return ClassRole.query.filter(ClassRole.uid == uid, 
            ClassRole.cid == cid).first().role
    except: return 0

def user_in_class(cid, uid=None):
    if uid is None:
        uid = session["uid"]
    if len(ClassRole.query.filter(ClassRole.uid == uid,
        ClassRole.cid == cid).all()) > 0: return True
    return False

def user_is_teacher(cid, uid=None):
    return get_user_role(cid, uid) == 1 or langlearn.auth.get_user_acl() == 2

def create_class(name, school, uid=None):
    if uid is None:
        uid = session["uid"]
    c = Class(name, school)
    db_session.add(c)
    db_session.commit()
    teacher = ClassRole(c.cid, uid, 1)
    db_session.add(teacher)
    db_session.commit()
    return c.cid

def get_class(cid):
    return Class.query.filter(Class.cid == cid).first()

@langlearn.app.context_processor
def inject_funcs():
    return dict(user_in_class = user_in_class,
            get_user_role = get_user_role,
            user_is_teacher = user_is_teacher,
            list_user_classes = list_user_classes,
            list_class_members = list_class_members)
