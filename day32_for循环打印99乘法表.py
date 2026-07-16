"""
用for循环打印99乘法表
"""
#外层循环控制行数
for i in range(1,10):
    #内层循环控制每行数据
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()