#menjumlahkan seluruh bilangan genap dari 1-100

jumlah_bilgenap = 0
for bil_genap in range (0,101,2):
    jumlah_bilgenap += bil_genap 
print(f"total bilangan genap dari 1 - 100 adalah {jumlah_bilgenap}")

#program forlooping dalam permainan fizzbuz
for i in range (1,101):
    if(i % 3 == 0 and i % 5 ==0 ):
        i= "fizzbuzz"
    elif (i % 5 == 0 ):
        i = "buzz"
    elif (i % 3 == 0 ):
        i = "fizz"
    print(i)
