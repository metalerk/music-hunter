from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Release(Base):
    __tablename__ = "release"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(String)
    