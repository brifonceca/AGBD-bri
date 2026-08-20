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