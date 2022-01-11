#program menentukan kalkulator cinta 
print(9*" "+"Selamat datang di Kalkulator cinta")
nama_1 = input("Masukkan nama pertama : ").lower()
nama_2 = input("Masukkan nama kedua : ").lower()

gabungan_nama = (nama_1 + nama_2)

t = gabungan_nama.count("t")
r = gabungan_nama.count("r")
u = gabungan_nama.count("u")
e = gabungan_nama.count("e")

true = t + r + u + e

l = gabungan_nama.count("l")
o = gabungan_nama.count("o")
v = gabungan_nama.count("v")
e = gabungan_nama.count("e")

love = l + o + v + e
jumlah_skor = str(true) + str(love)
total_skor = int(jumlah_skor)

if(total_skor < 10 or total_skor > 90):
    print(f"Total skor anda adalah {total_skor}, anda pergi bersama seperti coke dan mentos")
elif(total_skor >= 40 and total_skor <= 50):
    print(f"Total skor anda adalah {total_skor}, anda baik-baik saja bersama")
else:
    print(f"skor anda adalah {total_skor}")
