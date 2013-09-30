from sqlalchemy import Column, Integer, String
from database import Base
import time

class User(Base):
    __tablename__ = "users"
    uid = Column(Integer, primary_key = True)
    username = Column(String(512))
    passwd_hash = Column(String(512))
    acl = Column(Integer)

    def __init__(self, username, passwd_hash, acl=0):
        self.username = username
        self.passwd_hash = passwd_hash
        self.acl = acl

    def __repr__(self):
        return "<User {0}>".format(self.username)

class Class(Base):
    __tablename__ = "classes"
    cid = Column(Integer, primary_key = True)
    name = Column(String(512))
    school = Column(String(512))

    def __init__(self, name, school):
        self.name = name
        self.school = school

    def __repr__(self):
        return "<Class {0}>".format(self.name)

class ClassRole(Base):
    __tablename__ = "class_roles"
    roleid = Column(Integer, primary_key = True)
    cid = Column(Integer)
    uid = Column(Integer)
    role = Column(Integer)

    def __init__(self, cid, uid, role):
        self.cid = cid
        self.uid = uid
        self.role = role

    def __repr__(self):
        return "<ClassRole {0}>".format(self.role)

class NewsPost(Base):
    __tablename__ = "news_posts"
    postid = Column(Integer, primary_key = True)
    cid = Column(Integer)
    title = Column(String(512))
    content = Column(String(4096))

    def __init__(self, cid, title, content):
        self.cid = cid
        self.title = title
        self.content = content

    def __repr__(self):
        return "<NewsPost {0}>".format(self.title)
