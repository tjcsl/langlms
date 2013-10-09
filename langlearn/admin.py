from langlearn.models import User
from langlearn.database import db_session


def set_student(uid):
    """
    Set a user as a student (acl == 0). Takes a user id as a parameter.
    """
    User.query.filter(User.uid == uid).first().acl = 0
    db_session.commit()


def set_teacher(uid):
    """
    Set a user as a teacher (acl == 0). Takes a user id as a parameter.
    """
    User.query.filter(User.uid == uid).first().acl = 1
    db_session.commit()
