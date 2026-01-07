# =========================
#        CLASS PARENT
# =========================

class Mhs_Alumni:
    def __init__(self):
        self.lulus = 2024

    def info_alumni(self):
        print(f"Saya lulusan tahun {self.lulus}")


class Mhs_Aktif:
    def __init__(self):
        self.masuk = 2024

    def info_aktif(self):
        print(f"Saya masuk kuliah tahun {self.masuk}")


# =========================
#   MULTIPLE INHERITANCE
# =========================

class Mahasiswa(Mhs_Alumni, Mhs_Aktif):
    def __init__(self):
        Mhs_Alumni.__init__(self)
        Mhs_Aktif.__init__(self)
        self.ktm = "Aktif"
        self.ijazah = "Ada"
        self.beasiswa = "tidak ada"

    def info_mhs(self):
        print("Status KTM :", self.ktm)
        print("Ijazah     :", self.ijazah)
        print("Beasiswa   :", self.beasiswa)


# =========================
#     MULTILEVEL INHERITANCE
# =========================

class Mahasiswa_Utama(Mahasiswa):
    def __init__(self):
        super().__init__()
        self.prodi = "Informatika"

    def info_lengkap(self):
        print("=== DATA MAHASISWA ===")
        self.info_alumni()
        self.info_aktif()
        self.info_mhs()
        print("Prodi :", self.prodi)


# =========================
#     PEMANGGILAN OBJECT
# =========================

mhs = Mahasiswa_Utama()
