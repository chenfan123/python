name = 'this is a name variable'
print(f"{name}的长度是：{len(name)}")

name2 = 'this is a name variable2'


def my_len(str):
    length = 0
    for i in str:
        length += 1
    return length


print(f"{name2}的长度是：{my_len(name2)}")

print(None == False)  # false
