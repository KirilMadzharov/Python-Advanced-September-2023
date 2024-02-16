def even_odd(*args):
    operation = args[-1]
    numbers = args[:-1]
    even = []
    odd = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    if operation == "even":
        return even
    elif operation == "odd":
        return odd


# test code:
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
