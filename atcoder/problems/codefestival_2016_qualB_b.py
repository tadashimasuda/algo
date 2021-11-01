N,A,B = map(int,input().split(' '))
S = list(input())

cnt=0
b_cnt=0
for i in range(N):
    if (S[i]=='a') and (A+B > cnt):
        cnt+=1
        print('Yes')
    elif (S[i] == 'b') and (A+B > cnt) and (B > b_cnt):
        b_cnt+=1
        cnt+=1
        print('Yes')
    else:
        print('No')

