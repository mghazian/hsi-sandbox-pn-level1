# 3:21:55 Membaca File
users = open("data/users.txt", "r")

array = users.readlines()
print(array)

index = 1
for user in array:
    print(f"{index} -  {user}")
    index += 1

users.seek(0)

line = users.readline()
while line != "":
    print(line)
    line = users.readline()

users.close()