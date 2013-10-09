from flask import session, flash
from langlearn.models import Class, ClassRole, User
from langlearn.database import db_session
import langlearn
import langlearn.auth


def list_user_classes(uid=None):
    """
    List the classes that a user is a member of. If no user ID is given,
    defaults to the currently logged in user.
    """
    if uid is None:
        uid = session["uid"]
    classes = []
    for role in ClassRole.query.filter(ClassRole.uid == uid).all():
        classes.append(
            Class.query.filter(Class.cid == role.cid).first())
    return classes


def list_class_members(cid):
    """
    List the users in a class given a class ID.
    """
    return [User.query.filter(User.uid == i.uid).first() for i in
            ClassRole.query.filter(ClassRole.cid == cid).all()]


def add_class_member(username, cid):
    """
    Add a user to a class, given a username and a class ID.
    """
    try:
        uid = User.query.filter(User.username == username).first().uid
        db_session.add(ClassRole(cid, uid, 0))
        db_session.commit()
        flash("Success!", "success")
    except:
        flash("User does not exist!", "error")


def rm_class_member(username, cid):
    """
    Remove a user from a class, given a username and a class ID.
    """
    try:
        uid = User.query.filter(User.username == username).first().uid
        db_session.delete(ClassRole.query.filter(
            ClassRole.cid == cid, ClassRole.uid == uid).first())
        db_session.commit()
        flash("Success!", "success")
    except:
        flash("An error occured!", "error")


def get_user_role(cid, uid=None):
    """
    Get the role of a user in a class, given a class ID and a user ID. If the
    user ID is not specified, default to the currently logged in user.
    """
    if uid is None:
        uid = session["uid"]
    if langlearn.auth.get_user_acl(uid) == 2:
        return 1
    try:
        return ClassRole.query.filter(ClassRole.uid == uid,
                                      ClassRole.cid == cid).first().role
    except:
        return 0


def set_user_role(cid, uid, role):
    """
    Set the role of a user in a class given a class ID, user ID, and a role
    (0 == student, 1 == teacher).
    """
    crole = ClassRole.query.filter(ClassRole.uid == uid,
                                   ClassRole.cid == cid).first()
    crole.role = role
    db_session.commit()


def user_in_class(cid, uid=None):
    """
    Checks to see if a user is in a class given a class ID and a user ID. If
    the user ID is not specified, defaults to the currently logged-in user.
    """
    if uid is None:
        uid = session["uid"]
    if len(ClassRole.query.filter(ClassRole.uid == uid,
                                  ClassRole.cid == cid).all()) > 0:
        return True
    return False


def user_is_teacher(cid, uid=None):
    """
    shorthand for get_user_role(cid, uid) == 1
    """
    return get_user_role(cid, uid) == 1


def create_class(name, school, uid=None):
    """
    Create a class given a name, a school, and a UID (to set as teacher). If
    the user ID is not specified, default to the current user.
    """
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
    """
    Get the class object with a given class ID.
    """
    return Class.query.filter(Class.cid == cid).first()


@langlearn.app.context_processor
def inject_funcs():
    """
    Inject functions for templates to use.
    """
    return dict(user_in_class=user_in_class,
                get_user_role=get_user_role,
                user_is_teacher=user_is_teacher,
                list_user_classes=list_user_classes,
                get_class=get_class,
                list_class_members=list_class_members,
                enumerate=enumerate  # You don't see this.
                )
