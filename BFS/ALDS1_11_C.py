# from collections import deque

# u = map(int, input())
# graph = [(map(int, input().split())) for _ in range(u)]


u = 4
graph = [
    [2, 2, 4],
    [1, 4],
    [0],
    [1, 3],
]

# # v: step
# memo = {}
# q = deque()
# q.append((1, 0))

# while len(q) > 0:
#     u, step = q.popleft()

#     if not u in memo:
#         memo[u] = step
#     elif memo[u] < step:
#         memo[u] = step

#     item = graph[u - 1]
#     # k = item[0]
#     for v in item[2:]:
#         print(v)
#         q.append((v, step + 1))

# print(memo)


from collections import deque

u = 4
g = [
    "1 2 2 4",
    "2 1 4",
    "3 0",
    "4 1 3",
]
transformed_g = []
for row in g:
    transformed_g.append(list(map(int, row.split())))

q = deque()
result = {}
step = 0

result[transformed_g[0][0]] = step
q.append(transformed_g[0][0])


while len(q) > 0:
    step += 1
    pop_v = q.popleft()

    for v in transformed_g[pop_v - 1][2:]:
        val = result.get(v)
        if val:
            continue
        result[v] = step
        q.append(v)
    print(result)


print(result)
