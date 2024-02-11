n = int(input())

reservations = set()

for _ in range(n):
    reservation_number = input()
    reservations.add(reservation_number)

guest = input()

while guest != "END":
    reservations.remove(guest)
    guest = input()

print(len(reservations))

for num in sorted(reservations):
    print(num)
