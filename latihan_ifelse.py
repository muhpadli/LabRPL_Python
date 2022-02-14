# Latihan Percabangan if else
print('''Pak nyoman memiliki sebuah kantin yang menjual berbagai makanan kecil. harga makanan yang 
ia jual bervariasi mulai dari Rp.500,- hingga Rp.10.000,-.  Para pelanggan Pak Nyoman beranggapan 
makanan yang harganya dibawah Rp. 4.000,- termasuk murah, yang harganya diatas Rp. 7.500,- termasuk
mahal, sedangkan yang diantaranya termasuk sedang-sedang saja.
         
Buatlah sebuah program untuk membantu pak Nyoman menentukan sebuah harga murah, sedang, atau mahal.
program ini menerima masukan sebuah harga, lalu mengeluarkan kalimat "murah", "sedang", atau "mahal".''') 

harga = int(input("\nMasukkan harga makanan : "))
print (f"harga makanan : Rp. {harga} ")
if(harga > 10_000):
    kriteria = "-"
    print("Tidak menjual makanan yang diatas Rp.10.000")
elif(harga > 7_500 and harga <= 10_000):
    kriteria = "mahal"
elif(harga >= 4_000 and harga <= 7_500):
    kriteria = "sedang"
elif(harga >=500 and harga < 4_000):
    kriteria = "murah"
else:
    kriteria = "-"
    print("Tidak menjual makanan yang dibawah Rp.500")
    
print(f"kriteria : {kriteria}")