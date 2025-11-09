Ni Wayan Nadia Widianti: # Kelas Dasar (Superclass) - Mewakili Orang secara umum
class Orang:
    def _init_(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def sapa(self):
        """Metode sapa umum untuk setiap orang."""
        return f"Halo, nama saya {self.nama}."

# Kelas Turunan (Subclass) - Dosen mewarisi dari Orang
class Dosen(Orang):
    def _init_(self, nama, usia, nidn, mata_kuliah):
        # Memanggil konstruktor dari kelas dasar (Orang)
        super()._init_(nama, usia)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        """Metode khusus untuk Dosen."""
        return f"{self.nama} sedang mengajar {self.mata_kuliah}."

# Kelas Turunan (Subclass) - Mahasiswa mewarisi dari Orang
class Mahasiswa(Orang):
    def _init_(self, nama, usia, nim, jurusan):
        # Memanggil konstruktor dari kelas dasar (Orang)
        super()._init_(nama, usia)
        self.nim = nim
        self.jurusan = jurusan

    def belajar(self):
        """Metode khusus untuk Mahasiswa."""
        return f"{self.nama} sedang belajar di jurusan {self.jurusan}."

# --- Implementasi Data dari Proyeksi ---

# 1. Data Dosen
dosen_edy = Dosen(
    nama="EDY",
    usia=35,
    nidn="678910",
    mata_kuliah="Pemrograman Berorientasi Objek"
)

# 2. Data Mahasiswa
mahasiswanadia = Mahasiswa(
    nama="nadia widianti",
    usia=20,
    nim="200620",
    jurusan="Informatika"
)

# --- Menampilkan Output ---

print("=== Data Dosen ===")
print(f"Nama: {dosen_edy.nama}")
print(f"Usia: {dosen_edy.usia}")
# NIDN tidak ditampilkan di proyeksi, tapi ada di objek
# print(f"NIDN: {dosen_edy.nidn}")
print(f"Mata Kuliah: {dosen_edy.mata_kuliah}")
print(dosen_edy.mengajar())
print(dosen_edy.sapa()) # Menggunakan metode yang diwarisi dari kelas Orang

print("\n=== Data Mahasiswa ===")
print(f"Nama: {mahasiswa_nadia.nama}")
print(f"Usia: {mahasiswa_nadia.usia}")
print(f"NIM: {mahasiswa_nadia.nim}")
print(f"Jurusan: {mahasiswa_nadia.jurusan}")
print(mahasiswa_nadia.belajar())
print(mahasiswa_nadia.sapa()) # Menggunakan metode yang diwarisi dari kelas Orang
# === Pewarisan Kelas (Inheritance) ===
class Binatang:


    def _init_(self, nama):
        self.nama = nama
        self.hidup = True

    def makan(self):
        print(f"{self.nama} sedang makan")

    def tidur(self):
        print(f"{self.nama} sedang tidur")


class Kambing(Binatang):
    def suara(self):
        print("mbeeek")


class Babi(Binatang):
    def suara(self):
        print("nggook")


class Ular(Binatang):
    def suara(self):
        print("sssstttt")


# Membuat objek dari tiap kelas turunan
kambing = Kambing("Rizky")
babi = Babi("Koruptor")
ular = Ular("Fariz")

print("\n=== Aktivitas Binatang ===")
print(ular.nama)
print(ular.hidup)
ular.makan()
ular.tidur()

        


       


