from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv('modulos/db/.env')


def cliente_mysql():

    cliente = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASS"),
        database=os.getenv("MYSQL_DB")
    )
    return cliente