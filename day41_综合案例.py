# 定义全局变量money name
money=5000000
name=None

# 要求客户输入姓名
name=input("请输入你的姓名:")

# 定义查询函数
def query(show_header):
    if show_header: 
        print("-----查询余额-----")
    print(f"{name},你好,你的余额剩余{money}元")

# 定义存款函数
def saving(num):
    global money
    money+=num
    print("-----存款-----")
    print(f"{name},你好,你的存款{num}元成功")
    # 调用query函数查询余额
    query(False)
 # 定义取款函数
def get_money(num):
    global money
    money-=num
    print("-----取款-----")
    print(f"{name},你好,你的取款{num}元成功")
    # 调用query函数查询余额
    query(False)   
# 定义主菜单函数
def main():
    print("-----主菜单-----")
    print(f"{name},欢迎来到银行 请选操作")
    print("查询余额\t[输入1]")
    print("存款\t[输入2]")
    print("取款\t[输入3]")
    print("退出\t[输入4]")
    return input("请输入你的选择:")

# 设置无限循环,程序不退出
while True:
    keyboard=main()
    if keyboard=="1":
        query(True)
        continue
    elif keyboard=="2":
        num=int(input("输入你要输入多少钱，请输入"))
        saving(num)
        continue
    elif keyboard=="3":
        num=int(input("输入你要取出多少钱，请输入"))
        get_money(num)
        continue
    elif keyboard=="4":
        print("程序退出啦:")
        break  # 通过break退出循环
