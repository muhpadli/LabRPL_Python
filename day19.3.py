#program lama bekerja
#jam berupa angka 1 - 12 dan seoranga pekerja kurang dari 12 jam
#start
jam_masuk = int(input("masukkan jam anda masuk bekerja:"))
jam_keluar = int(input("masukkan jam anda keluar bekerja:"))

if(jam_keluar >= jam_masuk):
    lama = jam_keluar - jam_masuk
else:
    lama = (12 - jam_masuk) + jam_keluar

print("lama waktu anda bekerja adalah :", lama)
