def BOM_checker(factory: str, bom: list) -> dict:
    all_item_no = [item['itemNumber'] for item in bom]