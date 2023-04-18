def min_coin(V, C, A):
    V = reversed(V)
    C = reversed(C)

    ans = 0
    for c, v in zip(C, V):
        num = min(c, A // v)
        A -= num * v
        ans += num
        print(v, num)

    return ans


if __name__ == "__main__":
    V = [1, 5, 10, 50, 100, 500]
    C = [3, 2, 1, 3, 0, 2]
    A = 620

    print(min_coin(V, C, A))
