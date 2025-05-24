#If-Els dengan Input dan Modulus

donasi = int(input("Masukkan total donasi (Rp.) : "))
penerima = int(input("Masukkan jumlah penerima: "))
sisa = donasi % penerima
if sisa == 0:
    print(f"Maksum bagi donasi merata!")
else:
    print(f"Maksum punya sisa donasi Rp. {sisa}")
