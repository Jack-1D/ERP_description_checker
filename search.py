from connect import open_connect, close_connect
from checker import name_checker

def main_checker(name: str, factory: str) -> dict:
    connection, cursor = open_connect()
    all_name_check_result = name_checker(cursor, name, factory)
    
    
    print(all_name_check_result)
    close_connect(connection, cursor)
    return all_name_check_result