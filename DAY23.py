nama = input("masukkan nama pembeli : ")
status = input("apakah pelanggan <y/t> :")
status = status.lower()
waktu = int(input("masukkan waktu menyewa (jam) :"))
uang_bayar = int(input("masukkan uang yang dibayar :"))
diskon = 0                

if(status == "y"):
    keterangan = "Pelanggan"
    harga_1jam = 4000
    if(waktu >= 5):
        diskon = (50/100)
    elif(waktu >= 3):
        diskon = (30/100)
elif(status == "t"):
    keterangan = "umum"
    harga_1jam = 5000
    if(waktu >= 5):
        diskon = (50/100)
    elif(waktu >= 3):
        diskon = (30/100)

harga_sewa = waktu * harga_1jam
jumlah_bayar = harga_sewa - (diskon*harga_sewa)
uang_kembali = uang_bayar - jumlah_bayar

print("\n", 27*" ","W  A  R  N  E  T",
      "\n", 78*"=",
      "\nNama Pengunjung          :", nama,
      "\nketerangan               :", keterangan,
      "\nDiscount yang diperoleh  :", diskon * harga_sewa,
      "\nTotal pembayaran         :", jumlah_bayar,
      "\n", 78*"=",
      "\nUang bayar               :", uang_bayar,
      "\nUang kembali             :", uang_kembali,
      "\n", 78*"=",
      "\nTERIMAKASIH ATAS KUNJUNGAN ANDA")


        
