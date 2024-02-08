expression = input()
stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        star_index = stack.pop()
        last_index = index + 1

        print(expression[star_index:last_index])
