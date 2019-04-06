#coding:utf-8

import tkinter
import tkinter.messagebox

class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        #创建菜单
        menu = tkinter.Menu(self.root)
        #创建“系统”子菜单
        submenu  = tkinter.Menu(menu,tearoff=0)
        submenu.add_command(label = '关于。。。',command = self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label = '退出',command = self.MenuExit)
        menu.add_cascade(label='系统',menu= submenu)

        #创建"清理"子菜单
        submenu = tkinter.Menu(menu,tearoff = 0)
        submenu.add_command(label='扫描垃圾文件',command = self.MenuScanRubbish)
        submenu.add_command(label='删除垃圾文件',command = self.MenuDelRUbbissh)
        menu.add_cascade(label='清理',menu=submenu)

        #创建"查找"子菜单
        submenu = tkinter.Menu(menu,tearoff= 0)
        submenu.add_command(label= '搜索大文件',command = self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label = '按名称搜索文件',command = self.MenySearchFile)
        menu.add_cascade(label= '搜索',menu= submenu)

        self.root.config(menu= menu)

        #创建标签，用于显示状态信息
        self.progress = tkinter.Label(self.root,anchor = tkinter.W,text = '状态',bitmap = 'hourglass',compound= 'left')
        self.progress.place(x = 10,y=370,width = 480,height = 350)

        #创建文本框，显示文件列表
        self.flist = tkinter.Text(self.root)
        self.flist.place(x= 10 ,y = 10,width = 480,height = 350)
        #为文本添加垂直滚动条
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side = 'right',fill = 'y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview()

    def MainLoop(self):
        self.root.title('Findfat')
        self.root.minsize(500,400)
        self.root.maxsize(500,400)
        self.root.mainloop()

    def MenuAbout(self):
        tkinter.messagebox.showinfo('Findfat','这是使用python编写的Windows优化程序。\n 欢迎使用并提出宝贵意见')
    def MenuExit(self):
        self.root.quit()
    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion('Findfat','扫面垃圾文件将需要较长的时间，是否继续？')
        if result =='no':
            return
        tkinter.messagebox.showinfo('Findfat','马上开始删除垃圾文件！')
    def MenuDelRUbbissh(self):
        result = tkinter.messagebox.askquestion('Findfat','删除垃圾文件需要较长的时间，是否继续？')
        if result == 'no':
            return
        tkinter.messagebox.showinfo('Findfat','马上开始删除垃圾文件！')
    def MenuScanBigFile(self):
        result = tkinter.messagebox.askquestion('Findfat','扫描大文件需要较长的时间，是否继续？')
        if result == 'no':
            return
        tkinter.messagebox.showinfo('Findfat','马上开始扫描大文件！')
    def MenySearchFile(self):
        result = tkinter.messagebox.askquestion('Findfat','按名称搜索文件需要较长的时间，是否继续？')
        if result == 'no':
            return
        tkinter.messagebox.showinfo('Findfat','马上开始按名称搜索文件')
if __name__ == '__main__':
    window = Window()
    window.MainLoop()