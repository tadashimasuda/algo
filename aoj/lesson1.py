#ITP1_1_B
X = int(input())
print(X ** 3)

#ITP1_1_C
input = input()
a,b = [int(num) for num in input.split(' ')]
print(str(a * b) + ' ' + str(a * 2 + b * 2))

#ITP1_1_D
input = int(input())
h, mod = divmod(input, 3600)
m,s = divmod(mod, 60)
print(f"{h}:{m}:{s}")

#ITP1_2_A
input = input()
a,b = [int(num) for num in input.split(' ')]
if a<b:
    print('a < b')
elif a>b:
    print('a > b')
elif a == b:
    print('a == b')

# ITP1_2_B
input = input()
a,b,c = [int(num) for num in input.split(' ')]
if a < b  and b < c:
    print('Yes')
else:
    print('No')