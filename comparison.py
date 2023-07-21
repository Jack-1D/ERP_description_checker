import mysql.connector
import json
from typing import NewType
Cursor = NewType('Cursor',mysql.connector.cursor_cext.CMySQLCursor)

def compare_motherboard(cursor: Cursor, factory: str, description: str, comparison_dict_list: list) -> tuple[bool, str]:
    cursor.execute(f"SELECT * FROM description_to_motherboard WHERE factory = '{factory}' AND description = '{description}';")
    # 處理是否有登記資料
    item_no = cursor.fetchone()
    if item_no == None:
        return [False, "Factory or MVP name might be wrong."]
    else:
        item_no = item_no[0]

    cursor.execute(f"SELECT * FROM motherboard_parts WHERE item_no = '{item_no}';")
    parts = cursor.fetchone()
    if parts == None:
        return [False, "This motherboard's parts might not in database."]
    else:
        all_parts = [{'device':part[0].upper(), 'number':int(part[1])} for part in json.loads(parts[1])]
    diff = [part['device'] for part in comparison_dict_list if part not in all_parts]
    print(diff)
    if len(diff) != 0:
        return [False, ", ".join(diff) + " not in description."]
    return [True, ""]