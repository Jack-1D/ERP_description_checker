'''
做BOM檢查
目的: 抓取網頁上BOM的資料來跑規則
'''
from connect import Cursor
from bom_check.bom_check_comparison import *

def BOM_checker(cursor: Cursor, factory: str, bom: list, product_type: str, other_info: dict) -> dict:
    is_MXM = other_info['is_MXM']
    description = other_info['description']
    all_item_no = [item['itemNumber'] for item in bom]
    print(is_MXM)
    print(description)
    print(product_type)
    # 檢查ERP name展示的料號是否出現在BOM裡
    check_erp_in_bom()
    # 檢查必帶料
    check_must_have()
    # 檢查cable
    check_cable()
    # MXM檢查油沒有帶軟排線
    check_FPC()
    # 檢查背板散熱
    check_bp_cooler()
    # 檢查packing_box
    check_packing_box()
    # 檢查機箱
    check_chassis()
    # 檢查assm_part
    check_assm_part()
    # 檢查顯卡cooler
    check_graphiccard_cooler()
    # 檢查memory
    check_memory()
    # 檢查storage
    check_storage()
    # 檢查thermal_parts
    check_thermal_parts()

    return {}