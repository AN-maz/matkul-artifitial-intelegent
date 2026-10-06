import random

from lingkungan import Lingkungan, cetak_header, cetak_langkah

KONDISI_AWAL = [1, 0, 2, 0, 3]
EPISODE = 40
MAKS_LANGKAH = 20
ALPHA = 0.5
GAMMA = 0.9


def keadaan(env):
    posisi, kotor = env.persepsi()
    kiri = posisi > 0 and env.kotoran[posisi - 1] > 0
    kanan = posisi < env.jumlah_ruangan - 1 and env.kotoran[posisi + 1] > 0
    return (posisi, kotor > 0, kiri, kanan)


def aksi_valid(env):
    aksi = ["HISAP"]
    if env.posisi > 0:
        aksi.append("KIRI")
    if env.posisi < env.jumlah_ruangan - 1:
        aksi.append("KANAN")
    return aksi


def pilih_aksi(q, s, valid, epsilon):
    if random.random() < epsilon:
        return random.choice(valid)
    return max(valid, key=lambda a: q.get((s, a), 0.0))


def latih():
    q = {}
    epsilon = 1.0
    riwayat = []

    for episode in range(1, EPISODE + 1):
        env = Lingkungan(KONDISI_AWAL)
        total_hadiah = 0

        for _ in range(MAKS_LANGKAH):
            if env.semua_bersih():
                break
            s = keadaan(env)
            valid = aksi_valid(env)
            aksi = pilih_aksi(q, s, valid, epsilon)
            dibersihkan = env.lakukan(aksi)

            hadiah = dibersihkan * 10 - 1
            total_hadiah += hadiah
            if env.semua_bersih():
                hadiah += 20

            s_baru = keadaan(env)
            q_terbaik_berikutnya = max(
                (q.get((s_baru, a), 0.0) for a in aksi_valid(env)), default=0.0
            )
            q_lama = q.get((s, aksi), 0.0)
            q[(s, aksi)] = q_lama + ALPHA * (
                hadiah + GAMMA * q_terbaik_berikutnya - q_lama
            )

        riwayat.append((episode, total_hadiah, env.semua_bersih()))
        epsilon = max(0.05, epsilon * 0.9)

    return q, riwayat


def main():
    cetak_header(
        "5. Learning Agent",
        "belajar dari pengalaman (critic menilai, learning element memperbaiki)",
    )
    print(f"Melatih agen dengan Q-learning selama {EPISODE} episode...")
    print("Hadiah: +10 per tingkat kotoran dibersihkan, -1 per langkah, "
          "+20 jika semua bersih\n")

    q, riwayat = latih()

    print("Perkembangan selama pelatihan:")
    for episode, hadiah, selesai in riwayat:
        if episode == 1 or episode % 10 == 0:
            status = "semua bersih" if selesai else "belum selesai"
            print(f"  Episode {episode:>2}: total hadiah {hadiah:>4} ({status})")

    print("\nKebijakan hasil belajar (tanpa eksplorasi acak):")
    env = Lingkungan(KONDISI_AWAL)
    print(f"      {env.gambar()}\n")
    for langkah in range(1, MAKS_LANGKAH + 1):
        if env.semua_bersih():
            break
        s = keadaan(env)
        aksi = max(aksi_valid(env), key=lambda a: q.get((s, a), 0.0))
        env.lakukan(aksi)
        cetak_langkah(langkah, env, aksi)

    print("\nAgen tidak diberi aturan apa pun di awal. Perilaku membersihkan")
    print("yang efisien muncul murni dari coba-coba dan umpan balik hadiah.")


if __name__ == "__main__":
    random.seed(7)
    main()
