# -*- coding:utf-8 -*-
#
import tkinter
import tkinter.simpledialog
def InStr():
    r = tkinter.simpledialog.askstring('Python tkinter','Input String',
                                       initialvalue = 'tkinter')
    print(r)
def InInt():
    r = tkinter.simpledialog.askinteger('Python tkinter','Input Integer',initialvalue= '1')
    print(r)
def InFlo():
    r = tkinter.simpledialog.askfloat('Python tkinter','InputFloat')
    print(r)
root = tkinter.Tk()
button1 = tkinter.Button(root ,text= 'Input String',command = InStr)
button2 = tkinter.Button(root,text = 'Input Integer',command = InInt)
button3 = tkinter.Button(root ,text = 'Input Float',command = InFlo)
button1.pack(side = 'left')
button2.pack(side = 'left')
button3.pack(side = 'left')
root.mainloop()
