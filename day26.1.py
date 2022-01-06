#program emasukkan data input kedalam tabel
banyak_data = int(input("Masukkan jumlah data : "))
list_nama =[]
list_umur =[]
list_alamat = []
no = 1
for i in range (banyak_data):
    print("\nInput data ke-", no)
    nama = input("masukkan nama :")
    list_nama.append(nama)
    umur = int(input("Masukkan umur :"))
    list_umur.append(umur)
    alamat = input("masukkan alamat :")
    list_alamat.append(alamat)
    no += 1

print("\n+-----------------------------------------------------+"
      "\n|       Nama      |      umur      |      alamat      |"
      "\n+-----------------------------------------------------+")
for j in range (banyak_data):
    kolom_1 = str(list_nama[j])
    kolom_2 = str(list_umur[j])
    kolom_3 = str(list_alamat[j])
    print("| "+kolom_1+(16-len(kolom_1))*" "+
          "| "+kolom_2+(15-len(kolom_2))*" "+
          "| "+kolom_3+(17-len(kolom_3))*" "+"|")
print("+"+53*"-"+"+")