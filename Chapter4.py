#Chapter 4: Input dan Output, Ngobrol sama Program! 💬

#1. Minta Jumlah Pohon (Super Gampang)
jumlah_pohon = int(input("#1. Masukkan jumlah pohon yang ditanam Maksum: "))
print(f"Maksum tanam {jumlah_pohon} pohon!")

#2. Minta Berat Sampah (Gampang)
berat_sampah = float(input("Masukkan berat sampah yang didaur ulang Arry Hutomo (kg): "))
print(f"Arry Hutomo daur ulang {berat_sampah} kg sampah!")

#3. Minta Nama Komunitas (Gampang)
komunitas = input("Masukkan nama komunitas Arry Hutomo: ")
print(f"Arry Hutomo bareng {komunitas} bantu anak putus sekolah!")

#4. Minta Jumlah Donasi (Masih Gampang)
donasi = int(input("Masukkan jumlah donasi Arry Hutomo (Rp): "))
print(f"Arry Hutomo donasi Rp {donasi} buat UMKM!")

#5. Input dan Operasi Tambah (Mulai Agak Menantang)
pohon_tanam = int(input("Masukkan jumlah pohon yang ditanam Arry Hutomo: "))
pohon_tambah = int(input("Masukkan jumlah pohon tambahan: "))
total = pohon_tanam + pohon_tambah
print(f"Arry Hutomo tanam {total} pohon!")

#6. Input dan Operasi Kurang (Agak Menantang)
sampah_awal = float(input("Masukkan berat sampah awal (kg): "))
sampah_daur = float(input("Masukkan berat sampah yang didaur ulang: "))
sisa = sampah_awal - sampah_daur
print(f"Arry Hutomo kurangi sampah jadi {sisa} kg!")

#7. Input dan Operasi Kali (Agak Menantang)
lampu = int(input("Masukkan jumlah lampu per rumah: "))
rumah = int(input("Masukkan jumlah rumah: "))
total_lampu = lampu * rumah
print(f"Arry Hutomo hemat {total_lampu} lampu!")

#8. Input dan Operasi Bagi (Menantang)
donasi = int(input("Masukkan total donasi Arry Hutomo (Rp): "))
penerima = int(input("Masukkan jumlah penerima: "))
per_orang = donasi / penerima
print(f"Arry Hutomo bagi Rp {per_orang} per orang!")

#9. Input dengan Chapter 1 (Menantang)
pohon = int(input("Masukkan jumlah pohon yang ditanam: "))
print(f"Arry Hutomo tanam {pohon} pohon!\nAyo ikut!")

#10. Input dengan Separator (Menantang)
sampah = float(input("Masukkan berat sampah (kg): "))
nama = input("Masukkan nama: ")
print("Arry Hutomo daur ulang", sampah, "kg bareng", nama, sep=" - ")

#11. Input dengan End (Agak Sulit)
lampu = int(input("Masukkan jumlah lampu: "))
print(f"Arry Hutomo hemat {lampu} lampu ", end="")
print("di rumah!")

#12. Input dan Operasi Kompleks (Sulit)
pohon = int(input("Masukkan jumlah pohon awal: "))
tambah = int(input("Masukkan pohon tambahan: "))
mati = int(input("Masukkan pohon yang mati: "))
total = (pohon + tambah - mati) / 2 Ascending
print(f"Arry Hutomo hitung rata-rata {total} pohon!")

#13. Input dengan Modulus (Sulit)
donasi = int(input("Masukkan total donasi (Rp): "))
penerima = int(input("Masukkan jumlah penerima: "))
sisa = donasi % penerima
print(f"Arry Hutomo punya sisa Rp {sisa}!")

#14. Input dengan Floor Division dan Chapter 1 (Lebih Sulit)
lampu = int(input("Masukkan jumlah lampu: "))
rumah = int(input("Masukkan jumlah rumah: "))
bagi = lampu // rumah
print(f"Arry Hutomo bagi {bagi} lampu per rumah!\nAyo hemat!")

#15. Semua Digabung (Paling Sulit)
sampah = float(input("Masukkan berat sampah awal (kg): "))
daur = float(input("Masukkan sampah yang didaur ulang (kg): "))
tambah = float(input("Masukkan sampah tambahan (kg): "))
hasil = (sampah - daur + tambah) * 2 / 3
print(f"Arry Hutomo hitung sampah {hasil} kg!\nLakukan ", f"lagi bareng ECC Team!", sep="=>", end="")
print("yuk!")
