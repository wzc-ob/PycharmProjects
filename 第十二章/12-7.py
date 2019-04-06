# -*- coding:utf-8 -*-
#
import tkinter
root = tkinter.Tk()
menu  = tkinter.Menu(root ,tearoff = 0)
menu.add_command(label = 'Copy')
menu.add_command(label = 'Paste')
menu.add_separator()
menu.add_command(label = 'Cut')
def popumenu(event):
    menu.post(event.x_root,event.y_root)
root.bind('<Button-3>',popumenu)
root.mainloop()