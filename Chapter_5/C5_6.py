##Input dan Operasi

sampah = float(input("Masukkam berat sampah (kg) : "))
daur = float(input("Masukkan sampah yang didaur ulang (kg) : "))
sisa = sampah - daur
if sisa > 0:
    print(f"Maksum masih punya sisa {sisa} kg sampah")
else:
    print(f"Maksum sudah daur ulang semua sampah")
    