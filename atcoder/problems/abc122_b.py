S = str(input())
ACGT = 'ACGT'

cnt = 0
max = 0
for s in S:
    cnt+=1
    if not s in ACGT:
        cnt = 0

    if max<=cnt:
        max = cnt

print(max) 



