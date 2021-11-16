N,M,X = map(int,input().split(' '))
A = list(map(int,input().split(' ')))

A.append(M)
A.sort()
id = A.index(M)

left = len(A[:id-1])-1
right = len(A[id+1:])-1

print(left,right)
print(A[:id],A[id:])