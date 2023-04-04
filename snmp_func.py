from snmp_cmds import snmpwalk
from snmp_cmds import snmpget
import numpy as np

# cpu .1.3.6.1.2.1.25.3.3.1.2
# cpu不能一下子计算内存占用率，要取他们的平均值
def get_cpu(host):
    # cpu负载
    res = snmpwalk(ipaddress=host, oid='.1.3.6.1.2.1.25.3.3.1.2', community='public')
    sum = 0
    for line in res:
        sum += int(line[1])
    # oid表示cpu的负载，我的电脑是8核，所以乘以8
    return sum/ (8*len(res)) * 100

# 每个进程占据的ram：1.3.6.1.2.1.25.5.1.1.2
# 内存总的大小：.1.3.6.1.2.1.25.2.2.0
# 查询到内存的使用量，再除以内存总量就是使用率
def get_memory(host):
    # 内存总大小（Kb）
    memory_size = snmpget(ipaddress=host,oid='.1.3.6.1.2.1.25.2.2.0',community='public')
    # 内存使用量
    res = snmpwalk(ipaddress=host, oid='1.3.6.1.2.1.25.5.1.1.2', community='public')
    sum = 0
    for line in res:
        sum += int(line[1])
    memory_occupation = sum /int(memory_size)*100
    return int(memory_size)/1024/1024,memory_occupation

# 磁盘中簇的数目:.1.3.6.1.2.1.25.2.3.1.5
# 磁盘使用簇的数目：.1.3.6.1.2.1.25.2.3.1.6
def get_disk(host):
    description = snmpwalk(ipaddress=host, oid='.1.3.6.1.2.1.25.2.3.1.3', community='public')
    disk_total = snmpwalk(ipaddress=host, oid='.1.3.6.1.2.1.25.2.3.1.5', community='public')
    disk_occu = snmpwalk(ipaddress=host, oid='.1.3.6.1.2.1.25.2.3.1.6', community='public')
    disk_info =  [[] for i in range(len(description))]
    for i in range(len(disk_info)):
        disk_info[i].append(description[i][1])
        disk_info[i].append(round(int(disk_total[i][1])/1024/1024,2))
        #disk_info[i].append(int(disk_occu[i][1])/int(disk_total[i][1]))
    return disk_info

# 收到的流量：.1.3.6.1.2.1.2.2.1.10
# 发送的流量：.1.3.6.1.2.1.2.2.1.16
def get_flow(host):
    # 收到的流量（b）
    rec_flow = snmpwalk(ipaddress = host , oid = '.1.3.6.1.2.1.2.2.1.10',community= 'public')
    rec_sum = 0
    for i in rec_flow:
        rec_sum += int(i[1])
    send_flow  = snmpwalk(ipaddress = host , oid = '.1.3.6.1.2.1.2.2.1.16',community= 'public')
    send_sum = 0
    for i in send_flow:
        send_sum += int(i[1])
    return rec_sum/1024/1024,send_sum/1024/1024

if __name__ == "__main__":
    host = 'localhost'
    cpu = get_cpu(host)
    memory_size,memory_occupation  = get_memory(host)
    print(cpu,"%")
    print(memory_size,"G")
    print(memory_occupation,"%")

    disk_total = get_disk(host)
    print(disk_total)

    rec_flow,send_flow = get_flow(host)
    print(rec_flow,"Mb ",send_flow,"Mb")