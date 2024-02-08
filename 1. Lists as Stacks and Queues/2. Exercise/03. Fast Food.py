from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()
    if food < current_order:
        orders.appendleft(current_order)
        break

    food -= current_order

if not orders:
    print("Orders complete")
else:
    print("Orders left:", ' '.join(map(str, orders)))
