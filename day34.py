#program membuat function menggunakan return

def fungsi_tanpa_parameter():
    print("Contoh penggunaan fungsi tanpa parameter")
    a = 0
    for i in range(1,6):
        a += i
    return a

def fungsi_berparameter(nilai):
    print("Contoh penggunaan fungsi berparameter")
    b = 0
    for j in range(1,nilai):
        b += j
    return b
print(fungsi_tanpa_parameter())
print(fungsi_tanpa_parameter())

print(fungsi_berparameter(16))
print(fungsi_berparameter(25))