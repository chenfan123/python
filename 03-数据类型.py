a = 1
print(type(a))  # <class 'int'>
b = 1.1
print(type(b))  # <class 'float'>
c = 1.1j
print(type(c))  # <class 'complex'>
d = True
print(type(d))  # <class 'bool'>
e = "hello"
print(type(e))  # <class 'str'>
f = [1, 2, 3]
print(type(f))  # <class 'list'>
g = (1, 2, 3)
print(type(g))  # <class 'tuple'>
h = {1: 2, b: 3}
print(type(h))  # <class 'dict'>

print(type(type(a)))  # <class 'type'>

a = '123'
print(a)

aa = int('1')
bb = float('1.1')
cc = str(1)
print(aa, bb, cc)
