import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor
from dotenv import load_dotenv
from os import environ


def connect():
    load_dotenv()

    db_password = environ.get("DB_PASSWORD")
    if db_password is None:
        raise Exception("Did you remember to add you mysql password to the .env file?")

    db_conn = mysql.connector.connect(
        host="localhost", user="lucas", password=db_password, database="fishtrak"
    )

    return db_conn


class Controller:
    def __init__(self) -> None:
        self.db_conn: CMySQLConnection = connect()  # type: ignore
        print(type(self.db_conn))
        self.table: None | str = None

    def get_all(self) -> list[dict]:
        if self.table is None:
            raise Exception(
                "You did something wrong with inheriting from the base Controller class.\nYou idiot."
            )
        cursor: CMySQLCursor = self.db_conn.cursor(dictionary=True)
        query = f"SELECT * FROM {self.table};"
        cursor.execute(query)
        result: list[dict] = cursor.fetchall()  # type: ignore
        cursor.close()
        self.db_conn.close()

        return result