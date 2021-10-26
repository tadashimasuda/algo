N = int(input())
points = []

input_count = 0
while input_count<N:
    x,y = [int(_) for _ in input().split(' ')]
    points.append([x,y])
    input_count+=1

count = 0
for i in range(len(points)):
    for j in range(i+1,len(points)):
        x1 = points[i][0]
        x2 = points[j][0]

        y1 = points[i][1]
        y2 = points[j][1]

        print(y1,y2,x1,x2,':',i,j)

        try:
            print(abs(y1-y2)/abs(x1-x2))
        except ZeroDivisionError:
            print(0)
        # tilt1 = y1/x1
        # tilt2 = y2/x2
        
        # if(tilt1 == tilt2):
        #     for z in range(j,len(points)): 
        #         x3 = points[z][0]
        #         y3 = points[z][1]

        #         if(not tilt1 == y3/x3):
        #             count+=1
        # else:
        #     count+=1

print(count)