# LAPORAN PROYEK: IMPLEMENTASI MODULAR PENGOLAHAN CITRA DIGITAL

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
Pengolahan Citra Digital (PCD) merupakan disiplin ilmu yang fundamental dalam ilmu komputer, berfokus pada manipulasi dan analisis gambar digital untuk mengekstraksi informasi. Proyek ini dirancang sebagai implementasi praktis dari konsep-konsep dasar PCD, mencakup alur kerja dari akuisisi citra hingga analisis dan transformasi.

### 1.2 Tujuan Proyek
Tujuan utama dari proyek ini adalah untuk merancang dan mengimplementasikan serangkaian operasi dasar pengolahan citra secara modular. Proyek ini mendemonstrasikan kemampuan untuk:
1.  Mampu memuat dan menganalisis properti dasar citra.
2.  Melakukan konversi ruang warna (color space).
3.  Melakukan analisis statistik citra melalui histogram.
4.  Mampu menerapkan teknik segmentasi biner (thresholding).
5.  Mampu menampilkan operasi transformasi geometri.
6.  Memenuhi persyaratan implementasi spesifik, termasuk penggunaan struktur data `Tuple`, `Dictionary`, dan `List`.

### 1.3 Ruang Lingkup dan Teknologi
Proyek ini diimplementasikan menggunakan bahasa pemrograman **Python (v3.x)**. Fungsionalitas inti bergantung pada tiga pustaka (library) utama:
* **OpenCV (`cv2`)**: Digunakan untuk operasi pemrosesan citra inti, seperti membaca file, konversi warna, thresholding, dan transformasi geometri.
* **NumPy (`np`)**: Digunakan untuk operasi numerik yang efisien pada array N-dimensi (struktur data piksel) dan untuk perhitungan statistik.
* **Matplotlib (`plt`)**: Digunakan untuk visualisasi data, including menampilkan citra (dengan konversi BGR ke RGB yang tepat) dan memplot histogram.

---

## BAB II: METODOLOGI IMPLEMENTASI

### 2.1 Desain Arsitektur Modular
Arsitektur kode dirancang secara modular untuk meningkatkan keterbacaan, pemeliharaan, dan pengujian. Setiap tugas logis dalam alur kerja PCD dienkapsulasi ke dalam fungsi Python yang terpisah (misalnya, `langkah_1_muat_dan_analisis`, `langkah_2_konversi_grayscale`, dst.).

Fungsi `main()` bertindak sebagai titik eksekusi utama yang mengatur alur kerja (orchestrator), memanggil setiap fungsi langkah secara berurutan dan meneruskan data (objek citra) yang relevan dari satu langkah ke langkah berikutnya.

### 2.2 Pemanfaatan Struktur Data
Sesuai dengan spesifikasi proyek, struktur data bawaan Python dimanfaatkan sebagai berikut:
* **`Tuple`**: Atribut `.shape` dari citra (yang secara alami merupakan tuple) digunakan untuk mengambil dan menyimpan dimensi citra (Tinggi, Lebar, Kanal).
* **`Dictionary`**: Struktur data `dict` digunakan untuk menyimpan metadata citra secara terstruktur, memetakan kunci (seperti `'height'`, `'width'`, `'format'`) ke nilai yang sesuai.
* **`List`**: Struktur data `list` (yang berisi beberapa `tuple`) digunakan untuk menyimpan dan melaporkan hasil statistik deskriptif citra (nilai minimum, maksimum, rata-rata, dan standar deviasi).

### 2.3 Alur Pemrosesan
Alur kerja pemrosesan dieksekusi dalam urutan sebagai berikut:
1.  **Inisialisasi**: Pengguna menetapkan path ke gambar target dalam variabel global `PATH_GAMBAR`.
2.  **Pemuatan Citra**: Citra dimuat dari path yang ditentukan.
3.  **Analisis Awal**: Metadata dan dimensi diekstraksi.
4.  **Konversi Grayscale**: Citra berwarna dikonversi ke skala keabuan.
5.  **Analisis Statistik**: Histogram dan statistik dasar (min, max, mean) dihitung dari citra grayscale.
6.  **Segmentasi**: Teknik thresholding (Simple dan Otsu) diterapkan pada citra grayscale.
7.  **Transformasi**: Operasi geometri (Flip dan Rotasi) diterapkan pada citra berwarna asli.
8.  **Visualisasi**: Semua hasil utama dirangkum dan ditampilkan dalam satu plot subplot.

---

## BAB III: HASIL DAN PEMBAHASAN

Implementasi proyek menghasilkan serangkaian output visual dan tekstual pada setiap tahapan, yang didokumentasikan di bawah ini.

### 3.1 Langkah 1: Pemuatan dan Analisis Citra
Citra berhasil dimuat menggunakan `cv2.imread()`. Fungsi ini memvalidasi keberadaan file sebelum melanjutkan. Metadata dan dimensi citra berhasil diekstraksi dan ditampilkan di konsol, memenuhi persyaratan penggunaan `Tuple` untuk dimensi dan `Dictionary` untuk metadata. Citra asli (dalam format BGR OpenCV) dikonversi ke RGB dan ditampilkan dengan benar menggunakan Matplotlib.

![](https://github.com/feyon/adv-computer-vision/blob/main/output/Citra%20Asli%20(BGR%20-%3E%20RGB).png)

### 3.2 Langkah 2: Konversi Grayscale
Citra asli yang memiliki 3 kanal (BGR) berhasil dikonversi menjadi citra 1 kanal (skala keabuan) menggunakan fungsi `cv2.cvtColor()` dengan flag `COLOR_BGR2GRAY`. Hasilnya adalah representasi intensitas citra yang diperlukan untuk langkah-langkah selanjutnya.

![](https://github.com/feyon/adv-computer-vision/blob/main/output/Citra%20Grayscale.png)

### 3.3 Langkah 3: Analisis Histogram dan Statistik
Histogram intensitas untuk citra grayscale berhasil dihitung menggunakan `cv2.calcHist()`. Plot histogram yang dihasilkan memberikan visualisasi yang jelas tentang distribusi frekuensi nilai piksel. Selain itu, statistik deskriptif (min, max, mean, std_dev) dihitung menggunakan NumPy dan disajikan dalam format `List`, memberikan ringkasan kuantitatif dari properti citra.


![](https://github.com/feyon/adv-computer-vision/blob/main/output/histogram-citra-grayscale.png)

### 3.4 Langkah 4: Segmentasi Biner (Thresholding)
Dua metode segmentasi berbasis ambang batas (thresholding) berhasil diterapkan:
**Simple Thresholding**: Menggunakan nilai ambang batas statis (127), citra dibagi secara kaku menjadi piksel hitam (0) dan putih (255).

![](https://github.com/feyon/adv-computer-vision/blob/main/output/simple-threshold-ambang-127.png)

### 3.5 Langkah 5: Transformasi Geometri
Operasi manipulasi spasial pada citra asli (berwarna) berhasil dilakukan:
* **Flipping**: Citra dicerminkan secara horizontal (sumbu Y) menggunakan `cv2.flip()`.

![](https://github.com/feyon/adv-computer-vision/blob/main/output/manipulasi-flip-horizontal.png)

* **Rotasi**: Citra diputar 45 derajat mengelilingi titik pusatnya menggunakan matriks transformasi afinitas yang dihasilkan oleh `cv2.getRotationMatrix2D()` dan diterapkan dengan `cv2.warpAffine()`.

![](https://github.com/feyon/adv-computer-vision/blob/main/output/manipulasi-rotasi-45-derajat.png)

### 3.6 Langkah 6: Ringkasan Visual
Sebagai langkah akhir, fungsi `buat_ringkasan_visual()` berhasil mengagregasi semua keluaran visual utama ke dalam satu gambar komposit menggunakan `plt.subplots()`. Plot ringkasan ini (grid 2x3) menyajikan perbandingan berdampingan dari Citra Asli, Grayscale, Histogram, Thresholding Otsu, dan Rotasi, memberikan gambaran umum yang komprehensif dari seluruh alur kerja proyek.

![](https://github.com/feyon/adv-computer-vision/blob/main/output/ringkasan-project-pengolahan-citra-digital.png)

Script Log

![](https://github.com/feyon/adv-computer-vision/blob/main/output/script_log.png)

---

## BAB IV: KESIMPULAN

Proyek ini telah berhasil mengimplementasikan alur kerja fundamental pengolahan citra digital secara lengkap dan modular. Setiap tahapan, mulai dari pemuatan citra, analisis, konversi, segmentasi, hingga transformasi geometri, telah dieksekusi dan divalidasi.

Implementasi ini secara efektif mendemonstrasikan penggunaan praktis pustaka OpenCV, NumPy, dan Matplotlib. Selain itu, semua persyaratan spesifikasi proyek, termasuk pemanfaatan struktur data `Tuple`, `Dictionary`, dan `List` pada konteks yang tepat, telah terpenuhi. Arsitektur modular yang digunakan terbukti efisien, menghasilkan kode yang bersih, mudah dipahami, dan dapat diperluas untuk operasi PCD yang lebih kompleks di masa depan.
