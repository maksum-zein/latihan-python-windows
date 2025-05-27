# 15. Semua Digabung

jumlah = int(input("Masukkan jumlah pohon: "))
total = 0
for i in range(jumlah):
    total = total + 1
    if total > 2:
        print(f"Maksum tanam pohon ke-{total}!\nCukup!","bareng ECC Team!", sep="=>", end="")
    else:
        print(f"Maksum tanam pohon ke-{total}!\nAyo tambah ", "bareng ECC Team!", sep="=>", end="")
        print("yuk!")
              
