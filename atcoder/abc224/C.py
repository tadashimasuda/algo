N = int(input())
points = []

input_count = 0
while input_count<N:
    x,y = [int(_) for _ in input().split(' ')]
    points.append([x,y])
    input_count+=1

count = 0
for i1 in range(N):
    for i2 in range(i1):
        if i1==i2:
            continue
        for i3 in range(i2):
            if i2==i3 or i1==i3:
                continue

            x1 = points[i1][0]
            y1 = points[i1][1]

            x2 = points[i2][0]
            y2 = points[i2][1]

            x3 = points[i3][0]
            y3 = points[i3][1]

            if ((y2-y1)*(x3-x1) != (x2-x1)*(y3-y1)):
               count+=1


print(count)