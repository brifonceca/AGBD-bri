# SIN ORM
import sqlite3

conn = sqlite3.connect("mi_app.db")
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios ( 
id INTEGER PRIMARY KEY, 
nombre TEXT, 
email TEXT, 
activo INTEGER ) """) 
cursor.execute("INSERT INTO usuarios VALUES (1, 'Ana García', 'ana@mail.com', 1)") 
conn.commit();

# Escribimos el SQL nosotros
cursor.execute("""
    SELECT id, nombre, email
    FROM usuarios
    WHERE activo = 1
""")

rows = cursor.fetchall()

# Convertimos filas a diccionarios a mano
usuarios = [
    {'id': row[0], 'nombre': row[1], 'email': row[2]}
    for row in rows
]

conn.close()

#¿Que diferencias encuentran el lo que les devuelve el codigo sin ORM y con ORM?
# La diferencia que se encuentra al usar el codigo sin ORM es que tenemos que revisar cada query,
# y al utilizar ORM soll describimos q queremos buscar y el ORM decide como buscarlo.

#CON ORM

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