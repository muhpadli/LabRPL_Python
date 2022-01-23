#program Laundry Pakaian

print(45*" "+"P R O G R A M   L A U N D R Y   P A K A I A N"+
      "\n"+140*"="+
      "\n"
      "\n"+"Input Data Pesanan"+
      "\n"+18*"=")

layanan = ["1. Reguler", "2. Express", "3. Kilat"]
nama_pelanggan = input("\nNama Pelanggan :")
Alamat = input("Alamat :")
no_hp = int(input("No. Handphone :"))

print("\n"+"Kategori Cucian"+"\n"+15*"=")
for i in (layanan):
    print(i)

kategori_cucian = int(input("\nInput no kategori (1-3) :"))
berat_cucian = int(input("Masukkan Berat Cucian (kg) :"))

if(kategori_cucian == 1):
    jenis_layanan = "Reguler"
    biaya = 9_000
elif(kategori_cucian == 2):
    jenis_layanan = "Express"
    biaya = 12_000
elif(kategori_cucian == 3):
    jenis_layanan = "Kilat"
    biaya = 15_000
total_biaya = berat_cucian*biaya

print("\n"+"Resi Pesanan Laundry"+"\n"+20*"=")
print("\nnama Pelanggan :",nama_pelanggan,
     "\nAlamat :",Alamat,
     "\nNo Handphone :",no_hp,
     f"\nCucian {jenis_layanan} 1 hari : Rp. {biaya}",
     "\nTotal biaya : Rp. ",total_biaya,
     "\n")

bayar = int(input("Total bayar : Rp. "))
kembalian = bayar-total_biaya
print(f"Kembalian : Rp. {kembalian}",
      "\n"+140*"=",
      "\nTerimakasih telah datang di Laundry Kami")



