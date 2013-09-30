import langlearn.auth
import langlearn.news
from langlearn.models import NewsPost
from flask import request, render_template, redirect, url_for, session, flash

def create_newspost(cid):
    if not langlearn.news.can_create_newspost(cid):
        flash("You do not have permissions!", "error")
        return redirect(url_for("index"))
    if request.method == "POST":
        langlearn.news.create_newspost(cid,
                request.form["title"],
                request.form["content"]
                )
        flash("Post created.", "success")
        return redirect(url_for("class_overview", cid=cid))
    return render_template("news/post.html")
    
def delete_newspost(postid):
    cid = NewsPost.query.filter(NewsPost.postid == postid).first().cid
    if not langlearn.news.can_create_newspost(cid):
        flash("You do not have permissions!", "error")
        return redirect(url_for("index"))
    langlearn.news.delete_newspost(postid)
    flash("Post deleted.", "success")
    return redirect(url_for("class_overview", cid=cid))
