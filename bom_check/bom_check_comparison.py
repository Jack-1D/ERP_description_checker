'''
目的:為bom_checker_API的子程式
'''
from connect import Cursor
import json

# 類似運算元overloading的東西
class status:
    def __init__(self, state: str) -> None:
        self.state = state
    def __passable__(self) -> bool:
        if self.state == "pass" or self.state == "uncheck":
            return True
        return False

def check_erp_in_bom(bom: list, all_name_check_result: dict, extra_problem: str) -> tuple:
    '''檢查ERP name展示的料號是否出現在BOM裡'''
    for item in all_name_check_result.values():
        if item['item_no'] != None:
            item_used = False
            for bom_item in bom:
                if not item_used and bom_item['itemNumber'] == item['item_no']:
                    item_used = True
                    bom_item['result'] = "pass" if status(bom_item['result']).__passable__ else bom_item['result']
            if not item_used:
                extra_problem += f'ERP名稱帶到的料號: {item["item_no"]}沒帶到\n'
    return bom, extra_problem

def check_must_have(cursor: Cursor, bom: list, factory: str, product_type: str, description: str, extra_problem: str) -> tuple:
    '''檢查必帶料
    
    共有16種情形
    '''
    cursor.execute(f"SELECT parts FROM must_have WHERE factory = '{factory}' AND type = '{product_type}' AND description = '{description}';")
    for part in json.loads(cursor.fetchone()['parts']):
        part_used = False
        for bom_item in bom:
            if not part_used and bom_item['itemNumber'] == part:
                part_used = True
                bom_item['result'] = "pass" if status(bom_item['result']).__passable__ else bom_item['result']
        if not part_used:
            extra_problem += f"必帶料: {part}沒帶到\n"
    return bom, extra_problem

def check_cable(cursor: Cursor, bom: list, is_MXM: bool, extra_problm: str) -> tuple:
    '''檢查cable

    若不是MXM系列要多帶兩條cable，否則就是多帶
    '''
    cursor.execute('SELECT * FROM cable;')
    cable_list = [item['item_no'] for item in cursor.fetchall()]
    if not is_MXM:
        for cable in cable_list:
            cable_used = False
            for bom_item in bom:
                if not cable_used and bom_item['itemNumber'] == cable:
                    cable_used = True
                    bom_item['result'] = "pass" if status(bom_item['result']).__passable__ else bom_item['result']
            if not cable_used:
                extra_problm += f'cable: {cable}沒帶到\n'
    else:
        for cable in cable_list:
            cable_used = False
            for bom_item in bom:
                if not cable_used and bom_item['itemNumber'] == cable:
                    cable_used = True
                    bom_item['result'] = "fail"
            if cable_used:
                extra_problm += f'cable: {cable}多帶了\n'
    return bom, extra_problm

def check_FPC() -> tuple:
    '''MXM檢查有沒有帶軟排線'''
    pass

def check_bp_cooler() -> tuple:
    '''檢查背板散熱'''
    pass

def check_packing_box() -> tuple:
    '''檢查packing_box'''
    pass

def check_chassis() -> tuple:
    '''檢查機箱'''
    pass

def check_assm_part() -> tuple:
    '''檢查assm_part'''
    pass

def check_graphiccard_cooler() -> tuple:
    '''檢查顯卡cooler'''
    pass

def check_memory() -> tuple:
    '''檢查memory'''
    pass

def check_storage() -> tuple:
    '''檢查storage'''
    pass

def check_thermal_parts() -> tuple:
    '''檢查thermal_parts'''
    pass