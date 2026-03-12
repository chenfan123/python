# 元祖

tuple = (1, 2, 3, 4, 5)
print(tuple)
# 定义1个元素的元祖
tuple2 = (1,)

print(tuple[0])  # 1

for i in tuple:
    print(i, end=" ")  # 1 2 3 4 5

print(tuple[-1])  # 5

print(tuple[0::2])  # （1 3 5）
