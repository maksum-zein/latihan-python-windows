#15. Semua Digabung

berat_list = []
i = 0
while i < 3:
    berat = float(input(f"Masukkan berat sampah ke-{i+1} (kg): "))
    berat_list.append(berat)
    i = i + 1
total = 0
for berat in berat_list:
    total = total + berat
    if total > 10:
        print(f"Maksum daur ulang {total} kg!\nCukup ", "bareng ECC Teams!", sep="=>", end="")
        print(" yuk!")
    else:
        print(f"Maksum daur ulang {total} kg!\nTambah ", "bareng ECC Team!", sep="=>", end="")
        print("yuk!")
