#program menghitung rata - rata
list_nilai = []

banyak_data = int(input("Masukkan banyak data :"))

for i in range (banyak_data):
    nilai_ke = int(input(f"Masukkan nilai ke- {i+1} : "))
    list_nilai.append(nilai_ke)
    i += 1

rata_rata = round(sum(list_nilai)/banyak_data, 2)
print(f"rata-rata nya adalah {rata_rata}")


