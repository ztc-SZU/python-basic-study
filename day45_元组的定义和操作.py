# 定义元组
t1=(1,"ztc",True)
t1=()
t1=tuple()
print(t1)

# 定义单个元素
t1=("hello",)

# 元组的嵌套
t1=((1,2,3),(4,5,6))

# 下标访问
print(t1[1][1])

# index查找方法
t1=(1,"ztc",True)
index=t1.index("ztc")
print(index)

# 元组的遍历
index=0
while index<len(t1):
    print(t1[index])
    index+=1

for element in t1:
    print(element)

# 不可以修改元组内容，但是可以修改元组内的列表