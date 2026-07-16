"""
while嵌套案例
"""
#外层循环，表白10次
#内层循环，10朵玫瑰
i=1
while i<=10:
    print(f"今天是第{i}天表白")
    j=1
    while j<=10:
        print(f"这是第{j}朵玫瑰")
        j+=1
    print("小美我喜欢你")
    i+=1
