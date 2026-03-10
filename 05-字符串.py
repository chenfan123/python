info = """三引号写法，如果没有变量接收，那么这种作为多行注释存在，如果有变量接收值就是字符串"""

messge = "python is %s hahahah %s" % ("good", "haha")
print(messge)  # python is good hahahah haha
f1 = 1.19

print("sffsss%.1f" % f1)

n1 = 123
print("n1的值为：%6d" % n1)  # 会补充3个空格，总共6位
f2 = 1.23456789
print("f2的值为：%.3f" % f2)  # 会保留3位小数，四舍五入

name = input("请输入你的名字：")
print(f"你的名字是：{name}")
