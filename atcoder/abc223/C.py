N = int(input())
A = []
B = []
count=0
while count<N:
    a,b = map(int,input().split(' '))
    A.append(a)
    B.append(b)
    count+=1

time = 0
for i in range(N):
    time += A[i]/B[i]
time /= 2

ans = 0
for i in range(N):
    if A[i]/B[i] >= time:
        ans += B[i] * time
    else:
        ans += A[i]
        time -= A[i]/B[i]

print(ans)