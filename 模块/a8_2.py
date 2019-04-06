#调用自己写的模块
#文件名a8_2.py
import module_test
module_test.m_t_pr()
print('使用module_test模块中的变量：',module_test.name)

import py_compile;
py_compile.compile('a8_2.py','a8_2.pyc')
