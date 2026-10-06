from lingkungan import Lingkungan, cetak_header, cetak_langkah

NILAI_PER_KOTORAN = 10
BIAYA_LANGKAH = 4


def hitung_utilitas(kotoran, posisi):
    kandidat = []
    for i, k in enumerate(kotoran):
        if k == 0:
            continue
        nilai = k * NILAI_PER_KOTORAN - abs(i - posisi) * BIAYA_LANGKAH
        kandidat.append((i, k, nilai))
    return kandidat


def agen(posisi, kotoran):
    if kotoran[posisi] > 0:
        return "HISAP", "membersihkan ruangan ini"

    kandidat = hitung_utilitas(kotoran, posisi)
    if not kandidat:
        return "DIAM", "tidak ada kotoran tersisa"

    terbaik = max(kandidat, key=lambda c: c[2])
    if terbaik[2] <= 0:
        return "DIAM", f"utilitas terbaik {terbaik[2]} (tidak sebanding energinya)"

    arah = "KANAN" if terbaik[0] > posisi else "KIRI"
    return arah, f"menuju ruangan {terbaik[0]} (utilitas {terbaik[2]})"


def main():
    cetak_header(
        "4. Utility-Based Agent",
        "menimbang SEBERAPA BAIK tiap hasil (utilitas), bukan sekadar capai tujuan",
    )
    print(f"Fungsi utilitas: (tingkat kotoran x {NILAI_PER_KOTORAN}) "
          f"- (jarak x {BIAYA_LANGKAH})\n")

    env = Lingkungan([1, 0, 3, 0, 0, 1], posisi_awal=0)
    print("Kondisi awal:")
    print(f"      {env.gambar()}\n")

    langkah = 0
    while True:
        langkah += 1
        posisi, _ = env.persepsi()
        aksi, alasan = agen(posisi, env.kotoran)
        env.lakukan(aksi)
        cetak_langkah(langkah, env, aksi, f"({alasan})")
        if aksi == "DIAM":
            break

    print("\nPerbedaan dengan goal-based: agen TIDAK mengejar 'semua bersih'")
    print("secara membabi buta. Kotoran kecil di ruangan 5 dibiarkan karena")
    print("energi untuk ke sana lebih mahal daripada nilai membersihkannya.")


if __name__ == "__main__":
    main()
