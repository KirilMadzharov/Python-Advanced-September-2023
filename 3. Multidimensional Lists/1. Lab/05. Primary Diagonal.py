n = int(input())

matrix = []

for row in range(n):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

total = 0

for i in range(n):
    total += matrix[i][i]

print(total)


