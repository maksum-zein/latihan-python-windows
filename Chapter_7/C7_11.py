# 11. List dengan Input, Operasi dan For Loop

berat_list = []
jumlah = int(input("Masukkan jumlah sampah: "))
for i in range(jumlah):
    berat = float(input(f"Masukkan berat sampah ke-{i+1} (kg): "))
    berat_list.append(berat)
total = 0
for berat in berat_list:
    total = total + berat
print(f"Maksum daur ulang {total} kg!")

