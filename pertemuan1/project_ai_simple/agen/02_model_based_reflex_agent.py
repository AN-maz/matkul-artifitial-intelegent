from lingkungan import Lingkungan, cetak_header, cetak_langkah


def agen(model, posisi, kotor_di_sini, jumlah_ruangan):
    model[posisi] = kotor_di_sini

    if kotor_di_sini > 0:
        return "HISAP", "ruangan ini kotor"

    if all(model.get(i) == 0 for i in range(jumlah_ruangan)):
        return "DIAM", "model: semua ruangan sudah bersih"

    belum_diketahui = [i for i in range(jumlah_ruangan) if i not in model]
    target = min(belum_diketahui, key=lambda i: abs(i - posisi))
    arah = "KANAN" if target > posisi else "KIRI"
    return arah, f"model: ruangan {target} belum diketahui, menuju ke sana"


def main():
    cetak_header(
        "2. Model-Based Reflex Agent",
        "menyimpan model internal untuk melacak bagian dunia yang tak teramati",
    )

    env = Lingkungan([0, 2, 0, 3, 1], posisi_awal=0)
    model = {}
    print("Kondisi awal:")
    print(f"      {env.gambar()}\n")

    langkah = 0
    while True:
        langkah += 1
        posisi, kotor = env.persepsi()
        aksi, alasan = agen(model, posisi, kotor, env.jumlah_ruangan)
        env.lakukan(aksi)
        cetak_langkah(langkah, env, aksi, f"({alasan})")
        if aksi == "DIAM":
            break

    print("\nPerbedaan dengan simple reflex: model internal membuat agen tahu")
    print("keadaan ruangan lain, sehingga bisa berhenti (DIAM) saat semua bersih.")


if __name__ == "__main__":
    main()
