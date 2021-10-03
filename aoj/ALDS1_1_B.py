# x,y = [int(i) for i in input().split(' ')]
#
# max = 0
# for i in range(1,x+1):
#     x_result = x % i
#     y_result = y % i
#
#     if x_result ==0 and y_result ==0 and i>max:
#         max =i
#
# print(max)

x, y = [int(x) for x in input().split()]

while x % y != 0:
    x, y = y, x % y

print(y)