from flask import flash, request, render_template, session, redirect,\
    url_for
import langlearn.assessment
import langlearn.classes


def render_assessment(aid):
    a = langlearn.assessment.get_assessment(aid)
    if langlearn.classes.user_in_class(session["uid"], a.cid):
        return render_template("assessment/render.html", assessment=a)
    else:
        flash("You do not have permission to view this assessment!")
        return redirect(url_for("index"))
