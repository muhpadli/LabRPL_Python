#program pemberian komisi kepada sales oleh perusahaan dengan beberapa ketentuan

pendapatan = int(input("masukkan pendapatan sales : Rp."))

if(pendapatan >= 0 and pendapatan <= 200):
    uang_jasa = 10000
    komisi = (10/100)*pendapatan
elif(pendapatan <= 500):
    uang_jasa = 20000
    komisi = (15/100)*pendapatan
elif(pendapatan >= 500):
    uang_jasa = 30000
    komisi = (20/100)*pendapatan

total_komisi = uang_jasa + komisi
print("komisi total dari sales adalah Rp. ",total_komisi)
      
