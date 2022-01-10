#program mengonversi suhu celcius ke satuan suhu yang lainnya

celcius = float(input("Masukkan suhu dalam celcius :"))

#celcius
print(f"suhunya adalah {celcius} celcius")

#reamur 
reamur = round((4/5)*celcius,1)
print(f"suhu dalam reamur adalah {reamur} reamur")

#fahrenheit
fahrenheit = round((9/5)*celcius,1)
print(f"suhu dalam fahrenheit adalah {fahrenheit} fahrenheit ")

#kelvin
kelvin = round((celcius + 273),1)
print(f"suhu dalam kelvin adalah {kelvin} kelvin ")