# Proyek Dasar Pengolahan Citra Digital

Sebuah implementasi modular sederhana yang mendemonstrasikan alur kerja (workflow) dasar pengolahan citra digital menggunakan Python, OpenCV, dan Matplotlib.

Proyek ini adalah langkah fundamental untuk mempelajari Computer Vision (CV) dengan berfokus pada cara memuat, menganalisis, dan memanipulasi gambar di tingkat piksel.

## Demo Hasil Akhir

Skrip ini akan mengambil sebuah gambar input dan menghasilkan satu plot ringkasan yang menampilkan semua langkah pemrosesan:

![Contoh Hasil Proyek](https://github.com/feyon/adv-computer-vision/blob/main/output/ringkasan-project-pengolahan-citra-digital.png)


---

## Fitur Utama

* **Pemuatan & Analisis Metadata**: Membaca file gambar dan mengekstrak dimensi (Tinggi, Lebar, Kanal) ke dalam `Tuple` serta metadata lainnya ke dalam `Dictionary`.
* **Konversi Grayscale**: Mengubah citra berwarna (3-kanal BGR) menjadi citra skala keabuan (1-kanal).
* **Analisis Histogram**: Menghitung dan memvisualisasikan distribusi intensitas piksel dari citra grayscale.
* **Segmentasi Thresholding**: Menerapkan teknik segmentasi biner sederhana, termasuk metode **Simple Thresholding** dan **Otsu's Thresholding** otomatis.
* **Manipulasi Geometri**: Melakukan transformasi spasial dasar seperti **Flipping** (pencerminan) dan **Rotating** (rotasi).
* **Visualisasi Modular**: Setiap langkah diproses dalam fungsi terpisah dan ditampilkan secara individual, diakhiri dengan satu plot ringkasan komprehensif.

---

## Library yang dibutuhkan untuk menjalankan program ini

* [Python](https://www.python.org/)
* [OpenCV (cv2)](https://opencv.org/) - Untuk fungsi inti pemrosesan citra.
* [NumPy](https://numpy.org/) - Untuk komputasi numerik dan representasi matriks citra.
* [Matplotlib](https://matplotlib.org/) - Untuk visualisasi data dan menampilkan citra.