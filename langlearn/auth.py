import hashlib
import langlearn.database
import langlearn.models

def is_valid_login(username, password):
    passwd_hash = hashlib.sha256(password).hexdigest()
    matching = langlearn.models.User.query.filter(
            langlearn.models.User.username == username,
            langlearn.models.User.passwd_hash == passwd_hash).first()
    if matching is not None:
        return (username, matching.uid)
    return False

def create_account(username, password):
    passwd_hash = hashlib.sha256(password).hexdigest()
    user = langlearn.models.User(username, passwd_hash)
    langlearn.database.db_session.add(user)
    langlearn.database.db_session.commit()
    
