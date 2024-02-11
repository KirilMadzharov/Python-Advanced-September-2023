n = int(input())
unique = set()

for i in range(n):
    elements = input().split()

    for element in elements:
        unique.add(element)

print("\n".join(unique))
