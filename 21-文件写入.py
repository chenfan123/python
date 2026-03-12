# 文件写入操作
# 1.打开文件
file = open("19-text.txt", "w", encoding="utf-8")
# 2.写入文件
file.write("这是第一行\n")
file.write("这是第二行\n")
file.write("这是第三行\n")
file.flush()  # 刷新缓冲区，将内容真正写入文件
# 3.关闭文件
file.close()

# 绝对路径：/Users/chenjianhua/Desktop/python/python基础/19-text.txt

fff = open("21-text.txt", "a", encoding="utf-8")
fff.write("\n这是追加内容1\n")
fff.write("这是追加内容2\n")
fff.flush()
fff.close()

# b模式 二进制
fr = open("非文本文件起始", 'rb')  # 二进制，没有编码
fw = open("非文本文件目的路径", 'rb')

content = fr.read()
fw.write(content)

fr.close()
fw.close()
