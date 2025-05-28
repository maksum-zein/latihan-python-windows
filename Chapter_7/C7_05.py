# 5. List dengan Input

pohon_list = []
jumlah = int(input("Masukkan jumlah pohon: "))
for i in range(jumlah):
    pohon = input(f"Masukkan pohon ke-{i+1}: ")
    pohon_list.append(pohon)
    print("Maksum tanam pohon:", pohon_list)
    
