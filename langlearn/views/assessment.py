from flask import flash, request, render_template, redirect,\
    url_for
import langlearn.assessment
import langlearn.auth
import langlearn.classes
from langlearn.database import db_session


def render_assessment(aid):
    a = langlearn.assessment.get_assessment(aid)
    if langlearn.classes.user_in_class(a.cid):
        return render_template("assessment/render.html", assessment=a)
    else:
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))


def create_assessment(cid):
    if not langlearn.classes.user_is_teacher(cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        name = request.form["name"]
        a = langlearn.assessment.create_assessment(cid, name)
        return redirect(url_for("edit_assessment", aid=a))
    else:
        return render_template("assessment/create.html", cid=cid)


def delete_assessment(aid):
    assessment = langlearn.assessment.get_assessment(aid)
    if not langlearn.classes.user_is_teacher(assessment.cid):
        flash("You do not have permissions!", "error")
        return redirect(url_for("index"))
    items = langlearn.assessment.get_questions(aid)
    cid = assessment.cid
    for i in items:
        db_session.delete(i)
    db_session.delete(assessment)
    db_session.commit()
    return redirect(url_for("list_assessments", cid=cid))


def edit_assessment(aid):
    a = langlearn.assessment.get_assessment(aid)
    if not langlearn.classes.user_is_teacher(a.cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    return render_template("assessment/edit.html", assessment=a)


def list_assessments(cid):
    if not langlearn.classes.user_in_class(cid):
        flash("You are not a member of that class!")
        return redirect(url_for("index"))
    show_teacher = langlearn.classes.user_is_teacher(cid)
    a = langlearn.assessment.get_available_assessments(cid)
    return render_template("assessment/list.html",
                           assessments=a,
                           show_teacher=show_teacher,
                           cid=cid)


def add_question(qtype, aid):
    a = langlearn.assessment.get_assessment(aid)
    if not langlearn.classes.user_is_teacher(a.cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        if qtype == 0:
            mc_answers = [request.form["mcanswer"+str(i)] for i in range(4)]
            mc_correct = int(request.form["mccorrect"])
        else:
            mc_answers = []
            mc_correct = 0
        qtitle = request.form["qtitle"]
        langlearn.assessment.create_item(aid, qtitle, qtype, mc_answers,
                                         mc_correct)
        return redirect(url_for("edit_assessment", aid=aid))
    return render_template("assessment/addquestion.html",
                           qtype=qtype, assessment=a)


def edit_question(itemid):
    item = langlearn.assessment.get_item(itemid)
    assessment = langlearn.assessment.get_assessment(item.aid)
    if not langlearn.classes.user_is_teacher(assessment.cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        if item.qtype == 0:
            mc_answers = [request.form["mcanswer"+str(i)] for i in range(4)]
            mc_correct = int(request.form["mccorrect"])
            item.mcanswer0, item.mcanswer1, item.mcanswer2, item.mcanswer3 = \
                mc_answers
        else:
            mc_answers = []
            mc_correct = 0
        qtitle = request.form["qtitle"]
        item.qtitle = qtitle
        item.mc_correct = mc_correct
        db_session.commit()
        return redirect(url_for("edit_assessment", aid=item.aid))
    return render_template("assessment/editquestion.html", item=item)


def delete_question(itemid):
    item = langlearn.assessment.get_item(itemid)
    assessment = langlearn.assessment.get_assessment(item.aid)
    if not langlearn.classes.user_is_teacher(assessment.cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    aid = item.aid
    db_session.delete(item)
    db_session.commit()
    return redirect(url_for("edit_assessment", aid=aid))
