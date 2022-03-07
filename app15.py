# 1:39:55 Game Tebak Angka
trying = 0
secret_number = 7
limit = 3

while trying < limit:
    guess_number = input("Masukkan angka (1-9) : ")
    guess_number = int(guess_number)

    if guess_number == secret_number:
        print("Selamat, anda menang")
        break

    trying += 1