import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor
from dotenv import load_dotenv
from os import environ


def connect():
    load_dotenv()

    db_password = environ.get("DB_PASSWORD")
    user = environ.get("USER")
    if None in [db_password, user]:
        raise Exception("Did you remember to add info to your .env file?")

    db_conn = mysql.connector.connect(
        host="localhost", user=user, password=db_password, database="fishtrak"
    )

    return db_conn


class Controller:
    """
    A generic Controller class which should be inhereted from.
    All methods should be private.
    This class should never be instantiated.
    """

    def __init__(self) -> None:
        self.db_conn: CMySQLConnection = connect()  # type: ignore
        self.table: None | str = (
            None  # used to define the mysql table name in child class(es)
        )

    def _get_all(self) -> list[dict]:
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
