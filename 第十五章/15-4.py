import threading
import time
class MyThead(threading.Thread):
    def __init__(self,mynum):
        super().__init__()
        self.mynum = mynum
    def run(self):
        time.sleep(1)
        for i in range(self.mynum,self.mynum+5):
            print(str(i*i)+';')
def main():
    print('start..')
    ma = MyThead(1)
    mb = MyThead(16)
    ma.daemon = True
    mb.daemon = True
    ma.start()
    mb.start()
    print('end....')
if __name__ == '__main__':
    main()