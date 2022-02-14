# @Time  : 2022/01/29 13:24
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
"""
在对象的生命周期结束时, _del_会被调用,可以将_del_理解为"析构函数Destructor"
"""


# 当需要删除对象来释放类所占用的资源的时候，就需要调用析构方法__del__()

# class Dog:
#     def __init__(self, newcolor):
#         self.color = newcolor
#
#     def getColor(self):
#         print(f"{self.color}")
#
#     def __del__(self):
#         print("调用__del__的方法，程序结束自动释放空间")
#
#
# dog1 = Dog("黄色")
# dog1.getColor()

print("\n============================================================================================================")
# 如果需要手动释放空间，用del语句可以删除对象，释放它所占用的资源


class Dog:
    def __init__(self, newcolor):
        self.color = newcolor
        # num = 100  # 它是一个局部变量,当这个函数执行完之后,这个变量的空间就没有了,因此其他方法不能使用这个变量

    def __del__(self):
        print("程序结束自动释放空间")


# dog = Dog()
dog2 = Dog("黄色")
print("删除dog2对象")
del dog2
print(dog2.color)
