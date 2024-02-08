box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack = 0
racks = 0

while box_of_clothes:
    current_dress = box_of_clothes.pop()

    if current_rack + current_dress <= rack_capacity:
        current_rack += current_dress
    else:
        racks += 1
        current_rack = current_dress

    if not box_of_clothes:
        racks += 1

print(racks)
