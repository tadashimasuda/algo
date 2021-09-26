# #ITP1_1_B
# X = int(input())
# print(X ** 3)
#
# #ITP1_1_C
# input = input()
# a,b = [int(num) for num in input.split(' ')]
# print(str(a * b) + ' ' + str(a * 2 + b * 2))
#
# #ITP1_1_D
# input = int(input())
# h, mod = divmod(input, 3600)
# m,s = divmod(mod, 60)
# print(f"{h}:{m}:{s}")
#
# #ITP1_2_A
# input = input()
# a,b = [int(num) for num in input.split(' ')]
# if a<b:
#     print('a < b')
# elif a>b:
#     print('a > b')
# elif a == b:
#     print('a == b')
#
# # ITP1_2_B
# input = input()
# a,b,c = [int(num) for num in input.split(' ')]
# if a < b  and b < c:
#     print('Yes')
# else:
#     print('No')
#
# # ITP1_2_C
# input = input()
# list = [int(num) for num in input.split(' ')]
# list.sort()
# print(f"{list[0]} {list[1]} {list[2]}")
#
# #ITP1_2_D
# # input = input()
# input = '5 4 2 4 1'
# W,H,x,y,r = [int(num) for num in input.split(' ')]
#
#
# way = (x + r <= W,y + r <= H,x - r >= 0,y - r >= 0,y - r >= 0)
# if W >= x and H >= y:
#     if(all(way)):
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('No')
#
# # ITP1_3_A
# for _ in range(1000):
#     print('Hello World')
#
# # ITP1_3_C
# while True:
#     x, y = map(int, input().split())
#     if x == 0 and y == 0:
#         break
#     elif x < y:
#         print(x, y)
#     else:
#         print(y, x)

#ITP1_3_D
# input = input()
# a,b,c = [int(num) for num in input.split(' ')]
#
# count = 0
# for i in range(a,b+1):
#     if c % i ==0:
#         count+=1
# print(count)

# ITP1_4_A
# input = input()
# a,b = [int(num) for num in input.split(' ')]
#
# print("{0} {1} {2:.8f}".format(a//b,a%b,a/b))

#ITP1_4_B
# import math
#
# r = float(input()) #ここ大事
# print('{0:.6f} {1:.6f}'.format(r*r*math.pi, 2*r*math.pi))

#ITP1_5_A
# while True:
#     H,W = [int(num) for num in input().split(' ')]
#
#     if H==0 and W==0:
#         break
#
#     for h in range(H):
#         print("#" * W)
#     print()

#ITP1_5_C
# while True:
#     H,W = [int(num) for num in input().split(' ')]
#
#     if H == 0 and W == 0:
#         break
#
#     flag = True
#     for h in range(H):
#         list = []
#         if(h==0 or h%2==0): flag=True
#         else: flag=False
#         for w in range(W):
#             if not flag:
#                 list.append('.')
#                 flag=True
#             else:
#                 list.append('#')
#                 flag=False
#
#         print("".join([str(_) for _ in list]))
#     print()