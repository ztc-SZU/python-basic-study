# 1.查找某元素在列表内下标的索引
my_list=["ztc","szu","acm"]
index=my_list.index("szu")
print(index)

# 2.修改特定下标索引的值
my_list[2]="python"
print(my_list)

# 3.指定下标插入新元素
my_list.insert(1,"like")
print(my_list)

# 4.在列表尾部追加单个新元素
my_list.append("111")
print(my_list)

# 5.在列表尾部追加一批新的元素
list2=[1,2,3]
my_list.append(list2)
print(my_list)

# 6.删除指定下标索引的元素
my_list=["ztc","szu","acm"]
del my_list[1]
print(my_list)
my_list=["ztc","szu","acm"]
element=my_list.pop(1)
print(my_list)
print(element)

# 7.删掉列表中第一个匹配项
my_list=["ztc","ztc","szu","acm"]
my_list.remove("ztc")
print(my_list)

# 8.清除列表
my_list.clear()
print(my_list)

# 9.统计某个元素在列表中的数量
my_list=["ztc","ztc","szu","acm"]
count=my_list.count("ztc")
print(count)

# 10.统计列表中元素的数量
count=len(my_list)
print(count)