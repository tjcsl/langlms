from flask import render_template, session, flash, redirect, url_for

def settings():
    if "uid" not in session:
        flash("<i class='icon-white icon-remove-sign'></i>\
                You are not logged in, and cannot change your\
                settings.", "error")
        return redirect(url_for('login'))
    return render_template("user/settings.html")
