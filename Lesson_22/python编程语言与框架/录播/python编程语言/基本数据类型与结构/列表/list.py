# @Time  : 2022/01/18 19:43
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================


# 构造方法
list_a = list('hogwarts')
print(list_a)

# 列表推导式

list_b = [i for i in range(1, 10) if i % 2 == 0]
print(list_b)
print(list_b[:2])
print(list_b[0:2])
print(list_b[::-1])  # 逆向打印

result = []
for i in range(1, 11):
    if i % 2 == 0:
        result.append(i ** 2)
print(f'for循环:{result}')

result = [i ** 2 for i in range(1, 11) if i % 2 == 0]  # i ** 2 为列表的元素
print(f'列表推导式：{result}')
# 重复
l_a = [1]
print(l_a * 5)  # 打印[1,1,1,1,1]

l_b = [2, 5, 8]

l_s = l_a + l_b
print(l_s)  # 元素合并

# 判断
list_ = [1, 2]
print(100 in list_)

# 常用的列表方法

_list = [1, 2, 3, 4, 5]

print(_list.append('a'))  # 没有返回
print(_list.count(1))
print(_list)
print(len(_list))
_list.extend('a1sd389')  # iterable可迭代对象
print(_list)
_list.extend(['a', 1, 's', 'd', 3, 8, 9])  # iterable可迭代对象 : 可进行for循环
print(_list)
_list.extend(('a', 1, 's', 'd', 3, 8, 9))  # iterable可迭代对象
print(_list)
_list.extend({'a': 1, 'sb': 8})  # iterable可迭代对象 接收字典所有key
print(_list)

print(_list.pop(3))
print(_list.pop())

print(_list.remove(3))
print(_list)

list_ = [1, 2, 5, 0, 5, 3]
list_.sort()
print(list_)
list_.sort(reverse=True)
print(list_)
list_.sort(reverse=False)
print(list_)

list_ = ["python", "java", "go", "r"]
list_.sort(key=len)  # 传入一个函数，指明排序方法
print(list_)
