#program tipe data set

data = 3

negara = set()
ibukota = set()
for i in range(1,data+1):
    name_negara = input(f"\nmasukkan nama negara ke-{i} :")
    negara.update([name_negara])
    name_Ibukota = input(f"masukkan nama ibukota {name_negara} :")
    ibukota.update([name_Ibukota])


print(negara)
print(ibukota)

