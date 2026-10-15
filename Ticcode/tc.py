from sqlalchermy import URL, create_engine, text
from sqlalchermy.exc import SQLAlchermyError

DB_HOST= "10.9.120.5"
DB_PORT=3306
DB_DATABASE= "tic_code"
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