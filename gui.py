import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib
import snmp_func
host = 'localhost'

# 设置主窗口
root_window = tk.Tk()
root_window.title('snmp监控程序')
root_window.geometry('900x600')

# cpu
text1= tk.Label(root_window, text="CPU")
cpu = snmp_func.get_cpu(host)
text2 = tk.Label(root_window, text=round(cpu,2))
text3 = tk.Label(root_window,text = "%")
text1.place(x=10,y=20)
text2.place(x=40,y=20)
text3.place(x=80,y=20)

# memory
text4= tk.Label(root_window, text="内存")
memory = snmp_func.get_memory(host)
text5 = tk.Label(root_window, text=round(memory[0],2))
text6 = tk.Label(root_window,text = "G")
text4.place(x=10,y=40)
text5.place(x=40,y=40)
text6.place(x=80,y=40)

text7= tk.Label(root_window, text="内存占用率")
text8 = tk.Label(root_window, text=round(memory[1],2))
text9 = tk.Label(root_window,text = "%")
text7.place(x=10,y=60)
text8.place(x=80,y=60)
text9.place(x=120,y=60)

# 磁盘
disk = snmp_func.get_disk(host)
text10= tk.Label(root_window, text="磁盘")
text10.place(x=10,y=80)

list1 = tk.Listbox(root_window,width=100)
list1.place(x=40,y=80)

for item in disk:
    list1.insert("end", item)

# 流量
flow = snmp_func.get_flow(host)
text11= tk.Label(root_window, text="流入流量（Mb）")
text12 = tk.Label(root_window, text=round(flow[0],2))
text13= tk.Label(root_window, text="流出流量（Mb）")
text14 = tk.Label(root_window,text =round(flow[1],2))
text11.place(x=10,y=280)
text12.place(x=120,y=280)
text13.place(x=10,y=300)
text14.place(x=120,y=300)

# 设置阈值
entry1 = tk.Entry(root_window)
entry2 = tk.Entry(root_window)
entry1.place(x=10, y=340)
entry2.place(x=10,y=380)
# 插入默认文本
entry1.insert(0,'输入cpu的阈值')
entry2.insert(0,'输入内存的阈值')


def cpu_callback():
    # 得到输入框字符串
    cpu_limit = entry1.get()
    if int(cpu_limit) < cpu:
        messagebox.showinfo(title='温馨提示', message='CPU超出阈值')

def memory_callback():
    memory_limit = entry2.get()
    if int(memory_limit) < memory[1]:
        messagebox.showinfo(title='温馨提示', message='内存超出阈值')
# 使用按钮控件调用函数
b1 = tk.Button(root_window, text="设置cpu阈值", command=cpu_callback).place(x=10,y=420)
b2 = tk.Button(root_window, text="设置内存阈值", command=memory_callback).place(x=10,y=460)

entry3 = tk.Entry(root_window)
entry3.place(x=10, y=500)
# 插入默认文本
entry3.insert(0,'输入要监控的ip')
# 默认为localhost,如果要修改就取消这行注释
# host = entry3.get()

root_window.mainloop()