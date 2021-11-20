N,x = map(int,input().split(' '))
a = list(map(int,input().split(' ')))

a.sort()
cnt=0
if a[0]>x:
    print(0)
    exit()
    
for i in a:
    if x>=i:
        x-=i
        cnt+=1
    else:
        break

if x>0:
    cnt-=1
print(cnt)

