import os
import time

class AgenDasar:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = list(posisi)
        self.riwayat = []

    def persepsi(self, lingkungan):
        self.riwayat.append(lingkungan)
        return lingkungan

    def aksi(self, kondisi):
        raise NotImplementedError

class AgenVakum(AgenDasar):
    def aksi(self, kondisi):
        arah = {"utara": (-1, 0), "selatan": (1, 0), "timur": (0, 1), "barat": (0, -1)}
        if kondisi in arah:
            dx, dy = arah[kondisi]
            self.posisi[0] = max(0, min(4, self.posisi[0] + dx))
            self.posisi[1] = max(0, min(4, self.posisi[1] + dy))
            return f"Geser {kondisi} ke {self.posisi}"
        elif kondisi == "kotor":
            return "Membersihkan lantai 🧹"
        return "Standby ⏸"

class AgenKeamanan(AgenDasar):
    def __init__(self, nama, posisi, zona_aman):
        super().__init__(nama, posisi)
        self.zona_aman = zona_aman

    def aksi(self, kondisi):
        arah = {"utara": (-1, 0), "selatan": (1, 0), "timur": (0, 1), "barat": (0, -1)}
        if kondisi in arah:
            dx, dy = arah[kondisi]
            self.posisi[0] = max(0, min(4, self.posisi[0] + dx))
            self.posisi[1] = max(0, min(4, self.posisi[1] + dy))
            return f"Patroli {kondisi} ke {self.posisi}"
        elif kondisi not in self.zona_aman:
            return f"🚨 ALERT! '{kondisi}' tidak aman!"
        return f"✅ '{kondisi}' aman."

class AgenNavigasi(AgenDasar):
    def aksi(self, kondisi):
        arah = {"utara": (-1, 0), "selatan": (1, 0), "timur": (0, 1), "barat": (0, -1)}
        if kondisi in arah:
            dx, dy = arah[kondisi]
            self.posisi[0] = max(0, min(4, self.posisi[0] + dx))
            self.posisi[1] = max(0, min(4, self.posisi[1] + dy))
            return f"Navigasi ke koordinat {self.posisi}"
        return "🛑 Diam di tempat"

# Inisialisasi 3 agen dengan posisi awal berbeda di grid 5x5
vac = AgenVakum("VacBot", [0, 0])
guard = AgenKeamanan("GuardBot", [0, 4], ["lobby", "koridor", "A"])
nav = AgenNavigasi("NavBot", [2, 2])

agen_list = [vac, guard, nav]

# Skenario input untuk masing-masing agen di setiap langkah
skenario = [
    ("kotor", "koridor", "selatan"),
    ("timur", "utara", "timur"),
    ("bersih", "bahaya", "utara"),
    ("selatan", "barat", "barat")
]

def cetak_peta(agents):
    grid = [["⬜" for _ in range(5)] for _ in range(5)]
    icons = {"VacBot": "🧹", "GuardBot": "🛡️", "NavBot": "🤖"}
    
    # Tempatkan posisi masing-masing agen di grid
    for agen in agents:
        x, y = agen.posisi
        grid[x][y] = icons.get(agen.nama, "📍")
        
    print("\n" + "="*20 + " PETA MULTI-AGEN " + "="*20)
    for baris in grid:
        print("   " + " ".join(baris))
    print("="*55)
    print("Keterangan: 🧹 VacBot | 🛡️ GuardBot | 🤖 NavBot")

# Jalankan simulasi beranimasi
for step, inputs_langkah in enumerate(skenario, 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"=== LANGKAH SIMULASI KE-{step} ===\n")
    
    for agen, inp in zip(agen_list, inputs_langkah):
        agen.persepsi(inp)
        hasil = agen.aksi(inp)
        print(f"[{agen.nama}] Input: '{inp}' -> Aksi: {hasil}")
        
    cetak_peta(agen_list)
    time.sleep(1.5)