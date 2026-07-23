# 定义一个函数，接收其他函数输入
def fun(compute):
    result=compute(1,2)
    print(result)
# 通过lambda匿名函数，将匿名函数作为形式参数传入
fun(lambda x,y:x+y)