# 使用while遍历
def while_fun():
    my_list=["ztc","szu","acm"]
    index=0
    while index<len(my_list):
        element=my_list[index]
        print(element)
        index+=1
def for_fun():
     my_list=["ztc","szu","acm"]
     for element in my_list:
         print(element)
while_fun()
for_fun()