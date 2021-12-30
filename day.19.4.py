#program tunjangan gaji

Gaji_pokok = int(input("masukkan gaji pokok :"))
jml_anak = int(input(" masukkan jumlah anak :"))

if(jml_anak <= 3 and jml_anak > 0):
    tunjangan = jml_anak*(10/100)*Gaji_pokok
elif(jml_anak > 3):
    tunjangan = 3*(10/100)*Gaji_pokok
else:
    tunjangan = 0

print("Tunjangan dari gaji anda adalah Rp. %d- " %tunjangan)
