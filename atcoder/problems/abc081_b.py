N = int(input())
A = list(map(int,input().split(' ')))

cnt = float('inf')
flag = True

for a in A:
    cnt_ = 0
    while a%2==0:
        cnt_+=1
        a /= 2

    if cnt_ < cnt:
        cnt = cnt_

print(cnt)