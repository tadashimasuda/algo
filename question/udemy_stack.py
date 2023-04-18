from typing import List

from collections import deque


def add_list(input_numbers: List[int], add_num: int) -> List[int]:

    non_zero_numbers = input_numbers
    for num in input_numbers:
        if num != 0:
            break
        else:
            non_zero_numbers.remove(0)

    new_list = []
    deq = deque(new_list)
    for num in reversed(non_zero_numbers):
        if num + 1 > 9:
            deq.appendleft(0)
        else:
            deq.appendleft(num + 1)
            return list(deq)

    deq.appendleft(1)
    return list(deq)


def snake(numbers: List[int]):
    top = []
    middle = []
    bottom = []

    for i, number in enumerate(numbers):
        if i == 0 or i % 2 == 0:
            middle.append(number)
        elif len(bottom) < len(middle):
            pass

    return [top, middle, bottom]


def numbers_only(numbers: List[int]):
    cache = {}
    result = []
    for number in numbers:
        value = cache.get(number)
        if value is None:
            cache[number] = True
            result.append(number)
    return result


if __name__ == "__main__":
    # print(add_list([0, 0, 9, 9, 9, 9], 1))
    # numbers = [num for num in range(9) for _ in range(10)]
    # print(snake(numbers))
    print(numbers_only([1, 2, 2, 3, 3, 3, 5, 5, 6, 6]))
