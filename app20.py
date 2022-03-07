# 2:15:30 Menjumlahkan List
numbers = [a ** 3 - 2 * a + 11 for a in range(8)]
print(sum(numbers))

total = 0
for item in numbers:
    total = total + item

print(total)