import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("聚声泰K3查询工具")
width, height = 800, 800
window.geometry("%dx%d+%d+%d" % (width, height,
                                 (window.winfo_screenwidth() - width) / 2,
                                 (window.winfo_screenheight() - height) / 2))
left_tree = ttk.Treeview(window, height=30)
# 添加作为标识
# 参数:parent, index, iid=None, **kw (父节点，插入的位置，id，显示出的文本)


def showvalue(self, textvalue):
    ls = ['料号:3.01.1001', '库存:400', '入库数:600']
    label_value.config(text=ls)


def getvalue(self):
    item = left_tree.selection()[0]
    print("you clicked on ", left_tree.item(item, "values"))
    showvalue(self, left_tree.item(item, "values"))


primary1 = left_tree.insert("", 0, "出货成品", text="出货成品(9.xx)", value="9.xx")
child1_1 = left_tree.insert(primary1, 0, '耳机出货', text='耳机出货(9.01)', value='9.01')
child1_2 = left_tree.insert(primary1, 2, '喇叭出货', text='喇叭出货(9.02)', value='9.02')
child1_3 = left_tree.insert(primary1, 0, '麦克风出货', text='喇叭出货(9.03)', value='9.03')
primary2 = left_tree.insert("", 0, "原材料", text="原材料(3.xx)", value="3.xx")
child1_1 = left_tree.insert(primary2, 1, '约克', text='约克(3.01)', value='3.01')
left_tree.insert(child1_1, 1, '3.01.10001', text='3.01.10001',
                 value='3.01.10001')
child1_2 = left_tree.insert(primary2, 2, '华司', text='华司(4.01)', value='4.01')
child1_3 = left_tree.insert(primary2, 0, '漆包线', text='漆包线(5.01)', value='5.01')
left_tree.bind('<Double-1>', getvalue)
left_tree.pack()
label_value = tk.Label(window, bg='red', width=20, height=20)
label_value.pack()

window.mainloop()


# 有很多的一级节点,名字都要不同,以此类推
# 应该这样命名,一级节点 primary1,该节点下 二级节点
# child1_1/child1_2/child1_3 该节点下的三级节点
# child1_1_1/child1_1_2/child1_1_3/child1_2_1/child_2_2/child_2_3
