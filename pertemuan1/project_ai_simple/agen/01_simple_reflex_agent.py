from lingkungan import Lingkungan, cetak_header, cetak_langkah


def agen(posisi, kotor_di_sini, jumlah_ruangan):
    if kotor_di_sini > 0:
        return "HISAP"
    if posisi < jumlah_ruangan - 1:
        return "KANAN"
    return "KIRI"


def main():
    cetak_header(
        "1. Simple Reflex Agent",
        "aturan kondisi-aksi (if-then) dari persepsi saat ini, tanpa riwayat",
    )
    print("Aturan agen:")
    print("  jika ruangan kotor  -> HISAP")
    print("  jika belum di ujung -> KANAN")
    print("  jika di ujung kanan -> KIRI\n")

    env = Lingkungan([0, 2, 0, 3, 1], posisi_awal=0)
    print("Kondisi awal (angka = tingkat kotoran, A = posisi agen):")
    print(f"      {env.gambar()}\n")

    for langkah in range(1, 13):
        posisi, kotor = env.persepsi()
        aksi = agen(posisi, kotor, env.jumlah_ruangan)
        env.lakukan(aksi)
        info = "(semua sudah bersih, tapi agen tetap jalan!)" if env.semua_bersih() else ""
        cetak_langkah(langkah, env, aksi, info)

    print("\nKeterbatasan: agen tidak punya memori, jadi tidak tahu semua ruangan")
    print("sudah bersih. Ia memantul di dua ruangan ujung selamanya.")


if __name__ == "__main__":
    main()
