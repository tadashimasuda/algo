N = int(input())
A = list(map(int,input().split(' ')))

ans = [0]*N
for i,num in enumerate(A,1):
    ans[num-1] = i

ans_text = " ".join([str(_) for _ in ans])
print(ans_text)