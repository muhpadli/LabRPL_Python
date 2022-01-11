#program menghitung gaji total
golongan = int(input("masukkan golongan anda (1,2,3) :"))
tahun_kerja = int(input("Masukkan tahun mulai kerja :"))
masa_kerja = 2011 - tahun_kerja

if(tahun_kerja >= 7):
    bonus = 150_000
    if(golongan ==1):
        gaji_pokok = 1_500_000
    elif(golongan ==2):
        gaji_pokok = 1_200_000
    elif(golongan ==1):
        gaji_pokok = 1_000_000
else:
    bonus = 0
    if(golongan ==1):
        gaji_pokok = 1_500_000
    elif(golongan ==2):
        gaji_pokok = 1_200_000
    elif(golongan ==3):
        gaji_pokok = 1_000_000

print(f"Gaji total anda adalah Rp. {gaji_pokok+bonus} ")


    

