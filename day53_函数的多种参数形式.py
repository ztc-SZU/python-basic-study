"""
演示多种传参形式
"""
def fun(name,age,gender):
    print(f"姓名:{name},年龄:{age},性别:{gender}")
# 位置参数  默认使用形式
fun("ztc",18,'男')

# 关键字参数
fun(name='ztc',age='18',gender='男')  #可以乱序

# 缺省参数
def fun(name,age,gender='女'):
    print(f"姓名:{name},年龄:{age},性别:{gender}")
fun("ztc",18)

# 不定长的参数作为元组存在
def fun(*args):
    print(args)
fun('ztc',18,'男')

# 不定长的参数作为字典存在
def fun(**kwargs):
    print(kwargs)
fun(name='ztc',age=18,gender='男')