# 3:29:56 Menulis File
users = open("data/users_new.txt", "w")

users.write("Desi Latifa - desilatifa - User\n")

users.close()

users = open("data/users.txt", "a")

users.write("Desi Latifa - desilatifa - User\n")

users.close()