'''
主程式: js直接呼叫
'''
from connect import open_connect, close_connect
from checker import name_checker, BOM_checker

def main_checker(name: str, factory: str, bom: list) -> dict:
    connection, cursor = open_connect()
    all_name_check_result = name_checker(cursor, name, factory)
    all_BOM_check_result = BOM_checker(factory, bom)
    
    
    print(all_name_check_result)
    close_connect(connection, cursor)
    return {"name_check_result":all_name_check_result,"BOM_check_result":all_BOM_check_result}