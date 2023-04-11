from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    real_name = Column(String)
    images = Column()
    profile = Column(Text)
