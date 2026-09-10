#----------------------------ejercicio 1----------------------------
from sqlalchemy import Column, Integer, String, Float, create_engine, Boolean, or_
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Productos(Base):
    __tablename__ = "productos"
    id = Column (Integer, primary_key = True)
    nombre = Column (String)
    precio = Column (Float)
    stock = Column (Float)
    categoria = Column (String)
    activo = Column (Boolean, default = True)

engine = create_engine("sqlite:///tienda.bd", echo = True)    
Base.metadata.create_all(engine)

#----------------------------ejercicio 2----------------------------
with Session(engine) as session:
    productos =[
        Productos(nombre ="Teclado mecanico", precio = 8500,stock = 15,categoria = "perifericos" ),
        Productos(nombre ="Mouse inalambrico", precio = 4200,stock = 30,categoria = "perifericos" ),
        Productos(nombre ="Monitor 24 pulgadas", precio = 62000,stock = 8,categoria = "monitores" ),
        Productos(nombre ="Auriculares bluetooth", precio = 12300,stock = 20,categoria = "audio" ),
        Productos(nombre ="Webcam Full HD ", precio = 9800,stock = 12,categoria = "perifericos" ),
        Productos(nombre ="SSD 1TB ", precio = 18500,stock = 25,categoria = "almacenamiento" ),
        Productos(nombre ="RAM 16GB", precio = 15600,stock = 18,categoria = "componentes" ),
        Productos(nombre ="Mousepad XL", precio = 2100,stock = 40,categoria = "perifericos" ),
        Productos(nombre ="Hub USB-C", precio = 5400,stock = 6,categoria = "accesorios", activo = False ),
        Productos(nombre ="Cable HDMI", precio = 1800,stock = 50,categoria = "accesorios" ),
        Productos(nombre ="Camara", precio = None, stock = 10, categoria = "None"),
    ]

#session.add_all(productos)
#session.commit()

total = session.query(Productos).count()
print(f"Total de los productos en la tienda: {total}")

#----------------------------ejercicio 3----------------------------
pedido = session.query(Productos.nombre, Productos.precio)\
                .filter(Productos.categoria == "perifericos")\
                .all()

for nombre, precio in pedido:
    print(nombre, precio)

#----------------------------ejercicio 4----------------------------
mayor = session.query(Productos.nombre,Productos.precio)\
               .filter(Productos.precio > 10000)\
               .order_by(Productos.precio.desc())\
               .all()

for nombre, precio in mayor:
    print(nombre, precio)

#----------------------------ejercicio 5----------------------------
menor = session.query(Productos. nombre, Productos.stock, Productos.activo)\
               .filter(Productos.stock <= 12)\
               .all()

for nombre, stock, activo in menor:
    print (nombre, stock, activo)

#¿Por que no aparece el Hub USB-C si tiene stock 6?
# Porque Hub USB-C estaba activo = False, entonces hace que no lo muestre.

#----------------------------ejercicio 6----------------------------
entre = session.query(Productos.nombre, Productos.precio)\
               .filter(Productos.precio >= 5000)\
               .filter(Productos.precio <= 20000)\
               .all()

for nombre, precio in entre:
    print(nombre, precio)

#----------------------------ejercicio 7----------------------------
caro = session.query(Productos.nombre, Productos.precio)\
              .order_by(Productos.precio.desc())\
              .first()

if caro:
    nombre, precio = caro
    print(nombre, precio)   

#----------------------------ejercicio 8----------------------------    
act = session.query(Productos. nombre, Productos.activo)\
               .filter(Productos.activo == False)\
               .all()

for nombre, activo in act:
    print (nombre, activo)

#----------------------------ejercicio 9----------------------------
cat = session.query(Productos.nombre, Productos.categoria)\
                .filter(or_(Productos.categoria == "audio", Productos.categoria == "componentes"))\
                .all()

for nombre, categoria in cat:
    print(nombre, categoria)

#----------------------------ejercicio 10----------------------------
conte = session.query(Productos.nombre)\
               .filter(Productos.nombre.contains("a"))\
               .all()

for nombre in conte:
    print(nombre)

#¿Cuántos aparecen?
# Aparecen 8

#----------------------------ejercicio 11----------------------------
emp = session.query(Productos.nombre)\
               .filter(Productos.nombre.startswith("M"))\
               .all()

for nombre in emp:
    print(nombre)

#----------------------------ejercicio 12----------------------------
nada = session.query(Productos.nombre, Productos.categoria)\
               .filter(Productos.categoria == None)\
               .all()

for nombre, categoria in nada:
    print(nombre, categoria)

#¿Que pasa si filtran por precio == None? ¿Aparece el mismo producto?
#Si filtras por precio no pasa nada y te aparece el mismo producto

#----------------------------ejercicio 13----------------------------
hub = session.get(Productos, 9)

if hub:
    hub.stock = 20
    hub.activo = True
    session.commit()
    print("¡Producto actualizado con éxito!")

verificacion = session.get(Productos, 9)
print(f"Verificación - Producto: {verificacion.nombre}, Stock: {verificacion.stock}, Activo: {verificacion.activo}")

#----------------------------ejercicio 14----------------------------
perifericos = session.query(Productos)\
                     .filter(Productos.categoria == "perifericos")\
                     .all()

for p in perifericos:
    if p.precio is not None:
        p.precio = p.precio * 1.10

session.commit()

teclado = session.query(Productos).filter(Productos.nombre == "Teclado mecanico").first()
if teclado:
    print(f"Nuevo precio del {teclado.nombre}: {teclado.precio}")

#¿Cuanto cuesta el Teclado mecanico despues del aumento?
#Luego del aumento el precio actual del teclado es 10285

#----------------------------ejercicio 15----------------------------
cable = session.get(Productos, 10)

if cable:
    session.delete(cable)
    session.commit()

total_actualizado = session.query(Productos).count()
print(f"Total de productos actualizados: {total_actualizado}")  

#----------------------------ejercicio 16----------------------------
a_borrar = session.query(Productos)\
                  .filter(or_(Productos.precio < 2000, Productos.activo == False))\
                  .all()

for p in a_borrar:
    session.delete(p)

session.commit()
print(f"Cantidad de productos borrados: {len(a_borrar)}")

#¿Cuantos borraron?
# 0, debido a que el unico producto que era menor a 2000 era el Cable HDMI
#y como fue eliminado en el ejercicio 15 no vuelve a aparecer, ademas de que 
#Hub USB-C esta inactivo

#----------------------------EXTRA 1----------------------------
usb = session.query(Productos.nombre)\
                       .filter(Productos.nombre.contains("USB"))\
                       .all()

for nombre in usb:
    print(nombre)

#----------------------------EXTRA 2----------------------------
ordenados = session.query(Productos.nombre, Productos.categoria, Productos.precio)\
                   .order_by(Productos.categoria, Productos.precio)\
                   .all()

for nombre, categoria, precio in ordenados:
    print(nombre, categoria, precio)

#----------------------------EXTRA 3----------------------------
activos = session.query(Productos)\
                 .filter(Productos.activo == True)\
                 .count()
inactivos = session.query(Productos)\
                   .filter(Productos.activo == False)\
                   .count()

print(f"Productos activos: {activos}")
print(f"Productos inactivos: {inactivos}")
#Aparecen 0 inactivos pq en el ejercicio 13 cambie el estado del Hub USB-C