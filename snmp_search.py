from snmp_cmds import snmpwalk
from snmp_cmds import snmpget

# snmpwalk 遍历父节点
# snmpget 具体到单独的节点
# 如果报错，就检查下是不是oid不是子节点或者父节点
host = 'localhost'
oid  = input("请输入oid：")
res = snmpwalk(ipaddress=host,oid=oid,community='public')

for line in res:
    for i in line:
        print(i,end = "  ")
    print()

