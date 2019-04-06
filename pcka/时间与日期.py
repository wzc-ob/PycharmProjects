import datetime
print(datetime.datetime.now())
import time
print(time.time())
t1 = datetime.datetime(2015,3,7,23,14,56,139627)
print(t1)
t2 = datetime.datetime.now()
print(t2)
sub =  t2-t1
print(sub.seconds)#时间相差秒数
print(t2.year,t2.month,t2.day,t2.hour,t2.minute,t2.second)