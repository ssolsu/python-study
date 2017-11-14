import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("tree_view")
width, height = 800, 800
window.geometry("%dx%d+%d+%d" % (width, height,
                                 (window.winfo_screenwidth() - width) / 2,
                                 (window.winfo_screenheight() - height) / 2))
left_tree = ttk.Treeview(window,height=30)
#添加作为标识
primary_node = left_tree.insert("", 0, "出货成品", text="中国China", values=("1"))
child_node = left_tree.insert(primary_node, 0, "广东", text="中国广东", values=("2"))
left_tree.pack()
window.mainloop()
