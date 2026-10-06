import math
import random
from collections import Counter

DATA = [
    (5.1, 3.5, 1.4, 0.2, "setosa"),
    (4.9, 3.0, 1.4, 0.2, "setosa"),
    (5.0, 3.4, 1.5, 0.2, "setosa"),
    (5.4, 3.9, 1.7, 0.4, "setosa"),
    (4.6, 3.4, 1.4, 0.3, "setosa"),
    (5.8, 4.0, 1.2, 0.2, "setosa"),
    (7.0, 3.2, 4.7, 1.4, "versicolor"),
    (6.4, 3.2, 4.5, 1.5, "versicolor"),
    (6.9, 3.1, 4.9, 1.5, "versicolor"),
    (5.5, 2.3, 4.0, 1.3, "versicolor"),
    (6.5, 2.8, 4.6, 1.5, "versicolor"),
    (5.7, 2.8, 4.1, 1.3, "versicolor"),
    (6.3, 3.3, 6.0, 2.5, "virginica"),
    (5.8, 2.7, 5.1, 1.9, "virginica"),
    (7.1, 3.0, 5.9, 2.1, "virginica"),
    (6.3, 2.9, 5.6, 1.8, "virginica"),
    (6.5, 3.0, 5.8, 2.2, "virginica"),
    (7.6, 3.0, 6.6, 2.1, "virginica"),
]


def jarak_euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn_predict(data_latih, fitur_baru, k=3):
    jarak = []
    for baris in data_latih:
        fitur, label = baris[:4], baris[4]
        jarak.append((jarak_euclidean(fitur, fitur_baru), label))

    jarak.sort(key=lambda x: x[0])
    tetangga_terdekat = jarak[:k]
    suara = Counter(label for _, label in tetangga_terdekat)
    prediksi, jumlah_suara = suara.most_common(1)[0]

    print(f"  {k} tetangga terdekat: {dict(suara)}")
    return prediksi, jumlah_suara


def evaluasi(data_uji, data_latih, k=3):
    benar = 0
    for baris in data_uji:
        fitur, label_asli = baris[:4], baris[4]
        prediksi, _ = knn_predict(data_latih, fitur, k)
        cocok = prediksi == label_asli
        benar += cocok
        print(f"  Data {fitur} -> prediksi: {prediksi:11s} asli: {label_asli:11s} {'OK' if cocok else 'SALAH'}")

    akurasi = benar / len(data_uji) * 100
    print(f"\nAkurasi: {benar}/{len(data_uji)} = {akurasi:.0f}%")
    return akurasi


if __name__ == "__main__":
    print("Klasifikasi Bunga Iris dengan k-NN (BAB I - Machine Learning)")
    print("Paradigma: supervised learning (belajar dari data berlabel)\n")

    random.seed(42)
    data = DATA[:]
    random.shuffle(data)

    n_uji = 6
    data_uji, data_latih = data[:n_uji], data[n_uji:]
    print(f"Data latih: {len(data_latih)} baris, data uji: {len(data_uji)} baris\n")

    evaluasi(data_uji, data_latih, k=3)

    print("\nCoba bunga baru:")
    bunga_baru = (5.9, 3.0, 5.1, 1.8)
    prediksi, suara = knn_predict(data_latih, bunga_baru, k=3)
    print(f"  Bunga {bunga_baru} diprediksi: {prediksi} (suara {suara}/3)")
