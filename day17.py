def garis():
    print(30*"-")

negara = ["Indonesia", "Malaysia", "Singapura", "Brunai Darussalam"]

#enumerate
for i,asean in enumerate(negara):
    print("No.",i,asean)
    i +=1
garis()
#zip
ibukota = ["Jakarta", "Kuala Lumpur", "Singapura", "Bandar sri begawan"]
for i, asean2 in zip(negara,ibukota):
    print(i, "ibukotanya adalah", asean2)
garis()
#set
buah = {"apel", "mangga", "pisang", "anggur"}
for namabuah in sorted(buah):
    print(namabuah)
garis()
#dictionary
biodata = {"nama" : "Muh. Padli",
           "nim" : "D0221513",
           "prodi" : "Informatika"}
for i,identitas in biodata.items():
    print(i,":", identitas)
