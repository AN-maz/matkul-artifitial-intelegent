class Lingkungan:
    def __init__(self, kotoran, posisi_awal=0):
        self.kotoran = list(kotoran)
        self.posisi = posisi_awal

    @property
    def jumlah_ruangan(self):
        return len(self.kotoran)

    def persepsi(self):
        return self.posisi, self.kotoran[self.posisi]

    def lakukan(self, aksi):
        dibersihkan = 0
        if aksi == "HISAP":
            dibersihkan = self.kotoran[self.posisi]
            self.kotoran[self.posisi] = 0
        elif aksi == "KANAN":
            self.posisi = min(self.posisi + 1, self.jumlah_ruangan - 1)
        elif aksi == "KIRI":
            self.posisi = max(self.posisi - 1, 0)
        return dibersihkan

    def semua_bersih(self):
        return all(k == 0 for k in self.kotoran)

    def gambar(self):
        sel = []
        for i, k in enumerate(self.kotoran):
            penanda = "A" if i == self.posisi else " "
            sel.append(f"[{penanda}{k}]")
        return " ".join(sel)


def cetak_header(jenis, karakteristik):
    print(f"=== {jenis} ===")
    print(f"Karakteristik (materi 1.4.4): {karakteristik}\n")


def cetak_langkah(langkah, env, aksi, info=""):
    print(f"  {langkah:>2} | {env.gambar()} | -> {aksi:5s} {info}")
