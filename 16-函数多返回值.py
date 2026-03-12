def test():
    return 1, 2, 3, 4, 3


print(test())  # (1, 2, 3)
print(type(test()))  # <class 'tuple'>

# 自动解包，将元素的多个元素赋值给变量
x, y, z, a, b = test()
print(x, y, z, a, b)  # 1 2 3 4 3

j = test()
print(j)  # (1, 2, 3, 4, 3)
