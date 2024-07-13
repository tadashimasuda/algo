# abc 188 b
def b_188():
    N = map(int, input().split())
    a_list = map(int, input().split())
    b_list = map(int, input().split())

    result = 0
    for a, b in zip(a_list, b_list):
        result += a * b

    if result == 0:

        print("Yes")
    else:
        print("No")


# 191 b Remove It
def remove_it():
    N, X = map(int, input().split())
    A = map(int, input().split())
    A = list(A)

    result = []
    for a in A:
        if a != X:
            result.append(a)

    if len(A) == 0:
        print()
    else:
        print(*result)


# 190 B - Magic 3
def magic3():
    N, S, D = map(int, input().split())
    xy_list = []
    for _ in range(N):
        X, Y = map(int, input().split())
        xy_list.append((X, Y))

    flag = False
    for x, y in xy_list:
        if S > x and D < y:
            flag = True
            exit()

    if flag:
        print("Yes")
    else:
        print("No")


def second_highest_mountain():
    N = int(input())
    mountains = []
    for _ in range(N):
        name, value = input().split()
        mountains.append((name, int(value)))

    mountains = sorted(mountains, key=lambda mountain: mountain[1])
    print(mountains)


# [ '#....','#####','....#'] S[0][3]


def visibility():
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]

    result = 0

    check_Y = Y
    while W > check_Y:
        if S[X - 1][check_Y] == "#":
            break
        check_Y += 1
        result += 1

    check_Y = Y - 1 - 1
    while 0 <= check_Y:
        print(X - 1, check_Y)
        if S[X - 1][check_Y] == "#":
            break
        check_Y -= 1
        result += 1

    check_x = X
    while H > check_x:
        if S[check_x][X - 1] == "#":
            break
        check_x += 1
        result += 1

    check_x = X - 1 - 1
    while 0 <= check_x:
        if S[check_x][X - 1] == "#":
            break
        check_x -= 1
        result += 1

    result += 1

    print(result)


def alcoholic():
    N, X = map(int, input().split())
    VA = []
    for _ in range(N):
        V, P = map(int, input().split())

        # A = V * (P / 100)
        A = V * P
        VA.append([V, A])

    flag = False
    cnt = 0
    input_alcohol = 0
    # for va in VA:
    #     v = va[0]
    #     a = va[1]

    #     cnt += 1
    #     input_alcohol += a
    #     if X < input_alcohol:
    #         flag = True
    #         break

    for va in VA:
        v = va[0]
        a = va[1]

        cnt += 1
        input_alcohol += a
        if X * 100 < input_alcohol:
            flag = True
            break

    if flag:
        return cnt
    else:
        return -1


if __name__ == "__main__":
    # magic3()
    # second_highest_mountain()
    # visibility()
    print(alcoholic())
