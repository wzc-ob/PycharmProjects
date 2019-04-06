#coding:utf-8
import os,os.path,time
def FileSplit(sourceFile,targetFoder):
    sFile = open(sourceFile,'r')
    number = 50
    dataLine = sFile.readline()
    tempData = []
    fileNum = 1
    if not os.path.isdir(targetFoder):
        os.mkdir(targetFoder)
    while dataLine:
        for row in range(number):
            tempData.append(dataLine)
            dataLine = sFile.readline()
            if not  dataLine:
                break
        tFilename = os.path.join(targetFoder,os.path.split(sourceFile)[1]+str(fileNum)+'.txt')
        tFile = open(tFilename,'a+')
        # tFile.writelines(tempData)
        tFile.writelines(tempData)
        tFile.close()
        tempData = []
        print(tFilename+'创建于：'+str(time.ctime()))
        fileNum +=1
    sFile.close()
if __name__ == '__main__':
    FileSplit('access.log','access')