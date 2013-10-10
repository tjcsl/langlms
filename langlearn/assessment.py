from flask import session
import langlearn
from langlearn.models import Assessment, AssessmentItem, StudentResponse
from langlearn.database import db_session


def create_assessment(cid, name):
    """
    Create an assessment. Takes a class ID to assosciate the assessment with,
    as well as a name for the assessment.
    """
    a = Assessment(cid, name)
    db_session.add(a)
    db_session.commit()
    return a.aid


def create_item(aid, qtitle, qtype=1, mc_answers=[], mc_correct=0):
    """
    Create an item within an assessment. Takes an assessment ID to assosciate
    the item with, a title/description for the question, a question type (0 ==
    multiple choice, 1 == writing), and, iff this is multiple choice, a list
    of answers and an index of the correct answer.
    """
    print aid, qtitle, qtype, mc_answers, mc_correct
    db_session.add(AssessmentItem(aid, qtype, qtitle, mc_answers, mc_correct))
    db_session.commit()


def student_response(itemid, answer, uid=None):
    """
    Record a student response. Takes an item ID, the answer (an index for
    multiple choice, or a string for a writing response) and a user ID. If
    no user ID is specified, the default is the currently logged in user.
    """
    if uid is None:
        uid = session["uid"]
    current = StudentResponse.query.filter(StudentResponse.itemid == itemid,
                                           StudentResponse.uid == uid).first()
    if current:
        db_session.delete(current)
    db_session.add(StudentResponse(itemid, uid, answer))
    db_session.commit()


def get_response(itemid, uid):
    item = StudentResponse.query.filter(StudentResponse.itemid == itemid,
                                        StudentResponse.uid == uid).first()
    return item


def get_questions(aid):
    """
    Return a list of AssessmentItems in the assessment with the given ID.
    """
    return AssessmentItem.query.filter(AssessmentItem.aid == aid).all()


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


def get_item(itemid):
    """
    Return an AssessmentItem object given an item ID.
    """
    return AssessmentItem.query.filter(AssessmentItem.itemid == itemid).first()


def grade_assessment(aid, uid=None):
    """
    Return a student's percent score on a given assessment.
    """
    if uid is None:
        uid = session["uid"]
    questions = [q for q in get_questions(aid) if q.qtype == 0]
    try:
        correct = [i for i in questions if i.qtype == 0 and
                   get_response(i.itemid, uid).mcanswer == i.mccorrect]
    except:
        return "Test not completed"
    return str(int(100*(float(len(correct)) / len(questions)))) + "%"


@langlearn.app.context_processor
def inject_funcs():
    """
    Inject functions for use in templates.
    """
    return dict(
        get_available_assessments=get_available_assessments,
        get_questions=get_questions,
        get_assessment=get_assessment,
        grade_assessment=grade_assessment
        )
