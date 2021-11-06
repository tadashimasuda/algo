K,N = list(map(int,input().split(' ')))
A = list(map(int,input().split(' ')))

X = A[0]
lis = []
for i in range(1,N):
    lis.append(A[i] - X)
    X=A[i]
lis.append(K-A[N-1]+A[0])

print(sum(lis) - max(lis))

