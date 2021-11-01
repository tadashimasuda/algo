N = int(input())
X=list(map(int,input().split(' ')))

X.sort()

cnt = round(sum(X)/N)

ans = 0
for i in X:
    ans+=((i - cnt)**2)

print(ans)