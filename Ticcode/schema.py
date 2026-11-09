from sqlalchemy import URL, Column, Integer, String, Text, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

# Configuración de conexión a MySQL
DB_HOST = "10.9.120.5"
DB_PORT = 3306
DB_DATABASE = "Tic-Code"
DB_USERNAME = "tiCode"
DB_PASSWORD = "tc123456"

url = URL.create(
    "mysql+pymysql",
    host=DB_HOST,
    port=DB_PORT,
    database=DB_DATABASE,
    username=DB_USERNAME,
    password=DB_PASSWORD,
)

engine = create_engine(url, connect_args={"connect_timeout": 10, "read_timeout": 10})

class Base(DeclarativeBase):
    pass

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)

    alumnos = relationship("Alumno", back_populates="curso", cascade="all, delete-orphan")
    consignas = relationship("Consigna", back_populates="curso", cascade="all, delete-orphan")


class Alumno(Base):
    __tablename__ = "alumnos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    
    curso = relationship("Curso", back_populates="alumnos")   
    entregas = relationship("Entrega", back_populates="alumno", cascade="all, delete-orphan")


class Consigna(Base):
    __tablename__ = "consignas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text)  
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    
    curso = relationship("Curso", back_populates="consignas")    
    entregas = relationship("Entrega", back_populates="consigna", cascade="all, delete-orphan")


class Entrega(Base):
    __tablename__ = "entregas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(120), nullable=False)  
    codigo_enviado = Column(Text)  
    estado = Column(String(50))           

    alumno_id = Column(Integer, ForeignKey("alumnos.id"), nullable=False)
    consigna_id = Column(Integer, ForeignKey("consignas.id"), nullable=False)
    
    alumno = relationship("Alumno", back_populates="entregas")
    consigna = relationship("Consigna", back_populates="entregas")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("¡Tablas creadas y conectadas exitosamente en MySQL!")