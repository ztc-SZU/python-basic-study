#生成一个随机数
import random
num=random.randint(1,100)
#count记录猜了多少次
count=0
#flag判断循环是否结束
flag=True
while flag:
    guess_num=int(input("请输入你猜测的数字:"))
    count+=1
    if guess_num==num:
        print("猜对了")
        flag=False
    else:
        if guess_num>num:
            print("你猜的大了")
        else:
            print("你猜的小了")
