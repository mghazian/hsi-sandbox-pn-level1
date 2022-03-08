# 3:21:01 General Exception
try:
    level = input("Level kamu : ")
    level = int(level)
    level = level / 0
    print(level)
except:
    print("Terjadi kesalahan")
