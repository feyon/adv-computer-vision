# -------------------------------------------------------------------
# PROYEK DASAR PENGOLAHAN CITRA DIGITAL
# Implementasi modular berdasarkan proposal
# -------------------------------------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- GANTI INI ---
# Ganti dengan path (lokasi) gambar yang ingin Anda uji
# Contoh: 'D:/images/foto.jpg' atau 'logo.png'
#
# <--- PERBAIKAN 1: Nama variabel disamakan menjadi PATH_GAMBAR (huruf besar)
PATH_GAMBAR = '59582.jpg' 
# -----------------

# ===================================================================
# BAGIAN I: FUNGSI-FUNGSI HELPER (PEMBANTU)
# ===================================================================

def display_image(title, image, cmap=None):
    """
    Fungsi helper untuk menampilkan satu gambar menggunakan Matplotlib.
    Menangani konversi BGR ke RGB secara otomatis.
    """
    plt.figure(figsize=(7, 7))
    plt.title(title)
    
    if cmap:
        # Tampilkan sebagai grayscale
        plt.imshow(image, cmap=cmap)
    else:
        # Asumsikan gambar BGR (dari OpenCV) dan konversi ke RGB
        if len(image.shape) == 3 and image.shape[2] == 3:
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else:
            # Jika sudah RGB atau format lain, tampilkan apa adanya
            plt.imshow(image)
            
    plt.axis('off')
    plt.show()

def display_image_subplot(ax, title, image, cmap=None):
    """
    Fungsi helper untuk menampilkan gambar di dalam subplot Matplotlib (ax).
    Ini digunakan untuk plot ringkasan final.
    """
    ax.set_title(title)
    if cmap:
        ax.imshow(image, cmap=cmap)
    else:
        # Asumsikan BGR, konversi ke RGB
        if len(image.shape) == 3 and image.shape[2] == 3:
            ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else:
            ax.imshow(image)
    ax.axis('off')

# ===================================================================
# BAGIAN II: FUNGSI-FUNGSI MODULAR PROYEK
# ===================================================================

def langkah_1_muat_dan_analisis(path_gambar_input): # Menggunakan nama parameter yang berbeda
    """
    Langkah 1: Memuat citra, menampilkan, dan menganalisis metadata.
    Memenuhi persyaratan penggunaan Tuple dan Dictionary.
    """
    print("--- Langkah 1: Memuat Citra ---")
    img = cv2.imread(path_gambar_input) # Menggunakan parameter
    
    if img is None:
        print(f"ERROR: Gagal memuat gambar dari '{path_gambar_input}'.")
        print("Pastikan path file sudah benar dan file ada.")
        return None
    
    # Persyaratan Struktur Data: TUPLE untuk dimensi
    # img.shape sudah merupakan tuple (Tinggi, Lebar, Kanal)
    dimensi_tuple = img.shape
    print(f"Dimensi (Tuple): {dimensi_tuple}")
    
    # Persyaratan Struktur Data: DICTIONARY untuk metadata
    metadata_dict = {
        'height': dimensi_tuple[0],
        'width': dimensi_tuple[1],
        'channels': dimensi_tuple[2] if len(dimensi_tuple) == 3 else 1,
        'format': path_gambar_input.split('.')[-1]
    }
    print(f"Metadata (Dictionary): {metadata_dict}")
    
    # Tampilkan citra asli
    display_image("1. Citra Asli (BGR -> RGB)", img)
    
    return img

def langkah_2_konversi_grayscale(img_asli):
    """
    Langkah 2: Mengkonversi citra berwarna ke grayscale.
    """
    print("\n--- Langkah 2: Konversi Grayscale ---")
    gray = cv2.cvtColor(img_asli, cv2.COLOR_BGR2GRAY)
    
    print(f"Dimensi Grayscale (Tuple): {gray.shape}")
    display_image("2. Citra Grayscale", gray, cmap='gray')
    
    return gray

def langkah_3_histogram_dan_statistik(img_gray):
    """
    Langkah 3: Menghitung histogram dan statistik dasar.
    Memenuhi persyaratan penggunaan List atau Tuple untuk statistik.
    """
    print("\n--- Langkah 3: Analisis Histogram & Statistik ---")
    
    # 1. Hitung Histogram
    hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    
    # 2. Visualisasi Histogram
    plt.figure(figsize=(8, 5))
    plt.title("3. Histogram Citra Grayscale")
    plt.xlabel("Nilai Intensitas Piksel (0-255)")
    plt.ylabel("Jumlah Piksel (Frekuensi)")
    plt.plot(hist, color='black')
    plt.xlim([0, 256])
    plt.grid(True)
    plt.show()
    
    # 3. Persyaratan Struktur Data: LIST/TUPLE untuk statistik
    min_val = float(np.min(img_gray))
    max_val = float(np.max(img_gray))
    mean_val = float(np.mean(img_gray))
    std_val = float(np.std(img_gray))
    
    statistik_list = [
        ('min', min_val),
        ('max', max_val),
        ('mean', round(mean_val, 2)),
        ('std_dev', round(std_val, 2))
    ]
    print(f"Statistik Citra (List of Tuples): {statistik_list}")
    
    return hist

def langkah_4_segmentasi_thresholding(img_gray):
    """
    Langkah 4: Menerapkan thresholding untuk segmentasi biner.
    """
    print("\n--- Langkah 4: Segmentasi Thresholding ---")
    
    # 1. Simple Binary Thresholding
    ret_simple, thresh_simple = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    display_image("4a. Simple Thresholding (Ambang=127)", thresh_simple, cmap='gray')
    
    # 2. Otsu's Thresholding
    ret_otsu, thresh_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print(f"Nilai ambang otomatis (Otsu) yang ditemukan: {ret_otsu}")
    display_image(f"4b. Otsu's Thresholding (Ambang={int(ret_otsu)})", thresh_otsu, cmap='gray')
    
    return thresh_simple, thresh_otsu

def langkah_5_manipulasi_geometri(img_asli):
    """
    Langkah 5: Melakukan transformasi geometri (Flipping dan Rotasi).
    """
    print("\n--- Langkah 5: Manipulasi Geometri ---")
    
    # 1. Flipping (Pencerminan)
    img_flip_h = cv2.flip(img_asli, 1)
    display_image("5a. Manipulasi: Flip Horizontal", img_flip_h)
    
    # 2. Rotasi
    (h, w) = img_asli.shape[:2]
    pusat = (w // 2, h // 2)
    
    M = cv2.getRotationMatrix2D(pusat, 45, 1.0)
    img_rotasi = cv2.warpAffine(img_asli, M, (w, h))
    display_image("5b. Manipulasi: Rotasi 45 Derajat", img_rotasi)
    
    return img_flip_h, img_rotasi

def buat_ringkasan_visual(img_asli, img_gray, hist, thresh_otsu, img_rotasi):
    """
    Membuat satu plot ringkasan yang berisi semua hasil utama
    menggunakan subplot, sesuai persyaratan proyek.
    """
    print("\n--- Menampilkan Plot Ringkasan Proyek ---")
    
    fig, ax = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle("Ringkasan Proyek Pengolahan Citra Digital", fontsize=20)
    
    # Baris 1
    display_image_subplot(ax[0, 0], "1. Citra Asli", img_asli)
    display_image_subplot(ax[0, 1], "2. Grayscale", img_gray, cmap='gray')
    
    # Plot Histogram di axis ke-3
    ax[0, 2].set_title("3. Histogram")
    ax[0, 2].plot(hist, color='black')
    ax[0, 2].set_xlim([0, 256])
    ax[0, 2].set_xlabel("Intensitas")
    ax[0, 2].set_ylabel("Frekuensi")
    ax[0, 2].grid(True)
    
    # Baris 2
    display_image_subplot(ax[1, 0], "4. Otsu's Threshold", thresh_otsu, cmap='gray')
    display_image_subplot(ax[1, 1], "5. Rotasi", img_rotasi)
    
    # <--- PERBAIKAN 2: Kode yang hilang ditambahkan di bawah ---
    
    # Kosongkan plot terakhir
    ax[1, 2].axis('off')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout untuk suptitle
    plt.show()

# ===================================================================
# BAGIAN III: EKSEKUSI UTAMA (MAIN)
# <--- PERBAIKAN 2: Kode yang hilang ditambahkan di bawah ---
# ===================================================================

def main():
    """
    Fungsi utama untuk menjalankan alur proyek secara berurutan.
    """
    # Langkah 1: Memanggil fungsi dengan variabel PATH_GAMBAR (huruf besar)
    img_asli = langkah_1_muat_dan_analisis(PATH_GAMBAR)
    
    # Hanya lanjutkan jika gambar berhasil dimuat
    if img_asli is not None:
        # Langkah 2
        img_gray = langkah_2_konversi_grayscale(img_asli)
        
        # Langkah 3
        data_hist = langkah_3_histogram_dan_statistik(img_gray)
        
        # Langkah 4
        _, img_otsu = langkah_4_segmentasi_thresholding(img_gray) # Kita hanya butuh hasil Otsu
        
        # Langkah 5
        _, img_rotasi = langkah_5_manipulasi_geometri(img_asli) # Kita hanya butuh hasil rotasi
        
        # Langkah Terakhir: Tampilkan Ringkasan
        buat_ringkasan_visual(img_asli, img_gray, data_hist, img_otsu, img_rotasi)

if __name__ == "__main__":
    main()