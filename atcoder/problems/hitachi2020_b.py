A,B,M = map(int,input().split(' '))
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
xyc = [list(map(int,input().split(' '))) for _ in range(M)]

min_A,min_B = min(a),min(b)
ans = min_A+min_B
for x,y,c in xyc:
    ans =min(a[x-1]+b[y-1]-c,ans)
print(ans)