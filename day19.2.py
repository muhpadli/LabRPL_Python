print(27*"=", "program kondisi di tempat GRAVITY FOTOCOPY", 27*"=")

people = input("apakah pelanggan <y/t> :")
jumlah = int(input("berapa lembar yang ingin di fotocopy :"))
             
if(people == "t"):
    if(jumlah > 200):
        harga = jumlah * 80
    elif(jumlah >= 100 and jumlah <= 200):
        harga = jumlah * 100
    elif(jumlah < 100):
        harga = jumlah * 150
else:
    harga = jumlah * 75
    
print("Jumlah pembayaran adalah Rp. %d-" %harga)
