N,M,C = map(int,input().split(' '))
B = list(map(int,input().split(' ')))
A = [[int(i) for i in input().split(' ')] for _ in range(N)]

ans=0
add=C
for i in range(N):
    for j in range(M):
        add += (A[i][j] * B[j])

    if(add>0):
        ans+=1
    add=C
print(ans)
