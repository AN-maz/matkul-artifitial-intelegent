class Agen:
    """Agen Simple Reflex dengan aturan if-then"""

    def __init__(self, nama):
        self.nama = nama
        self.riwayat = []        # memori agen

    def persepsi(self, lingkungan):
        self.riwayat.append(lingkungan)
        return lingkungan

    def keputusan(self, kondisi):
        """Simple Reflex: aturan if-then"""
        if kondisi == "kotor":
            return "bersihkan"
        elif kondisi == "bersih":
            return "diam"
        elif kondisi == "gelap":
            return "nyalakan lampu"
        elif kondisi == "hujan":
            return "berteduh"
        elif kondisi == "bahaya":
            return "menghindar"
        elif kondisi == "rusak":
            return "cari bengkel"
        elif kondisi == "panas":
            return "cari tempat teduh"
        else:
            return "eksplorasi"

    def aksi(self, keputusan):
        print(f"[{self.nama}] Aksi: {keputusan.upper()}")

    def jalankan(self, kondisi_list):
        print(f"\n{'='*40}")
        print(f"  Agen '{self.nama}' mulai beroperasi")
        print(f"{'='*40}")
        for kondisi in kondisi_list:
            p = self.persepsi(kondisi)
            k = self.keputusan(p)
            self.aksi(k)
        print(f"\nRiwayat: {self.riwayat}")


# Cara menjalankan yang benar:
agen_purwa = Agen("Andrian")
agen_purwa.jalankan(["kotor", "gelap", "rusak"])

