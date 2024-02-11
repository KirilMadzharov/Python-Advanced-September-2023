rows, columns = [int(x) for x in input().split(", ")]

matrix = []
total = 0

for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    total += sum(elements)
    matrix.append(elements)

print(total)
print(matrix)
