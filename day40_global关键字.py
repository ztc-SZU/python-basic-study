# 使用global关键字可以在函数内部声明变量为全局变量
num=100
def fun():
    global num
    num=500
fun()
print(num)