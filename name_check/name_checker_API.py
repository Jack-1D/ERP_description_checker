'''
做ERP name檢查
目的:主要處理字串後丟入comparison做比較
'''
from name_check.name_check_comparison import compare_motherboard, compare_CPU, compare_backplane, compare_memory, compare_storage
from connect import Cursor
import re

is_MXM = False

def name_checker(cursor: Cursor, name: str, factory: str) -> tuple:
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
        other_devices = check_devices[check_devices.find("CFast")+5:]
        check_devices = check_devices[:check_devices.find("CFast")+5]
    else:
        if check_devices.find("M.2") > check_devices.find("USIM"):
            other_devices = check_devices[check_devices.find("M.2")+3:]
            check_devices = check_devices[:check_devices.find("M.2")+3]
        else:
            other_devices = check_devices[check_devices.find("USIM")+4:]
            check_devices = check_devices[:check_devices.find("USIM")+4]
    check_devices = check_devices.split(",")
    check_devices = [device.replace(" ","") for device in check_devices]
    # 把需要忽略的判斷拿掉
    ignore = ["PCI","DI","line-out/mic-in","TPM2.0","MXM"]
    mb_check_devices = [device for device in check_devices if all(ignore_item not in device for ignore_item in ignore)]
    print(mb_check_devices)
    # 拆分物件和數量
    check_devices_to_dict = []
    for device in mb_check_devices:
        if device.find("*") == -1 and device.find("pc") == -1 and device.find("x") == -1:
            check_devices_to_dict.append({"device":device.upper().strip(' '), "number": 1})
        elif device.find("*") != -1:
            device = device.split("*")
            check_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
        elif device.find("pcs") != -1:
            device = device.split("pcs")
            check_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
        elif device.find("pc") != -1:
            device = device.split("pc")
            check_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
        elif device.find("x") != -1:
            device = device.split("x")
            check_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
    # 主板代號與ERP description檢查
    ERP_part_name_split = ERP_part_name.split("-")
    motherboard_description = ERP_part_name_split[0][:2]
    
    # MXM和CFast分開檢查-----------------------------------------------------------------------------------
    is_MXM = True if ERP_description.find("MXM") != -1 else False
    motherboard_description += "MXM" if ERP_description.find("MXM") != -1 else ""
    mb_name_result = compare_motherboard(cursor, factory, motherboard_description, check_devices_to_dict)
    
    # CPU代號與ERP description檢查-------------------------------------------------------------------------
    cpu_description = ERP_description.split(",")[0]
    cpu_token = ERP_part_name_split[0][3]
    cpu_name_result = compare_CPU(cursor, cpu_token, cpu_description)

    # 背板代號與ERP description檢查-------------------------------------------------------------------------
    bp_token = int(ERP_part_name_split[0][2])
    e_posi = ERP_part_name_split[-1].split('/')[0].find('E')
    if bp_token == 0:
        if e_posi != -1:
            bp_name_result = {"status":False, "error_msg":"沒背板槽位，卻有PCIe", "item_no":None}
        else:
            bp_name_result = {"status":True, "error_msg":"", "item_no":None}
    else:
        e_token = int(ERP_part_name_split[-1].split('/')[0][:e_posi])
        print(check_devices)
        bp_check_devices = [device for device in check_devices if device.find("PCI") != -1 and device.find("mPCIe") == -1]
        bp_check_devices = [item.replace(" ","") for device in bp_check_devices for item in device.split('+')]
        bp_check_devices_to_dict = [{"device":device,"number":1} if device.find("PCI") == 0 else \
                                    {"device":device[device.find("PCI"):],"number":int(device[:device.find("PCI")])} \
                                        for device in bp_check_devices]
        # 名稱標準化
        bp_check_devices_to_dict = [{"device":"PCI","number":device['number']} if device['device'].find("PCIs") != -1 \
                                    else {"device":device["device"],"number":device['number']} for device in bp_check_devices_to_dict]
        bp_check_devices_to_dict = [{"device":"PCIex4","number":device['number']} if device['device'].find("4") != -1 \
                                    else {"device":device["device"],"number":device['number']} for device in bp_check_devices_to_dict]
        bp_check_devices_to_dict = [{"device":"PCIex16","number":device['number']} if device['device'].find("16") != -1 \
                                    else {"device":device["device"],"number":device['number']} for device in bp_check_devices_to_dict]
        bp_name_result = compare_backplane(cursor, bp_token, e_token, bp_check_devices_to_dict, is_MXM, factory)

    total_check_result = {"motherboard":mb_name_result, "CPU":cpu_name_result, "backplane":bp_name_result}

    # 其他零件檢查--------------------------------------------------------------------------------------
    other_devices = other_devices.split(",")
    other_devices = [device.strip(' ') for device in other_devices]
    if '' in other_devices: other_devices.remove('')

    other_devices_to_dict = []
    for device in other_devices:
        if device.find("*") == -1 and device.find("pc") == -1 and device.find("x") == -1:
            other_devices_to_dict.append({"device":device.upper().strip(' '), "number": 1})
        elif device.find("*") != -1:
            device = device.split("*")
            other_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
        elif device.find("pcs") != -1:
            device = device.split("pcs")
            other_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
        elif device.find("pc") != -1:
            device = device.split("pc")
            other_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
        elif device.find("x") != -1:
            device = device.split("x")
            other_devices_to_dict.append({"device":device[1].upper().strip(' '), "number": int(device[0]) if device[0].find('+') \
                                          == -1 else eval(device[0][device[0].find('('):device[0].find(')')+1])})
    
    part_name_end_pointer = ERP_part_name.find('/')
    for device in other_devices_to_dict:
        # 處理memory
        if device['device'].find("DDR") != -1:
            (memory_description_GB, memory_comparison_GB) = (None, None)
            # description的memory大小
            memory_pattern = re.compile(r'(\d+)G')
            if memory_pattern.search(device['device']) != None: memory_description_GB = int(memory_pattern.search(device['device']).groups()[0]) * device['number']
            memory_pattern = re.compile(r'(\d+)T')
            if memory_pattern.search(device['device']) != None: memory_description_GB = int(memory_pattern.search(device['device']).groups()[0]) * device['number'] * 1000
            # MVP的memory大小
            memory_pattern = re.compile(r'M(\d+)G')
            if memory_pattern.search(ERP_part_name[part_name_end_pointer:]) != None:
                memory_comparison_GB = int(memory_pattern.search(ERP_part_name[part_name_end_pointer:]).groups()[0])
                part_name_end_pointer = int(memory_pattern.search(ERP_part_name[part_name_end_pointer:]).span()[1])
            memory_pattern = re.compile(r'M(\d+)T')
            if memory_pattern.search(ERP_part_name[part_name_end_pointer:]) != None:
                memory_comparison_GB = int(memory_pattern.search(ERP_part_name[part_name_end_pointer:]).groups()[0]) * 1000
                part_name_end_pointer = int(memory_pattern.search(ERP_part_name[part_name_end_pointer:]).span()[1])
            memory_name_result = compare_memory(memory_description_GB, memory_comparison_GB)
            total_check_result["memory"] = memory_name_result
        # 處理storage
        if device['device'].find("SSD") != -1:
            (storage_description_GB, storage_comparison_GB) = (0, 0)
            # description的memory大小
            storage_pattern = re.compile(r'(\d+)G')
            if storage_pattern.search(device['device']) != None: storage_description_GB = int(storage_pattern.search(device['device']).groups()[0]) * device['number']
            storage_pattern = re.compile(r'(\d+)T')
            if storage_pattern.search(device['device']) != None: storage_description_GB = int(storage_pattern.search(device['device']).groups()[0]) * device['number'] * 1000
            # MVP的storage大小
            storage_pattern = re.compile(r'(\d+)G')
            if storage_pattern.search(ERP_part_name[part_name_end_pointer:]) != None:
                storage_comparison_GB = int(storage_pattern.search(ERP_part_name[part_name_end_pointer:]).groups()[0])
                part_name_end_pointer = int(storage_pattern.search(ERP_part_name[part_name_end_pointer:]).span()[1])
            storage_pattern = re.compile(r'(\d+)T')
            if storage_pattern.search(ERP_part_name[part_name_end_pointer:]) != None:
                storage_comparison_GB = int(storage_pattern.search(ERP_part_name[part_name_end_pointer:]).groups()[0]) * 1000
                part_name_end_pointer = int(storage_pattern.search(ERP_part_name[part_name_end_pointer:]).span()[1])
            storage_name_result = compare_storage(storage_description_GB, storage_comparison_GB)
            total_check_result["storage"] = storage_name_result

    return total_check_result, {"is_MXM":is_MXM, "description":motherboard_description}