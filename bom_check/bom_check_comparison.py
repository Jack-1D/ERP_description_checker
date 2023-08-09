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
    for item in all_name_check_result.values():
        if item['item_no'] != None:
            item_used = False
            for bom_item in bom:
                if bom_item['itemNumber'] == item['item_no'] and not item_used:
                    item_used = True
                    bom_item['result'] = "pass" if status(bom_item['result']).__passable__ else bom_item['result']
            if not item_used:
                extra_problem += f'ERP名稱帶到的料號: {item["item_no"]}沒帶到\n'
    return bom, extra_problem

def check_must_have(cursor: Cursor, bom: list, factory: str, product_type: str, description: str, extra_problem: str) -> tuple:
    cursor.execute(f"SELECT parts FROM must_have WHERE factory = '{factory}' AND type = '{product_type}' AND description = '{description}';")
    for part in json.loads(cursor.fetchone()['parts']):
        part_used = False
        for bom_item in bom:
            if bom_item['itemNumber'] == part and not part_used:
                part_used = True
                bom_item['result'] = "pass" if status(bom_item['result']).__passable__ else bom_item['result']
        if not part_used:
            extra_problem += f"必帶料: {part}沒帶到\n"
    return bom, extra_problem

def check_cable() -> list:
    pass

def check_FPC() -> list:
    pass

def check_bp_cooler() -> list:
    pass

def check_packing_box() -> list:
    pass

def check_chassis() -> list:
    pass

def check_assm_part() -> list:
    pass

def check_graphiccard_cooler() -> list:
    pass

def check_memory() -> list:
    pass

def check_storage() -> list:
    pass

def check_thermal_parts() -> list:
    pass