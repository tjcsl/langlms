import langlearn
import langlearn.auth
from langlearn.models import User
from langlearn.database import db_session


def set_student(uid):
    User.query.filter(User.uid == uid).first().acl = 0
    db_session.commit()

def set_teacher(uid):
    User.query.filter(User.uid == uid).first().acl = 1
    db_session.commit()

