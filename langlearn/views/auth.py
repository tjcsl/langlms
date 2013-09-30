from flask import flash, request, render_template, session, redirect,\
    url_for
import langlearn.auth

def login():
    if request.method == "POST":
        response = langlearn.auth.is_valid_login(
                request.form["username"],
                request.form["password"]
                )
        if response:
            session["username"] = response[0]
            session["uid"] = response[1]
            flash("<i class='icon-ok-sign icon-white'></i>\
                    Login success.", "success")
            return redirect(url_for("index"))
        flash("<i class='icon-remove-sign icon-white'></i>\
                Login failed!", "error")
    return render_template("auth/login.html")

def register():
    if request.method == "POST":
        if langlearn.auth.create_account(
                request.form["username"],
                request.form["password"]
                ):
            flash("<i class='icon-ok-sign icon-white'></i>\
                    Account created. Please login.", "success")
            return render_template("auth/login.html")
        else:
            flash("Account creation failure, please try a different username."
                  , "error")
    return render_template("auth/register.html")

def logout():
    if "username" in session or "uid" in session:
        if "username" in session: session.pop("username")
        if "uid" in session: session.pop("uid")
        flash("<i class='icon-ok-sign icon-white'></i>\
                Logged out.", "success")
        return redirect(url_for("login"))
    flash("<i class='icon-ok-sign icon-white'></i>\
            You are already logged out!", 
            "success")
    return redirect(url_for("logout"))
        
