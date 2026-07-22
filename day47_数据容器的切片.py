# 对list开始进行切片,从1开始，4结束，步长为1
my_list=[0,1,2,3,4,5,6]
new_my=my_list[1:4]
print(new_my)

# 对tuple开始进行切片,从头到尾,步长为1
my_list=(0,1,2,3,4,5,6)
new_my=my_list[:]
print(new_my)

# 对str进行切片,从头到尾，步长为2
my_list="0123456"
new_my=my_list[::2]
print(new_my)

# 对str进行切片,从头到尾，步长为-1
my_list="0123456"
new_my=my_list[::-1]
print(new_my) # 反转字符串

# 对列表进行切片，从3到1，步长为-1
my_list=[0,1,2,3,4,5,6]
new_my=my_list[3:1:-1]
print(new_my)

# # 对tuple开始进行切片,从头到尾,步长为-2
my_list=(0,1,2,3,4,5,6)
new_my=my_list[::-2]
print(new_my)
