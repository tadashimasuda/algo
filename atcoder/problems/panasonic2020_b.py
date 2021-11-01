import math
H,W = map(int,input().split(' '))

if H==1 or W==1:
    ans=1
elif H%2==0:
    ans = W * H/2
else:
    ans = W * (H-1)/2
    ans +=  math.ceil(W/2)

print(int(ans))