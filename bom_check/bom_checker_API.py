'''
做BOM檢查
目的: 抓取網頁上BOM的資料來跑規則
'''
from connect import Cursor
from bom_check.bom_checker_API import *

def BOM_checker(cursor: Cursor, factory: str, bom: list) -> dict:
    all_item_no = [item['itemNumber'] for item in bom]
    return {}