# -*- coding=utf-8 -*-
# @Time    : 2023/04/03 22:41
# @Author  : ╰☆H.俠ゞ
# =============================================================
from typing import List

"""得到由列表元素组成的第二大数"""


class Solution:

    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
        :type arr: List[int]
        :rtype: List[int]
        :: 逆序 即从大到小 例如：3,2,1
        """
        try:
            n = len(arr)
            print(n)
            if n > 3:
                for i in range(n - 2, 1, -1):  # n-1 倒数第1个数的正向下标; n-1 + 1 = n
                    print(f"i为：{i}")  # 3，2
                    if arr[i] < arr[i + 1]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                arr[1], arr[2] = arr[2], arr[1]
                arr[2], arr[-1] = arr[-1], arr[2]
            elif n == 3:
                if arr[1] > arr[2]:
                    arr[1], arr[2] = arr[2], arr[1]
        except TypeError as e:
            print("type is error")
            raise e
        else:
            return arr

    # print(Solution().prevPermOpt1([1, 9, 4, 6, 7]))
    # print(Solution().prevPermOpt1([1, 9, 4]))

    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        n = len(coordinates)
        l = []
        for i in range(0, n):
            if coordinates[i][0] == coordinates[i][0] + 1:
                l.append(i)
        return l
        # if len(l) == n:
        #     print(len(l))
        #     return 1 == 1

    def checkStraightLine1(self, c: List[List[int]]) -> bool:
        '''
            分析：
                1、水平直线：所有点的x坐标均相等
                2、竖直直线：所有点的y坐标均相等
                3、有斜率的直线：所有点均在公式：
                        y=(y1-y2)/(x1-x2)x+(x1y2-x2y1)/(x1-x2)
        '''
        if c[0][0] == c[1][0]:
            def not_in_line(p: List[int]) -> int:
                return p[0] != c[0][0]
        elif c[0][1] == c[1][1]:
            def not_in_line(p: List[int]) -> int:
                return p[1] != c[0][1]
        else:
            a = (c[0][1] - c[1][1]) / (c[0][0] - c[1][0])
            b = (c[0][0] * c[1][1] - c[1][0] * c[0][1]) / (c[0][0] - c[1][0])

            def not_in_line(p: List[int]) -> int:
                return p[1] != a * p[0] + b

        return not bool(sum([1 for _ in range(2, len(c)) if not_in_line(c[_])]))


"""2"""

print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))

"""3"""
# print(Solution().checkStraightLine1([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
