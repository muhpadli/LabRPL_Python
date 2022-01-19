#program for nestedloop

batas = int(input("Masukkan batas data :"))

for i in range (1,batas+1):
    for j in range (i):
        print(i, end=" ")
    print("")

