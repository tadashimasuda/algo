from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        # 一番大きいのが最後にくるので比べる範囲を狭めていく
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

# def check_sort(numbers):
#     for i in range(len(numbers)-1):
#         if numbers[i] > numbers[i+1]:
#             return False
#     return True
#
# def bubble_sort(numbers):
#     while not check_sort(numbers):
#         for i in range(len(numbers)-1):
#             print(numbers)
#             if numbers[i] > numbers[i+1]:
#                 numbers[i],numbers[i + 1] = numbers[i+1],numbers[i]
#
#     return numbers

if __name__ == '__main__':
    print(bubble_sort([2,5,1,8,7,3]))