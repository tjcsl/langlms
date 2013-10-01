from flask import session, flash
from langlearn.models import Class, Assessment, AssessmentItem, StudentResponse
from langlearn.database import db_session

def create_assessment(cid, name):
    db_session.add(Assessment(cid, name))
    db_session.commit()

def create_item(aid, qtype, qtitle, mc_answers=[], mc_correct=0):
    db_session.add(AssessmentItem(aid, qtype, qtitle, mc_correct, *mc_answers))
    db_session.commit()

def student_response(itemid, answer, uid=None):
    if uid is None:
        uid = session["uid"]
    db_session.add(StudentResponse(itemid, uid, answer))
    db_session.commit()
