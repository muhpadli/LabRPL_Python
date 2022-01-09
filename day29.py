#program menentukan sisa hidup dengan usia normal 90 tahun

usia_sekarang = int(input("Masukkan usia anda sekarang :"))

sisa_usia_dalam_tahun = 90 - usia_sekarang
sisa_usia_dalam_bulan = sisa_usia_dalam_tahun * 12
sisa_usia_dalam_minggu = sisa_usia_dalam_tahun * 52
sisa_usia_dalam_hari = sisa_usia_dalam_tahun * 365

print(f"sisa hidup anda adalah {sisa_usia_dalam_tahun}tahun, {sisa_usia_dalam_bulan} bulan, {sisa_usia_dalam_minggu} minggu,{sisa_usia_dalam_hari} hari")
