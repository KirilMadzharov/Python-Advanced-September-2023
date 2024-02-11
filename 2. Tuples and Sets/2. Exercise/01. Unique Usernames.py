# n = int(input())
#
# unique_names = set()
#
# for i in range(n):
#     current_name = input()
#     unique_names.add(current_name)
#
# for name in unique_names:
#     print(name)

n = int(input())

unique_names = {input() for _ in range(n)}

for name in unique_names:
    print(name)
