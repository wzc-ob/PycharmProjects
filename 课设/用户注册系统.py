# coding:utf-8
import tkinter
import tkinter.messagebox
import sqlite3
con = sqlite3.connect('login.db')
cur = con.cursor()
from register import RegisterWindow
from success import NewWindow
class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        # 创建菜单
        self.usernamelabel  = tkinter.Label(self.root,text = '用户名',
                                      bg = 'blue')
        self.usernamelabel.place(relx= 0.3,rely =0.11,relwidth = 0.1,relheight = 0.05)
        self.passwordlabel = tkinter.Label(self.root, text='密码',
                                           bg='red')
        self.passwordlabel.place(relx=0.3, rely=0.21, relwidth=0.1, relheight=0.05)
        #用户名和密码输入`
        self.loginusername = tkinter.StringVar()
        self.loginpassword = tkinter.StringVar()

        self.loginusernameEntry = tkinter.Entry(self.root,textvariable = self.loginusername)
        self.loginusernameEntry.place(relx=0.45,rely = 0.11,  width=150,relheight = 0.05,height = 1)
        self.loginpasswordEntry = tkinter.Entry(self.root,show = '*',textvariable = self.loginpassword)
        self.loginpasswordEntry.place(relx=0.45, rely=0.20, width=150, relheight=0.05)
        #登陆
        self.loginbutton = tkinter.Button(self.root, text='登录', anchor=tkinter.N,
                                             width=20, height=1,command = self.Login)
        self.loginbutton.place(relx=0.35, rely=0.3, relwidth=0.1, relheight=0.07)
        #注册
        self.loginbutton = tkinter.Button(self.root,text = '注册',anchor = tkinter.N,
                                          width = 20,height =1,command = self.Register)
        self.loginbutton.place(relx = 0.45,rely =0.3,relwidth = 0.1,relheight =0.07)
        #退出
        self.exitbutton = tkinter.Button(self.root, text='退出', anchor=tkinter.N,
                                          width=20, height=1, command=self.Exit)
        self.exitbutton.place(relx=0.55, rely=0.3, relwidth=0.1, relheight=0.07)
    def MainLoop(self):
        self.root.title('用户注册系统')
        self.root.minsize(500, 400)
        self.root.maxsize(1200, 1000)
        self.root.mainloop()
    def Exit(self):
        self.root.destroy()
    def Register(self):
        registerwindow = RegisterWindow()
        registerwindow.MainLoop()
    def Login(self):
        if self.loginusername.get() :
            if self.loginpassword.get():
                cur.execute('SELECT *FROM mytab')
                for item, username, password,people in cur.fetchall():
                    # print(username, password,people)
                    if username == self.loginusername.get() and password == self.loginpassword.get():
                        # tkinter.messagebox.showinfo('用户注册系统', '登陆成功')
                        newwindow = NewWindow(username,password,people)
                        newwindow.MainLoop()
                        break
                else:
                    if username == self.loginusername.get():
                        tkinter.messagebox.showinfo('用户注册系统','密码错误')
                    else:
                        tkinter.messagebox.showinfo('用户注册系统', '用户名错误')

            else:
                tkinter.messagebox.showinfo('用户注册系统', '密码不能为空')
        else:
            tkinter.messagebox.showinfo('用户注册系统', '用户名不能为空')
if __name__ == '__main__':
    registerwindow = Window()
    registerwindow.MainLoop()