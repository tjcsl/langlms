import langlearn
import langlearn.admin
import langlearn.auth
from langlearn.models import User, Class, ClassRole
from flask import flash, redirect, url_for, render_template, request, session
from functools import wraps


def require_admin(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if langlearn.auth.get_user_acl() < 2:
            flash("You do not have permissions to access admin functions!"
                , "error")
            langlearn.app.logger.warning("Attempted access to admin functions\
 by UID %s" % str(session["uid"]))
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return wrapped

@require_admin
def get_students():
    students = User.query.filter(User.acl == 0).all()
    return render_template("admin/viewusers.html", users=students)

@require_admin
def get_teachers():
    teachers = User.query.filter(User.acl == 1).all()
    return render_template("admin/viewusers.html", users=teachers)

@require_admin
def get_siteadmins():
    admins = User.query.filter(User.acl == 2).all()
    return render_template("admin/viewusers.html", users=admins)

@require_admin
def get_classes():
    classes = Class.query.all()
    return render_template("admin/viewclasses.html", classes=classes)

@require_admin
def get_classes_no_teacher():
    classes = Class.query.all()
    classes_no_teacher = []
    for i in classes:
        roles = ClassRole.query.filter(ClassRole.cid == i.cid, 
                                       ClassRole.role == 1).all()
        if len(roles) == 0:
            classes_no_teacher.append(i)
    return render_template("admin/viewclasses.html", 
                           classes=classes_no_teacher)

@require_admin
def set_user_student(uid):
    langlearn.admin.set_student(uid)
    return redirect(request.headers["Referer"])

@require_admin
def set_user_teacher(uid):
    langlearn.admin.set_teacher(uid)
    return redirect(request.headers["Referer"])
