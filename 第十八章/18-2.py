# -*- coding:utf-8 -*-
#
class PyQueue:
    def __init__(self,size = 20):
        self.queue = []
        self.size = size
        self.end = -1
    def SetSize(self,size):
        self.size = size
    def In(self,element):
        if self.end<self.size-1:
            self.queue.append(element)
            self.end = self.end+1
        else:
            raise QueueException('PuQueueFull')
    def Out(self):
        if self.end!=-1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end = self.end-1
            return element
        else:
            raise QueueException('PyQueueEmpty')
    def End(self):
        return self.end
    def empty(self):
        self.queue = []
        self.end = [-1]

class QueueException(Exception):
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return self.data
if __name__ == '__main__':
    queue = PyQueue()
    for i in range(10):
        queue.In(i)
    print(queue.End())
    for i in range(10):
        print(queue.Out())
    for i in range(20):
        queue.In(i)
    queue.empty()
    for i in range(20):
        print(queue.Out())