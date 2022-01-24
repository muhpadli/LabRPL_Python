import sys

total = []

print("\n"+"-"*84,
      "\n"+" "*35,"TOKO ANUGRAH"," "*35,
      "\n"+"-"*84,"\n")

def daftar_barang():
    no = [1,2,3,4,5]
    nama_barang = ["Downi", "Baygon", "Mamy Poko", "Ovaltine", "Beras"]
    harga = ["Rp. 23.000", "Rp. 41.100", "Rp. 59.000", "Rp. 23.000", "Rp. 70.000"]

    print("-"*84,
          "\n|   No   |                 Nama Barang                |           Harga            |",
          "\n","-"*83)

    for i in range (5):
        kolom_1 = str(no[i])
        kolom_2 = str(nama_barang[i])
        kolom_3 = str(harga[i])
        print("|   "+kolom_1+ (5-len(kolom_1))*" "+
        "| "+kolom_2+(43-len(kolom_2))*" "+
        "| "+kolom_3+(27-len(kolom_3))*" "+"|")
    print("-"*84)

    kode = int(input("Masukkan Angka barang : "))
    jml_barang = int(input("Masukkan Jumlah barang : "))

    if(kode == 1):
        total_1 = 23_000 * jml_barang
        total.append(total_1)
    elif(kode == 2):
        total_2 = 41_000 * jml_barang
        total.append(total_2)
    elif(kode == 3):
        total_3 = 59_000 * jml_barang
        total.append(total_3)
    elif(kode == 4):
        total_4 = 23_000 * jml_barang
        total.append(total_4)
    elif(kode == 2):
        total_5 = 70_000 * jml_barang
        total.append(total_5)  
    print(tambah())

def tambah():
    print("\n"+" "*84)
    tanya = input("Ingin tambah barang (y/n) ? :").lower()
    if(tanya == "y"):
        daftar_barang()
    else:
        akhir()

def akhir():
    for i in total:
        total_harga_barang = sum(total )
        print("total harga barang :", total_harga_barang)
        diskon = 0
        if(total_harga_barang > 500_000):
            diskon = (8/100)*total_harga_barang
        elif(total_harga_barang > 300_000):
            diskon = (5/100)*total_harga_barang
        elif(total_harga_barang > 200_000):
            diskon = (3/100)*total_harga_barang
        elif(total_harga_barang > 100_000):
            diskon = (1/100)*total_harga_barang

        total_bayar = total_harga_barang - diskon
        print("Potongan harga  : Rp. ", diskon)
        print("Total Bayar     : Rp. ", total_bayar)        
        bayar = int(input("Jumlah yang di bayar : Rp."))
        kembalian = bayar - total_bayar 
        print("Kembalian : Rp. ", kembalian)
        print("\n"+84*"-"+"\n"+" "*35+"TERIMA KASIH"+"\n"+84*"-")
daftar_barang()