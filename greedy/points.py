N = 6
R = 10
N = 6
X = [1, 7, 15, 20, 30, 50]

point = X[0]
i = 0
ans = 0
while i < N:
    s = X[i]
    i += 1
    while i < N and X[i] <= s + R:
        i += 1  # 現在地から一番右
    # sから距離Rを超える点は印をつける
    p = X[i - 1]
    while i < N and X[i] <= p + R:
        i += 1
    ans += 1

print(ans)
