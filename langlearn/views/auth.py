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
            flash("Login successful.", "success")
            return redirect(url_for("index"))
        flash("Login failed!", "error")
    return render_template("auth/login.html")

def register():
    if request.method == "POST":
        langlearn.auth.create_account(
                request.form["username"],
                request.form["password"]
                )
        flash("Account created. Please login.", "success")
        return render_template("auth/login.html")
    return render_template("auth/register.html")

def logout():
    if "username" in session or "uid" in session:
        if "username" in session: session.pop("username")
        if "uid" in session: session.pop("uid")
        flash("Logged out.", "success")
        return redirect(url_for("login"))
    flash("You are already logged out!", "success")
    return redirect(url_for("logout"))
        
