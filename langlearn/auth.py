import hashlib
import langlearn
import langlearn.database
import langlearn.models
from flask import session


def is_valid_login(username, password):
    """
    Checks if a given username/password combination exists. If it does,
    returns a two-tuple (username, user id). If it's not, return False.
    """
    passwd_hash = hashlib.sha256(password).hexdigest()
    matching = langlearn.models.User.query.filter(
        langlearn.models.User.username == username,
        langlearn.models.User.passwd_hash == passwd_hash).first()
    if matching is not None:
        return (username, matching.uid)
    return False


def create_account(username, password):
    """
    Create an account given a username/password combination.
    """
    usernames = [i.username for i in langlearn.models.User.query.all()]
    if username in usernames or len(username) < 4:
        return False
    passwd_hash = hashlib.sha256(password).hexdigest()
    user = langlearn.models.User(username, passwd_hash)
    langlearn.database.db_session.add(user)
    langlearn.database.db_session.commit()
    return True


def get_user_acl(uid=None):
    """
    Get the access of a given user id. If no userid is given, defaults to
    the currently logged in user.
    """
    if uid is None:
        uid = session["uid"]

    match = langlearn.models.User.query.filter(
        langlearn.models.User.uid == uid).first()

    if match:
        return match.acl
    return 0


@langlearn.app.context_processor
def inject_funcs():
    """
    Inject functions for use in templates.
    """
    return dict(get_user_acl=get_user_acl)
