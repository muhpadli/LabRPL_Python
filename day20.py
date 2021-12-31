#latihan percabangan if else

angka = int(input("masukkan nilai angka:"))

if(angka % 2 != 0):
    print("weird")
elif(angka  >= 2 and angka <= 5):
    print("not weird")
elif(angka  >= 6 and angka <= 20):
    print("weird")
else:
    angka >20
    print("not weird")
    
