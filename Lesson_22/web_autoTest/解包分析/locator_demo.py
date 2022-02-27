# -*- coding=utf-8 -*-


def fond(*locator):
    if len(locator) > 1:
        print(type(locator))
        by, element_ = locator
        print(f"元素的定位策略为{by}")
        print(f"元素的定位元素为{element_}")

    print(type(locator))
    print(locator)
    # print(f"元素的定位策略为{by}")
    # print(f"元素的定位元素为{element_}")


# fond("q", "kw")
fond('("q", "kw")')
