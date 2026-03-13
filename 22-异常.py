# 异常
try:
    print('可能发生错误的代码')
except:
    print('发生了错误')

# 针对某个异常做处理
try:
    1/0
except ZeroDivisionError as e:  # 除0异常，可以针对某种异常解决
    print('除0异常', e)

# 针对某些异常做处理
try:
    1 / 0
except (ZeroDivisionError, FileNotFoundError) as e:
    print('多个异常处理')

try:
    1 / 0
except Exception as e:  # Exception，是老祖宗
    print('出现问题了', e)
else:
    print('没有异常')
finally:
    print('最终处理')
