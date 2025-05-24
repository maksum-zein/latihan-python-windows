#If-else dengan Floor Division dan Chapter 1
lampu = int(input("Masukkan jumlah lampu: "))
rumah = int(input("Masukkan jumlah rumah: "))
bagi = lampu // rumah
if bagi > 5:
    print(f"Maksum bagi {bagi} lampur per rumah!\nLuar biasa!")
else:
    print(f"Maksum bagi {bagi} lampu per rumah!\nAyo tambah lagi!")
