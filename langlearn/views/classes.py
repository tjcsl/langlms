import langlearn.auth
import langlearn.classes
from flask import flash, render_template, redirect, url_for, request,\
    session


def create_class():
    if langlearn.auth.get_user_acl() < 1:
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        cid = langlearn.classes.create_class(
                request.form["name"],
                request.form["school"]
                )
        flash("Class creation complete!", "success")
        return redirect(url_for("class_overview", cid=cid))
    return render_template("classes/create.html")


def edit_students(cid):
    if not langlearn.classes.user_is_teacher(cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    return render_template("classes/students.html", 
            c=langlearn.classes.get_class(cid))


def add_student():
    cid = int(request.form["cid"])
    username = request.form["username"]
    if not langlearn.classes.user_is_teacher(cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    langlearn.classes.add_class_member(username, cid)
    return redirect(url_for("edit_students", cid=cid))


def rm_student():
    cid = int(request.form["cid"])
    username = request.form["username"]
    if not langlearn.classes.user_is_teacher(cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    langlearn.classes.rm_class_member(username, cid)
    return redirect(url_for("edit_students", cid=cid))


def class_overview(cid):
    if not langlearn.classes.user_in_class(cid) and \
       not langlearn.classes.user_is_teacher(cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    return render_template("classes/overview.html", 
            c=langlearn.classes.get_class(cid))


def make_teacher(cid, uid):
    if not langlearn.classes.user_is_teacher(cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    langlearn.classes.set_user_role(cid, uid, 1)
    flash("User set to teacher.", "success")
    return redirect(url_for("edit_students", cid=cid))


def make_student(cid, uid):
    if not langlearn.classes.user_is_teacher(cid):
        flash("You do not have permission!", "error")
        return redirect(url_for("index"))
    langlearn.classes.set_user_role(cid, uid, 0)
    flash("User set to student.", "success")
    return redirect(url_for("edit_students", cid=cid))
