print(16*"=","belajar perulangan while, else, break",16*"=")

def garis():
    print(25*"-")
    
angka = 1

while angka < 11:
    print("nilai angka adalah", angka)
    angka += 1
    if angka == 5:
        print("nilai angka terbatas di", angka)
        break
else:
    print("nilai angka diluar while adalah", angka)

print("di luar while")

garis()

