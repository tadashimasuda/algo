N = int(input())
D,X = list(map(int,input().split(' ')))
A=[]
cnt=0

while N>cnt:
    A.append(int(input()))
    cnt+=1

choco_cnt = 0

for i in A:
    for _ in range(1,D+1,i):
        choco_cnt+=1

print(choco_cnt+X)