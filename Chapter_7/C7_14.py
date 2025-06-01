#14. List dengan For Loop, If-Else, dan Chapter 1

donasi_list = [100000, 200000, 50000]
for donasi in donasi_list:
    if donasi > 150000:
        print(f"Maksum donasi Rp {donasi}!\nBanyak ", "buat UMKM!", sep="=>", end="")
        print(" yuk!")
    else:
        print(f"Maksum donasi Rp {donasi}!\nTambah ", "buat UMKM!", sep="=>", end="")
        print(" yuk!")