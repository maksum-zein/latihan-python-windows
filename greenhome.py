# Meminta input nama pelanggan
print('Selamat datang di "GreenHome Solutions"!')
print("Kami akan membantu Anda menemukan solusi energi ramah lingkungan.")
Nama = input("Silahkan masukkan nama anda terlebih dahulu : ")
print('Selamat datang ', Nama, '!')

# Meminta input dari pelanggan
jumlah_perangkat = int(input("Masukkan jumlah perangkat listrik di rumah Anda: "))
print("Jumlah perangkat listrik Anda: ", jumlah_perangkat)

# Menghitung kebutuhan energi
energi_per_perangkat = 0.3  # kWh per hari
total_energi = jumlah_perangkat * energi_per_perangkat
print("Kebutuhan energi harian Anda:", total_energi, "kWh")

# Memberikan saran
print("Saran: Gunakan panel surya untuk memenuhi kebutuhan energi Anda dan hemat biaya, \n       Serta jangan lupa untuk mematikan perangkat saat tidak digunakan untuk hemat energi!")
print("Semoga Bumi kita menjadi tetap lestari dan lebih nyaman dihuni")
print("Terima kasih telah memilih solusi ramah lingkungan bersama GreenHome Solutions!")
