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

def check_erp_in_bom(bom: list, all_name_check_result: dict) -> list:
    for item in all_name_check_result.values():
        for bom_item in bom:
            if bom_item['itemNumber'] == item['item_no']:
                bom_item['result'] = "pass" if status(bom_item['result']).__passable__ else bom_item['result']
    return bom

def check_must_have() -> list:
    pass

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