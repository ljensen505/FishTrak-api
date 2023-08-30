import mysql.connector
from dotenv import load_dotenv
from os import environ

load_dotenv()

db_password = environ.get("DB_PASSWORD")
if db_password is None:
    raise Exception("Did you remember to add you mysql password to the .env file?")

db_conn = mysql.connector.connect(
    host="localhost", user="lucas", password=db_password, database="fishtrak"
)
