# 导入自定义模块并使用
from fun import test
test(1,2)

# 导入不同模块的同名功能
from fun import test
from fun1 import test
test(1,2)  # 调用后面模块的功能

# __main__
from fun import test
test(1,2)

# __all__变量   当使用from xxx import *,只能引入某个功能
from fun import *
testa()
#  testb()会报错