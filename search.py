'''
主程式: js直接呼叫
'''
from connect import open_connect, close_connect
from name_check import name_checker_API
from bom_check import bom_checker_API

def main_checker(name: str, factory: str, bom: list, product_type: str) -> dict:
    connection, cursor = open_connect()
    all_name_check_result, other_info = name_checker_API.name_checker(cursor, name, factory)
    all_BOM_check_result = bom_checker_API.BOM_checker(cursor, factory, bom, product_type, other_info)
    
    
    print(all_name_check_result)
    close_connect(connection, cursor)
    return {"name_check_result":all_name_check_result,"BOM_check_result":all_BOM_check_result}