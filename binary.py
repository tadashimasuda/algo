from typing import List

def binary_search(numbers:List[int],value:int) -> int:
    len_numbers = len(numbers)
    left = 0
    right = len_numbers - 1

    while left <= right:
        mid = (left+right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid+1
        else:
            right = mid -1

    return -1

if __name__ == '__main__':
    print(binary_search([0,1,5,7,9,11,15,20,24],5))