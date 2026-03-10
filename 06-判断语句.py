v1 = True  # 布尔类型
v2 = False  # 布尔类型
print(v1, type(v1))
print(v2, type(v2))

print(1 > 2)  # False
print(1 < 2)  # True
print(1 >= 1)  # True
print(1 <= 1)  # True
print(1 == 1)  # True
print(1 != 1)  # False
print(1 == "1")  # False
print(1 != "1")  # True
print(1 == True)  # True
print(1 != False)  # True
print(0 == False)  # True
######################################
# 逻辑运算符
age = 10
print("5 < age < 18 = ? %s" % (age > 5 and age < 18))
print("%s" % (not age > 5))  # True

num = 20
if num > 10:
    print("num > 10")
else:
    print("num <= 10")

tt = 10

if tt > 5 and num > 10:
    print("tt > 5 and num > 10")
else:
    print("tt <= 5 or num <= 10")

if tt > 9:
    print("tt > 9")
elif tt > 5:
    print("tt > 5")
else:
    print("tt <= 5")

####################################
# 嵌套使用
if (int(input("请输入你的年龄：")) > 18):
    print("你已经成年了")
    if (int(input("请输入你的身高：")) > 180):
        print("你身高180以上")
    else:
        print("你身高180以下")
else:
    print("你未成年")
