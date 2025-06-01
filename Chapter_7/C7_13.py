#13. List dengan While Loop, Input, dan Operasi

lampu_list = []
i = 0
while i < 3:
    lampu = int(input(f"Masukkan jumlah lampu ke-{i+1}: "))
    lampu_list.append(lampu)
    i = i + 1
total = 0
for lampu in lampu_list:
    total = total + lampu
print(f"Maksum hemat {total} lampu!")
