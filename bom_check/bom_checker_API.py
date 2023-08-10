'''做BOM檢查

目的: 抓取網頁上BOM的資料來跑規則
'''
from connect import Cursor
from bom_check.bom_check_comparison import *

def BOM_checker(cursor: Cursor, factory: str, bom: list, product_type: str, all_name_check_result: dict, other_info: dict) -> dict:
    # 用來記錄額外問題
    extra_problem = ""
    is_MXM = other_info['is_MXM']
    description = other_info['description']
    bp_token = other_info['bp_token']
    graphiccard = all_name_check_result['graphiccard']['name'] if "graphiccard" in all_name_check_result else None
    # 增加result至BOM中
    bom = [{**item, "result":"uncheck"} for item in bom]
    # 檢查ERP name展示的料號是否出現在BOM裡
    bom, extra_problem = check_erp_in_bom(bom, all_name_check_result, extra_problem)
    # 檢查必帶料
    bom, extra_problem = check_must_have(cursor, bom, factory, product_type, description, extra_problem)
    # 檢查cable
    bom, extra_problem = check_cable(cursor, bom, is_MXM, extra_problem)
    # MXM檢查油沒有帶軟排線
    bom, extra_problem = check_FPC(cursor, bom, is_MXM, description, extra_problem)
    # 檢查背板散熱
    bom, extra_problem = check_bp_cooler(cursor, bom, extra_problem)
    # 檢查packing_box
    bom, extra_problem = check_packing_box(cursor, bom, description, extra_problem)
    # 檢查機箱
    bom, extra_problem = check_chassis(cursor, bom, description, bp_token, extra_problem)
    # 檢查assm_part
    bom, extra_problem = check_assm_part(cursor, bom, is_MXM, graphiccard, description, bp_token, extra_problem)
    # 檢查顯卡cooler
    bom, extra_problem = check_graphiccard_cooler(cursor, bom, is_MXM, description, graphiccard, extra_problem)
    # 檢查memory
    bom, extra_problem = check_memory(cursor, bom, all_name_check_result, extra_problem)
    # 檢查storage
    check_storage()
    # 檢查thermal_parts
    check_thermal_parts()

    return {}