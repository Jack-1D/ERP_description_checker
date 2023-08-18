'''
抓取本機IPv4地址
'''
import os, re
def get_ipv4(PORT: int) -> None:
    '''ipv4地址寫檔至Server_Address.txt'''
    ip_list = []
    ip_result = os.popen('ipconfig','r').read()
    ip_result = re.finditer(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ip_result, re.I)
    for ip in ip_result:
        ip_list.append(ip.group())
    with open('Server_Address.txt', 'w') as f:
        f.write(f"https://{ip_list[2]}:{PORT}/")
    return