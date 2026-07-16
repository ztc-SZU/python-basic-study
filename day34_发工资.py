# 定义余额
money=10000

# for循环发工资
for i in range(1,21):
    import random
    score=random.randint(1,10)

    if score<5:
        print(f"员工{i}绩效{score}不足，下一位")
        #continue跳过
        continue

    #判断余额不足:
    if money>=1000:
        money-=1000
        print(f"员工{i}发工资1000,公司余额:{money}")
    else:
        print(f"余额不足,当前余额:{money}元,不足以发工资,下月再来")
        #break结束发放
        break