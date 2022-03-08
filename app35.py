# 3:35:49 Membaca CSV
import csv
users = open("data/users.csv", "r")

users_csv = csv.reader(users, delimiter = ",")

for name, username, role in users_csv:
    print(f"{name} (@{username}) - {role}")

users.seek(0)

for row in users_csv:
    print(f"Name : {row[0]}. Username : {row[1]}. Role : {row[2]}")

users.close()