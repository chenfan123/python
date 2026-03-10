i = 0
while i < 100:
    print(i)
    i += 1

#################################
# while循环嵌套应用
firstNum = 1
secondNum = 1
while firstNum <= 9:
    while secondNum <= firstNum:
        print(f"{firstNum}*{secondNum}={firstNum * secondNum}", end="\t")
        secondNum += 1
    print()
    firstNum += 1
    secondNum = 1
