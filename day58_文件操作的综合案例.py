# 打开文件,得到文件对象,读取
fr=open(r"D:\SZU-AI-ACM-Project python-basic\python-basic\bill.txt","r",encoding="UTF-8")
# 打开文件,得到文件对象,写入
fw=open(r"D:\SZU-AI-ACM-Project python-basic\python-basic\bill.txt.bak","w",encoding="UTF-8")
# for循环读取文件
for line in fr:
    line=line.strip()
    if line.split(",")[4]=="测试":
        continue
    fw.write(line)
    fw.write("\n")
fr.close()
fw.close()