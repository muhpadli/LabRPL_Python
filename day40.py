#program looping pada dictionary

Identitas = {
             "Negara" : "Indonesia",
             "Dasar Negara" : "Pancasila",
             "Bahasa" : "Indonesia",
             "Mata Uang" : "Rupiah",
             "Semboyan" : "Bhinneka Tunggal Ika"
}

for i in Identitas:
    print(i,(13-len(i))*" ", "=>", Identitas[i])