from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///produ.db", echo=True)

class Producto(Base):
    __tablename__ = "productos"

    id      = Column(Integer, primary_key=True)
    nombre  = Column(String)
    precio   = Column(Float)
    stock  = Column(Integer)
    categoria = Column(String)


Base.metadata.create_all(engine)

with Session(engine) as session: 
    LisProductos = [
    Producto(nombre = "Mouse", precio = 200, stock = 15, categoria = "Tecnologico"),
    Producto(nombre = "Celular", precio = 490, stock = 8, categoria = "Tecnologico"),
    Producto(nombre = "Teclado", precio = 450, stock = 20, categoria = "Tecnologico"),
    Producto(nombre = "Auriculares", precio = 250, stock = 20, categoria = "Audio"),
    Producto(nombre = "PC", precio = 499, stock = 20, categoria = "Tecnologico"),
]

    session.add_all(LisProductos)
    
    session.commit()

with Session(engine) as session:
    ProduBaratos = session.query(Producto).filter(Producto.precio < 500).all()

    print("\n--- PRODUCTOS CON PRECIO MENOR A $500 ---")
    for prod in ProduBaratos:
        print(f"{prod.nombre} | Precio: ${prod.precio} | Categoría: {prod.categoria}")