#https://atcoder.jp/contests/abc224/tasks/abc224_b

H,W = map(int,input().split(' '))
A = []
count = 0
while True:

    if (count ==H):
        break

    input_list = [ int(_) for _ in input().split(' ')]
    A.append(input_list)
    
    count+=1

flag = False
for h in range(H):
    for w in range(W):
        if((h < h+1 < H) and (w < w+1 < W)):
            left = A[h][w] + A[h+1][w+1]
            right = A[h+1][w] + A[h][w+1]
            if(not left <= right):
                flag = True
                break

if(not flag):
    print("Yes")
else:
    print("No")

