# coding:utf-8
import tkinter
import tkinter.messagebox ,tkinter.simpledialog
import os, os.path
import threading
rubbishExt = ['.tmp', '.bak', '.old', '.wbk', '.xlk','.log', '._mp', '.gid', '.chk', '.syd', '$$$', '@@@', '.~*']  #
class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        # 创建菜单
        menu = tkinter.Menu(self.root)
        # 创建“系统”子菜单
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label='关于。。。', command=self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label='退出', command=self.MenuExit)
        menu.add_cascade(label='系统', menu=submenu)

        # 创建"清理"子菜单
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label='扫描垃圾文件', command=self.MenuScanRubbish)
        submenu.add_command(label='删除垃圾文件', command=self.MenuDelRUbbissh)
        menu.add_cascade(label='清理', menu=submenu)

        # 创建"查找"子菜单
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label='搜索大文件', command=self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label='按名称搜索文件', command=self.MenySearchFile)
        menu.add_cascade(label='搜索', menu=submenu)

        self.root.config(menu=menu)

        # 创建标签，用于显示状态信息
        self.progress = tkinter.Label(self.root, anchor=tkinter.W, text='状态', bitmap='hourglass', compound='left')
        self.progress.place(x=10, y=370, width=480, height=15)

        # 创建文本框，显示文件列表
        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10, y=10, width=480, height=350)
        # 为文本添加垂直滚动条
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side='right', fill='y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview()
    def MainLoop(self):
        self.root.title('Findfat')
        self.root.minsize(500, 400)
        self.root.maxsize(1200, 1000)
        self.root.mainloop()
    def MenuAbout(self):
        tkinter.messagebox.showinfo('Findfat', '这是使用python编写的Windows优化程序。\n 欢迎使用并提出宝贵意见')
    def MenuExit(self):
        self.root.quit()
    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion('Findfat', '扫面垃圾文件将需要较长的时间，是否继续？')
        if result == 'no':
            return
        tkinter.messagebox.showinfo('Findfat', '马上开始扫描垃圾文件！')
        self.drives = self.GetDrives()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()
        # self.ScanRubbish()
    def MenuDelRUbbissh(self):
        result = tkinter.messagebox.askquestion('Findfat', '删除垃圾文件需要较长的时间，是否继续？')
        if result == 'no':
            return
        tkinter.messagebox.showinfo('Findfat', '马上开始删除垃圾文件！')
        self.drives = self.GetDrives()
        t = threading.Thread(target=self.DeleteRubbish,args=(self.drives,))
        t.start()
    def MenuScanBigFile(self):
        s = tkinter.simpledialog.askinteger('Findfat','请设置大文件的大小（M）')
        t = threading.Thread(target=self.ScanBigFile,args=(s,))
        t.start()
        # result = tkinter.messagebox.askquestion('Findfat', '扫描大文件需要较长的时间，是否继续？')
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo('Findfat', '马上开始扫描大文件！')
    def MenySearchFile(self):
        s = tkinter.simpledialog.askstring('Findfat','请输入文件名的部分字符')
        t = threading.Thread(target=self.SearchFile,args=(s,))
        t.start()
        # result = tkinter.messagebox.askquestion('Findfat', '按名称搜索文件需要较长的时间，是否继续？')
        # if result == 'no':
        #     return
        # tkinter.messagebox.showinfo('Findfat', '马上开始按名称搜索文件')
    def ScanRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:  # 扩展名在垃圾文件扩展名列表中

                                fname = os.path.join(os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                if total % 15 == 0:
                                    self.flist.delete(0.0, tkinter.END)
                                self.flist.insert(tkinter.END, fname + '\n')
                                l = len(fname)
                                if l > 50:
                                    self.progress['text'] = fname[:30] + '...' + fname[1 - 30:1]
                                else:
                                    self.progress['text'] = fname
                                    total += 1  # 计数
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "找到%s个垃圾文件，共占用%.2f M磁盘空间" % (total, filesize / 1024 / 1024)
    def DeleteRubbish(self,scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root,dirs,files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] =='':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1])>=0:
                                fname = os.path.join(os.path.abspath(root),fil)
                                filesize +=os.path.getsize(fname)
                                try:
                                    os.remove(fname)
                                    l = len(fname)
                                    if l >50:
                                        fname = fname[:25] + '...' +fname[1-25:1]
                                    if total % 15 ==0:
                                        self.flist.delete(0.0,tkinter.END)
                                        self.flist.insert(tkinter.END,'Deleted'+ fname +'\m')
                                        self.progress['text'] = fname
                                        total +=1
                                except:
                                    pass
                        except ValueError:
                            pass
                except Exception as e :
                    print(e)
                    pass
        self.progress['text'] = "删除%s个垃圾文件，共收回%.2f M磁盘空间" % (total, filesize / 1024 / 1024)
    def GetDrives(self):
        drives = []
        for i in range(65, 91):
            vol = chr(i) + ':/'
            if os.path.isdir(vol):
                drives.append(vol)
        return tuple(drives)
    def ScanBigFile(self,filesize):
        total = 0
        filesize = filesize*1024*1024
        for drive in self.GetDrives():
            for root ,dors ,files in os.walk(drive):
                for fil in files:
                    try:
                        fname = os.path.abspath(os.path.join(root,fil))
                        fsize = os.path.getsize(fname)
                        self.progress['text'] = fname
                        if fsize>=filesize:
                            total +=1
                            self.flist.insert(tkinter.END,'%s,[%.2f M]\n'%(fname,fsize/1024/1024))
                    except:
                        pass
        self.progress['text'] = "共找到%s个超过%s M的大文件" % (total, filesize / 1024 / 1024)
    def SearchFile(self,fname):
        total = 0
        fname= fname.upper()
        for drive in self.GetDrives():
            for root ,dirs,files in os.walk(drive):
                for fil in files:
                    try:
                        fn = os.path.abspath(os.path.join(root,fil))
                        l = len(fn)
                        if l>50:
                            self.progress['text'] = fn[:25] +'...' +fn[1-25:1]
                        else:
                            self.progress['text'] = fn
                        if fil.upper().find(fname) >=0:
                            total +=1
                            self.flist.insert(tkinter.END,fn+'\n')
                    except:
                        pass
            self.progress['text'] = '找到%s个文件'%(total)
if __name__ == '__main__':
    window = Window()
    window.MainLoop()