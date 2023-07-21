import mysql.connector
from typing import NewType

Cursor = NewType('Cursor',mysql.connector.cursor_cext.CMySQLCursor)
Connection = NewType('Connection',mysql.connector.connection_cext.CMySQLConnection)

def open_connect() -> tuple[Connection, Cursor]:
    connection = mysql.connector.connect(
        host='localhost',          # 主機名稱
        database='std_rule', # 資料庫名稱
        user='root',        # 帳號
        password='adlink')  # 密碼
    cursor = connection.cursor()
    return connection, cursor

def close_connect(connection: Connection, cursor: Cursor) -> None:
    cursor.close()
    connection.close()
    return