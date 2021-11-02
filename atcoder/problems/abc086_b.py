a, b = map(int, input().split())
x = (int(str(a) + str(b))) ** 0.5
if x == int(x):
    print('Yes')
else:
    print('No')