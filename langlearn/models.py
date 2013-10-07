from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    uid = Column(Integer, primary_key=True)
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
    cid = Column(Integer, primary_key=True)
    name = Column(String(512))
    school = Column(String(512))

    def __init__(self, name, school):
        self.name = name
        self.school = school

    def __repr__(self):
        return "<Class {0}>".format(self.name)


class ClassRole(Base):
    __tablename__ = "class_roles"
    roleid = Column(Integer, primary_key=True)
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
    postid = Column(Integer, primary_key=True)
    cid = Column(Integer)
    title = Column(String(512))
    content = Column(String(4096))

    def __init__(self, cid, title, content):
        self.cid = cid
        self.title = title
        self.content = content

    def __repr__(self):
        return "<NewsPost {0}>".format(self.title)


class Assessment(Base):
    __tablename__ = "assessments"
    aid = Column(Integer, primary_key=True)
    cid = Column(Integer)
    name = Column(String(512))

    def __init__(self, cid, name):
        self.cid = cid
        self.name = name

    def __repr__(self):
        return "<Assessment {0}>".format(self.name)


class AssessmentItem(Base):
    __tablename__ = "assessment_items"
    itemid = Column(Integer, primary_key=True)
    aid = Column(Integer)
    qtype = Column(Integer)  # Question type (0=mc,1=writing)
    qtitle = Column(String(2048))
    # Multiple choice datafields
    mcanswer0 = Column(String(512))
    mcanswer1 = Column(String(512))
    mcanswer2 = Column(String(512))
    mcanswer3 = Column(String(512))
    mccorrect = Column(Integer)

    def __init__(self, aid, qtype, qtitle, mccorrect=0, *args):
        if qtype == 0:
            while len(args) < 4:
                args.append("")
            self.mcanswer0, self.mcanswer1, \
                self.mcanswer2, self.mcanswer3 = args
        self.mccorrect = mccorrect
        self.aid = aid
        self.qtype = qtype
        self.qtitle = qtitle

    def __repr__(self):
        return "<AssessmentItem {0}>".format(self.qtitle)


class StudentResponse(Base):
    __tablename__ = "assessment_responses"
    rid = Column(Integer, primary_key=True)
    uid = Column(Integer)
    aid = Column(Integer)
    mcanswer = Column(Integer)
    writinganswer = Column(String(8192))

    def __init__(self, itemid, uid, answer):
        self.itemid = itemid
        self.uid = uid
        if isinstance(answer, int):
            self.mcanswer = answer
            self.writinganswer = ""
        else:
            self.mcanswer = 0
            self.writinganswer = answer

    def __repr__(self):
        return "<StudentResponse to {0}>".format(self.aid)
