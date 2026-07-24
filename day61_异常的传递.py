def fun1():
    print("fun1开始执行")
    print(1/0)
    print("fun1结束执行")
def fun2():
    print("fun2开始执行")
    fun1()
    print("fun2结束执行")
def main():
    try:
        fun2()
    except Exception as e:
        print(e)

main()