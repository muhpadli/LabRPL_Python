#program membuat tabel sederhana
jmlh_kode_rumah = 3
kode_rumah = ["A", "B", "C"]
tipe_rumah = ["RSS", "RS", "MEWAH"]
uang_muka = ["Rp. 80.000,-", "Rp. 100.000,-", "Rp. 12.000.000,-"]
harga = ["20.000.000,-", "25.000.000,-", "300.000.000,-"]

print(
    "+-----------------------------------------------------------------------+"
    "\n|    Kode Rumah   |    Tipe Rumah   |    Uang Muka    |    Harga        |"
    "\n+-----------------------------------------------------------------------+" )

for i in range (jmlh_kode_rumah):
    kolom_1 = str(kode_rumah[i])
    kolom_2 = str(tipe_rumah[i])
    kolom_3 = str(uang_muka[i])
    kolom_4 = str(harga[i])
    print("| "+ kolom_1 + (16-len(kolom_1))*" "+
         "| " + kolom_2 + (16-len(kolom_2))*" "+
         "| " + kolom_3 + (16-len(kolom_3))*" "+
         "| " + kolom_4 + (16-len(kolom_4))*" "+"|")
print(73*"-")