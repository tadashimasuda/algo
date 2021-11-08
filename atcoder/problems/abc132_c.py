N = int(input())
d = list(map(int,input().split(' ')))

ans =0
d.sort()
if d[(N//2)-1] == d[(N//2)]:
    ans = 0
else:
    ans = d[(N//2)] - d[(N//2)-1]

print(ans)
