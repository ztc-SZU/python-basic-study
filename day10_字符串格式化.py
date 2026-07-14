# 通过占位的方式来拼接
name="ZTC"
message="我的名字是: %s" % name
print(message)
 
#通过占位的方式完成数字和字符串的拼接
name="ZTC"
age=18
message="我的名字是: %s,我的年龄是: %d" % (name,age)
print(message)

mark=4.08
message="我的名字是: %s,我的年龄是: %d,我的成绩是: %.2f" % (name,age,mark)
print(message)

# 快速格式化
name="博客"
price=19.99
year=2006
print(f"我的名字是: {name},我的价格是: {price},我的年龄是: {year}")