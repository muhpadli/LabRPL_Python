def deret_aritmatika(a,b,n):
    angka = 1
    hasil = 0
    for suku in range(a,n,b):
        hasil += suku
        angka += 1
        print(f"suku ke-{angka} adalah {suku}")
    print(f"Sn suku ke-{angka} adalah {hasil} ")

deret_aritmatika(a = 5,n =75,b = 5)
