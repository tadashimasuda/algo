N = int(input())
v = list(map(int,input().split(' ')))

v.sort()

avr = (v[0]+v[1])/ 2 
for i in range(2,N):
    avr = (avr+v[i])/2

print(avr)