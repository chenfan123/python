# 集合(set)
# 不支持重复，并且内容无序，可以修改
a = {'a', 'v', 'd', 's', 'g'}

b = {1, True, 0, False}

print(b)  # {0, 1}

# 添加元素
a.add('z')
print(a)  # {'a', 'v', 'd', 's', 'g', 'z'}

# 删除元素
a.remove('z')
print(a)  # {'a', 'v', 'd', 's', 'g'}

# 清空集合
a.clear()
print(a)  # set()

# 统计集合长度
print(len(a))  # 0

# 取出2个集合的差集
print(a.difference(b))  # {'a', 'v', 'd', 's', 'g'}

# 消除2个集合的差集,会修改集合1
c = {1, 2, 3}
d = {2, 3, 4}
c.difference_update(d)
print(c)  # {1}
print(d)  # {2, 3, 4}

# 合并集合
print(c.union(d))  # {1, 2, 3, 4}

# 遍历集合
for i in c:
    print(i)  # 1
