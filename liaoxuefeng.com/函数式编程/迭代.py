# @Time  : 2021/05/20 15:46
# @Author    : House Lee
# -*-coding=utf-8-*-

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(f'\nx的值为{x}')
    print(f'\ny的值为{y}')

"""
如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
"""
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
