from sqlalchemy import Column, Integer, String, Float, create_engine, Boolean, or_
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Clses(Base):
    __tablename__ = "clases"
    id = Column (Integer, primary_key=True, autoincrement=True)
    nombre = Column (String)

