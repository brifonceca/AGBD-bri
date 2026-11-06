from sqlalchemy import Column, Integer, String, Float, create_engine, Boolean, or_, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship

engine = create_engine("mysql+pymysql://tiCode:tc123456@10.9.120.5:3306/Tic-Code")

class Base(DeclarativeBase):
    pass


class Curso(Base):
    __tablename__= "cursos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))

    alumnos = relationship("Alumno", back_populates="curso")
    consignas = relationship("Consigna", back_populates="curso")


class Alumno(Base):
    __tablename__ = "alumnos"
    id = Column (Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    curso_id = Column(Integer, ForeignKey("cursos.id"))
    
    curso = relationship("Curso", back_populates="alumnos")   
    entregas = relationship("Entrega", back_populates="alumno")
    


class Consigna(Base):
    __tablename__= "consignas"
    id = Column (Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100))
    curso_id = Column(Integer, ForeignKey("cursos.id"))
    
    curso = relationship("Curso", back_populates="consignas")    
    entregas = relationship("Entrega", back_populates="consigna")



class Entrega(Base):
    __tablename__= "entregas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_enviado = Column(String(500))  
    estado = Column(String(50))           

    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
    consigna_id = Column(Integer, ForeignKey("consignas.id"))
    
    alumno = relationship("Alumno", back_populates="entregas")
    consigna = relationship("Consigna", back_populates="entregas")

