import mysql.connector
import json
from typing import NewType
Cursor = NewType('Cursor',mysql.connector.cursor_cext.CMySQLCursor)

def compare_motherboard(cursor: Cursor, factory: str, description: str, comparison_dict_list: list) -> dict:
    cursor.execute(f"SELECT * FROM description_to_motherboard WHERE factory = '{factory}' AND description = '{description}';")
    # 處理是否有登記資料
    item_no = cursor.fetchone()
    if item_no == None:
        return {"status":False, "error_msg":"Factory or MVP name might be wrong.", "item_no":None}
    else:
        item_no = item_no["item_no"]

    cursor.execute(f"SELECT * FROM motherboard_parts WHERE item_no = '{item_no}';")
    parts = cursor.fetchone()
    if parts == None:
        return {"status":False, "error_msg":"This motherboard's parts might not in database.", "item_no":item_no}
    all_parts = [{'device':part[0].upper(), 'number':int(part[1])} for part in json.loads(parts["parts"])]
    diff = [part['device'] for part in comparison_dict_list if part not in all_parts]
    print(diff)
    if len(diff) != 0:
        return {"status":False, "error_msg":", ".join(diff) + " not in description.", "item_no":item_no}
    return {"status":True, "error_msg":"", "item_no":item_no}

def compare_CPU(cursor: Cursor, token: str, cpu_description: str) -> dict:
    cursor.execute(f"SELECT * FROM cpu WHERE token = '{token}';")
    cpu_info = cursor.fetchone()
    if cpu_info == None:
        return {"status":False, "error_msg":"CPU token not exists.", "item_no":None}
    item_no = cpu_info["item_no"]
    cpu_name = cpu_info["name"]
    if cpu_description != cpu_name:
        return {"status":False, "error_msg":"CPU name error.", "item_no":item_no}
    return {"status":True, "error_msg":"", "item_no":item_no}