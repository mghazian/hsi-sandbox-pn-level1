# 2:18:36 Mencari Angka Max
numbers = [8, 2, -8, 11, 4, 0, 9]
print(max(numbers))

highest = -1000000
for item in numbers:
    if item > highest:
        highest = item
print(highest)

highest = -1000000
for item in numbers:
    highest = max(highest, item)
print(highest)

numbers.sort()
print(numbers[-1])