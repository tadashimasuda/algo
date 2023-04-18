"""
左右対称チェック
input [(1,2),(3,5),(4,7),(5,3),(7,4)]
output [(5,3),(7,4)]
"""
from typing import List, Tuple

#  my ans O(n^2)
def symmetric_check(input: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    result = []
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[i][0] == input[j][1] and input[i][1] == input[j][0]:
                result.append(input[i])

    return result


# sample ans O(n)
# https://www.udemy.com/course/python-algo/learn/lecture/20248290#content
# ペアを探すときは、全探索で比較ではなく。これまでに見たペアをcacheしておく。蓄積したcacheと比較することで、O(n)でペアを探すことができる。
# 全探索しそうなときは、cacheを検討
def symmetric_check2(pairs: List[Tuple[int, int]]):
    cache = {}
    result = []
    for pair in pairs:
        first, second = pair[0], pair[1]

        value = cache.get(second)
        if not value:
            # if not val -> new key val
            cache[first] = second
        elif value == first:
            result.append(pair)

    return result


if __name__ == "__main__":
    input = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    # print(symmetric_check(input))
    print(symmetric_check2(input))
