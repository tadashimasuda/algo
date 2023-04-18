n = 7
dir = "BFFBFBB"
dir = [0 if x == "F" else 1 for x in dir]


def calc(k):
    res, g = 0, 0
    f = [0] * n
    for i in range(n - k + 1):  # 7-1+1
        # 牛を左から順に見る
        if (dir[i] + g) % 2 != 0:
            # 後ろを向いている場合 => 区間反転
            res += 1
            f[i] = 1
            print(k, ";", f)
        g += f[i]
        if i - k + 1 >= 0:
            g -= f[i - k + 1]

    # n-k+1までは前を向かせた => 残りが前を向いているか確認
    for i in range(n - k + 1, n):
        if (dir[i] + g) % 2 != 0:
            # 解無し
            return -1
        if i - k + 1 >= 0:
            g -= f[i - k + 1]
    return res


if __name__ == "__main__":
    ans_k, ans_m = 1, n
    for k in range(1, n + 1):  # ｋを１から始めていく。
        m = calc(k)
        if m >= 0 and ans_m > m:
            ans_k, ans_m = k, m

    print(ans_k, ans_m)
