A,B = map(int,input().split(' '))

ans = 0
cnt = 1
while cnt < B:
    ans +=1
    cnt +=A-1

print(ans)
