# 定义字典
my_dict={"a":99,"b":88,"c":77}
# 定义空字典
my_dict2={}
my_dict3=dict()
print(my_dict)
print(my_dict2)
print(my_dict3)

# 定义重复的字典，后面的值会覆盖前面的值

# 从字典中基于key获取value
my_dict={"a":99,"b":88,"c":77}
print(my_dict["a"])

# 字典的嵌套
my_dict={
    "a":{
        "英语":99,
        "数学":88,
        "语文":77
    },
    "b":{
        "英语":99,
        "数学":88,
        "语文":77
    },
    "c":{
        "英语":99,
        "数学":88,
        "语文":77
    }
}
print(my_dict["b"]["数学"])