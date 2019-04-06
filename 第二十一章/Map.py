#coding:utf-8
import os,os.path,re
def Map(sourceFile,targetFoder):
    sFile = open(sourceFile,'r')
    dataLine =sFile.readline()
    tempData = {}
    if not os.path.isdir(targetFoder):
        os.mkdir()
    while dataLine:
        p_re = re.compile(r'(open|register)\s(.*?)\s(ok|successed)',re.IGNORECASE)
        match = p_re.findall(dataLine)
        if match:
            visitUrl = match[0][1]
            if visitUrl in tempData:
                tempData[visitUrl] +=1
            else:
                tempData[visitUrl] =1
        dataLine = sFile.readline()
    sFile.close()
    tList = []
    for key,value in sorted(tempData.items(),key= lambda k:k[1],reverse= True):
        tList.append(key+'  '+str(value)+'\n')
    tFilename = os.path.join(targetFoder,os.path.split(sourceFile)[1]+'_map.txt')
    tFile = open(tFilename,'a+')
    tFile.close()
if __name__ == '__main__':
    Map('access\\access.log1.txt','access')
    Map('access\\access.log2.txt','access')
    Map('access\\access.log3.txt','access')