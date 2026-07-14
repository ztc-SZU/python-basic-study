"""
猜数字游戏
"""
num=5
if int(input("请输入你猜的数字:"))==num:
    print("恭喜你猜对了")
elif int(input("猜错了，再猜一次:"))==num:
    print("你猜对了")
elif int(input("猜错了，再猜一次:"))==num:
    print("恭喜你最后一次猜对了")
else:
    print("你三次都没有猜对，游戏结束")