import json
import math
from collections import Counter
from pathlib import Path

FILE_DATA = Path(__file__).parent / "data_siswa.json"

DATA_AWAL = [
    (45, 50, 40, 42, "perlu bimbingan"),
    (55, 58, 52, 50, "perlu bimbingan"),
    (60, 55, 48, 55, "perlu bimbingan"),
    (50, 62, 55, 58, "perlu bimbingan"),
    (62, 60, 58, 52, "perlu bimbingan"),
    (70, 68, 65, 68, "berkembang"),
    (75, 72, 70, 66, "berkembang"),
    (72, 75, 68, 72, "berkembang"),
    (78, 70, 74, 70, "berkembang"),
    (68, 74, 72, 75, "berkembang"),
    (80, 72, 76, 74, "berkembang"),
    (88, 85, 86, 88, "unggul"),
    (92, 90, 88, 91, "unggul"),
    (85, 88, 90, 85, "unggul"),
    (95, 92, 94, 90, "unggul"),
    (90, 86, 84, 89, "unggul"),
]

SEGMENT = ["perlu bimbingan", "berkembang", "unggul"]

REKOMENDASI = {
    "perlu bimbingan": "Jadwalkan konseling, kirim materi remedial, dan pantau kehadiran.",
    "berkembang": "Berikan latihan tambahan dan tantangan bertahap.",
    "unggul": "Tawarkan materi pengayaan atau proyek lanjutan.",
}


def muat_data():
    if FILE_DATA.exists():
        with open(FILE_DATA, encoding="utf-8") as f:
            return [tuple(baris) for baris in json.load(f)]
    return list(DATA_AWAL)


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def jarak_euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def prediksi_segmen(data_latih, fitur, k=3):
    jarak = sorted(
        (jarak_euclidean(baris[:4], fitur), baris[4]) for baris in data_latih
    )
    tetangga = jarak[:k]
    suara = Counter(label for _, label in tetangga)
    segmen = suara.most_common(1)[0][0]
    return segmen, suara


def input_nilai(prompt, batas_bawah=0, batas_atas=100):
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("  Masukkan angka.")
            continue
        if batas_bawah <= nilai <= batas_atas:
            return nilai
        print(f"  Nilai harus antara {batas_bawah} dan {batas_atas}.")


def input_fitur_siswa():
    print("Masukkan data siswa:")
    kehadiran = input_nilai("  Kehadiran (0-100%): ")
    tugas = input_nilai("  Rata-rata tugas (0-100): ")
    uts = input_nilai("  Nilai UTS (0-100): ")
    uas = input_nilai("  Nilai UAS (0-100): ")
    return (kehadiran, tugas, uts, uas)


def menu_prediksi(data_latih):
    fitur = input_fitur_siswa()
    segmen, suara = prediksi_segmen(data_latih, fitur)
    print(f"\nHasil voting tetangga terdekat: {dict(suara)}")
    print(f"Segmen siswa: {segmen.upper()}")
    print(f"Rekomendasi tindakan: {REKOMENDASI[segmen]}")


def menu_tambah_data(data_latih):
    fitur = input_fitur_siswa()
    print("Segmen sebenarnya:")
    for i, seg in enumerate(SEGMENT, 1):
        print(f"  {i}. {seg}")
    while True:
        pilihan = input("Pilih (1-3): ").strip()
        if pilihan in ("1", "2", "3"):
            segmen = SEGMENT[int(pilihan) - 1]
            break
        print("  Pilih 1, 2, atau 3.")
    data_latih.append((*fitur, segmen))
    simpan_data(data_latih)
    print(f"Data tersimpan. Total data latih sekarang: {len(data_latih)}")


def menu_statistik(data_latih):
    jumlah = Counter(baris[4] for baris in data_latih)
    print(f"Total data latih: {len(data_latih)}")
    for seg in SEGMENT:
        print(f"  {seg:16s}: {jumlah.get(seg, 0)} siswa")


def main():
    data_latih = muat_data()
    print("=== Segmentasi Siswa LMS (k-NN, materi BAB I) ===")
    print("Fitur: kehadiran, rata-rata tugas, UTS, UAS")

    while True:
        print("\nMenu:")
        print("  1. Prediksi segmen siswa")
        print("  2. Tambah data latih (model belajar)")
        print("  3. Statistik data latih")
        print("  4. Keluar")
        pilihan = input("Pilih (1-4): ").strip()

        if pilihan == "1":
            menu_prediksi(data_latih)
        elif pilihan == "2":
            menu_tambah_data(data_latih)
        elif pilihan == "3":
            menu_statistik(data_latih)
        elif pilihan == "4":
            print("Selesai.")
            break
        else:
            print("Pilihan tidak dikenal.")


if __name__ == "__main__":
    main()
