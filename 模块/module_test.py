#模块文件
#文件名称：module_test.py
print('导入的测试模块输出')

name = 'module_test'
def m_t_pr():
    print('模块module_test中的 m_t_pr()函数')

if __name__ =='__main__':
    m_t_pr()
    print(name)#判断是否独立运行



