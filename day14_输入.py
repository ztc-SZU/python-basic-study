import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
演示python中输入的使用
"""
name=input("请输入你的名字:")
print("你的名字是: %s" % name)

#输入数字类型
num=input("请告诉我你的银行卡密码:")
num=int(num)
print("你的银行卡密码是: %d" %num)