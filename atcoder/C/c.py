import itertools


def kaprekarNumber():
    N, K = map(int, input().split())

    def g1(number):
        return int("".join(sorted(list(str(number)), reverse=True)))

    def g2(number):
        return int("".join(sorted(list(str(number)))))

    next = N
    for _ in range(K):
        next = g1(next) - g2(next)

    return next


def unlucky():
    N = int(input())

    ans = 0
    for n in range(1, N):
        if str(7) not in str(n) or str(7) not in str(oct(7)):
            ans += 1

    return ans


def cream_puff():
    def Dicisor_List(N):
        i = 1

        divisor = []

        while i**2 <= N:
            if N % i == 0:
                divisor.append(i)
                if i != N // i:
                    divisor.append(N // i)

            i += 1
        divisor.sort()

        return divisor

    N = int(input())

    return Dicisor_List(N)


def friends_and_travel_cost():
    N, K = map(int, input().split())
    AB = {}
    for _ in range(N):
        A, B = map(int, input().split())
        if not A in AB:
            AB[A] = B
        else:
            AB[A] += B

    prev_village = 0
    current_village = 0
    # while K > 0:
    #     current_village += 1
    #     K -= 1

    #     if K == 0:
    #         for i in range(prev_village + 1, current_village + 1):
    #             if i in AB:
    #                 K += AB[i]
    #         prev_village = current_village

    # print(current_village)

    while K > 0:
        prev_village = current_village
        current_village += K
        K = 0

        for i in range(prev_village + 1, current_village + 1):
            if i in AB:
                K += AB[i]
                del AB[i]

        prev_village = current_village

    print(current_village)


def collinearity():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[i][0], points[i][1]
                x3, y3 = points[i][0], points[i][1]

                if (x2 - x1) * (y3 - y1) == (y2 - y1)(x3 - x1):
                    print("Yes")
                    exit()
    print("No")


def to3():
    N = int(input())


def travel():
    N, K = map(int, input().split())
    T = []

    for _ in range(N):
        line = list(map(int, input().split()))
        T.append(line)

    for root in itertools.permutations(range(2, N + 1)):
        now_time = 0
        now_time += T[0][root[0]]
        new_city = root[0]

        for i in range(1, N - 1):
            to_city = root[i]


def unexpressed():
    N = int(input())

    pass


if __name__ == "__main__":
    # print(kaprekarNumber())
    # print(unlucky())
    # print(cream_puff())
    # print(friends_and_travel_cost())
    # print(collinearity())
    print(travel())
