import tkinter
import sqlite3
import tkinter.messagebox
con = sqlite3.connect('login.db')
cur = con.cursor()

def singleton(cls):
    global instances
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance
@singleton
class NewWindow(object):
    def __init__(self,username,password,people):
        self.root = tkinter.Toplevel()
        self.root.attributes('-topmost', 1)

        self.username= tkinter.StringVar()
        self.password= tkinter.StringVar()
        self.people = tkinter.StringVar()
        self.usernamelabel = tkinter.Label(self.root, text='用户名',
                                           bg='blue')
        self.usernamelabel.place(relx=0.3, rely=0.11, relwidth=0.1, relheight=0.05)
        self.passwordlabel = tkinter.Label(self.root, text='密码',
                                           bg='red')
        self.passwordlabel.place(relx=0.3, rely=0.21, relwidth=0.1, relheight=0.05)
        self.peoplelabel = tkinter.Label(self.root, text='身份',
                                           bg='yellow')
        self.peoplelabel.place(relx=0.3, rely=0.31, relwidth=0.1, relheight=0.05)



        self.registerusernameEntry = tkinter.Entry(self.root,textvariable  =self.username,state = 'readonly')
        self.registerusernameEntry.place(relx=0.45, rely=0.11, width=150, relheight=0.05, height=1)
        self.username.set(username)
        self.password.set(password)
        self.loginpasswordEntry = tkinter.Entry(self.root,show = '*',textvariable  = self.password)
        self.loginpasswordEntry.place(relx=0.45, rely=0.20, width=150, relheight=0.05)


        self.loginpeopleEntry = tkinter.Entry(self.root,textvariable=self.people,state = 'readonly')
        self.loginpeopleEntry.place(relx=0.45, rely=0.30, width=150, relheight=0.05)
        self.people.set(people)

        self.changebutton = tkinter.Button(self.root,text = '修改',anchor=tkinter.N,
                                         width=20, height=1,command = self.Update)
        self.changebutton.place(relx=0.35, rely=0.4, relwidth=0.1, relheight=0.07)
        self.exitbutton = tkinter.Button(self.root, text='退出', anchor=tkinter.N,
                                         width=20, height=1, command=self.Exit)
        self.exitbutton.place(relx=0.55, rely=0.4, relwidth=0.1, relheight=0.07)
        self.root.protocol("WM_DELETE_WINDOW", self.Exit)

    def MainLoop(self):
        self.root.title('用户注册系统')
        self.root.minsize(500, 400)
        self.root.maxsize(1200, 1000)
        self.root.mainloop()
    def Exit(self):
        instances.clear()
        self.root.destroy()
    def Update(self):
        if  self.password.get():
            cur.execute('UPDATE mytab SET passwd=? WHERE name=?',(self.password.get(),self.username.get()))
            con.commit()
            tkinter.messagebox.showinfo('用户注册系统','修改成功')
        else:
            tkinter.messagebox.showinfo('用户注册系统','密码不能为空')

if __name__ == '__main__':
    newwindow = NewWindow(1,1,'学生')
    newwindow.MainLoop()