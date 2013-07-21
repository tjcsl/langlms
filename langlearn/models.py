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

