# import sys
# print(sys.path)
# sys.path.append('D:\\PycharmProjects\\模块')#添加Apath为模块查找路径
import sys
sys.path.append('D:\\PycharmProjects\\模块')
import module_test
module_test.m_t_pr()
print('使用module_test模块中的变量：',module_test.name)


