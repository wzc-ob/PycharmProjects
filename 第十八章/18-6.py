# -*- coding:utf-8 -*-
#
def searchGraph(graph,start,end):         # 搜索树
    result = []
    generatePath(graph,[start],end,result)
    result.sort(key=lambda x:len(x))
    return result
def generatePath(graph,path,end,results):   #生成树
    state  = path[-1]
    if state ==end:
        results.append(path)
    else:
        for arc in graph[state]:
            if arc not in path:
                generatePath(graph,path+[arc],end,results)
if __name__ == '__main__':
    Graph = {'a':['b','c','d'],'b':['e'],'c':['d','f'],'d':['b','e','g'],'e':[],'f':['d','g'],'g':['e']}
    r = searchGraph(Graph,'a','d')
    print('**************************')
    print('       path a to d')
    print('**************************')
    for i in r:
        print(i)
    r = searchGraph(Graph,'a','e')
    print('**************************')
    print('       path a to e')
    print('**************************')
    for i in r:
        print(i)
    r = searchGraph(Graph,'c','e')
    print('**************************')
    print('       path c to e')
    print('**************************')
    for i in r:
        print(i)


