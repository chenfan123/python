# 函数作为参数传入
def test_fun(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_fun(compute)  # 3

# lambda 匿名函数
# 函数的定义中
# # def关键字可以定义带有名称的函数
# # lambda关键字可以定义匿名函数（无名称）
# 有名称的函数可以基于名称重复使用；无名称的匿名函数，只能临时使用一次
# # lambda 传入参数:函数体(一行代码)
# # lambda是关键字，表示定义匿名函数；
# # 传入参数表示匿名函数的形式参数，如：x,y表示接受2个形式参数
# # 函数体，就是函数的执行逻辑，只能写一行

print((lambda x, y: x+y)(1, 2))  # 3
test_fun(lambda x, y: x+y)  # 3
