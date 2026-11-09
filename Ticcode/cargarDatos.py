from sqlalchemy.orm import Session
from schema import engine, Curso, Alumno, Consigna, Entrega

def cargar_datos(session):
    if session.query(Curso).count() > 0:
        print("La base ya tiene datos cargados. No se hace nada.")
        return

    cursos = [
        Curso(nombre="1° Año - Introducción a la Computación y Algoritmos"),
        Curso(nombre="2° Año - Lógica de Programación y Estructuras Básicas"),
        Curso(nombre="3° Año - Bases de Datos Relacionales y SQL"),
        Curso(nombre="4° Año - Programación Orientada a Objetos (Python / Java)"),
        Curso(nombre="5° Año - Desarrollo Web Full Stack y APIs"),
        Curso(nombre="6° Año - Proyecto Integrador y Prácticas Profesionales")
    ]
    session.add_all(cursos)
    session.commit()  

    alumnos = [
        Alumno(nombre="Martina Gómez", curso_id=cursos[0].id),    # 1° Año
        Alumno(nombre="Lucas Rodríguez", curso_id=cursos[0].id),  # 1° Año
        Alumno(nombre="Sofía Benítez", curso_id=cursos[1].id),    # 2° Año
        Alumno(nombre="Mateo Fernández", curso_id=cursos[2].id),  # 3° Año
        Alumno(nombre="Valentina López", curso_id=cursos[4].id)   # 5° Año
    ]
    session.add_all(alumnos)
    session.commit()

    consignas = [
        Consigna(
            titulo="Práctica 1: Introducción a pseudocódigo", 
            descripcion="Resolver los primeros diagramas de flujo básicos.", 
            curso_id=cursos[0].id
        ),
        Consigna(
            titulo="TP Integrador: Consultas SQL Básicas", 
            descripcion="Diseñar y consultar tablas usando SELECT, WHERE y JOIN en phpMyAdmin.", 
            curso_id=cursos[2].id
        ),
        Consigna(
            titulo="Consigna API: Endpoints con Spring Boot", 
            descripcion="Configurar controladores REST y conexión a base de datos.", 
            curso_id=cursos[4].id
        )
    ]
    session.add_all(consignas)
    session.commit()

    entregas = [
        Entrega(
            nombre="Entrega TP1 - Martina",
            codigo_enviado="Algoritmo Inicio\n Escribir 'Hola mundo'\nFinAlgoritmo",
            estado="Aprobado",
            alumno_id=alumnos[0].id,
            consigna_id=consignas[0].id
        ),
        Entrega(
            nombre="Entrega SQL - Mateo",
            codigo_enviado="SELECT * FROM alumnos WHERE curso_id = 3;",
            estado="Pendiente",
            alumno_id=alumnos[3].id,
            consigna_id=consignas[1].id
        )
    ]
    session.add_all(entregas)
    session.commit()

    print("¡Datos de TIC code insertados correctamente!")
    print(f"  Cursos:   {session.query(Curso).count()}")
    print(f"  Alumnos:  {session.query(Alumno).count()}")
    print(f"  Consignas:{session.query(Consigna).count()}")
    print(f"  Entregas: {session.query(Entrega).count()}")


if __name__ == "__main__":
    with Session(engine) as session:
        cargar_datos(session)