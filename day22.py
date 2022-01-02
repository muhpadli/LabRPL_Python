print(15*" ","Warung Mas Bro",
      "\n",8*" ", "jalan poros majene mamuju",
      "\n",43*"=","\n",3*" ", "Daftar menu :")
no = 1
makanan = {"Ayam Goreng":"(Rp. 10.000)","Nasi Goreng":"(Rp. 12.000)",
           "Mie Pangsit":"(Rp. 10.000)", "Pecel Ayam+Nasi":"(Rp. 15.000)",
           "Nasi Rames":"(Rp. 8.000)","Jus Jeruk":"(Rp. 5.000)","Teh Manis":"(Rp. 2.000)"}

for i,menu in makanan.items():
    print(4*" ","%d."%no,i,menu)
    no +=1
print("\n",43*"=")

pesanan = int(input("masukkan nomor menu pilihan anda : "))
jml_porsi = int(input("masukkan jumlah porsi : "))


if(pesanan == 1):
    harga = 10000
    total_bayar = harga * jml_porsi
elif(pesanan == 2):
    harga = 12000
    total_bayar = harga * jml_porsi
elif(pesanan == 3):
    harga = 10000
    total_bayar = harga * jml_porsi
elif(pesanan == 4):
    harga = 15000
    total_bayar = harga * jml_porsi
elif(pesanan == 5):
    harga = 8000
    total_bayar = harga * jml_porsi
elif(pesanan == 6):
    harga = 5000
    total_bayar = harga * jml_porsi
elif(pesanan == 7):
    harga = 2000
    total_bayar = harga * jml_porsi
else:
    print(4*" ","maaf pilhan yang anda masukkan salah")
    pass

print("total harganya        :Rp.", total_bayar)
dibayar = int(input("Dibayar               :Rp. "))
print("kembali               :Rp.", dibayar - total_bayar)
print("Terima kasih atas kunjungan anda di warung Mas Bro")
    
