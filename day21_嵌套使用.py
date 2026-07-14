print("欢迎来到动物园")
if int(input("请输入你的身高(cm):"))>=120:
    print("如果你的vip>=3,你可以不需要买票")
    if int(input("请输入你的vip等级:"))>=3:
        print("不需要买票")
    else:
        print("需要买票")
else:
    print("不需要买票")