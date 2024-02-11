n = int(input())

cars = set()

for _ in range(n):
    direction, car_plate = input().split(", ")
    if direction == "IN":
        cars.add(car_plate)
    elif direction == "OUT":
        cars.remove(car_plate)

if cars:
    for car in cars:
        print(car)

else:
    print("Parking Lot is Empty")
