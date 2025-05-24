print('Selamat datang di "GreenHome Solutions"!')
print("Kami akan membantu Anda menemukan solusi energi ramah lingkungan.")

# Validasi input nama
while True:
    nama = input("Silahkan masukkan nama anda terlebih dahulu: ").strip()
    if nama:
        break
    print("Nama tidak boleh kosong. Silakan coba lagi.")

print('Selamat datang', nama, '!')

# Validasi input jumlah perangkat
while True:
    try:
        jumlah_perangkat = int(input("Masukkan jumlah perangkat listrik di rumah Anda: "))
        if jumlah_perangkat < 0:
            print("Jumlah perangkat tidak boleh negatif.")
            continue
        break
    except ValueError:
        print("Masukkan angka yang valid!")

print("Jumlah perangkat listrik Anda:", jumlah_perangkat)

# Menghitung kebutuhan energi
energi_per_perangkat = 0.3  # kWh per hari
total_energi = jumlah_perangkat * energi_per_perangkat
print("Kebutuhan energi harian Anda:", total_energi, "kWh")

# Memberikan saran
if total_energi > 10:
    print("Saran: Kebutuhan energi Anda cukup besar, pertimbangkan untuk menggunakan panel surya berkapasitas tinggi.")
elif total_energi > 0:
    print("Saran: Gunakan panel surya untuk memenuhi kebutuhan energi Anda dan hemat biaya.")
else:
    print("Anda belum memasukkan perangkat apa pun.")

print("Jangan lupa untuk mematikan perangkat saat tidak digunakan untuk hemat energi!")
print("Semoga Bumi kita tetap lestari dan lebih nyaman dihuni.")
print("Terima kasih telah memilih solusi ramah lingkungan bersama GreenHome Solutions!")
