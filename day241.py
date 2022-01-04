print(18*" ", "S E J A H T E R A   C A F E\n",68*"=",
       "\n Tersedia :\n")
kode = [1,2,3]
paket = ["Paket Hemat", "Paket Nasi", "Paket Spesial"]
for i,j in zip (kode,paket):
    print(" %d. %s" %(i,j))

pesanan = int(input("\nMasukkan kode paket [1...3] :"))
jumlah_beli = int(input("Jumlah beli :"))
Kode_kasir = input("Masukkan kode kasir :")
Nama_Kasir = input("Masukkan Nama kasir :")
Uang_bayar = int(input("Masukkan uang yang dibayar :"))

if(pesanan == 1):
    paket_dipilih = "Paket Hemat"
    harga = 7500
elif(pesanan == 2):
    paket_dipilih = "Paket Nasi"
    harga = 10000
elif(pesanan == 3):
    paket_dipilih = "Paket Spesial"
    harga = 15000

jumlah_harga = harga * jumlah_beli
ppn = jumlah_harga * (10/100)
total_bayar = jumlah_harga + ppn

print("\n ", 68*"=", "\n %s" %paket_dipilih,
      "\n %d      x       %d  " %(jumlah_beli, harga),
      "\n Total          : Rp. %d"%jumlah_harga,
      "\n PPN            : Rp. %d"%(ppn),
      "\n Jumlah Bayar   : Rp. %d"%total_bayar,
      "\n Bayar          : Rp. %d"%Uang_bayar,
      "\n Kembali        : Rp. %d"%(Uang_bayar-total_bayar),
      "\n", 68*"=",
      "\n SELAMAT MENIKMATI",
      "\n TERIMAKASIH"
      "\n %s   %s" %(Nama_Kasir, Kode_kasir))


    