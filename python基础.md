# python 基础语法

### 常见的 6 种值

##### 数字

- 整数（int)：123
- 浮点数（float）：123.456
- 复数（complex）：123.456j，以 j 结尾表示复数
- 布尔（bool）：True、False，True 和 False 首字母大写

##### 字符串

- 字符串（str）：'hello'、"hello"、'''hello'''、"""hello"""

##### 列表

- 列表（list）：有序的可变序列：[1, 2, 3]、['a', 'b', 'c']、[True, False]

##### 元祖

- 元祖（tuple）：有序的不可变序列：(1, 2, 3)、('a', 'b', 'c')、(True, False)

##### 集合

- 集合（set）：无序的不重复集合：{1, 2, 3}、{'a', 'b', 'c'}、{True, False}

##### 字典

- 字典（dict）：无序的键值对集合：{'a': 1, 'b': 2, 'c': 3}、{'a': 1, 'b': 2, 'c': 3}、{True: 1, False: 2}

string int float

数据类型之间，在特定的场景下，是可以相互转换的，如字符串转数字、数字转字符串等。

函数：

- type(x)：用来获取变量的类型
- int(x): 转换成一个整数
- float(x): 转换成一个浮点数
- str(x): 转换成一个字符串

### 标识符

变量名 方法名 类名等等，只允许英文、中文、数字、下划线。不建议中文数字开头。

### 运算符

#### 算数运算符

-

*

- /
  // ： 取整除：9//2 输出 4，9.0//2.0 输出 4.0
  % ：取余
  \*\*：指数：2\*\*3 输出 8

#### 赋值运算符

+= ----> c+=a ==> c = c + a
-= ----> c-=a ==> c = c - a
_= ----> c_=a ==> c = c \* a
/= ----> c/=a ==> c = c / a
//= ----> c//=a ==> c = c // a
%= ----> c%=a ==> c = c % a
\*\*= ----> c\*\*=a ==> c = c \*\* a

### 字符串

#### 字符串拼接

字符串无法和非字符串变量进行拼接，因为类型不一致，无法接上。
字符串乘以数字可以做到将字符串复制多少份前后拼接到一起

#### 字符串格式化

%：表示占位，

- s 表示将变量变成字符串放入占位的地方
- d 将内容转换成整数
- f 将内容转换成浮点型,.后表示保留小数点后几位

#### 精度控制

默认浮点数为 6 位小数点
可以使用辅助符号“m.n”来控制数据的宽度和精度
m，控制宽度，要求是数字，设置的宽度小于数字自身，不生效
.n,控制小数点精度，要求是数字，会进行小数的四舍五入

#### 快速格式化

f"{变量名}":`print(f"我是{变量名}")`
`f"{变量:精度}"`:`print(f"我是{变量:10.2f}")`长度为 10，不够的话空格填充，精度 2 位

#### 对表达式进行格式化

`print("1*1的结果是：%d" % (1*1))`
`print(f"1*1的结果是：{1*1}")`
`print("字符串在Python中的类型是：%s" % type(str))`

#### 数据输入

`name = input("请输入你的名字：")`

### 判断语句

#### 布尔类型和比较类型

比较运算符

- == 判断左右两边是否相等
- != 判断左右两边是否不相等
- > 判断左边是否大于右边
- < 判断左边是否小于右边
- > = 判断左边是否大于等于右边
- <= 判断左边是否小于等于右边

#### 布尔类型

- True
- False

全部小写字母 > 全部大写字母 > 全部数字

#### 逻辑运算符

1. and 与: 多条件同时满足，则结果为 True，否则为 False
2. or 或: 多条件有一个满足，则结果为 True，否则为 False
3. not 非: 条件为 True，则结果为 False，条件为 False，则结果为 True
   `print("5 < age < 18 = ? %s" % (age > 5 and age < 18))`

#### if 语句

python 是通过缩进判断代码块的归属关系

```python
num = 20
if num > 10:
    print("num > 10")
else:
    print("num <= 10")
```

```python
tt = 10
if tt > 5 and num > 10:
    print("tt > 5 and num > 10")
else:
    print("tt <= 5 or num <= 10")
```

```python
if tt > 9:
    print("tt > 9")
elif tt > 5:
    print("tt > 5")
else:
    print("tt <= 5")
```

##### 判断语句的嵌套使用

```python
if (int(input("请输入你的年龄：")) > 18):
    print("你已经成年了")
    if (int(input("请输入你的身高：")) > 180):
        print("你身高180以上")
    else:
        print("你身高180以下")
else:
    print("你未成年")
```

### 循环语句

#### while 循环

```python
i = 0
while i < 100:
    print(i)
    i += 1
```

> print 输出不换行：`print(内容, end="") `这种形式不换行，end 是 print 的形式参数，决定了输出内容的最后是什么。默认我们没有使用 end 参数，所以是换行的。如果不需要自动带有\n 效果可以用 end=？修改，比如`end=""`最后什么都不加
> \t: 制表符，相当于按下 tab 键，一般用于对齐

#### for 循环

```python
name = "this is a name variable"

for i in name:
    print(i)
```

##### range

- 语法：range(start, end, step)
- 作用：生成一个整数序列
- 参数：
  - start：起始值，默认为 0
  - end：结束值，默认为 0
  - step：步长，默认为 1

```python
for i in range(10):
    print(i)
```

##### 变量的作用域

很神奇，for 循环中定义的变量，在循环结束后，仍然可以访问。

##### 循环中断

- break：中断循环
- continue：跳过本次循环，继续下一次循环

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

## 函数

- len(x): 计算字符串长度

#### 函数的定义

```python
def 函数名(传入参数):
    函数体
    return 返回值
```

有一个特殊的字面量`None`，表示空值，表示没有返回值，类型是`<class 'NoneType'>`

在 if 判断中`None`等同于`False`

变量初始值可以使用`None`

#### 作用域

如何将函数内定义的变量声明为全局变量：使用 global 关键字`global 变量名`

## 数据容器

### 列表

```python
list = [1, 2, 3, 4, 5]
print(list)
```

列表的索引从 0 开始,也可以反向取，比如：-1

#### 列表的常用操作

- 修改某个值：`list[index] = item`
- 列表的切片：`list[start:end:step]`
- 列表的追加：`list.append(item)`
- 列表的插入：`list.insert(index, item)`,是在指定位置插入元素，即插入到 index 的位置，如果插入到超出索引范围，会插入到尾部
- 列表的删除：`list.remove("xxx")`
- 列表的清空：`list.clear()`
- 查找列表的下标：`list.index(item)`
- 尾部新增一批元素：`list.extend(iterable)`
- 删除元素：`list.pop(index)`
- 删除元素：`del list[index]`
- 统计元素个数：`list.count(item)`
- 统计列表长度：`len(list)`
- 判断元素是否存在：`item in list`
- 判断元素是否不存在：`item not in list`
- 判断列表是否为空：`list == []`
- 判断列表是否不为空：`list != []`

### 元祖(tuple)

元祖不可被修改,一个元素的元祖需要后面添加`,`

#### 元祖的常用操作

- 查找某个数据，返回下标：`tuple.index(item)`
- 统计某个数据出现的次数：`tuple.count(item)`
- 统计元祖长度：`len(tuple)`
  注：可以修改元祖内 list 的内容，但是不能修改元祖内 list 的地址

### 字符串(str)

字符串是一个无法修改的数据容器。

#### 字符串的常用操作

- 访问下标`str[index]`
- 字符串搜索：`str.index(item)`
- 字符串替换：`str.replace(old, new)`，这个不是修改字符串本身，而是得到一个新的字符串
- 字符串分割：`str.split(sep)`，按照一个指定的符号拆分出 list
- 去掉前后空格：`str.strip()`，如果 strip 传如参数就是去前后指定字符串
- 统计字符串某个值个数`str.count(xxx)`

### 序列的切片操作

- 语法：`序列[start:end:step]`,从一个序列中取出一个子序列，即一个切片
  - 起始下标表示从何处开始，留空表示从头开始
  - 结束下标（不含）表示从何处结束，留空就是到末尾
  - 步长 n 表示每次跳过 n-1 个元素取
  - 步长为负数表示反向取（起始下标和结束下标也要反向标记）
- 作用：切片
- 参数：
  - start：起始值，默认为 0
  - end：结束值，默认为 0
  - step：步长，默认为 1

```python
print(list[0:3:1])
```

### 集合(set)

- 集合（set）：无序的不重复集合：{1, 2, 3}、{'a', 'b', 'c'}、{True, False}

空集合必须使用`set()`来创建，不能使用`{}`来创建，因为`{}`创建的是一个空字典。

下标访问无法使用，因为无序

#### 集合的常用操作

- 添加元素：`set.add(item)`
- 删除元素：`set.remove(item)` 如果元素不存在，会报错
- 清空集合：`set.clear()`
- 统计集合长度：`len(set)`
- 判断元素是否存在：`item in set`
- 判断元素是否不存在：`item not in set`
- 随机取出元素：`set.pop()`,理论上是取第一个，但是本身就无序，所以是随机。会修改集合本身，返回被删除的元素
- 取出 2 个集合的差集`set1.difference(set2)`：集合 1 有集合 2 没有，返回一个新的集合，不会修改集合 1 本身
- 消除 2 个集合的差集`set1.difference_update(set2)`：集合 1 会删除集合 2 有的元素,会修改集合 1 本身
- 合并集合`set1.union(set2)`：合并 2 个集合，返回一个新的集合，不会修改集合 1 本身

集合的遍历：

```python
for i in set:
    print(i)
```

不支持 while 循环，因为不支持下标索引

### 字典(dict)

使用`{}`存储原始，每一个元素是一个键值对；key 和 value 可以是任意类型的数据;key 不可重复，不可为字典。

#### 常用操作

- 新增元素：`dict[key] = value`
- 修改元素：`dict[key] = value`
- 删除元素：`del dict[key]`
- 清空字典：`dict.clear()`
- 获取全部的 key：`dict.keys()`
- 获取全部的 value：`dict.values()`
- 获取全部的键值对：`dict.items()`
- 遍历字典：`for key, value in dict.items():`
- 删除字典：`dict.pop(key)`
- 删除字典：`del dict[key]`
- 统计字典长度：`len(dict)`

字典的遍历：

```python
for key, value in dict.items():
    print(key, value)
```

不支持 while 循环，因为不支持下标索引

### 数据容器对比总结

##### 是否支持下标索引

- 支持： 列表、元祖、字符串 —— 序列类型
- 不支持：集合、字典 —— 非序列类型

##### 是否支持重复元素

- 支持： 列表、元祖、集合
- 不支持：字符串、字典

##### 是否有序

- 有序： 列表、元祖、字符串 —— 序列类型
- 无序：集合、字典 —— 非序列类型

##### 是否可变

- 可变： 列表、集合、字典
- 不可变：元祖、字符串

##### 应用场景

- 列表： 需要频繁修改数据时
- 元祖： 不需要频繁修改数据时
- 集合： 需要频繁修改数据时
- 字典： 需要频繁修改数据时

> 扩展：字符串的大小比较，是按照字符串的 ASCII 码进行比较的。逐位挨个挨个比

## 函数进阶

### 多返回值

```python
def test():
    return 1, 2, 3

print(test())  # (1, 2, 3)

x,y,z = test()
print(x,y,z)  # 1 2 3
```

### 函数参数

#### 位置参数

```python
def test(a,b,c):
    print(a,b,c)

test(1,2,3)
```

#### 关键字参数

```python
def test(a,b,c):
    print(a,b,c)

test(a=1,b=2,c=3)
```

#### 缺省参数

```python
def test(a,b,c=10):
    print(a,b,c)

test(1,2)
```

#### 不定长参数

不确定调用的时候会传递多少个参数，不传参也可以，用\*args 表示接收不定长位置参数，\*\*kwargs 表示接收不定长关键字参数

```python
def test(*args, **kwargs):
    print(args, kwargs)

test(1,2,3,4,5,6,7,8,9,10,name="张三",age=18,gender="男")
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) {'name': '张三', 'age': 18, 'gender': '男'}
```

### 匿名函数

#### 函数作为参数传入

```python
def test_fun(compute):
    result = compute(1, 2)
    print(result)

def compute(x, y):
    return x + y

test_fun(compute)  # 3
```

#### lambda 匿名函数

- def 关键字可以定义带有名称的函数，lambda 关键字可以定义匿名函数（无名称）
- 有名称的函数可以基于名称重复使用；无名称的匿名函数，只能临时使用一次
- lambda 传入参数:函数体(一行代码)
- lambda 是关键字，表示定义匿名函数；
- 传入参数表示匿名函数的形式参数，如：x,y 表示接受 2 个形式参数
- 函数体，就是函数的执行逻辑，只能写一行

```python
print((lambda x, y: x+y)(1, 2))  # 3
```

## 文件系统

### 文件读取

#### open()打开函数

- 语法：open(文件路径, 访问模式, 编码格式)
- 参数：
  - 文件路径：文件的绝对路径或者相对路径
  - 访问模式：
    - r：只读模式，文件不存在会报错
    - w：写入模式，文件不存在会创建，文件存在会清空
    - a：追加模式，文件不存在会创建，文件存在会追加
    - b：二进制模式
    - t：文本模式
    - +：读写模式
  - 编码格式：
    - utf-8：默认编码格式
    - gb2312：中文编码格式
- 返回值：
  - 文件对象
- 示例：
  - file = open("19-text.txt", "r", encoding="utf-8")
  - content = file.read()
  - print(content)
  - file.close()

#### read()方法

文件对象.read(num)
文件对象.read(n)：读取文件内容，返回字符串，n 表示读取的字节数,如果没有传 num 就表示读取文件中所有。

#### readline()方法

文件对象.readline()：读取文件内容，返回字符串，只读取一行，读取完一行后，会自动换行。

#### readlines()方法

文件对象.readlines()：读取文件内容，返回列表，每行一个元素

#### with open() as 文件对象:

with open(文件路径, 访问模式, 编码格式) as 文件对象

会自动关闭文件，避免遗忘 close 方法

### 文件写入

#### 直接调用 write，write 方法必须传递字符串

但是并未真实写入，是积攒在内存中，称之为缓冲区。
调用 flush 的时候，内容会真正写入文件。
为了避免频繁的操作硬盘，导致效率下降

**因为硬盘是低速设备，程序是 cpu 执行，速度极快。所以未来避免低速设备拉慢程序的执行，在操作的时候会在内存中开辟缓冲区，作用是将要写入硬盘的数据先积攒在缓冲区中，当缓冲区满、或者调用 flush、或调用 close 的时候，数据才会从缓冲区真正写入硬盘。**

> 只有文本文件可以 r w a，非文本文件需要用 b，以二进制模式处理

## 异常

### 语法

```python
try:
    print('可能发生错误的代码')
except:
    print('发生错误')
```

#### 针对某个异常做处理

```python
try:
    1/0
except ZeroDivisionError as e:  # 除0异常，可以针对某种异常解决
    print('除0异常', e)
```

#### 针对多个异常做处理

```python
try:
    1 / 0
except (ZeroDivisionError, FileNotFoundError) as e:
    print('多个异常处理')
```

#### 捕获所有异常

```python
try:
    1 / 0
except Exception as e:
    print('出现问题了', e)
```

#### 异常传递

异常具有传递性，如果内部发生异常，没有去捕获就会往上层传递

### python 模块

模块：以.py 为结尾的文件。
作用：快速实现一个功能，一个模块就是一个工具包，里面有各种工具。

#### 模块的导入

```python
import 模块名
```

#### 模块的导入

```python
from 模块名 import 函数名1, 类，变量，方法
import 模块名
from 模块名 import *
import 模块名 as 别名
from 模块名 import 函数名 as 别名
```

#### 自定义模块

```python
def test(a, b):
    return a + b

def say_hello():
    print("hello")
```

```python
import a

print(a.test(1, 2))
a.say_hello()
```

##### \_\_name\_\_ 内置变量

文件导入时，会执行文件中代码。如果想不执行，可以加 if \_\_name\_\_ == "\_\_main\_\_": 判断，只有当前文件执行时，才会执行。

```python
# 如果本文件被直接执行，则内置变量__name__会被赋值为“__main__”
# 如果本文件被import 或from导入，则内置变量会被赋值为：文件名称
if __name__ == "__main__":
    print(test(1, 2))
```

##### \_\_all\_\_

如果一个模块文件中有这个变量，当使用`from xxx import *`的时候，只能导入这个列表中的元素

```python
__all__ = ["test", "say_hello"]

from c import *
test(1, 2)  # 3
say_hello()  # hello
# ttt()  # 报错
```

#### 自定义包

一个包里面包含多个模块，包里有一个\_\_init\_\_.py 文件，这个文件是包的初始化文件，里面可以包含包的初始化代码。

需要在\_init\_\_.py 文件中添加\_\_all\_\_ = ["模块名 1", "模块名 2", "模块名 3"]，这样在使用 from 包名 import \* 的时候，只能导入这个列表中的模块。

导入方式

```python
import 包名.模块名
```

#### 安装第三方包

`pip install 包名`
