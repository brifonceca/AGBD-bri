from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

# 1. Definimos la clase (una sola vez)
class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuarios"

    id      = Column(Integer, primary_key=True)
    nombre  = Column(String)
    email   = Column(String)
    activo  = Column(Boolean)

# 2. Consultamos como si fueran objetos Python
engine = create_engine("sqlite:///mi_app.db")

# Crea todas las tablas definidas si aún no existen
Base.metadata.create_all(engine)

with Session(engine) as session:
    usuarios = session.query(Usuario) \
                      .filter(Usuario.activo == True) \
                      .all()

    for u in usuarios:
        print(u.nombre, u.email)  # ← atributos reales, no índices

