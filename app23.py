# 2:27:03 Unpack
numbers = (5, 6, 7)
x = numbers[0]
y = numbers[1]
z = numbers[2]
print(f"{x} {y} {z}")

a, b, c = numbers
print(f"{a} {b} {c}")

numbers = [5, 6, 7]
p, q, r = numbers
# p, q = numbers # error: too many values to unpack
# p, q, r, s = numbers # error: not enough values to unpack
print(f"{p} {q} {r}")

r, _, _ = numbers
print(f"{p} {q} {r}")

r, *q = numbers
print(f"{p} {q} {r}")

numbers = (5, 6, 7)
r, *q = numbers
print(f"{p} {q} {r}")