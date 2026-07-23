"""
演示对文件读取
"""
"""
打开文件
f=open("D:/测试.txt","r",encoding="UTF-8")
读取文件 read()
print(f"读取10个字节的结果{f.read(10)}")
print(f"读取全部内容的结果{f.read()}")

读取文件 readlines
lines=f.readlines()  # 读取文件全部行,封装到列表中

读取文件 readline
line1=f.readline() 
print(f"第一行数据是:{line1}")

for循环读取文件行
for line in f:
    print(line)
关闭文件
f.close()

withopen操作文件,自动关闭
with open("D:/测试.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)
"""