#-*- coding:utf-8 -*-
import tkinter
root = tkinter.Tk()
label = tkinter.Label(root,text= 'Hello,tkinter')
label.pack()
button1 = tkinter.Button(root,text = 'Button1')
button1.pack(side = tkinter.LEFT)
button2 = tkinter.Button(root,text = 'Button2')
button2.pack(side  =tkinter.RIGHT)
root.mainloop(r)