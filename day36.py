
nama =input("Masukkan nama Mahasiswa:")
jml_makul = int(input("Masukkan jumlah mata kuliah : "))
sks = []
bobot_makul = []

for i in range (jml_makul):
    makul = input(f"\nMasukkan nama makul ke-{i+1} :")
    sks_permakul = int(input(f"Masukkan sks mata kuliah {makul} :"))
    sks.append(sks_permakul)
    nilai = int(input(f"Masukkan nilai mata kuliah {makul} :"))
    
    if(nilai >=80 and nilai <= 100):
        bobot =  4 * sks_permakul
        print(f"predikat nilai dari mata kuliah {makul} adalah A")
    elif(nilai >= 65 and nilai <= 79):
        bobot = 3 * sks_permakul
        print(f"predikat nilai dari mata kuliah {makul} adalah B")
    elif(nilai >= 55 and nilai <= 64):
        bobot = 2 * sks_permakul
        print(f"predikat nilai dari mata kuliah {makul} adalah C")
    else:
        bobot =  0* sks_permakul
        print(f"predikat nilai dari mata kuliah {makul} adalah D")
    
    bobot_makul.append(bobot) 
    i += 1

total_bobot = sum(bobot_makul)
total_sks = sum(sks)
ipk_mahasiswa = total_bobot / total_sks
print(f"Total SKS dari mahasiswa adalah {total_sks}")
print(f"IPK dari mahawsiswa adalah {ipk_mahasiswa}")

if(ipk_mahasiswa >= 3.5 and ipk_mahasiswa <= 4):
    print("PREDIKAT DENGAN PUJIAN")
elif(ipk_mahasiswa >= 3 and ipk_mahasiswa <= 3.49):
    print("PREDIKAT SANGAT MEMUASKAN")
elif(ipk_mahasiswa >= 2.5 and ipk_mahasiswa <= 2.99):
    print("PREDIKAT MEMUASKAN")
else:
    print("PREDIKAT LULUS")



