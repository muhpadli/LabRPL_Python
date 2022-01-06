mtk = int(input("Masukkan nilai Matematika :"))
B_ing = int(input("Masukkan nilai Bahasa Inggris :"))
B_ina = int(input("Masukkan nilai Bahasa Indonesia :"))
nilai = []
nilai.insert(B_ing, B_ina)
nilai.append(mtk)
rata_rata = sum(nilai)/len(nilai)
print("\n Pilih Minat:")
minat = ["1. Elektro", "2. Mesin", "3. Pariwisata"]
for i in minat:
    print(i)
pilihan_minat = int(input("masukkan kode pilihan minat [1..3] :"))
if(rata_rata > 70 and rata_rata <= 100):
    print("anda bebas memilih yang disukai")
elif(rata_rata == 70):
    if(pilihan_minat == 1):
        print("Bidang Elektro")
    elif(pilihan_minat == 2):
        print("Bidang Elektro")
    else:
        print("Biadang Pariwisata")
    print("skor anda adalah %d, anda dinyatakan lolos kebidang berikutnya" %rata_rata)
elif(rata_rata < 70):
    print("anda tidak dinyatakan lolos karena skor anda adalah %d" %rata_rata)