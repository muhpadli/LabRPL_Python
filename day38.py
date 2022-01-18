#program kasir

print("\n",89*"*",
      35*" ", "R U M  A H   M A K A N",
      "\n",29*" ", "N A S I   B A L A P   P U Y U N G",
      "\n",89*"*",
      "\n Menu Makanan",25*" ","Harga")

menu = ["1. AYAM GORENG","2. NASI GORENG", "3. MIE PANGSIT","4. NASI BALAP PUYUNG", "5. NASI CAMPUR", "6. JUS JERUK", "7. AIR GELAS"]
harga = ["Rp. 10.000", "Rp. 8.000", "Rp. 10.000", "Rp. 12.000", "Rp. 8.000", "Rp. 6.000", "Rp. 500"]

for i in range(7):
    kolom_1 = str(menu[i])
    kolom_2 = str(harga[i])
    print(kolom_1 + (39-len(kolom_1))*" " + kolom_2)

kode_pesanan = int(input("\nMasukkan nomor pilihan yang anda pesan :"))

if(kode_pesanan == 1):
    pesanan = "Ayam Goreng"
    harga = 10_000
elif(kode_pesanan == 2):
    pesanan = "Nasi Goreng"
    harga = 8_000
elif(kode_pesanan == 3):
    pesanan = "Mie Pangsit"
    harga = 10_000 
elif(kode_pesanan == 4):
    pesanan = "Nasi balap puyung"
    harga = 12_000 
elif(kode_pesanan == 5):
    pesanan = "Nasi Campur"
    harga = 8_000 
elif(kode_pesanan == 6):
    pesanan = "Jus Jeruk"
    harga = 6_000 
elif(kode_pesanan == 7):
    pesanan = "Air Gelas"
    harga = 8_000 

jml_pesanan = int(input(f"\nMasukkan jumlah {pesanan} yang ingin anda pesan :"))
total_harga = jml_pesanan * harga
print(f"Total harganya yaitu : Rp.{total_harga}")
bayar = int(input("Uang dibayar sebesar : Rp."))
kembali = bayar - total_harga
print(f"Uang kembali sebesar : Rp.{kembali}")
print("\nTERIMAKASIH ATAS KUNJUNGAN ANDA")

    

    

