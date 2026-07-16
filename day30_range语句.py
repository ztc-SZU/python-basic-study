"""
python语句中range()使用
"""

# 语法1 range(num)
for x in range(10):
    print(x)

# 语法2 range(num1,num2)
for x in range(5,10):
#从5到9，不包括10
    print(x)

# 语法3 range(num1,num2,step)
for x in range(5,10,2):
#输出5,7,9
    print(x)
    