# 演示循环中断语句continue
for i in range(1,11):
    print("语句1")
    continue
    print("语句2")

# 演示continue嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")
print("语句4")

#演示break嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
print("语句4")
