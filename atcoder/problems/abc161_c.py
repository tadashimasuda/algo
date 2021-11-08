N,K =list(map(int,input().split(' ')))
X = N
ans = min(abs(N%K),abs(K-N%K))
print(ans)