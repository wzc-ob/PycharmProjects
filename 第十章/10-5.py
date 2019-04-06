class FileMgr:
    def __init__(self,filename):
        self.filename = filename
        self.f = None
    def __enter__(self):
        self.f = open(self.filename,encoding='utf-8')
        return self.f
    def __exit__(self, t,v,tb):
        if self.f:
            self.f.close()
if __name__ == '__main__':
    with FileMgr('10-4.py') as f:
        for line in f.readlines():
            print(line,end='')

