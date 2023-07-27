from comparison import compare_motherboard, compare_CPU
from connect import Cursor


def name_checker(cursor: Cursor, name: str, factory: str) -> dict:
    name = name.split('*ERP')
    name.pop(2)
    name.pop(0)
    name = [n[n.find(':')+1:] for n in name]

    ERP_part_name = name[0][4:]
    ERP_description = name[1]
    # 利用description檢查ERP_part_name
    # 找motherboard位置，並拆解需檢查的零組件
    check_devices = ERP_description[ERP_description.find(', ')+2:]
    if check_devices.find("CFast") != -1:
        check_devices = check_devices[:check_devices.find("CFast")+5]
    else:
        check_devices = check_devices[:check_devices.find("M.2")+3]
    check_devices = check_devices.split(",")
    check_devices = [device.replace(" ","") for device in check_devices]
    # 把需要忽略的判斷拿掉
    ignore = ["PCIex", "DI","line-out/mic-in","TPM2.0"]
    for device in check_devices.copy():
        for ignore_item in ignore:
            if device.find(ignore_item) != -1:
                check_devices.remove(device)
    # 拆分物件和數量
    check_devices_to_dict = []
    for device in check_devices:
        if device.find("*") == -1 and device.find("pcs") == -1 and device.find("x") == -1:
            check_devices_to_dict.append({"device":device.upper(), "number": 1})
        elif device.find("*") != -1:
            device = device.split("*")
            check_devices_to_dict.append({"device":device[1].upper(), "number": int(device[0])})
        elif device.find("pcs") != -1:
            device = device.split("pcs")
            check_devices_to_dict.append({"device":device[1].upper(), "number": int(device[0])})
        elif device.find("x") != -1:
            device = device.split("x")
            check_devices_to_dict.append({"device":device[1].upper(), "number": int(device[0])})
    # 主板代號與ERP description檢查
    ERP_part_name_split = ERP_part_name.split("-")
    motherboard_description = ERP_part_name_split[0][:2]
    if ERP_part_name_split[1].find("MXM") != -1:
        motherboard_description += "MXM"
    mb_name_result = compare_motherboard(cursor, factory, motherboard_description, check_devices_to_dict)
    
    # CPU代號與ERP description檢查
    cpu_description = ERP_description.split(",")[0]
    token = ERP_part_name_split[0][3]
    cpu_name_result = compare_CPU(cursor, token, cpu_description)
    
    return {"motherboard":mb_name_result, "CPU":cpu_name_result}