# BAB I: PENGENALAN KECERDASAN BUATAN

## Capaian Pembelajaran

1. Menjelaskan konsep dasar Kecerdasan Buatan dan dapat membedakannya dengan Kecerdasan Alami.
2. Menjelaskan bidang ilmu yang menjadi dasar Kecerdasan Buatan, sejarah perkembangannya, serta aplikasinya.
3. Menjelaskan peran agen intelejen dalam Kecerdasan Buatan.
4. Menjelaskan bahasa pemrograman yang digunakan di ranah AI beserta alasan pemilihannya.

---

## 1.1 Pengertian Kecerdasan Buatan

Kecerdasan Buatan (Artificial Intelligence/AI) adalah cabang ilmu komputer yang mempelajari bagaimana membuat mesin atau sistem komputer mampu melakukan tugas-tugas yang biasanya membutuhkan kecerdasan manusia, seperti bernalar, belajar dari pengalaman, memahami bahasa, mengenali pola, dan mengambil keputusan.

Istilah "Artificial Intelligence" diperkenalkan oleh John McCarthy dalam proposal Dartmouth tahun 1955 (McCarthy dkk., 1955). Sejak itu, para peneliti merumuskan definisi AI dari sudut pandang yang berbeda-beda.

### 1.1.1 Empat Pendekatan Definisi AI

Russell dan Norvig (2021) mengelompokkan definisi AI ke dalam empat pendekatan berdasarkan dua sumbu: berpikir vs bertindak, dan seperti manusia vs rasional.

| **Pendekatan** | **Berpikir (Thinking)** | **Bertindak (Acting)** |
| --- | --- | --- |
| **Seperti Manusia (Humanly)** | **Cognitive Modeling** — meniru proses berpikir manusia. | **Turing Test** — mesin dianggap cerdas jika manusia tidak dapat membedakan jawabannya dari jawaban manusia. |
| **Rasional (Rationally)** | **Laws of Thought** — bernalar mengikuti aturan logika formal. | **Rational Agent** — bertindak untuk mencapai hasil terbaik yang diharapkan. |

Buku teks modern, termasuk Russell dan Norvig, menjadikan pendekatan agen rasional sebagai kerangka utama karena bersifat umum dan dapat dirumuskan secara matematis.

### 1.1.2 Kecerdasan Buatan vs Kecerdasan Alami

| **Aspek** | **Kecerdasan Alami (Manusia)** | **Kecerdasan Buatan (AI)** |
| --- | --- | --- |
| **Sifat** | Kreatif dan berkembang secara alami | Konsisten dan relatif tetap, kecuali diprogram atau dilatih ulang |
| **Kecepatan Proses** | Relatif lambat untuk perhitungan kompleks | Sangat cepat dalam memproses perhitungan dan data dalam jumlah besar |
| **Transfer Pengetahuan** | Sulit ditransfer secara utuh kepada individu lain | Mudah disalin, didistribusikan, dan digandakan |
| **Biaya** | Membutuhkan pendidikan dan pengembangan selama bertahun-tahun | Biaya komputasi dan data dapat tinggi di awal, tetapi murah untuk direplikasi |
| **Adaptasi terhadap Konteks Baru** | Sangat baik dalam menghadapi situasi yang belum pernah dijumpai | Lebih terbatas pada data dan pola yang telah dipelajari |
| **Pemahaman Akal Sehat (*Common Sense*)** | Bawaan dan sangat kaya | Masih menjadi tantangan dalam penelitian AI |
| **Konsumsi Energi** | Sangat efisien; otak manusia menggunakan sekitar 20 watt | Model AI berukuran besar membutuhkan energi dan perangkat keras yang lebih besar |

### 1.1.3 Tingkatan dan Jenis AI

Berdasarkan cakupan kemampuan, AI sering dibedakan menjadi:

- **Narrow AI (ANI):** dirancang untuk satu tugas atau domain tertentu, misalnya filter spam, pengenal wajah, atau mesin rekomendasi. Seluruh sistem AI yang digunakan saat ini termasuk kategori ini, termasuk model bahasa besar yang tampak serba bisa.
- **Artificial General Intelligence (AGI):** AI hipotetis yang mampu memahami dan mempelajari tugas intelektual apa pun seperti manusia. Masih menjadi tujuan riset dan bahan perdebatan.
- **Artificial Superintelligence (ASI):** AI hipotetis yang melampaui kemampuan manusia di hampir semua bidang. Bersifat spekulatif.

### 1.1.4 Hubungan AI, Machine Learning, dan Deep Learning

Tiga istilah ini sering tertukar, padahal hubungannya berjenjang:

- **AI** adalah payung terluas: segala teknik yang membuat mesin tampak cerdas, termasuk sistem berbasis aturan dan pencarian.
  - **Machine Learning (ML)** adalah bagian dari AI di mana sistem belajar pola dari data, bukan hanya diprogram dengan aturan eksplisit (Mitchell, 1997).
    - **Deep Learning (DL)** adalah bagian dari ML yang memakai jaringan saraf tiruan berlapis banyak (LeCun dkk., 2015).

Contoh DL: pengenalan citra, penerjemah mesin, model bahasa besar (LLM).

*Gambar 1.1 Hubungan AI, machine learning, dan deep learning*

Paradigma pembelajaran dalam ML terbagi menjadi tiga: supervised learning (belajar dari data berlabel), unsupervised learning (menemukan struktur pada data tanpa label), dan reinforcement learning (belajar lewat umpan balik berupa hadiah/hukuman).

### 1.1.5 Subbidang dan Aplikasi AI

| Subbidang | Contoh Aplikasi |
| --- | --- |
| Pemrosesan Bahasa Alami (NLP) | Penerjemah mesin, chatbot, asisten virtual, analisis sentimen |
| Visi Komputer | Pengenalan wajah, diagnosis citra medis, kendaraan otonom |
| Pengenalan Suara | Asisten suara, transkripsi otomatis |
| Robotika | Robot industri, robot gudang, drone |
| Sistem Pakar dan Representasi Pengetahuan | Sistem diagnosis berbasis aturan, konsultasi teknis |
| Perencanaan dan Penjadwalan | Logistik, penjadwalan produksi, navigasi |
| Sistem Rekomendasi | Rekomendasi film, musik, produk |
| AI Generatif | Pembuatan teks, gambar, kode, dan audio |

Di Indonesia, contoh penerapannya antara lain deteksi penipuan pada layanan keuangan, chatbot layanan pelanggan, prediksi permintaan pada e-commerce, serta analisis citra untuk pertanian dan kesehatan.

### 1.1.6 Etika dan Tanggung Jawab dalam AI

Penerapan AI menimbulkan isu yang perlu dipahami sejak awal, antara lain:

- **Bias dan keadilan:** model dapat mewarisi bias dari data latih.
- **Privasi dan perlindungan data pribadi:** pengumpulan data dalam skala besar berisiko menyalahgunakan data. Di Indonesia, hal ini diatur dalam Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi.
- **Transparansi dan keterjelasan (explainability):** model kompleks sulit dijelaskan alasan keputusannya.
- **Akuntabilitas:** siapa yang bertanggung jawab ketika sistem AI membuat kesalahan.
- **Dampak pada pekerjaan dan lingkungan:** otomasi dan kebutuhan energi pelatihan model.

UNESCO (2021) menerbitkan *Recommendation on the Ethics of Artificial Intelligence* sebagai kerangka etika global yang dapat dijadikan rujukan.

## 1.2 Bidang Ilmu yang Menjadi Dasar Kecerdasan Buatan

AI bersifat multidisipliner. Russell dan Norvig (2021) merangkum kontribusi berbagai bidang berikut:

| Bidang Ilmu | Kontribusi bagi AI | Contoh Konsep |
| --- | --- | --- |
| Filsafat | Dasar logika, penalaran, hakikat pikiran, dan pertanyaan apakah mesin dapat "berpikir". | Logika Aristoteles, rasionalisme vs empirisme |
| Matematika | Logika formal, probabilitas, statistik, aljabar linear, kalkulus, dan teori komputasi. | Teorema Bayes, turunan untuk optimasi, komputabilitas |
| Ekonomi | Teori keputusan dan teori permainan yang mendasari agen rasional. | Utilitas, proses keputusan Markov |
| Neurosains | Cara kerja otak dan saraf sebagai inspirasi model komputasi. | Neuron, jaringan saraf tiruan |
| Psikologi | Psikologi kognitif menjelaskan cara manusia berpikir, belajar, dan memutuskan. | Memori, persepsi, pemecahan masalah |
| Teknik Komputer | Perangkat keras dan arsitektur komputasi yang membuat AI praktis dijalankan. | CPU, GPU, TPU, komputasi awan |
| Teori Kendali dan Sibernetika | Sistem yang mengendalikan dirinya berdasarkan umpan balik (feedback). | Pengendali PID, kontrol optimal |
| Linguistik | Dasar pengolahan bahasa alami agar mesin memahami dan menghasilkan bahasa manusia. | Sintaksis, semantik, pragmatik |

## 1.3 Sejarah Kecerdasan Buatan

Perkembangan AI tidak lepas dari kontribusi Alan Turing, yang pada tahun 1950 mengajukan pertanyaan "Can machines think?" melalui makalah *Computing Machinery and Intelligence* dan memperkenalkan uji yang kini dikenal sebagai Turing Test (Turing, 1950).

| Periode | Peristiwa Penting |
| --- | --- |
| 1943 | Warren McCulloch dan Walter Pitts mengusulkan model matematis pertama untuk neuron buatan (McCulloch & Pitts, 1943). |
| 1950 | Alan Turing menerbitkan makalah yang memperkenalkan Turing Test. |
| 1951 | Marvin Minsky dan Dean Edmonds membangun SNARC, mesin jaringan saraf pertama. |
| 1956 | Lokakarya Dartmouth; istilah "Artificial Intelligence" digunakan secara resmi dan bidang AI dianggap lahir. |
| 1957 | Frank Rosenblatt memperkenalkan Perceptron. |
| 1956–1974 | Era antusiasme awal: program pemecah masalah umum, pembuktian teorema, dan bahasa LISP. |
| 1974–1980 | "Musim Dingin AI" pertama: pendanaan menurun akibat ekspektasi tak tercapai, dipicu antara lain oleh Laporan Lighthill (1973) dan kritik terhadap perceptron. |
| 1980–1987 | Kebangkitan melalui expert system yang dipakai secara komersial. |
| 1986 | Popularisasi algoritma backpropagation (Rumelhart, Hinton, & Williams, 1986), membuka jalan bagi jaringan saraf modern. |
| 1987–1993 | "Musim Dingin AI" kedua: mahalnya perawatan sistem pakar dan keterbatasan pendekatan berbasis aturan. |
| 1997 | Deep Blue (IBM) mengalahkan juara dunia catur Garry Kasparov. |
| 1990-an–2000-an | Pendekatan statistik dan machine learning menguat: pengenalan suara, logistik, data mining. |
| 2011 | IBM Watson memenangi kuis Jeopardy!. |
| 2012 | AlexNet memenangi ImageNet dan memicu ledakan deep learning (Krizhevsky dkk., 2012). |
| 2016 | AlphaGo (DeepMind) mengalahkan Lee Sedol dalam permainan Go. |
| 2017 | Arsitektur Transformer diperkenalkan (Vaswani dkk., 2017), dasar bagi model bahasa besar. |
| 2020-an | Era AI generatif dan Large Language Model (LLM) yang menghasilkan teks, gambar, kode, dan berinteraksi alami dengan manusia. |

Pelajaran dari sejarah: kemajuan AI berjalan dalam siklus antusiasme dan kekecewaan. Terobosan terbaru ditopang tiga faktor: ketersediaan data besar, daya komputasi (GPU), dan algoritma yang lebih baik.

## 1.4 Agen Intelejen

### 1.4.1 Agen dan Lingkungannya

Agen (agent) adalah segala sesuatu yang dapat dipandang mempersepsikan lingkungannya melalui sensor dan bertindak terhadap lingkungan tersebut melalui aktuator (Russell & Norvig, 2021). Interaksi ini berkelanjutan: agen terus menerima persepsi (percept) dan menghasilkan aksi.

Secara formal, perilaku agen digambarkan oleh fungsi agen yang memetakan urutan persepsi ke aksi, sedangkan program agen adalah implementasi konkret fungsi tersebut pada suatu arsitektur (perangkat keras dan sensor/aktuatornya).

Agen menerima persepsi dari lingkungan melalui sensor, dan memengaruhi lingkungan melalui aksi (sumber: Wikimedia Commons, CC BY-SA 3.0, Lyesice).

*Gambar 1.2 Agen dan lingkungannya* — Program agen memetakan urutan persepsi ke aksi (fungsi agen). Contoh (mobil otonom): sensor kamera, radar, lidar; aktuator kemudi, rem, gas; lingkungan jalan raya, kendaraan lain, dan pejalan kaki.

Kerangka untuk mendesain agen dikenal dengan singkatan PEAS:

- **Performance measure:** ukuran keberhasilan agen.
- **Environment:** lingkungan tempat agen beroperasi.
- **Actuators:** alat yang digunakan agen untuk bertindak.
- **Sensors:** alat yang digunakan agen untuk mempersepsi lingkungan.

Contoh deskripsi PEAS:

| Agen | Performance | Environment | Actuators | Sensors |
| --- | --- | --- | --- | --- |
| Mobil otonom | Aman, cepat, legal, nyaman | Jalan, lalu lintas, pejalan kaki, cuaca | Kemudi, gas, rem, lampu sein | Kamera, radar, lidar, GPS, speedometer |
| Sistem diagnosis medis | Diagnosis tepat, biaya pasien rendah | Pasien, rumah sakit, tenaga kesehatan | Tampilan pertanyaan, tes, diagnosis, rekomendasi | Input gejala dan jawaban pasien |
| Robot vacuum | Area bersih, hemat baterai | Ruangan, perabot, lantai | Roda, sikat, penyedot | Sensor tabrakan, sensor jatuh, kamera |
| Chatbot layanan pelanggan | Masalah terselesaikan, kepuasan pelanggan | Percakapan dengan pengguna, basis pengetahuan | Teks balasan, tiket eskalasi | Teks masukan pengguna |

### 1.4.2 Konsep Rasionalitas

Sebuah agen rasional memilih, untuk setiap kemungkinan urutan persepsi, aksi yang diharapkan memaksimalkan ukuran kinerjanya berdasarkan bukti dari urutan persepsi dan pengetahuan bawaan agen.

Rasionalitas pada suatu waktu bergantung pada empat hal:

1. Ukuran kinerja yang menentukan keberhasilan.
2. Pengetahuan agen tentang lingkungannya sejauh ini.
3. Aksi-aksi yang dapat dilakukan agen.
4. Urutan persepsi yang telah diterima agen sampai saat itu.

Perlu dibedakan antara rasionalitas dan omniscience (mahatahu): agen rasional tidak harus mengetahui hasil aksinya secara pasti, ia hanya perlu bertindak sebaik mungkin berdasarkan informasi yang tersedia. Rasionalitas juga berbeda dari kesempurnaan (perfection): rasionalitas memaksimalkan kinerja yang diharapkan, sedangkan kesempurnaan memaksimalkan kinerja aktual.

Agen rasional juga perlu melakukan pengumpulan informasi (information gathering), eksplorasi, dan belajar agar keputusannya membaik, serta bersifat otonom, yaitu tidak hanya bergantung pada pengetahuan bawaan perancangnya.

### 1.4.3 Sifat Lingkungan Tugas

| Dimensi | Penjelasan | Contoh |
| --- | --- | --- |
| Fully vs Partially observable | Apakah sensor dapat mengakses keadaan lingkungan secara lengkap atau hanya sebagian. | Catur (penuh) vs poker (sebagian) |
| Single agent vs Multi-agent | Beroperasi sendiri atau bersama agen lain yang saling memengaruhi (kompetitif/kooperatif). | Teka-teki silang vs catur |
| Deterministic vs Stochastic | Keadaan berikutnya ditentukan sepenuhnya oleh keadaan sekarang dan aksi, atau mengandung ketidakpastian. | Puzzle vs mengemudi |
| Episodic vs Sequential | Pengalaman terbagi episode independen, atau keputusan sekarang memengaruhi keputusan mendatang. | Klasifikasi cacat produk vs catur |
| Static vs Dynamic | Lingkungan berubah saat agen berpikir atau tidak. | Teka-teki silang vs taksi otonom |
| Discrete vs Continuous | Keadaan, waktu, persepsi, dan aksi bersifat terhingga atau kontinu. | Catur vs kendali robot |
| Known vs Unknown | Agen atau perancangnya mengetahui aturan hasil setiap aksi atau tidak. | Permainan kartu dengan aturan dikenal vs permainan baru |

Lingkungan yang paling sulit adalah yang partially observable, multi-agent, stochastic, sequential, dynamic, continuous, dan unknown, misalnya mengemudi di jalan raya.

### 1.4.4 Struktur Agen

Russell dan Norvig (2021) mengelompokkan agen menjadi lima jenis, dari yang paling sederhana hingga paling kompleks:

| Jenis Agen | Karakteristik | Contoh | Keterbatasan |
| --- | --- | --- | --- |
| Simple reflex agent | Bertindak berdasarkan persepsi saat ini dengan aturan kondisi-aksi (if-then), tanpa riwayat. | Termostat, sensor pintu otomatis | Gagal bila lingkungan tidak dapat diamati penuh |
| Model-based reflex agent | Menyimpan model internal tentang cara kerja dunia untuk melacak bagian yang tak teramati. | Robot vacuum yang mengingat peta ruangan | Belum memiliki tujuan eksplisit |
| Goal-based agent | Memilih aksi yang mendekatkan pada tujuan, memakai pencarian dan perencanaan. | Navigasi/GPS pencari rute | Tidak membedakan seberapa baik suatu hasil |
| Utility-based agent | Mempertimbangkan seberapa baik (utilitas) hasil di antara beberapa pilihan. | Sistem rekomendasi yang memaksimalkan kepuasan pengguna | Perhitungan utilitas dapat mahal |
| Learning agent | Belajar dan memperbaiki kinerja dari pengalaman. Terdiri atas performance element, learning element, critic, dan problem generator. | Sistem ML yang dilatih ulang berkala | Membutuhkan data dan umpan balik |

*Gambar 1.3 Struktur learning agent* — Performance element memilih aksi; critic menilai kinerja; learning element memperbaiki kinerja; problem generator mengusulkan eksperimen.

Contoh pseudocode agen reflex sederhana (vacuum cleaner dua ruang):

```
fungsi AGEN_VACUUM(lokasi, status):
    jika status = KOTOR  maka kembalikan HISAP
    jika lokasi = A      maka kembalikan KANAN
    jika lokasi = B      maka kembalikan KIRI
```

## 1.5 Bahasa Pemrograman untuk Kecerdasan Buatan

Tidak ada satu bahasa yang paling benar untuk AI. Pilihan bahasa bergantung pada jenis masalah (penalaran simbolik, komputasi numerik, atau produksi skala industri), ketersediaan pustaka, dan ekosistem komunitas.

### 1.5.1 Sejarah dan Peran Bahasa Pemrograman AI

| Tahun | Bahasa | Peran dalam Perkembangan AI |
| --- | --- | --- |
| 1958 | LISP (John McCarthy) | Bahasa AI paling awal dan berpengaruh. Mendukung pemrosesan simbolik, rekursi, dan manajemen memori otomatis (garbage collection). Menjadi standar riset AI selama puluhan tahun (McCarthy, 1960; Steele & Gabriel, 1993). |
| 1972 | Prolog (Alain Colmerauer dan rekan; Robert Kowalski sebagai penggagas dasar logikanya) | Bahasa pemrograman logika; program berupa fakta dan aturan, dan eksekusinya berupa pembuktian. Dipakai pada sistem pakar, penalaran berbasis aturan, dan NLP (Colmerauer & Roussel, 1993). |
| 1980-an | OPS5, CLIPS | OPS5 adalah bahasa berbasis aturan produksi. CLIPS dikembangkan di NASA sebagai alat (tool) pembangun sistem pakar. Keduanya mewakili masa kejayaan sistem pakar (Giarratano & Riley, 2005). |
| 1991 | Python (Guido van Rossum) | Awalnya bahasa serba guna. Kini dominan di riset dan industri AI/ML karena sintaks mudah dibaca dan ekosistem pustakanya. |
| 1993 | R (Ihaka & Gentleman) | Berfokus pada komputasi dan visualisasi statistik; kuat untuk analisis data dan ML statistik (Ihaka & Gentleman, 1996). |
| 1995 | Java | Dipakai pada sistem AI skala enterprise berkat portabilitas dan pustaka seperti Weka dan Deeplearning4j. |
| 2012 | Julia | Dirancang untuk komputasi numerik berkinerja tinggi dengan sintaks tingkat tinggi (Bezanson dkk., 2017). |

> **Catatan:** sebagian materi sebelumnya menyebut OPS5 dan CLIPS sebagai "bahasa shell sistem pakar". Istilah yang lebih tepat: OPS5 sebuah bahasa pemrograman berbasis aturan, sedangkan CLIPS sebuah tool/lingkungan pengembangan sistem pakar.

### 1.5.2 Bahasa Utama dan Penjelasannya

#### Python

Python adalah bahasa paling umum untuk AI dan ML saat ini. Alasan utamanya adalah sintaks ringkas dan ekosistem pustaka yang matang. Pustaka inti antara lain NumPy untuk array dan komputasi numerik (Harris dkk., 2020), pandas untuk data tabular, scikit-learn untuk ML klasik (Pedregosa dkk., 2011), serta PyTorch (Paszke dkk., 2019) dan TensorFlow (Abadi dkk., 2016) untuk deep learning. Python juga menjadi bahasa pemrograman yang banyak dipakai menurut Stack Overflow Developer Survey 2025, yang mencatat penggunaan Python naik sekitar tujuh poin persentase dibanding 2024 dan dipakai sekitar 58% responden (Stack Overflow, 2025). Kelemahan: kecepatan eksekusi Python murni lebih rendah, sehingga bagian berat biasanya dijalankan oleh pustaka yang ditulis dalam C/C++/CUDA.

Contoh singkat klasifikasi dengan scikit-learn:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier().fit(X_train, y_train)
print("Akurasi:", model.score(X_test, y_test))
```

#### LISP

LISP (List Processing) menyajikan kode dan data dalam struktur yang sama (daftar), sehingga mudah memanipulasi program sebagai data. Ciri ini cocok untuk penalaran simbolik. Dialek modernnya meliputi Common Lisp, Scheme, dan Clojure. Walau kini jarang untuk ML, gagasan LISP seperti rekursi, fungsi sebagai objek, dan garbage collection sudah diadopsi bahasa modern (McCarthy, 1960; Steele & Gabriel, 1993).

```lisp
(defun faktorial (n)
  (if (<= n 1) 1 (* n (faktorial (- n 1)))))
```

#### Prolog

Prolog bersifat deklaratif: pemrogram menyatakan fakta dan aturan, lalu mesin inferensi mencari jawaban melalui unifikasi dan backtracking. Cocok untuk sistem pakar, pemecahan kendala, dan penalaran logis (Colmerauer & Roussel, 1993; Kowalski, 1988).

```prolog
orang_tua(budi, ani).
orang_tua(ani, citra).
kakek_nenek(X, Z) :- orang_tua(X, Y), orang_tua(Y, Z).
% ?- kakek_nenek(budi, Siapa).   Siapa = citra
```

#### R

R berfokus pada statistika, eksplorasi data, dan visualisasi. Banyak dipakai di akademik, bioinformatika, dan analisis data. Untuk deep learning skala besar, R kurang dominan dibanding Python (Ihaka & Gentleman, 1996).

#### Java dan Bahasa JVM Lain

Java (juga Kotlin dan Scala) dipakai ketika AI harus terintegrasi dengan sistem enterprise berskala besar dan membutuhkan stabilitas serta kinerja. Contoh pustaka: Weka (ML klasik) dan Deeplearning4j.

#### Julia

Julia menjanjikan kecepatan mendekati C dengan sintaks tingkat tinggi, memakai multiple dispatch dan kompilasi JIT. Cocok untuk komputasi ilmiah, simulasi, dan ML yang menuntut performa (Bezanson dkk., 2017).

#### C/C++ dan CUDA

Hampir seluruh pustaka AI populer memiliki inti komputasi (backend) dalam C/C++ dan memanfaatkan CUDA untuk GPU. Bahasa ini dipilih untuk robotika, sistem tertanam, kendaraan otonom, dan inference berlatensi rendah.

#### Bahasa Pendukung

- **SQL:** mengakses dan menyiapkan data, tahap yang memakan banyak waktu dalam proyek AI.
- **JavaScript/TypeScript:** menjalankan model di peramban dan aplikasi web (mis. TensorFlow.js).
- **Rust dan Go:** dipakai untuk infrastruktur dan layanan yang menuntut keamanan memori atau konkurensi.

### 1.5.3 Perbandingan dan Panduan Memilih Bahasa

| Bahasa | Paradigma Utama | Kekuatan | Keterbatasan | Cocok Untuk |
| --- | --- | --- | --- | --- |
| Python | Multi-paradigma | Ekosistem AI/ML terbesar, mudah dipelajari | Eksekusi murni relatif lambat | ML, deep learning, NLP, prototipe, riset |
| LISP | Fungsional/simbolik | Manipulasi simbol, fleksibel | Komunitas kecil, kurva belajar | Penalaran simbolik, riset AI klasik |
| Prolog | Logika/deklaratif | Inferensi dan pencarian bawaan | Kurang cocok untuk komputasi numerik | Sistem pakar, kendala, representasi pengetahuan |
| R | Fungsional/statistik | Statistik dan visualisasi kuat | Kurang efisien untuk sistem produksi besar | Analisis data, statistik, riset |
| Java | Berorientasi objek | Portabel, stabil, skala enterprise | Lebih verbose, ekosistem DL lebih kecil | Sistem AI enterprise, Android |
| Julia | Multi-paradigma | Cepat, sintaks ilmiah | Ekosistem lebih kecil | Komputasi ilmiah, ML performa tinggi |
| C/C++ | Prosedural/OOP | Kinerja tertinggi, kontrol perangkat keras | Pengembangan lebih rumit | Robotika, embedded, inference cepat |

*Rule of thumb:* mulai dengan Python, tambahkan SQL untuk data, pelajari Prolog atau LISP bila tertarik pada AI simbolik dan logika, dan gunakan C++ bila membutuhkan kinerja tinggi.

## Rangkuman

- AI dapat didefinisikan melalui empat sudut pandang: berpikir seperti manusia, bertindak seperti manusia, berpikir rasional, dan bertindak rasional. Pendekatan agen rasional menjadi kerangka utama.
- AI adalah payung bagi ML dan DL. Seluruh AI saat ini termasuk narrow AI.
- AI bersifat multidisipliner: filsafat, matematika, ekonomi, neurosains, psikologi, teknik komputer, teori kendali, dan linguistik.
- Sejarah AI berlangsung dalam siklus: Dartmouth 1956, dua "musim dingin AI", hingga era deep learning dan AI generatif.
- Agen intelejen mempersepsi lingkungan lewat sensor dan bertindak lewat aktuator untuk memaksimalkan ukuran kinerja. Lima struktur agen: simple reflex, model-based reflex, goal-based, utility-based, dan learning agent.
- Bahasa pemrograman AI berkembang dari LISP dan Prolog (AI simbolik) ke Python, R, Julia, dan C++ (AI statistik dan deep learning). Pilihan bahasa menyesuaikan kebutuhan.
- Penerapan AI harus memperhatikan etika: bias, privasi, transparansi, dan akuntabilitas.

## Glosarium

| Istilah | Arti |
| --- | --- |
| Agen | Entitas yang mempersepsi lingkungan lewat sensor dan bertindak lewat aktuator |
| Percept | Masukan persepsi agen pada satu saat |
| Fungsi agen | Pemetaan urutan persepsi ke aksi |
| Rasionalitas | Memilih aksi yang memaksimalkan ukuran kinerja yang diharapkan |
| Turing Test | Uji kecerdasan mesin berbasis kemampuan meniru jawaban manusia |
| Machine Learning | Sistem yang belajar pola dari data |
| Deep Learning | ML dengan jaringan saraf berlapis banyak |
| AI Winter | Periode menurunnya pendanaan dan minat riset AI |
| Sistem pakar | Program yang meniru penalaran pakar memakai basis pengetahuan dan aturan |

## Daftar Pustaka

Abadi, M., dkk. (2016). TensorFlow: A system for large-scale machine learning. *Proceedings of the 12th USENIX Symposium on Operating Systems Design and Implementation (OSDI)*.

Bezanson, J., Edelman, A., Karpinski, S., & Shah, V. B. (2017). Julia: A fresh approach to numerical computing. *SIAM Review*, 59(1), 65-98.

Colmerauer, A., & Roussel, P. (1993). The birth of Prolog. *ACM SIGPLAN Notices*, 28(3), 37-52.

Giarratano, J. C., & Riley, G. D. (2005). *Expert Systems: Principles and Programming* (4th ed.). Thomson Course Technology.

Harris, C. R., dkk. (2020). Array programming with NumPy. *Nature*, 585, 357-362.

Ihaka, R., & Gentleman, R. (1996). R: A language for data analysis and graphics. *Journal of Computational and Graphical Statistics*, 5(3), 299-314.

Kowalski, R. (1988). The early years of logic programming. *Communications of the ACM*, 31(1), 38-43.

Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. *Advances in Neural Information Processing Systems 25 (NIPS)*.

LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*, 521, 436-444.

Lighthill, J. (1973). *Artificial Intelligence: A General Survey*. Science Research Council, London.

McCarthy, J. (1960). Recursive functions of symbolic expressions and their computation by machine, Part I. *Communications of the ACM*, 3(4), 184-195.

McCarthy, J., Minsky, M. L., Rochester, N., & Shannon, C. E. (1955). *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*.

McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biophysics*, 5, 115-133.

Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.

Paszke, A., dkk. (2019). PyTorch: An imperative style, high-performance deep learning library. *Advances in Neural Information Processing Systems 32 (NeurIPS)*.

Pedregosa, F., dkk. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.

Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533-536.

Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

Stack Overflow. (2025). *2025 Developer Survey*. https://survey.stackoverflow.co/2025

Steele, G. L., & Gabriel, R. P. (1993). The evolution of Lisp. *ACM SIGPLAN Notices*, 28(3), 231-270.

Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, 59(236), 433-460.

UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. https://www.unesco.org/en/artificial-intelligence/recommendation-ethics


bikin app, deadline 4 bulan 
dinas 
1. dokumen diskominfo sudah sama yuda irgi
2. buat teknologi web app 
