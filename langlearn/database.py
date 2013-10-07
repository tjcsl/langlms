from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine(
    os.environ['DATABASE_URL'],
    convert_unicode=True
    )
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
    )
    )

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """
    Initialize the database.
    """
    import langlearn.models
    langlearn.models
    Base.metadata.create_all(bind=engine)
