my_dict={"a":99,"b":88,"c":77}
# 新增元素
my_dict["d"]=66
print(my_dict)

# 删除元素
my_dict.pop("a")
print(my_dict)

# 清除
score=my_dict.pop("b")
print(my_dict)
print(score)

# 获取全部的key
my_dict={"a":99,"b":88,"c":77}
keys=my_dict.keys()
print(keys)

# 遍历字典
# 1.通过key遍历
for key in keys:
    print(key)
    print(my_dict[key])

# 2.
for key in my_dict:
    print(key)
    print(my_dict[key])
 
# 统计字典中元素的数量
print(len(my_dict))