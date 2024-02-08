from collections import deque

quantity = int(input())
water_queue = deque()

name = input()

while name != "Start":
    water_queue.append(name)
    name = input()

command = input()

while command != "End":

    data = command.split()

    if len(data) == 1:
        litters_to_give = int(data[0])
        person_name = water_queue.popleft()
        if litters_to_give <= quantity:
            print(f"{person_name} got water")
            quantity -= litters_to_give
        else:
            print(f"{person_name} must wait")

    else:
        litters_to_add = int(data[1])
        quantity += litters_to_add

    command = input()

print(f"{quantity} liters left")
