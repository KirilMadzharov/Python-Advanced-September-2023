nums = tuple(float(i) for i in input().split())

occ = {}

for num in nums:
    occ[num] = nums.count(num)

for key, value in occ.items():
    print(f"{key} - {value} times")
