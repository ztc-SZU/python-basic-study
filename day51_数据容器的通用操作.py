my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str="abcdefg"
my_set={1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key":4,"key5":5}
# len元素个数
print(len(my_list))
print(len(my_tuple))
print(len(my_str))
print(len(my_set))
print(len(my_dict))

# max
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))
# min
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))
# 类型转换
# 容器转列表
print(list(my_list))
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict))

# 容器转元组
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_str))
print(tuple(my_set))
print(tuple(my_dict))

# 容器转字符串
print(str(my_list))
print(str(my_tuple))
print(str(my_str))
print(str(my_set))
print(str(my_dict))

# 容器转集合
print(set(my_list))
print(set(my_tuple))
print(set(my_str))
print(set(my_set))
print(set(my_dict))

# 不能转字典
# 对容器进行排序
my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str="abcdefg"
my_set={1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key":4,"key5":5}
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))
# 倒序排序
print(sorted(my_list,reverse=True))
print(sorted(my_tuple,reverse=True))
print(sorted(my_str,reverse=True))
print(sorted(my_set,reverse=True))
print(sorted(my_dict,reverse=True))