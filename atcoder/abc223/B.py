from collections import deque
S = input()

shift_text = []
S = deque(list(S))
for i in range(len(S)):
    end = S.pop()
    S.appendleft(end)
    shift_text.append("".join([str(_) for _ in S]))

shift_text.sort()
print(shift_text[0])
print(shift_text[-1])