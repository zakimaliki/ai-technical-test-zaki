# Technical Task 2

## Deskripsi

Script ini digunakan untuk menganalisis data freelancer dari file `freelancers.csv` dan menghasilkan dua output:

- `out.csv`: Menampilkan freelancer dengan jumlah project terbanyak dan total penghasilan tertinggi.
- `top_roles.csv`: Menampilkan 10 kombinasi client company dan project role dengan total earnings tertinggi di Q1 2024.

## Struktur File

- `main.py` : Script utama untuk memproses data.
- `freelancers.csv` : Data input utama.
- `test_main.py` : Unit test untuk memvalidasi logika pemrosesan data.
- `out.csv` dan `top_roles.csv` : Output hasil analisis.

## Cara Menjalankan

1. Pastikan sudah menginstall dependensi berikut:

   - pandas
   - pytest (untuk testing)

   Install dengan perintah:

   ```bash
   pip install pandas pytest
   ```

2. Jalankan script utama:

   ```bash
   python main.py
   ```

   Output akan tersimpan di `out.csv` dan `top_roles.csv`.

3. Untuk menjalankan unit test:
   ```bash
   python -m pytest test_main.py -v
   ```

## Catatan

- Pastikan file `freelancers.csv` berada di direktori yang sama dengan `main.py`.
- Script ini otomatis mengekstrak email dari kolom `_meta` yang berformat JSON.
