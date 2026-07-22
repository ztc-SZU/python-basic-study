# 定义集合
my_set={0,1,2,3,3,2,1,0}
my_set1=set()
print(my_set)
print(my_set1)

# 不支持下表索引访问，因为乱序
my_set.add(5)
print(my_set)

# 移除元素
my_set.remove(5)
print(my_set)

# 随机取出一个元素
element=my_set.pop()
print(f"集合为:{my_set},取出的元素为:{element}")

# 清空集合
my_set.clear()
print(my_set)

# 取2个集合的差集
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(set3)
print(set1)
print(set2) # 得到新集合，原来的两个集合不变

# 消除2集合的差集
set1={1,2,3}
set2={1,5,6}
set1.difference_update(set2)
print(set1)
print(set2) # 集合1修改。集合2不变

# 2个集合合并
set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(set3)
print(set1)
print(set2) # 得到新集合，原来的两个集合不变

# 统计集合元素的数量
my_set={0,1,2,3,3,2,1,0}
print(len(my_set))

# 集合的遍历,不可以用while,可以用for
for it in my_set:
    print(it)