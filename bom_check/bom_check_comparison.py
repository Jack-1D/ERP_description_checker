'''用BOM的資料來檢查額外需要帶的料件

目的:為bom_checker_API的子程式
'''
from connect import Cursor
import json

# 類似運算元overloading的東西
class bom_status:
    def __init__(self, state: str) -> None:
        self.state = state
    def __passable__(self) -> bool:
        if self.state['result'] == "pass" or self.state == "uncheck":
            return True
        return False
    def check_qty(self, qty: int) -> bool:
        if int(self.state['Qty']) == qty:
            return True
        return False

def check_erp_in_bom(bom: list, all_name_check_result: dict, extra_problem: str) -> tuple[list, str]:
    '''檢查ERP name展示的料號是否出現在BOM裡'''
    for item in all_name_check_result.values():
        if item['item_no'] != None:
            item_used = False
            for bom_item in bom:
                if not item_used and bom_item['itemNumber'] == item['item_no']:
                    item_used = True
                    if not bom_status(bom_item).check_qty(1):
                        bom_item['result'] = "fail"
                        extra_problem += f"料件: {item['item_no']}數量有錯\n"
                    else:
                        bom_item['result'] = "pass" if bom_status(bom_item).__passable__ else bom_item['result']
            if not item_used:
                extra_problem += f"ERP名稱帶到的料號: {item['item_no']}沒帶到\n"
    return bom, extra_problem

def check_must_have(cursor: Cursor, bom: list, factory: str, product_type: str, description: str, extra_problem: str) -> tuple[list, str]:
    '''檢查必帶料
    
    共有16種情形
    '''
    cursor.execute(f"SELECT parts FROM must_have WHERE factory = '{factory}' AND type = '{product_type}' AND description = '{description}';")
    for part in json.loads(cursor.fetchone()['parts']):
        part_used = False
        for bom_item in bom:
            if not part_used and bom_item['itemNumber'] == part[0]:
                part_used = True
                if not bom_status(bom_item).check_qty(int(part[1])):
                    bom_item['result'] = "fail"
                    extra_problem += f"料件: {part[0]}數量有錯\n"
                else:
                    bom_item['result'] = "pass" if bom_status(bom_item).__passable__ else bom_item['result']
        if not part_used:
            extra_problem += f"必帶料: {part[0]}沒帶到\n"
    return bom, extra_problem

def check_cable(cursor: Cursor, bom: list, is_MXM: bool, extra_problm: str) -> tuple[list, str]:
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
                    if not bom_status(bom_item).check_qty(1):
                        bom_item['result'] = "fail"
                        extra_problem += f"料件: {cable}數量有錯\n"
                    else:
                        bom_item['result'] = "pass" if bom_status(bom_item).__passable__ else bom_item['result']
            if not cable_used:
                extra_problm += f"Cable: {cable}沒帶到\n"
    else:
        for cable in cable_list:
            cable_used = False
            for bom_item in bom:
                if not cable_used and bom_item['itemNumber'] == cable:
                    cable_used = True
                    bom_item['result'] = "fail"
            if cable_used:
                extra_problm += f"Cable: {cable}多帶了\n"
    return bom, extra_problm

def check_FPC(cursor: Cursor, bom: list, is_MXM: bool, description: str, extra_problm: str) -> tuple[list, str]:
    '''MXM檢查有沒有帶軟排線
    
    MXM系列須帶多帶一條軟排線
    '''
    if is_MXM:
        cursor.execute(f"SELECT item_no FROM fpc WHERE description = '{description}';")
        fpc_list = [item['item_no'] for item in cursor.fetchall()]
        for fpc in fpc_list:
            fpc_used = False
            for bom_item in bom:
                if not fpc_used and bom_item['itemNumber'] == fpc:
                    fpc_used = True
                    if not bom_status(bom_item).check_qty(1):
                        bom_item['result'] = "fail"
                        extra_problem += f"料件: {fpc}數量有錯\n"
                    else:
                        bom_item['result'] = "pass" if bom_status(bom_item).__passable__ else bom_item['result']
            if not fpc_used:
                extra_problm += f"FPC: {fpc}沒帶到\n"
    return bom, extra_problm

def check_bp_cooler(cursor: Cursor, bom: list, extra_problm: str) -> tuple[list, str]:
    '''檢查背板散熱
    
    背板背後的零件有幾個就需要幾個散熱
    '''
    backplane_item_no = ""
    cooler = []
    cursor.execute(f"SELECT * FROM backplane_cooler")
    item_used = False
    for item in cursor.fetchall():
        if not item_used:
            for bom_item in bom:
                if bom_item['itemNumber'] == item['item_no']:
                    item_used = True
                    backplane_item_no = item['item_no']
                    cooler = json.loads(item['parts'])
                    break
    # 若背板需附上cooler
    if len(cooler) != 0:
        cooler_used = False
        for bom_item in bom:
            if not cooler_used and bom_item['itemNumber'] == cooler[0]:
                cooler_used = True
                if not bom_status(bom_item).check_qty(int(cooler[1])):
                    bom_item['result'] = "fail"
                    extra_problem += f"料件: {cooler[0]}數量有錯\n"
                else:
                    bom_item['result'] = "pass" if bom_status(bom_item).__passable__ else bom_item['result']
        # BOM裡若找不到必帶的cooler，回去找背板顯示錯誤
        if not cooler_used:
            item_used = False
            for bom_item in bom:
                if not item_used and bom_item['itemNumber'] == backplane_item_no:
                    item_used = True
                    bom_item['result'] = 'fail'
                    extra_problm += f"背板cooler: {cooler[0]}沒帶到\n"
    return bom, extra_problm

def check_packing_box(cursor: Cursor, bom: list, description: str, extra_problm: str) -> tuple[list, str]:
    '''檢查packing_box
    
    共2種packing_box
    '''
    packing_box_item_no = ""
    cursor.execute(f"SELECT * FROM packing_box")
    for item in cursor.fetchall():
        if description in json.loads(item['description']):
            packing_box_item_no = item['item_no']
            break
    packing_box_used = False
    for bom_item in bom:
        if not packing_box_used and bom_item['itemNumber'] == packing_box_item_no:
            packing_box_used = True
            if not bom_status(bom_item).check_qty(1):
                bom_item['result'] = "fail"
                extra_problem += f"料件: {packing_box_item_no}數量有錯\n"
            else:
                bom_item['result'] = "pass" if bom_status(bom_item).__passable__ else bom_item['result']
    if not packing_box_used:
        extra_problm += f'Packing box: {packing_box_item_no}沒帶到\n'
    return bom, extra_problm


def check_chassis() -> tuple[list, str]:
    '''檢查機箱'''
    pass

def check_assm_part() -> tuple[list, str]:
    '''檢查assm_part'''
    pass

def check_graphiccard_cooler() -> tuple[list, str]:
    '''檢查顯卡cooler'''
    pass

def check_memory() -> tuple[list, str]:
    '''檢查memory'''
    pass

def check_storage() -> tuple[list, str]:
    '''檢查storage'''
    pass

def check_thermal_parts() -> tuple[list, str]:
    '''檢查thermal_parts'''
    pass