from typing import List

# def bubble_v1(numbers:List[int])->List[int]:
#
#     for limit in reversed(range(len(numbers))):
#         j = 0
#
#         while j < limit:
#             if numbers[j] > numbers[j+1]:
#                 numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
#             j += 1
#
#     return numbers

def bubble_v2(numbers:List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        for j in range(len_numbers-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

if __name__ == '__main__':
    numbers = [2,5,1,8,7,3]
    print(bubble_v2(numbers))
