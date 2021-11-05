N = int(input())

ans = 0
cnt = 1

for i in range(2,N):
    if cnt * 2 <= N:
        ans = i
        cnt *= 2

print(ans)