from flask import session
from langlearn.models import Assessment, AssessmentItem, StudentResponse
from langlearn.database import db_session


def create_assessment(cid, name):
    """
    Create an assessment. Takes a class ID to assosciate the assessment with,
    as well as a name for the assessment.
    """
    db_session.add(Assessment(cid, name))
    db_session.commit()


def create_item(aid, qtitle, qtype=1, mc_answers=[], mc_correct=0):
    """
    Create an item within an assessment. Takes an assessment ID to assosciate
    the item with, a title/description for the question, a question type (0 ==
    multiple choice, 1 == writing), and, iff this is multiple choice, a list
    of answers and an index of the correct answer.
    """
    db_session.add(AssessmentItem(aid, qtype, qtitle, mc_correct, *mc_answers))
    db_session.commit()


def student_response(itemid, answer, uid=None):
    """
    Record a student response. Takes an item ID, the answer (an index for
    multiple choice, or a string for a writing response) and a user ID. If
    no user ID is specified, the default is the currently logged in user.
    """
    if uid is None:
        uid = session["uid"]
    db_session.add(StudentResponse(itemid, uid, answer))
    db_session.commit()


def get_available_assessments(cid):
    """
    Return a list of the available assessments in a class. Takes a class ID.
    """
    return Assessment.query.filter(Assessment.cid == cid).all()


def get_assessment(aid):
    """
    Return an Assessment object given an assessment ID.
    """
    return Assessment.query.filter(Assessment.aid == aid).first()
