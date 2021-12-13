N,M = map(int,input().split(' '))
L = []
R = []
cnt = 0

while M>cnt:
    l,r = map(int,input().split(' '))
    L.append(l)
    R.append(r)
    cnt+=1

maxL = max(L)
minR = min(R)

print(minR-maxL+1) if maxL <= minR else print("0")