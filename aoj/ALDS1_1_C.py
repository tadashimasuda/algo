import math
def is_prime(number:int)->bool:
    if number == 2:
        return True
    if number<2 and number % 2 == 0:
        return False

    i=3
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i = i+2

    return True

if  __name__ == '__main__':
    judge_num = int(input())
    numbers=[]
    count=0
    while count<judge_num:
        numbers.append(int(input()))
        count+=1

    count = 0
    for i in range(2,len(numbers)):
        if is_prime(i):
            count+=1
    print(count)