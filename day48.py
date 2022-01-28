#program nested list

Indonesia = ["Jakarta", "Bandung", "Surabaya", "Makassar", "Samarinda", "Aceh"]
Malaysia = ["Kuala Lumpur", "Kuala Selangor", "Johor bahru", "Pulau Pinang", "Kota Kinabalu", "Kota Melaka"]

ASEAN = [Indonesia, Malaysia]
print(ASEAN)
print()

#program meletakan zonk 
baris_1 = ["1","1","1"]
baris_2 = ["1","1","1"]
baris_3 = ["1","1","1"]
map = [baris_1,baris_2,baris_3]
print(f"{baris_1}\n{baris_2}\n{baris_3}")

posisi = input("dimana anda ingin meletakkan zonk :")

baris = int(posisi[0])
kolom = int(posisi[1])


map[kolom -1][baris - 1]= "0"
print(f"{baris_1}\n{baris_2}\n{baris_3}")