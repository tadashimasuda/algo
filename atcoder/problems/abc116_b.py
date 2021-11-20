n = int(input())

lis = []
def is_number(num):
    return num in lis

while True:
    lis.append(n)

    if n%2 == 0:
        n = n//2
    else:
        n = 3*n+1
    
    if is_number(n):
        lis.append(n)
        print(len(lis))
        break