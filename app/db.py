import mysql.connector
from dotenv import load_dotenv
from os import environ

load_dotenv()

db_password = environ.get("DB_PASSWORD")
print(db_password)

db_conn = mysql.connector.connect(
    host="localhost", user="lucas", password=db_password, database="fishtrak"
)
