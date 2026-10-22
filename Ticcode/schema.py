from sqlalchemy import Column, Integer, String, Float, create_engine, Boolean, or_
from sqlalchemy.orm import DeclarativeBase, Session,relationship

class Base(DeclarativeBase):
    pass

class Profesores(Base):
    __tablename__ = "profesores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)



class Alumno(Base):
    __tablename__ = "alumnos"
    id = Column (Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    
    
class Curso(Base):
    __tablename__= "cursos"
    id = Column(Integer, primary_key=True, autoincrement=True)



class Consigna(Base):
    __tablename__= "consignas"
    id = Column (Integer, primary_key=True, autoincrement=True)



class Entrega(Base):
    __tablename__= "entregas"
    id = Column (Integer, primary_key=True, autoincrement=True)
    


