# 列表
list = [1, 2, 3, 4, 5]
print(list)

print(list[0])  # 1

for i in list:
    print(i, end=" ")  # 1 2 3 4 5

print(list[-1])  # 5

list2 = [[1, 2, 3], ['a', 'b', 'c']]
print(list2[0][0])  # 1
print(list2[1][1])  # b

# 列表的常用操作
# 修改某个值
list[1] = 100
print(list)  # [1, 100, 3, 4, 5]

# 插入元素
list.insert(0, 0)
print(list)  # [0, 1, 100, 3, 4, 5]

# 追加元素
list.append(6)
print(list)  # [0, 1, 100, 3, 4, 5, 6]

# 切片
print(list[:5:2])  # [0, 100, 4]

# 删除元素
list.remove(0)
print(list)  # [1,100, 3, 4, 5, 6]

# 删除方式2
a = list.pop(0)
print(list)  # [100, 3, 4, 5, 6]
print(a)  # 1

# 删除方式3
del list[0]
print(list)  # [ 3, 4, 5,6]

# 清空列表
list.clear()  # 清空列表
print(list)  # []

# 尾部新增一批元素
list.extend([7, 8, 9])
print(list)  # [7, 8, 9]

# 查找元素
print(list.index(7))  # 0

##############################
# 列表的遍历
list22 = [1, 3, 5, 7, 9]
for i in list22:
    print(i, end=" ")  # 1 3 5 7 9

j = 0
while j < len(list22):
    print(list22[j], end=" ")  # 1 3 5 7 9
    j += 1
