N = int(input())

ans = 0
cnt = 1

for i in range(N):
    if 2**i <= N:
        cnt *= 2
        ans = 2**i

print(ans)
