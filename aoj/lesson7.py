# ITP1_7_A
# while True:
#     m,f,r = [int(i) for i in input().split(' ')]
#
#     if m == -1 and f == -1 and r == -1:
#         break
#
#     all_point = m + f
#     if m == -1 or f == -1:
#         print('F')
#     elif all_point>=80:
#         print('A')
#     elif all_point>=65:
#         print('B')
#     elif all_point>=50:
#         print('C')
#     elif all_point>=30:
#         if r>=50:
#             print('C')
#         else:
#             print('D')
#     else:
#         print('F')

# ITP1_7_C
# column_num,row_num = [int(i) for i in input().split(' ')]
# count =0
# data =[]
# last_list = []
#
# while column_num > count:
#     data.append([int(i) for i in input().split(' ')])
#     count+=1
#
# row_all = 0
# for row in data:
#     row.append(sum(row))
#     row_all+=sum(row)
#
# column_all =0
# for x in range(row_num):
#     column_all = 0
#     for y in range(column_num):
#         column_all+=data[y][x]
#     last_list.append(column_all)
#
# last_list.append(sum(last_list))
# data.append(last_list)
#
# for i in data:
#     print(" ".join([str(_) for _ in i]))

#個人的な別解
# column_num,row_num = [int(i) for i in input().split(' ')]
# count =0
# data =[]
# last_list = []
#
# while column_num > count:
#     data.append([int(i) for i in input().split(' ')])
#     count+=1
#
# column_list =[int(0) for _ in range(row_num)]
#
# for x in range(row_num):
#     for y in range(column_num):
#         print(data[x][y],end=' ')
#         column_list[y] += data[x][y]
#
#     print(sum(data[x]))
#
# print(" ".join([str(_) for _ in column_list]),end = ' ')
# print(sum(column_list))
