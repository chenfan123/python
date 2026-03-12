# 字典dict
# 使用{}存储原始，每一个元素是一个键值对；key和value可以是任意类型的数据;key不可重复，不可为字典
# 常用操作
# 新增元素
dict = {'name': '张三', 'age': 18}
dict['gender'] = '男'
print(dict)  # {'name': '张三', 'age': 18, 'gender': '男'}

# 修改元素
dict['age'] = 20
print(dict)  # {'name': '张三', 'age': 20, 'gender': '男'}

# 删除元素
del dict['age']
print(dict)  # {'name': '张三', 'gender': '男'}

# 清空字典
dict.clear()
print(dict)  # {}

# 获取全部的key
dict2 = {'name': '张三', 'age': 18, 'gender': '男'}
print(dict2.keys())  # dict_keys(['name', 'age', 'gender'])

# 获取全部的value
print(dict2.values())  # dict_values(['张三', 18, '男'])

# 获取全部的键值对
# dict_items([('name', '张三'), ('age', 18), ('gender', '男')])
print(dict2.items())

# 遍历字典
for key, value in dict2.items():
    print(key, value)  # name 张三 age 18 gender 男

for key in dict2.keys():
    print(key)  # name age gender

for value in dict2.values():
    print(value)  # 张三 18 男

# 删除字典
delValue = dict2.pop('age')  # 仅返回value
print(dict2)  # {'name': '张三', 'gender': '男'}
