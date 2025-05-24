#Semua digabung
sampah = float(input("Masukkan berat sampah awal (kg) : "))
daur = float(input("Masukkan sampah yang didaur ulang (kg) : "))
tambah = float(input("Masukkan sampah tambahan (kg) : "))
total = (sampah-daur+tambah) *2 / 3
if total > 50:
    print(f"Maksum hitung sampah {total} kg!\nLuar biasa ", "bareng ECC Teams!", sep="=>", end="")
    print("Yuk!")
else:
    print(f"Maksum hitung sampah {total} kg!\nAyo tambah lagi ","bareng ECC Team!", sep="=>", end="")
    print("yuk!")
    