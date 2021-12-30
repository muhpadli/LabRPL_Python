print(21*"=","Belajar Kalkulator Sederhana",21*"=")


nilai_1 = float(input("masukkan nilai pertama :"))
operator = input("masukkan operator (+,-,*,/) :")
nilai_2 = float(input("masukkan nilai kedua :"))

if(operator == "+"):
    hasil = nilai_1 + nilai_2
elif(operator == "-"):
    hasil = nilai_1 - nilai_2
elif(operator == "*"):
    hasil = nilai_1 * nilai_2
elif(operator == "/"):
    hasil = nilai_1 / nilai_2

print("Hasil dari operator aritmatikanya adalah :", hasil)
