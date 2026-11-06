from sqlalchemy.orm import sessionmaker
# Importá tu engine y tus modelos desde el archivo donde los tenés (por ej. schema.py o models.py)
from schema import engine, Curso, Alumno, Consigna, Entrega

# 1. Crear la sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# 2. Insertar Cursos
cursos = [
    Curso(nombre="1° Año - Introducción a la Programación"),
    Curso(nombre="2° Año - Lógica y Algoritmos"),
    Curso(nombre="3° Año - Programación Web y BD"),
    Curso(nombre="4° Año - Desarrollo de Software")
]
session.add_all(cursos)
session.commit()  # Al hacer commit, SQLAlchemy asigna automáticamente los IDs (1, 2, 3, 4)

# 3. Insertar Alumnos (usando los IDs o instancias de los cursos recién creados)
alumnos = [
    Alumno(nombre="Martina Gómez", curso_id=cursos[0].id),
    Alumno(nombre="Lucas Rodríguez", curso_id=cursos[0].id),
    Alumno(nombre="Sofía Benítez", curso_id=cursos[1].id),
    Alumno(nombre="Mateo Fernández", curso_id=cursos[2].id),
    Alumno(nombre="Valentina López", curso_id=cursos[3].id)
]
session.add_all(alumnos)
session.commit()  # Asigna IDs a los alumnos (1, 2, 3, 4, 5)

# 4. Insertar Consignas / Tareas
consignas = [
    Consigna(titulo="Práctica 1: Bucles `for` y `while`", descripcion="Resolver los 5 ejercicios de lógica usando estructuras repetitivas.", curso_id=cursos[0].id),
    Consigna(titulo="TP Integrador: POO y Clases", descripcion="Crear un diagrama de clases y su implementación en código.", curso_id=cursos[1].id),
    Consigna(titulo="Creación de Base de Datos y ORM", descripcion="Configurar SQLAlchemy y realizar la carga inicial de datos.", curso_id=cursos[2].id)
]
session.add_all(consignas)
session.commit()  # Asigna IDs a las consignas (1, 2, 3)

# 5. Insertar Entregas (Relaciona al Alumno con la Consigna enviada)
entregas = [
    Entrega(
        nombre="Entrega TP1 - Martina",
        codigo_enviado="for i in range(10):\n    print('Hola Mundo')",
        estado="Aprobado",
        alumno_id=alumnos[0].id,      # Martina Gómez
        consigna_id=consignas[0].id   # Práctica 1: Bucles
    ),
    Entrega(
        nombre="Entrega TP1 - Lucas",
        codigo_enviado="count = 0\nwhile count < 10:\n    print(count)\n    count += 1",
        estado="Pendiente",
        alumno_id=alumnos[1].id,      # Lucas Rodríguez
        consigna_id=consignas[0].id   # Práctica 1: Bucles
    ),
    Entrega(
        nombre="Entrega ORM - Mateo",
        codigo_enviado="session.add_all([Curso(...), Alumno(...)])\nsession.commit()",
        estado="Revisar",
        alumno_id=alumnos[3].id,      # Mateo Fernández
        consigna_id=consignas[2].id   # Creación de Base de Datos
    )
]
session.add_all(entregas)
session.commit()

print("¡Datos de TIC code insertados correctamente en phpMyAdmin!")