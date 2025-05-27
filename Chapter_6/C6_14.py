# 14. While Loop dengan Input, If-Else, dan Chapter 1

target  = int(input("Masukkan target donasi (Rp): "))
donasi = 0
while donasi < target:
    donasi = donasi + 50000
    if donasi >= target:
        print(f"Maksum donasi Rp. {donasi}!\nTarget tercapai!")
    else:
        print(f"Maksum donasi Rp. {donasi}!\nMasih kurang!")
