def consumer():
    print('等待接受处理任务。。。')
    while True:
        data =(yield )
        print('收到任务：',data)

def producer():
    c = consumer()
    c.__next__()
    for  i in range(3):
        print('发送一个任务。。','任务%d'%i)
        c.send('任务%d'%i)
if  __name__ =='__main__':
    producer()



