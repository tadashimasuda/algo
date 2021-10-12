N,MAX_W= [int(i) for i in input().split(' ')]

w = v = []
for i in range(N):
    x,y = [int(i) for i in input().split(' ')]
    w.append(x)
    v.append(y)

dp = [[0]*(MAX_W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(MAX_W+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j],dp[i][j-w[i]] + v[i])

