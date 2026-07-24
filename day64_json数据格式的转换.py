import json
# 准备列表,列表内每一个元素都是字典，将其转化为json
data=[{"name":"ztc","age":18},{"name":"szu","age":18}]
json_str=json.dumps(data)
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为json
data={"name":"ztc","age":18}
json_str=json.dumps(data)
print(type(json_str))
print(json_str)

# 将json字符串转换为python数据类型
data='[{"name":"ztc","age":18},{"name":"szu","age":18}]'
json_str=json.dumps(data)
print(type(json_str))
print(json_str)
# 将json字符串转换为python数据类型
data='{"name":"ztc","age":18}'
json_str=json.dumps(data)
print(type(json_str))
print(json_str)
