#Mencari nilai tertinggi dengan forlooping

daftar_nilai = input("Masukkan daftar nilai :\n").split()
for  n in range (0, len(daftar_nilai)):
    daftar_nilai[n] = int(daftar_nilai[n])
print(daftar_nilai)

nilai_tertinggi = 0
for nilai in daftar_nilai:
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai

print(f"nilai tertinggi dari daftar nilai yang di input adalah {nilai_tertinggi}")