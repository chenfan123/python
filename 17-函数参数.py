def user_info(name, age, gender):
    print(f"name: {name}, age: {age}, gender: {gender}")


user_info("张三", 18, "男")  # 位置参数，根据位置一一对应
user_info(age=18, name="张三", gender="男")  # 关键字参数，根据关键字一一对应
user_info(gender="男", name="张三", age=18)  # 关键字参数，根据关键字一一对应

# 缺省参数


def user_info(name, age, gender="男"):
    print(f"name: {name}, age: {age}, gender: {gender}")


user_info("张三", 18)
user_info("张三", 18, "女")

# 不定长参数


def user_info(name, age, *args, **kwargs):
    print(f"name: {name}, age: {age}, args: {args}, kwargs: {kwargs}")


user_info("张三", 18, "男", "女", "男", "女", name="张三", age=18, gender="男")

# 不定长参数，*args 表示接收不定长位置参数，**kwargs 表示接收不定长关键字参数


def ttt(*arg):
    print(arg)


ttt(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def func(name, *args, **kwargs):
    print(name, args, kwargs)


func("张三", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name="张三", age=18, gender="男")

# 张三 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) {'name': '张三', 'age': 18, 'gender': '男'}
