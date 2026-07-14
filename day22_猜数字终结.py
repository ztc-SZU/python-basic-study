import random
num=random.randint(1,100)
guess_num=int(input("请输入你猜的数字:"))
if guess_num==num:
    print("恭喜你猜对了")
else:
    if guess_num>num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")
    guess_num=int(input("猜错了，再猜一次:"))
    if(guess_num==num):
        print("你猜对了"  )
    else:
        if guess_num>num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")
        guess_num=int(input("猜错了，再猜一次:"))
        if(guess_num==num):
            print("恭喜你最后一次猜对了")
        else:
            print("你三次都没有猜对，游戏结束")
            