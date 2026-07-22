my_str="ztc szu acm"
# 按下标索引
value_1=my_str[0]
value_2=my_str[-1]
print(value_1)
print(value_2)

# 字符串是一个无法修改的容器

# index方法
print(my_str.index("szu"))

# replace
new_str=my_str.replace("szu","and")
print(new_str)

# split字符串分割
my_str_list=my_str.split(" ")
print(f"分割后{my_str_list},类型:{type(my_str_list)}")

# strip方法
my_str="  ztc szu acm  "
new_str=my_str.strip()
print(f"原字符串是:{my_str},新字符串是:{new_str}")
my_str="12ztc szu acm21"
new_str=my_str.strip("12")
print(f"原字符串是:{my_str},新字符串是:{new_str}")  # 按照单个字符‘1’，‘2’移除

# 统计字符串出现的次数
count=my_str.count("ztc")
print(count)

# 统计字符串出现的长度
len=len("my_str")
print(len)