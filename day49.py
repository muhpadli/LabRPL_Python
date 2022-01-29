
def centimeter(n):
    centimeter = n * 100
    return centimeter

def kilometer(x):
    kilometer = x / 1000
    return kilometer

print("PROGRAM MENGUBAH METER KE CENTIMETER DAN KILOMETER")
JAWAB = "y"
while JAWAB == "y" :
    print("\nPilih menu dibawah ini :")
    menu = ["1. Meter ke centimeter", "2. Meter ke kilometer"]
    for i in menu:
        print(i)   
    pilihan = int(input("Masukkan pilhan menu (1/2) : "))          
    if(pilihan == 1):
        bilangan = int(input("Masukkan bilangan (m) :"))
        hasil = centimeter(bilangan)
        print(f"hasilnya adalah {hasil} cm")
    elif(pilihan == 2):
        bilangan = int(input("Masukkan bilangan (m) :"))
        hasil = kilometer(bilangan)
        print(f"hasilnya adalah {hasil} km")
    else:
        print("Mohon maaf menu yang anda pilih tidak tersedia")

    JAWAB = input("Mau lanjut atau tidak? (y/n" ).lower()
    if (JAWAB == "n"):
        break
