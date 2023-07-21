from connect import open_connect, close_connect
from checker import motherboard_checker

def main_checker(name: str) -> list:
    connection, cursor = open_connect()
    motherboard_check_result, error_msg = motherboard_checker(name, cursor)
    print(motherboard_check_result)
    print(error_msg)
    
    
    # print(check_devices_to_dict)
    close_connect(connection, cursor)
    return [error_msg]