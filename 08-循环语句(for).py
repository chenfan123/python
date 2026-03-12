name = "this is a name variable"

for i in name:
    print(i)

# range 语句
r1 = range(10)

for i in r1:
    print(i)

r2 = range(1, 10)
for i in r2:
    print(i)  # 1 2 3 4 5 6 7 8 9

r3 = range(1, 10, 2)
for i in r3:
    print(i)  # 1 3 5 7 9

print(i)  # 9
###############################################################
# 循环中断
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4


for i in range(10):
    if i == 5:
        continue
    print(i)  # 0 1 2 3 4 6 7 8 9
