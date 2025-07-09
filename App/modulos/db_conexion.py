from dotenv import load_dotenv
import os
import mysql.connector


dotenv_path = os.path.join(os.path.dirname(__file__), 'db_credenciales.env')
load_dotenv(dotenv_path)


def cliente_mysql():

    cliente = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASS"),
        database=os.getenv("MYSQL_DB")
    )
    return cliente