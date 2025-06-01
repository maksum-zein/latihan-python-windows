# List dengan Input dan For Loop

pohon_list = []
for i in range(3):
    pohon = input(f"Masukkan pohon ke-{i+1}:")
    pohon_list.append(pohon)
for pohon in pohon_list:
    print(f"Maksum tanam {pohon}!")
    