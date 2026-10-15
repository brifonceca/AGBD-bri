from sqlalchemy import URL, create_engine, text
from sqlalchemy.exc import SQLAlchemyError

DB_HOST= "10.9.120.5"
DB_PORT=3306
DB_DATABASE= "Tic-Code"
DB_USERNAME= "tiCode"
DB_PASSWORD= "tc123456"

url = URL.create(
    "mysql+pymysql",
    host= DB_HOST,
    port= DB_PORT,
    database= DB_DATABASE,
    username= DB_USERNAME,
    password= DB_PASSWORD,    
)

motor = create_engine(url, connect_args={"connect_timeout": 10, "read_timeout": 10})


try:
    with motor.connect() as conexion:
        resultado = conexion.execute(text("SELECT 1")).scalar_one()
    print("conexion a MySQL OK.")
except SQLAlchemyError as error:
    print("No se pudo conectar, revisar to")
    print(error.orig)        
else: 
    print(f'exitosa conexion ok {resultado}')