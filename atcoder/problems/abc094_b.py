N,M,X = map(int,input().split(' '))
A = list(map(int,input().split(' ')))

cnt_front = 0
cnt_back = 0
for i in range(1,N):
    if i in A:
        if i < X:
            cnt_front+=1
        else:
            cnt_back+=1

print(min(cnt_front,cnt_back))