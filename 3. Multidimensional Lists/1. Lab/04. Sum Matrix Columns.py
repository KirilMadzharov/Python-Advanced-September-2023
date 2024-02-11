rows, columns = [int(x) for x in input().split(", ")]

matrix = []
total = 0

for row in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for col in range(columns):
    for row in range(rows):
        current_element = matrix[row][col]
        total += matrix[row][col]
    print(total)
    total = 0
