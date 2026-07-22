"""
演示数据容器之list
"""
# 定义一个列表
my_list=["ztc","szu","acm"]
print(my_list)

# 列表嵌套
my_list=[[1,2,3],[4,5,6]]
print(my_list)

my_list=["ztc","szu","acm"]
# 下表索引,从前往后
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 从后往前
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取出嵌套列表的元素
my_list=[[1,2,3],[4,5,6]]
print(my_list[1][1])