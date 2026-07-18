"""
函数返回的语法格式
"""

# 定义一个函数,完成两数相加
def add(x,y):
    result=x+y
    return result
r=add(3,4)
print(r)

# None用于if判断
def check_age(age):
    if(age>18):
        return "SUCCESS"
    else:
        return None
result=check_age(16)
if not result:
    print("未成年")
    
