from collections import deque

def reverse(queue: deque)->deque:
    if queue:
        new_queue = deque()
        while queue:
            new_queue(queue.pop())
        return new_queue


if __name__ == "__main__":
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.reverse()
    print(q)

