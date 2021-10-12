length = int(input())
data = [int(i) for i in input().split(' ')]

dp = [float('inf') for _ in range(length)]

dp[0] = 0
for i in range(1,length):
    if i == 1:
        dp[i] = (dp[i-1] + abs(data[i] - data[i-1]))
    else:
        dp[i] = min(dp[i-1] + abs(data[i] - data[i-1]),dp[i-2] + abs(data[i] - data[i-2]))

print(sum(dp))