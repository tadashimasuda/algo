from typing import List


def get_pair(numbers: List[int], target: int):
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return num, val
        cache.add(num)


"""
input: X [1,2,3,4,4,5,5,8,10] Y:[4,5,5,5,6,7,8,8,10]
    => X [1,2,3,4,4,10] Y[5,5,5,6,7,8,8,10]
"""

{2: {"A": 4}}


# def pick_numbers(A: List[int], B: List[int]):
#     cache = {}
#     for number in A:
#         if number not in cache:
#             cache[number] = {"A": A.count(number)}

#     for number in B:
#         if number not in cache:
#             cache[number] = {"B": B.count(number)}
#         elif "A" not in cache[number]:
#             cache[number] = {"B": B.count(number)}
#         elif cache[number]["A"] < B.count(number):
#             cache[number] = {"B": B.count(number)}

#     new_A = []
#     new_B = []
#     for number in cache:
#         if "A" in cache[number]:
#             new_A.append(number)
#         else:
#             new_B.append(number)

#     print(new_A)
#     print(new_B)


if __name__ == "__main__":
    pick_numbers([1, 2, 3, 4, 4, 5, 5, 8, 10], [4, 5, 5, 5, 6, 7, 8, 8, 10])

# memo from collections import Counter
