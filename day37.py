#program kasir

pilihan = "y"

while pilihan == "y":
    print("""
    **********************************************
            N U R L I N D A    C O F F E
     L I S T   M E N U   M I N U M A N    K O P I
    **********************************************

    A. ES Kopi Susu  : Rp. 10.000
    B. ES Kopi Coklat  : Rp. 12.000
    C. ES Kopi Hitam  : Rp. 10.000
    D. Ice Americano  : Rp. 14.000
    """) 

    pesanan = input("Masukkan kode list abjad menu kopi (A/B/C/D) :").lower()
    jml_pesanan = int(input("jumlah pesanan :"))

    if(pesanan == "a"):
        menu_pesanan = "Es Kopi Susu"
        harga = 10_000 * jml_pesanan
        ppn = harga * 0.1

        if(jml_pesanan >= 5):
            diskon = harga * 0.2
            total_harga = harga - diskon + ppn
        else:
            diskon = 0
            total_harga = harga - diskon + ppn
    elif(pesanan == "b"):
        menu_pesanan = "ES Kopi Coklat"
        harga = 12_000 * jml_pesanan
        ppn = harga * 0.1

        if(jml_pesanan >= 5):
            diskon = harga * 0.2
            total_harga = harga - diskon + ppn
        else:
            diskon = 0
            total_harga = harga - diskon + ppn
    elif(pesanan == "c"):
        menu_pesanan = "ES Kopi Hitam "
        harga = 10_000 * jml_pesanan
        ppn = harga * 0.1
        diskon = 0
        total_harga = harga - diskon + ppn
    elif(pesanan == "d"):
        menu_pesanan = "Ice American"
        harga = 14_000 * jml_pesanan
        ppn = harga * 0.1
        diskon = 0
        total_harga = harga - diskon + ppn
    else:
        menu_pesanan = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        total_harga = "-"
        print("mohon maaf, menu ini tidak tersedia")
        pilihan = input("apakah anda ingin pesan kembali (y/n) :")
        if(pilihan != "y"):
            break
        
    
    print(f"""\n
    ***************************************************
              N U R L I N D A   C O F F E 
    ***************************************************
    Menu           : {menu_pesanan}
    Jumlah Pesanan : {jml_pesanan}
    Harga          : {harga}
    Diskon         : {diskon}
    PPN            : {ppn}
    ***************************************************
    Jumlah Bayar   : {total_harga}
    ***************************************************
    """)

    pilihan = input("apakah anda ingin pesan kembali (y/n) :")



    
    
    







