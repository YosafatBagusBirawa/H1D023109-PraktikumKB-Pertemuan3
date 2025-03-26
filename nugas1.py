import datetime
import random

angka_tebak = random.randint(1, 100)
percobaan_tebak = []
mulai= datetime.datetime.now()

print("permainan tebak tebakan angka 1 - 100")
print("kalau menyerah input angka 0")

while True:
    tebak = input("\nmasukan tebakan anda: ")

    if not tebak.isdigit():
        print("input hanya boleh berbenruk angka! coba lagi")
        continue

    tebak=int(tebak)

    percobaan_tebak.append(tebak)

    if tebak == 0:
        print(f"anda surrend, PAYAH!. Angkanya adalah {angka_tebak}")
        break

    if tebak < angka_tebak:
        print("angka anda lebih kecil. coba lagi!")
    elif tebak > angka_tebak:
        print("angka anda lebih besar. coba lagi!")
    elif tebak == angka_tebak:
        print(f"benar! anda menebak angka {angka_tebak} yang dicari")
        break

selesai = datetime.datetime.now()
waktu = selesai - mulai

print("\nringkasan:")
print(f"semua tebakan anda: {percobaan_tebak}")
print(f"waktu yang dibutuhkan : {waktu.seconds} detik")

