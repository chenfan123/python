def test(a, b):
    return a + b


def say_hello():
    print("hello")


# 如果本文件被直接执行，则内置变量__name__会被赋值为“__main__”
# 如果本文件被import 或from导入，则内置变量会被赋值为：文件名称
if __name__ == "__main__":
    print(test(1, 2))
