A = [[int(i) for i in input().split(' ')] for _ in range(3)]
Bingo = [[0 for _ in range(3)] for _ in range(3)]
N = int(input())
B = []
cnt = 0

while cnt<N:
    B.append(int(input()))
    cnt+=1

for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            Bingo[i][j]='X'

for i in range(3):
    if Bingo[i].count('X') ==3:
        print('Yes')
        exit()

if Bingo[0][0] =='X' and Bingo[1][0]=='X' and Bingo[2][0] =='X':
    print('Yes')
    exit()

elif Bingo[0][1] =='X' and Bingo[1][1]=='X' and Bingo[2][1] =='X':
    print('Yes')
    exit()

elif Bingo[0][2] =='X' and Bingo[1][2]=='X' and Bingo[2][2] =='X':
    print('Yes')
    exit()

elif Bingo[0][0] =='X' and Bingo[1][1]=='X' and Bingo[2][2] =='X':
    print('Yes')
    exit()

elif Bingo[0][2] =='X' and Bingo[1][1]=='X' and Bingo[0][2] =='X':
    print('Yes')
    exit()
else:
    print('No')