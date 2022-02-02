#program pemuat kata sandi rumit
import random

huruf = ["a","b","c","d","e","f","g","h","i","j","k",
         "l","m","n","o","p","q","r","s","t","u","v",
         "w","x","z","A","B","C","D","E","F","G","H",
         "I","J","K","L","M","N","O","P","Q","R","S",
         "T","U","V","W","X","Y","Z"]

angka = ["0","1"",2","3","4","5","6","7","8","9"]

simbol = ["!","@","#","$","%","^","&","*","?"]

print("SELAMAT DATANG DI BOT PEMBUAT KATA SANDI RUMIT")
jml_huruf = int(input("\nMasukkan jumlah huruf yang digunakan: "))
jml_angka = int(input("Masukkan jumlah angka yang digunakan: "))
jml_simbol = int(input("Masukkan jumlah simbol yang digunakan: "))

list_kata_sandi = []
for p_huruf in range(jml_huruf):
    list_kata_sandi += random.choice(huruf)
for p_angka in range(jml_angka):
    list_kata_sandi += random.choice(angka)
for p_simbol in range(jml_simbol):
    list_kata_sandi += random.choice(simbol)

random.shuffle(list_kata_sandi)

katasandi = ""
for member in list_kata_sandi:
    katasandi += member
print(f"\nkata sandi anda adalah {katasandi}")

