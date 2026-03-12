def user_info(name, age, gender):
    print(f"name: {name}, age: {age}, gender: {gender}")


user_info("张三", 18, "男")  # 位置参数，根据位置一一对应
user_info(age=18, name="张三", gender="男")
user_info(gender="男", name="张三", age=18)
