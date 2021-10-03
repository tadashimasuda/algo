len_numbers = int(input())
numbers = [int(i) for i in input().split()]

for i in range(1,len_numbers):

    text = " ".join([str(_) for _ in numbers])
    print(text)
    temp = numbers[i]
    j = i-1
    while j >= 0 and numbers[j] > temp:

        numbers[j+1] =numbers[j]
        j-=1

    numbers[j+1] =temp

text = " ".join([str(_) for _ in numbers])
print(text)
