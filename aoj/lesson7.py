while True:
    m,f,r = [int(i) for i in input().split(' ')]

    if m == -1 and f == -1 and r == -1:
        break

    all_point = m + f
    if m == -1 or f == -1:
        print('F')
    elif all_point>=80:
        print('A')
    elif all_point>=65:
        print('B')
    elif all_point>=50:
        print('C')
    elif all_point>=30:
        if r>=50:
            print('C')
        else:
            print('D')
    else:
        print('F')