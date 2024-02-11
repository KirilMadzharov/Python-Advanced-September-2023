rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split(", ")]
    matrix.append(elements)

flattening_matrix = []

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattening_matrix.append(matrix[row_index][col_index])

print(flattening_matrix)
