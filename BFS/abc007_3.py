from collections import deque

# R, C = map(int, input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
# c = [input() for _ in range(R)]

R, C = 7, 8
sy, sx = 1, 1
gy, gx = 3, 4
c = [
    "########",
    "#......#",
    "#.######",
    "#..#...#",
    "#..##..#",
    "##.....#",
    "########",
]

visited = [[False for _ in range(C)] for _ in range(R)]

step = 0
ans = 0
q = deque()
q.append((sy, sx, step))

while len(q) > 0:
    y, x, step = q.popleft()

    if y == gy and x == gx:
        ans = step
        break

    if visited[y][x]:
        continue

    if y < 0 or y >= R or x < 0 or x >= C:
        continue

    if c[y][x] == "#":
        continue

    visited[y][x] = True
    q.append((y + 1, x, step + 1))
    q.append((y - 1, x, step + 1))
    q.append((y, x + 1, step + 1))
    q.append((y, x - 1, step + 1))

print(q)
print(ans)

# memo = [[0 for _ in range(C)] for _ in range(R)]

# current_y = sy
# current_x = sx

# current_index = 0
# while True:
#     current_index += 1

#     # GOAL
#     if current_y + 1 == gy and current_x + 1 == gx:
#         break

#     if c[current_y][current_x + 1] == ".":
#         c[current_y][current_x + 1] = current_index

#     if c[current_y][current_x - 1] == ".":
#         c[current_y][current_x - 1] = current_index

#     if c[current_y + 1][current_x] == ".":
#         c[current_y + 1][current_x] = current_index

#     if c[current_y - 1][current_x] == ".":
#         c[current_y - 1][current_x] = current_index
