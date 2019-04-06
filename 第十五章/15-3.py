import threading
import time
def thrfun(x,y,thr = None):
    if thr:
        thr.join()
    else:
        time.sleep(2)
    for i in range(x,y):
        print(str(i*i)+';')
ta = threading.Thread(target=thrfun,args=(1,6))
tb = threading.Thread(target=thrfun,args=(16,21,ta))
ta.start()
tb.start()