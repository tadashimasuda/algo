# N,MAX_W= [int(i) for i in input().split(' ')]

# w = v = []
# for i in range(N):
#     x,y = [int(i) for i in input().split(' ')]
#     w.append(x)
#     v.append(y)

# dp = [[0]*(MAX_W+1) for _ in range(N+1)]

# for i in range(N):
#     for j in range(MAX_W+1):
#         if j < w[i]:
#             dp[i+1][j] = dp[i][j]
#         else:
#             dp[i + 1][j] = max(dp[i][j],dp[i][j-w[i]] + v[i])

# print(dp[-1][-1])

# N W
# v w
# vw

from typing import List, Tuple


def knapsack(N: int, MaxW: int, wt: List[int], vals: List[int]):
    # dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    # for i in range(N + 1):
    #     wi, vi = wt[i], vals[i]
    #     for w in range(W + 1):
    #         if w - wi < 0: #  itemのweightがｗより大きくないか
    #             dp[i][w] = dp[i - 1][w]
    #         else:
    #             dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)

    # print(dp)

    dp = [[0 for _ in range(MaxW + 1)] for _ in range(N + 1)]

    for i in range(N):
        wi, vi = wt[i], vals[i]
        for w in range(MaxW + 1):
            if w - wi < 0:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)

    print(dp)





if __name__ == "__main__":

    # N = 4
    # W = 10
    # wt = [2, 3, 9, 1]
    # vals = [5, 4, 15, 5]

    # knapsack(N, W, wt, vals)
