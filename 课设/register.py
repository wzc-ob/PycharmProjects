# coding:utf-8
from abc import abstractclassmethod,ABCMeta
import tkinter
import tkinter.messagebox
import sqlite3
con = sqlite3.connect('login.db')
cur = con.cursor()
# cur.execute('CREATE TABLE mytab(id integer PRIMARY KEY AUTOINCREMENT NOT NULL ,name text,passwd text)')
from functools import wraps
def singleton(cls):
    global instances
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance
@singleton
class RegisterWindow:
    def __init__(self):
        self.root = tkinter.Toplevel()
        self.root.attributes('-topmost', 1)
        global registerusername
        global registerpassword
        registerusername = tkinter.StringVar()
        registerpassword = tkinter.StringVar()
        self.value = tkinter.StringVar()
        self.value.set('学生')
        self.systemlabel = tkinter.Label(self.root, text='用户注册系统',height = 2
                                          )
        self.systemlabel.pack()
        self.usernamelabel  = tkinter.Label(self.root,text = '用户名',
                                      bg = 'blue')
        self.usernamelabel.place(relx= 0.3,rely =0.11,relwidth = 0.1,relheight = 0.05)
        self.passwordlabel = tkinter.Label(self.root, text='密码',
                                           bg='red')
        self.passwordlabel.place(relx=0.3, rely=0.21, relwidth=0.1, relheight=0.05)
        #用户名和密码输入

        self.registerusernameEntry = tkinter.Entry(self.root,textvariable = registerusername)
        self.registerusernameEntry.place(relx=0.45,rely = 0.11,  width=150,relheight = 0.05,height = 1)
        self.loginpasswordEntry = tkinter.Entry(self.root,show = '*',textvariable = registerpassword)
        self.loginpasswordEntry.place(relx=0.45, rely=0.20, width=150, relheight=0.05)

        #身份选择
        self.studengradio = tkinter.Radiobutton(self.root,variable = self.value,value = '学生',text = '学生')
        self.studengradio.place(relx = 0.35,rely =0.3)
        self.teacherradio = tkinter.Radiobutton(self.root,variable = self.value,value = '教师',text = '教师')
        self.teacherradio.place(relx = 0.45,rely =0.3)



        #注册
        self.registerbutton = tkinter.Button(self.root,text = '注册',anchor = tkinter.N,
                                          width = 20,height =1,command = self.GetUsername)
        self.registerbutton.place(relx = 0.35,rely =0.4,relwidth = 0.1,relheight =0.07)
        #退出
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
    def GetUsername(self):
        self.people = PeopleFactory().create_people(self.value.get())
        # print(self.value.get())
        # for item, username, password in cur.fetchall():
        #     print(item)
        if registerusername.get():
            if registerpassword.get():
                # print(self.registerusername.get(),self.registerpassword.get())
                cur.execute('SELECT *FROM mytab')
                for item, username, password,people in cur.fetchall():
                    if username == registerusername.get():
                        tkinter.messagebox.showinfo('用户注册系统', '该用户名已经被使用')
                        break
                else:
                    self.people.register()
                    self.registerusernameEntry.delete(0, 'end')
                    self.loginpasswordEntry.delete(0, 'end')
                    # tkinter.messagebox.showinfo('用户注册系统', '注册成功')
            else:
                tkinter.messagebox.showinfo('用户注册系统','密码不能为空')
        else:
            tkinter.messagebox.showinfo('用户注册系统','用户名不能为空')

def abc(myclass):
    class Innerclass:
        def __init__(self):
            self.wrapper = myclass()
        def register(self):
            self.wrapper.register()
            tkinter.messagebox.showinfo('用户注册系统', '注册成功')
    return Innerclass




class People(metaclass=ABCMeta):
    @abstractclassmethod
    def register(self):
        pass

@abc
class Student(People):
    def register(self):
        cur.execute('INSERT INTO mytab(name,passwd,people)VALUES(?,?,?)',
                    (registerusername.get(),registerpassword.get(),'学生'))
        con.commit()

@abc
class Teacher(People):
    def register(self):
        cur.execute('INSERT INTO mytab(name,passwd,people)VALUES(?,?,?)',
                    (registerusername.get(), registerpassword.get(),'教师'))
        con.commit()

class PeopleFactory():

    def create_people(self, type):
        map_ = {
            '学生': Student(),
            '教师': Teacher()
        }
        return map_[type]

if __name__ == '__main__':

    window = RegisterWindow()
    window.MainLoop()