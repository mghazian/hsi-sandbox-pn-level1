# 3:41:16 With Block
import csv
with open("data/users.csv", "r") as users:
    users_csv = csv.reader(users, delimiter = ",")

    for name, username, role in users_csv:
        print(f"{name} (@{username}) - {role}")