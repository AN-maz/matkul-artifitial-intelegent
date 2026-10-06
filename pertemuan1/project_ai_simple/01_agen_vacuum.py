from enum import Enum


class Lokasi(Enum):
    A = "A"
    B = "B"


class Status(Enum):
    BERSIH = "BERSIH"
    KOTOR = "KOTOR"


class Aksi(Enum):
    HISAP = "HISAP"
    KANAN = "KANAN"
    KIRI = "KIRI"
    DIAM = "DIAM"


def agen_vacuum_reflex(lokasi, status):
    if status == Status.KOTOR:
        return Aksi.HISAP
    if lokasi == Lokasi.A:
        return Aksi.KANAN
    if lokasi == Lokasi.B:
        return Aksi.KIRI
    return Aksi.DIAM


def agen_vacuum_model_based(model, lokasi, status):
    model[lokasi] = status

    if status == Status.KOTOR:
        return Aksi.HISAP

    if None not in model.values() and all(
        s == Status.BERSIH for s in model.values()
    ):
        return Aksi.DIAM

    if lokasi == Lokasi.A:
        return Aksi.KANAN
    return Aksi.KIRI


def simulasi(agen, judul, gunakan_model=False):
    print(f"\n=== {judul} ===")
    lingkungan = {Lokasi.A: Status.KOTOR, Lokasi.B: Status.KOTOR}
    model = {Lokasi.A: None, Lokasi.B: None}
    lokasi_agen = Lokasi.A
    skor = 0

    for langkah in range(1, 8):
        status = lingkungan[lokasi_agen]
        if gunakan_model:
            aksi = agen(model, lokasi_agen, status)
        else:
            aksi = agen(lokasi_agen, status)

        print(
            f"Langkah {langkah}: lokasi={lokasi_agen.value} "
            f"status={status.value} -> aksi={aksi.value}"
        )

        if aksi == Aksi.HISAP:
            lingkungan[lokasi_agen] = Status.BERSIH
            if gunakan_model:
                model[lokasi_agen] = Status.BERSIH
            skor += 1
        elif aksi == Aksi.KANAN:
            lokasi_agen = Lokasi.B
        elif aksi == Aksi.KIRI:
            lokasi_agen = Lokasi.A
        else:
            print("Semua ruangan bersih, agen berhenti.")
            break

    kotor_tersisa = sum(1 for s in lingkungan.values() if s == Status.KOTOR)
    print(f"Selesai. Ruangan kotor tersisa: {kotor_tersisa}, hisap berhasil: {skor}")


if __name__ == "__main__":
    print("Simulasi Agen Vacuum Cleaner (BAB I - Agen Intelejen)")
    print("Performance measure: jumlah ruangan yang berhasil dibersihkan")
    print("Environment: dua ruangan A dan B")
    print("Actuators: hisap, bergerak kanan/kiri")
    print("Sensors: sensor lokasi dan sensor kotoran")

    simulasi(agen_vacuum_reflex, "Simple Reflex Agent")
    simulasi(agen_vacuum_model_based, "Model-Based Reflex Agent", gunakan_model=True)
