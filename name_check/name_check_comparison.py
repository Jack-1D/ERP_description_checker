'''
處理各料件名稱比較
目的:為name_checker_API的子程式
'''
from connect import Cursor
import json

def compare_motherboard(cursor: Cursor, factory: str, description: str, comparison_dict_list: list) -> dict:
    cursor.execute(f"SELECT * FROM description_to_motherboard WHERE factory = '{factory}' AND description = '{description}';")
    # 處理是否有登記資料
    item_no = cursor.fetchall()
    if item_no == None:
        return {"status":False, "error_msg":"Factory or MVP name might be wrong.", "item_no":None}
    else:
        item_no = [item['item_no'] for item in item_no]

    item_no_string = ", ".join(f'\'{item}\'' for item in item_no)
    cursor.execute(f"SELECT * FROM motherboard_parts WHERE item_no IN ({item_no_string});")
    parts = cursor.fetchall()
    if parts == None:
        return {"status":False, "error_msg":"This motherboard's parts might not in database.", "item_no":None}

    com_num = [device['number'] for device in comparison_dict_list if device['device'] == "COM"]
    item_no = []
    for part in parts:
        part_dict = {p[0]:p[1] for p in json.loads(part['parts'])}
        if json.loads(part['parts'])[0][0] == comparison_dict_list[0]['device'] and int(part_dict['COM']) == int(com_num[0]):
            item_no.append(part['item_no'])
    if len(item_no) > 1 or len(item_no) == 0:
        return {"status":False, "error_msg":"Ambiguous motherboard.", "item_no":None}
    
    item_no = item_no[0]
    all_parts = [{'device':p[0].upper(), 'number':int(p[1])} for part in parts if part['item_no'] == item_no for p in json.loads(part["parts"])]
    diff = [part['device'] for part in comparison_dict_list if part not in all_parts]
    # print(diff)
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
    if cpu_description.find(cpu_name) == -1:
        return {"status":False, "error_msg":"CPU name error.", "item_no":item_no}
    return {"status":True, "error_msg":"", "item_no":item_no}

def compare_backplane(cursor: Cursor, bp_token: int, e_token: int, comparison_dict_list: list, is_MXM: bool, factory: str) -> dict:
    cursor.execute(f"SELECT * FROM backplane_parts WHERE factory = '{factory}'")
    backplane_infos = cursor.fetchall()
    # 若是MXM須加回一個PCIex16再比較，且這裡的list比較裡面的字典順序不能變
    inside = False
    if is_MXM:
        for item in comparison_dict_list:
            if "PCIex16" in [item.values()]:
                inside = True
                item['number'] += 1
                break
        if not inside:
            comparison_dict_list.insert(0,{"device":"PCIex16", "number":1})

    item_no = next((backplane['item_no'] for backplane in backplane_infos if \
                [{"device": part[0], "number": int(part[1])} for part in json.loads(backplane['parts'])] == comparison_dict_list), "")
    if item_no == "":
        return {"status": False, "error_msg": "description背板帶的料有錯", "item_no": None}

    # 檢查背板的總槽數是否正確
    if bp_token != sum(device['number'] for device in comparison_dict_list):
        return {"status":False, "error_msg":"總槽數錯誤", "item_no":item_no}
    # 檢查e槽數是否正確
    if e_token != sum(device['number'] for device in comparison_dict_list if device['device'].find("PCIex") != -1) - is_MXM:
        return {"status":False, "error_msg":"e槽數錯誤", "item_no":item_no}
    return {"status":True, "error_msg":"", "item_no":item_no}

def compare_memory(description_GB: int, comparison_GB: int) -> dict:
    if description_GB == None:
        return {"status":False, "error_msg":"Memory description error.", "item_no":None}
    if comparison_GB == None:
        return {"status":False, "error_msg":"Memory part name error.", "item_no":None}
    if description_GB != comparison_GB:
        return {"status":False, "error_msg":"Memory not match.", "item_no":None}
    return {"status":True, "error_msg":"", "item_no":None, "capacity":description_GB}

def compare_storage(description_GB: int, comparison_GB: int) -> dict:
    if description_GB == None:
        return {"status":False, "error_msg":"Storage description error.", "item_no":None}
    if comparison_GB == None:
        return {"status":False, "error_msg":"Storage part name error.", "item_no":None}
    if description_GB != comparison_GB:
        return {"status":False, "error_msg":"Storage not match.", "item_no":None}
    return {"status":True, "error_msg":"", "item_no":None, "capacity":description_GB}