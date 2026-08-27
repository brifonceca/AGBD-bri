#----------------------------ejercicio 1----------------------------
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Productos(Base):
    __tablename__ = "PRODUCTOS"

    id = Column (Integer, primary_key = True)
    nombre = Column (String)
    precio = Column (Float)
    stock = Column (Float)
    categoria = Column (String)

engine = create_engine("sqlite:///:tienda.bd", echo = True)    
Base.metadata.create_all(engine)

#----------------------------ejercicio 2----------------------------
from sqlalchemy.orm import Session

productos =[
    Producto(nombre ="Teclado mecanico", precio = 8500,stock = 15,categoria = "perifericos" ),
    Producto(nombre =" Mouse inalambrico", precio = 4200,stock = 30,categoria = "perifericos" ),
    Producto(nombre ="Monitor 24 pulgadas", precio = 62000,stock = 8,categoria = "monitores" ),
    Producto(nombre =" Auriculares bluetooth", precio = 12300,stock = 20,categoria = "audio" ),
    Producto(nombre ="Webcam Full HD ", precio = 9800,stock = 12,categoria = "perifericos" ),
    Producto(nombre ="SSD 1TB ", precio = 18500,stock = 25,categoria = "almacenamiento" ),
    Producto(nombre ="RAM 16GB", precio = 15600,stock = 18,categoria = "componentes" ),
    Producto(nombre ="Mousepad XL", precio = 2100,stock = 40,categoria = "perifericos" ),
    Producto(nombre =" Hub USB-C", precio = 5400,stock = 6,categoria = "accesorios", activo = False ),
    Producto(nombre =" Cable HDMI", precio = 1800,stock = 50,categoria = "accesorios" ),
]
with Session(engine) as session: 
    session.add_all(productos)

session.commit()

with Session(engine) as session:
    total = session.query(Productos).count()
    print(f"Total de los productos en la tienda: {total}")