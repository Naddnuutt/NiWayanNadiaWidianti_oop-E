class Kendaraan:
    def __init__(self, nama, jenis, warna, kecepatan):
        # Instance variable
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
        self.kecepatan = kecepatan

    def tampilkan_info(self):
        print(f"Nama Kendaraan : {self.nama}")
        print(f"Jenis Kendaraan: {self.jenis}")
        print(f"Warna Kendaraan: {self.warna}")
        print(f"Kecepatan Maks : {self.kecepatan} km/jam")

    def ubah_warna(self, warna_baru):
        self.warna = warna_baru
        print(f"Warna {self.nama} diubah menjadi {self.warna}")

# Membuat objek dari class Kendaraan (versi lama diganti)
motor = Kendaraan("NMAX", "Motor", "Hitam", 110)
mobil = Kendaraan("Civic", "Mobil", "Pink", 130)

# Menampilkan informasi
motor.tampilkan_info()
print()  # spasi
mobil.tampilkan_info()

print("\nSetelah ubah warna motor:")
motor.ubah_warna("Merah")
