# 打开文件,相对路径写法
file = open("19-text.txt", "r", encoding="utf-8")
# 读取文件
content = file.read()
print(content)
# 关闭文件
file.close()
# 绝对路径：/Users/chenjianhua/Desktop/python/python基础/19-text.txt

# 读取文件,readline()方法
file = open("19-text.txt", "r", encoding="utf-8")
content = file.readline().strip()  # 去掉换行符
print(content)  # 读取第一行
content2 = file.readline().strip()
print(content2)  # 读取第二行
content3 = file.readline().strip()
print(content3)  # 读取第三行
file.close()

# 读取文件,readlines()方法
file = open("19-text.txt", "r", encoding="utf-8")
content = file.readlines()
print(content)  # 读取所有行，每行是列表的一个元素，最后需要关闭文件
file.close()
