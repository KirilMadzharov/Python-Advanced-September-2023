data = input().split(", ")

rows = int(data[0])
cols = int(data[1])

matrix = []

for row in range(rows):
    elements = list(map(int, input().split(", ")))
    matrix.append(elements)

max_sum = float("-inf")
max_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        next_element_below = matrix[row_index + 1][col_index + 1]

        sum_elements = current_element + next_element + element_below + next_element_below

        if max_sum < sum_elements:
            max_sum = sum_elements
            max_matrix = [
                [current_element, next_element],
                [element_below, next_element_below]
            ]

for row in max_matrix:
    print(" ".join(map(str, row)))
print(max_sum)
