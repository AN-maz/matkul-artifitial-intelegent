from collections import deque

from lingkungan import Lingkungan, cetak_header, cetak_langkah


def cari_rencana(posisi_awal, kotoran_awal):
    awal = (posisi_awal, tuple(kotoran_awal))
    antrean = deque([(awal, [])])
    dikunjungi = {awal}

    while antrean:
        (posisi, kotoran), rencana = antrean.popleft()
        if all(k == 0 for k in kotoran):
            return rencana

        for aksi in ("HISAP", "KIRI", "KANAN"):
            posisi_baru, kotoran_baru = posisi, list(kotoran)
            if aksi == "HISAP":
                if kotoran_baru[posisi] == 0:
                    continue
                kotoran_baru[posisi] = 0
            elif aksi == "KIRI":
                if posisi == 0:
                    continue
                posisi_baru = posisi - 1
            else:
                if posisi == len(kotoran) - 1:
                    continue
                posisi_baru = posisi + 1

            keadaan_baru = (posisi_baru, tuple(kotoran_baru))
            if keadaan_baru not in dikunjungi:
                dikunjungi.add(keadaan_baru)
                antrean.append((keadaan_baru, rencana + [aksi]))
    return []


def main():
    cetak_header(
        "3. Goal-Based Agent",
        "memilih aksi yang mendekatkan pada TUJUAN, memakai pencarian & perencanaan",
    )

    env = Lingkungan([0, 2, 0, 3, 1], posisi_awal=0)
    print("Kondisi awal:")
    print(f"      {env.gambar()}\n")

    print("Tujuan agen: semua ruangan bersih.")
    rencana = cari_rencana(env.posisi, env.kotoran)
    print(f"Rencana hasil pencarian (BFS): {' -> '.join(rencana)}\n")

    for langkah, aksi in enumerate(rencana, 1):
        env.lakukan(aksi)
        cetak_langkah(langkah, env, aksi)

    print("\nPerbedaan dengan reflex: agen punya tujuan eksplisit dan menyusun")
    print("rencana terlebih dahulu, bukan sekadar bereaksi terhadap persepsi.")


if __name__ == "__main__":
    main()
