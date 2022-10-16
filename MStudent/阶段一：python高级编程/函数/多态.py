# -*- coding=utf-8 -*-
# @Time    : 2022/10/16 20:06
# @Author  : ╰☆H.俠ゞ
# =============================================================


class Animal(object):
    def run(self):
        print('Animal is running...')


# class Cat(Animal):
#
#     def run(self):
#         print('Cat is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


Dog().run()
# def run_twice(animal):
#     animal.run()
#     animal.run()


# run_twice(Cat())
# run_twice(Dog())