# 3:52:41 Random
import random

print(random.random())
print(random.randint(10, 30))
characters = ['a', 'b', 'e', 'p', 'x', 't', 'y', 'm', 'i']

batas_bawah = 0
batas_atas = len(characters) - 1

random_int = random.randint(batas_bawah, batas_atas)
chosen = characters[random_int]

print(chosen)
print(random.choice(characters))