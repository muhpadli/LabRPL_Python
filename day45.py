#program function menampilkan bilangan prima

def bilprima(n):
    if(n == 2 or n ==3): 
        return f"{n} adalah bilangan Prima"
    elif(n % 2 ==0 or n <2 ):
        return f"{n} adalah bukan bilangan Prima"
    for i in range (3, int(n ** 1/2)+1,2):
        if(n % 2 == 0):
            return f"{n} adalah  bukan bilangan Prima"
        return f"{n} adalah bilangan Prima"

print(bilprima(32))

#program mencari rata-rata
def cari_ratarata(list_nilai):
    rata_rata = sum(list_nilai)/len(list_nilai)
    return rata_rata

nilai_uas = [98,89,85,95,67,98]
rata2_uas = round(cari_ratarata(nilai_uas),2)
print(f"Nilai rata-rata UAS adalah {rata2_uas}")
    


