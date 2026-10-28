
# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Mafatihun Nabila  
**NIM:** 2225250198  
**Kelas:** 3 B

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file menggunakan Python serta menangani kesalahan yang mungkin terjadi selama proses pengolahan data.

## Format File Input

File input yang digunakan adalah `data/nilai.txt` dengan format:

NIM,nilai

Contoh isi file:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Program memproses data dengan nilai yang valid dan melewati baris yang tidak dapat dikonversi menjadi angka.

## Struktur Folder

- `data/catatan.txt`: File untuk latihan menulis dan menambahkan teks.
- `data/nilai.txt`: File input berisi NIM dan nilai.
- `data/hasil_rekap.txt`: File output berisi ringkasan hasil pengolahan nilai.
- `latihan/01_tulis_file.py`: Latihan menulis file.
- `latihan/02_baca_file.py`: Latihan membaca file.
- `latihan/03_append_file.py`: Latihan menambahkan isi file.
- `latihan/04_proses_baris.py`: Latihan memproses data per baris.
- `latihan/05_file_not_found.py`: Latihan menangani file yang tidak ditemukan.
- `latihan/06_value_error.py`: Latihan menangani kesalahan input.
- `tugas/rekap_nilai_file.py`: Program utama untuk merekap nilai dari file.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal dari folder utama proyek:

```bash
python tugas/rekap_nilai_file.py
```

Jika menggunakan perintah Python 3, jalankan:

```bash
python3 tugas/rekap_nilai_file.py
```

Program akan membaca file input, memvalidasi data, menghitung statistik nilai, dan menyimpan hasilnya ke `data/hasil_rekap.txt`.

## Error yang Ditangani

- `FileNotFoundError`: Menangani kondisi ketika file input tidak ditemukan.
- `ValueError`: Menangani nilai yang tidak dapat dikonversi menjadi angka.
- `OSError`: Menangani kesalahan saat menulis file rekap, jika penanganan ini diterapkan pada program.

## Test Case

| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| Semua baris valid | Semua data diproses dan statistik dihitung dengan benar. | Data valid berhasil diproses. | Berhasil |
| File input hilang | Pesan file tidak ditemukan ditampilkan dan program tidak crash. | Belum diuji. | Perlu diuji |
| Nilai invalid (`A004,abc`) | Baris invalid dilewati dan data lain tetap diproses. | 1 baris invalid dilewati; 5 data valid diproses. | Berhasil |
| Baris kosong | Baris kosong dilewati. | Belum diuji. | Perlu diuji |
| Nilai tepat 60 | Nilai 60 dihitung sebagai lulus. | Belum diuji. | Perlu diuji |

## Hasil Pengujian

Berdasarkan data input yang diberikan, program memproses lima data valid dan melewati satu baris yang memiliki nilai invalid.

- Jumlah data valid: 5
- Rata-rata nilai: 83.40
- Nilai minimum: 74
- Nilai maksimum: 92
- Jumlah lulus: 5

## Refleksi

Saat mengerjakan tugas ini, saya menemukan kesalahan berupa nilai yang tidak dapat dikonversi menjadi angka, yaitu `abc` pada data A004. Jika tidak ditangani, kesalahan tersebut dapat menghentikan proses program. Saya menggunakan `try-except ValueError` agar baris yang tidak valid dapat dilewati dan data lainnya tetap diproses. Saya juga mempelajari penggunaan `FileNotFoundError` untuk menangani kondisi ketika file input tidak tersedia.
