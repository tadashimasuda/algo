# 3 3
# 0 0
# 2 0
# s..
###.
# g..

from collections import deque

h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
s = []
for i in range(h):
    s.append(input())


visited = [[False for j in range(w)] for i in range(h)]

q = deque()
q.append((sy, sx, 0))

answer_step = -1
while len(q) - 1:
    y, x, step = q.popleft()

    # ゴールしているか
    if y == gy and x == gx:
        answer_step = step
        break

    # 外側にはみ出ているか
    if y < 0 or y >= h or x < 0 or x >= w:
        continue

    # ＃であるか
    if s[y][x] == "#":
        continue

    # すでに訪れているか
    if visited[y][x]:
        continue

    visited[y][x] = True

    # 次の候補地を追加する
    q.append((y + 1, x, step + 1))
    q.append((y - 1, x, step + 1))
    q.append((y, x + 1, step + 1))
    q.append((y, x - 1, step + 1))

if answer_step == -1:
    print("No")
else:
    print(answer_step)
