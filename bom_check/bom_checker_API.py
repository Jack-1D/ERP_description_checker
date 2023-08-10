'''做BOM檢查

目的: 抓取網頁上BOM的資料來跑規則
'''
from connect import Cursor
from bom_check.bom_check_comparison import *

def BOM_checker(cursor: Cursor, factory: str, bom: list, product_type: str, all_name_check_result: dict, other_info: dict) -> dict:
    # 用來記錄額外問題
    extra_problm = ""
    is_MXM = other_info['is_MXM']
    description = other_info['description']
    bp_token = other_info['bp_token']
    # 增加result至BOM中
    bom = [{**item, "result":"uncheck"} for item in bom]
    # 檢查ERP name展示的料號是否出現在BOM裡
    bom, extra_problm = check_erp_in_bom(bom, all_name_check_result, extra_problm)
    # 檢查必帶料
    bom, extra_problm = check_must_have(cursor, bom, factory, product_type, description, extra_problm)
    # 檢查cable
    bom, extra_problm = check_cable(cursor, bom, is_MXM, extra_problm)
    # MXM檢查油沒有帶軟排線
    bom, extra_problm = check_FPC(cursor, bom, is_MXM, description, extra_problm)
    # 檢查背板散熱
    bom, extra_problm = check_bp_cooler(cursor, bom, extra_problm)
    # 檢查packing_box
    bom, extra_problm = check_packing_box(cursor, bom, description, extra_problm)
    # 檢查機箱
    bom, extra_problm = check_chassis(cursor, bom, description, bp_token, extra_problm)
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