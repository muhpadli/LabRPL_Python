def garis():
    print(30*"-")

print("latihan Looping")
garis()
jumlah_biodata = int(input("jumlah daftar biodata yang dicetak :"))
listnama = []
listusia = []
listalamat = []
for i in range (jumlah_biodata):
    garis()
    nama = input("masukkan nama :",)
    listnama.append(nama)
    usia = int(input("masukkan usia :",))
    listusia.append(usia)
    alamat = input("masukkan alamat :",)
    listalamat.append(alamat)
print()
garis()
for i in range(jumlah_biodata):
    print("nama :", listnama[i])
    print("usia :", listusia[i])
    print("alamat :", listalamat[i])
    garis()
