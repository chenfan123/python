## 函数

- len(x): 计算字符串长度

#### 函数的定义
```python
def 函数名(传入参数):
    函数体
    return 返回值
```

有一个特殊的字面量`None`，表示空值，表示没有返回值，类型是`<class 'NoneType'>`

在if判断中`None`等同于`False`

变量初始值可以使用`None`

#### 作用域

如何将函数内定义的变量声明为全局变量：使用global关键字`global 变量名`

## 数据容器
### 列表
```python
list = [1, 2, 3, 4, 5]
print(list)
```

列表的索引从0开始,也可以反向取，比如：-1

#### 列表的常用操作
- 修改某个值：`list[index] = item`
- 列表的切片：`list[start:end:step]`
- 列表的追加：`list.append(item)`
- 列表的插入：`list.insert(index, item)`,是在指定位置插入元素，即插入到index的位置，如果插入到超出索引范围，会插入到尾部
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
注：可以修改元祖内list的内容，但是不能修改元祖内list的地址


### 字符串(str)
字符串是一个无法修改的数据容器。

#### 字符串的常用操作
- 访问下标`str[index]`
- 字符串搜索：`str.index(item)`
- 字符串替换：`str.replace(old, new)`，这个不是修改字符串本身，而是得到一个新的字符串
- 字符串分割：`str.split(sep)`，按照一个指定的符号拆分出list
- 去掉前后空格：`str.strip()`，如果strip传如参数就是去前后指定字符串
- 统计字符串某个值个数`str.count(xxx)`