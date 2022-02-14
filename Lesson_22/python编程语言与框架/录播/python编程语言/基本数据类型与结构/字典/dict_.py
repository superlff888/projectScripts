# @Time  : 2022/01/19 10:33
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

# 使用字典的构造方法创建字典

dict_a = dict([("a", 1), ('b', 2)])
print(dict_a)

# 使用字典推导式创建字典

dict_b = {k: v for k, v in [("a", 1), ('b', 2)]}  # k, v = ("a", 1) 运用了解包的知识点
print(dict_b)
print(dict_a.get("a"))
print(dict_b.items())
print(dict_b.keys())
print(f'返回的value：{dict_b.pop("a")}')

dict_b = {'a': 1, 'b': 2}
dict_ = {k: v**2 for k, v in dict_b.items() if v >= 1}
print(f'字典推导式：{dict_}')
dict_ = {k: v for k, v in dict_b.items() if v >= 1}

# key和value交换
dict_r = {v: k for k, v in dict_b.items() if v >= 1}
print(f"key和value交换后，变成新的字典：{dict_r}")


# 字典常用方法练习
# 创建字典的两种方法
dict1 = {"k1": "v1", "k2": "v2"}
dict2 = dict(k3="v3", k4="v4")
print("第一种创建结果为：", dict1)
print("第二种创建结果为：", dict2)

# 清空字典内所有元素
print("dict2字典被clear了：", end="")
print(dict2.clear())

# 字典的复制
dict_copy = dict1.copy()  # 浅拷贝
print("dict_copy是从dict1复制过来的：", end="")
print(dict_copy)

# 用传入的序列和值创建新的字典，值可选，默认为None
dict_new = dict.fromkeys(("a1", "a2", "a3"), 5)
print("利用fromkeys创建的新字典为：", dict_new)

# 通过键获取值的两种方法：
print("利用数组下标获取：", dict1["k1"])
print("利用get方法获取：", dict1.get("k1"))
# 两种方法的区别：利用下标获取，下标越界时系统抛异常，利用get则直接返回None
# print("越界的下标获取：",dict1["k3"])
print("越界的下标获取：", dict1.get("k3"))

# 获取字典所有键、值和键值对
print("所有键：", dict1.keys())  # dict_keys(['k1', 'k2'])
print("所有值：", dict1.values())  # dict_values(['v1', 'v2'])
print("所有键值对：", dict1.items())  # dict_items([('k1', 'v1'), ('k2', 'v2')])
# 应用
for k, v in dict1.items():
    print("键为：", k, "值为：", v)

# 删除指定键值对，最少传一个参数：
# dict1.pop("k1")
print(dict1.pop("k1"))  # 返回k1对应的value

print("键为k1的被删除后：", dict1)

# 随机删除字典中的一个键值对，但个人测试N次，都是删"d":"4"。。。有没有大神给讲解下
dict3 = {"a": "1", "b": "2", "c": "3", "d": "4"}
print("未用popitem删除之前：", dict3)
dict3.popitem()
print("用popitem删除之后：", dict3)

# 查找指定键所对应的值，存在返回值，不存在则创建并赋默认值
print("查找的键存在时：", dict3.setdefault("a"))
print(dict3.setdefault("这个键原来是不存在的", "查找完就被添加进去了"))
# 查看dict3的变化
print("dict3的变化：", dict3)

dict4 = {"name": "lee", "age": 12}
dict5 = {"sex": "man"}
# 利用update实现对现有字典内容的更新
print("dict4被update之前：", dict4)
dict4.update({"age": 20})  # 注意传入的参数为字典
print("dict4被update之后（更新数据）：", dict4)
dict4.update(dict5)
print("更新内容不在现有字典内，则为添加操作：", dict4)

# 将values转成成列表元素
a = {'a': 1, 'b': 2}
print(type(a.values()))
print(list(a.values()))