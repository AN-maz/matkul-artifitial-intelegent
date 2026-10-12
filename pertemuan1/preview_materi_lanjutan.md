# Preview Materi Lanjutan: Dari Agen Sederhana menuju LLM

Dokumen ini menjembatani materi BAB I (lihat `eLearning.md`) dengan topik yang lebih lanjut, sampai ke pertanyaan: *seberapa dekat kita bisa membangun sesuatu yang menyerupai LLM?*

---

## 1. Peta Jalan Bertingkat

Materi BAB I adalah fondasi. Di atasnya ada jenjang kemampuan yang bisa dibangun bertahap:

| Tingkat | Topik | Hubungan dengan BAB I | Status di Project |
| --- | --- | --- | --- |
| 0 | Agen reflex, model-based, goal-based, utility-based | Materi 1.4.4 | Sudah dibuat (`agen/`) |
| 0 | ML klasik: k-NN | Materi 1.1.4 (supervised learning) | Sudah dibuat (`ml/`) |
| 1 | **Perceptron** (1957, Rosenblatt) | Materi 1.3 sejarah + 1.4.2 rasionalitas | **Target berikutnya** |
| 2 | **Neural network kecil** (backpropagation 1986) | Materi 1.3 sejarah | Target berikutnya |
| 3 | **Model bahasa n-gram** | Materi 1.1.5 NLP | Target berikutnya |
| 4 | Word embedding, neural language model | Deep learning (1.1.4) | Butuh pustaka (NumPy/PyTorch) |
| 5 | **Transformer** (2017, Vaswani dkk.) | Materi 1.3 sejarah | Konsep bisa dipelajari, implementasi butuh GPU |
| 6 | **LLM** (GPT, dkk.) | Materi 1.3 era 2020-an | Tidak realistis dilatih sendiri; cukup dipahami & dipakai |

## 2. Seberapa Jauh Kita dari LLM?

LLM pada dasarnya adalah **model yang memprediksi kata (token) berikutnya** — sama seperti model bahasa n-gram, hanya skalanya jauh berbeda:

| Aspek | n-gram (bisa dibuat sekarang) | LLM (GPT-4 dkk.) |
| --- | --- | --- |
| Tugas inti | Prediksi kata berikutnya | Prediksi kata (token) berikutnya |
| "Otak" | Tabel frekuensi | Neural network Transformer |
| Jumlah parameter | Ratusan ribu entri tabel | Ratusan miliar parameter |
| Data latih | Beberapa paragraf teks | Ratusan miliar kata |
| Komputasi | Laptop biasa, hitungan detik | Ribuan GPU, berminggu-minggu |
| Bisa dibuat mahasiswa? | **Ya, pure Python** | Tidak (tapi bisa dipakai lewat API) |

Kesimpulan: konsep LLM *bisa* dicicipi sekarang lewat n-gram; skalanya yang tidak.

## 3. Tiga Praktek "Satu Tingkat di Atas" Materi Sekarang

### 3.1 Perceptron dari Nol

Neuron buatan paling sederhana: mengalikan input dengan bobot, menjumlahkan, lalu mengaktifkan lewat fungsi langkah. Dilatih dengan aturan perceptron (menyesuaikan bobot saat prediksi salah).

- Nyambung ke: sejarah 1957 (Rosenblatt) dan kritik terhadap perceptron yang memicu AI Winter pertama.
- Bisa dilatih untuk fungsi logika AND/OR dengan ±10 baris inti.
- Pure Python, tanpa dependensi.

### 3.2 Neural Network Kecil (XOR)

Perceptron tunggal **tidak bisa** menyelesaikan XOR — inilah kritik Minsky yang disebut di materi sejarah. Solusinya: tambah satu hidden layer dan latih dengan backpropagation (1986).

- Nyambung ke: kebangkitan jaringan saraf modern di materi 1.3.
- Mahasiswa melihat sendiri mengapa "satu neuron tidak cukup" — sejarah jadi terasa.

### 3.3 Model Bahasa n-gram (Proto-LLM)

Model yang menghitung peluang kata berikutnya dari 1-2 kata sebelumnya, lalu bisa **membangkitkan kalimat baru**. Inilah bentuk paling sederhana dari cara kerja LLM.

- Nyambung ke: NLP di materi 1.1.5 dan Transformer di materi 1.3.
- Latih dari teks bebas (misalnya isi `eLearning.md`), lalu minta model "menulis" kalimat baru bergaya materi kuliah.
- Pure Python, puluhan baris.

Contoh keluaran yang bisa diharapkan (setelah dilatih dari teks materi):

```
> agen rasional memilih aksi yang diharapkan memaksimalkan ukuran kinerja
> berdasarkan data latih model dapat mewarisi bias dari lingkungan
```

## 4. Urutan Belajar yang Disarankan

1. **Perceptron** → paham neuron, bobot, dan aturan belajar.
2. **Neural network XOR** → paham hidden layer dan backpropagation secara intuitif.
3. **n-gram language model** → paham intuisi "LLM = penebak kata berikutnya".
4. Setelah itu baru layak masuk deep learning sungguhan (PyTorch/TensorFlow, materi 1.5.2) dan arsitektur Transformer.

## 5. Referensi Lanjutan

- Vaswani, A., dkk. (2017). Attention is all you need. *(arsitektur Transformer — dasar LLM)*
- Rosenblatt, F. (1958). The Perceptron: A probabilistic model for information storage and organization in the brain.
- Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533-536.
- Jurafsky, D., & Martin, J. H. *Speech and Language Processing* — bab n-gram dan neural language model.
