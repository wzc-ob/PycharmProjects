# def file_hdl(name ='python.txt'):
#     f = open(name)
#     res = 0
#     i =0
#     for line in f :
#         i+=1
#         print('第%s行的数据为：'%line.strip(),line)
#         res +=int(line)
#     print('这些数的和为：',res)
#     f.close()
# if __name__ == '__main__':
#     file_hdl()

def file_hdl(name = 'python.txt'):
    with open(name) as f :
        res = 0
        i= 0
        for line in f :
            i +=1
            print('第%s行的数据为：' % line.strip(), line)
            res +=int(line)
    print('这些数的和为：', res)
    f.close()
if __name__ == '__main__':
    file_hdl()