n = int(input())
matrix = []

for row in range(n):
    matrix.append([])
    elements = [int(x) for x in input().split(", ")]

    for i in elements:
        if i % 2 == 0:
            matrix[row].append(i)

print(matrix)