# 1.打开文件
file = open("19-text.txt", "r", encoding="utf-8")
# 2.读取文件
for line in file:
    print(line.strip())
# 3.关闭文件
file.close()

# with open() as 文件对象:
with open("19-text.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
