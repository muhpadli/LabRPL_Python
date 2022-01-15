#program penggunaan while, else, break

nama_negara = ["Jerman", "Jepang", "Amerika", "Asutralia", "Indonesia", "Malaysia"]

Negara_yg_dicari = input("Masukkan nama negara yang di cari :").lower()

i = 0
while i < len(nama_negara):
    if(nama_negara[i].lower() == Negara_yg_dicari):
        print(f"ketemu di index {i}")
        break
    print(f"bukan {nama_negara[i]}")
    i += 1
else:
    print("Maaf, Negara yang anda cari tidak ditemukan.")
