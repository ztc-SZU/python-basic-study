"""
了解异常
"""
# 基本补货语法
try:
    f=open("D:/abc.txt","r",encoding="UTF-8")
except:
    print("出现异常,改用别的方式打开")
    f=open("D:/abc.txt","w",encoding="UTF-8")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现变量未定义异常")

# 捕获多个异常
try:
    print(name)
except (NameError,ZeroDivisionError) as e:
    print("出现变量未定义异常或除以0错误")

try:
    print(1/0)
except (NameError,ZeroDivisionError) as e:
    print("出现变量未定义异常或除以0错误")

# 捕获所有异常
try:
    print(1/0)
except Exception as e:
    print("出现异常")

# else没有异常要执行的代码
try:
    print("hello")
except Exception as e:
    print("出现异常")
else:
    print("太好了,没问题")

# finally无论是否异常都要执行的代码
try:
    f=open("D:/abc.txt","r",encoding="UTF-8")
except Exception as e:
    print("出现异常")
else:
    print("太好了,没问题")
finally:
    f.close()