# LAPORAN PROYEK AKHIR DATA SCIENCE

## Prediksi Nilai Akhir Matematika Siswa Menggunakan Data Sosial, Keluarga, dan Sekolah

**Disusun untuk:** Praktikum Data Science  
**Program Studi:** Informatika  
**Fakultas:** Teknik Industri  
**Universitas:** Universitas Pembangunan Nasional “Veteran” Yogyakarta  
**Tahun:** 2026

# 4 Sehat 5 Enam
## Nomor Kelompok: 48
## Anggota Kelompok:
### Tazkya Syakieb Dwiningtyas (123240029)
### Aisyah Yasmine Kirana (123240064)
### Chatarina Giftadiyana (123240183)
### Amalya Kumalasari (123240198)

## 1. Business Understanding

### 1.1 Latar Belakang
Performa akademik siswa dipengaruhi oleh berbagai faktor yang berkaitan dengan kebiasaan belajar, dukungan keluarga, kondisi sosial, dan lingkungan sekolah. Analisis data dapat membantu memahami karakteristik dataset dan menguji apakah fitur-fitur tersebut memiliki kemampuan prediktif terhadap nilai akhir. Hasil analisis harus ditafsirkan secara hati-hati karena data observasional tidak dapat membuktikan hubungan sebab-akibat.

### 1.2 Rumusan Masalah
1. Bagaimana struktur dan kualitas dataset Student Performance untuk mata pelajaran matematika?
2. Bagaimana distribusi nilai akhir siswa dan hubungannya dengan beberapa fitur yang tersedia?
3. Seberapa baik model regresi memperkirakan nilai akhir berdasarkan fitur sosial, keluarga, kebiasaan, dan sekolah?
4. Fitur apa yang relatif berpengaruh terhadap prediksi model, dan apa batasan interpretasinya?

### 1.3 Tujuan
- Memahami sumber, struktur, dan kualitas dataset.
- Melakukan EDA dan dokumentasi pembersihan data.
- Menyiapkan fitur dengan pipeline preprocessing yang konsisten.
- Membandingkan baseline dan model regresi menggunakan metrik yang sesuai.
- Menyampaikan keterbatasan hasil serta peluang pengembangan.

### 1.4 Metrik Keberhasilan
Kualitas data dinilai dari pemeriksaan dimensi, nilai kosong, duplikasi, dan konsistensi. Model regresi dinilai menggunakan MAE, RMSE, dan R² pada data uji serta validasi silang. MAE/RMSE yang lebih kecil umumnya lebih baik; R² harus ditafsirkan bersama metrik lain dan karakteristik data.

## 2. Data Gathering dan Data Understanding

Dataset diperoleh dari UCI Machine Learning Repository: Cortez, P. (2008), *Student Performance*, https://doi.org/10.24432/C5TG7T. Lisensi dataset tercantum sebagai CC BY 4.0. Dataset memiliki berkas matematika dan bahasa Portugis; proyek ini memakai `student-mat.csv`. Notebook mengambil data dari arsip resmi saat dijalankan apabila file lokal belum tersedia.

Kolom mencakup informasi sekolah dan latar belakang siswa, kebiasaan, dukungan keluarga, absensi, serta nilai periode pertama (`G1`), kedua (`G2`), dan nilai akhir (`G3`). Definisi rinci dan tipe data diperiksa di notebook.

## 3. Exploratory Data Analysis (EDA)

EDA meliputi ukuran data, tipe kolom, nilai kosong, baris duplikat, statistik deskriptif, distribusi target `G3`, distribusi sejumlah fitur numerik/ordinal, korelasi, serta perbandingan nilai menurut fitur kategorikal. Grafik dan interpretasi final harus disesuaikan dengan keluaran aktual setelah notebook dijalankan. Korelasi atau perbedaan kelompok tidak menunjukkan kausalitas.

## 4. Cleaning dan Preprocessing

Langkah yang terdokumentasi dalam notebook meliputi penyalinan data asli, pemeriksaan duplikasi dan nilai target, audit nilai ekstrem, pemisahan fitur dan target, serta pembagian data latih-uji. Pipeline preprocessing menggunakan imputasi untuk nilai kosong, standardisasi fitur numerik, dan one-hot encoding fitur kategorikal. Fitur `G1` dan `G2` dikeluarkan dari model utama karena memiliki hubungan yang sangat dekat dengan target akhir dan dapat menimbulkan kebocoran informasi untuk tujuan prediksi berbasis latar belakang.

Pencilan tidak dihapus secara otomatis hanya karena berada di luar rentang statistik; keputusan perlu mempertimbangkan apakah nilai tersebut salah input atau memang mencerminkan observasi valid.

## 5. Modeling

Eksperimen membandingkan model baseline `DummyRegressor`, `LinearRegression`, dan `RandomForestRegressor`. Pipeline memastikan transformasi fitur dipelajari hanya dari data latih. Jika Random Forest belum dibahas di materi praktikum, sesuaikan kandidat model dengan metode yang disetujui dosen.

## 6. Evaluasi

Evaluasi dilakukan pada data uji menggunakan MAE, RMSE, dan R², dilengkapi validasi silang dan permutation importance. Masukkan hasil aktual setelah notebook dijalankan:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| DummyRegressor (mean) | 3.646 | 4.550 | -0.010 |
| Linear Regression | 3.395 | 4.196 | 0.141 |
| Random Forest | 3.041 | 3.804 | 0.294 |

Model dipilih berdasarkan RMSE rata-rata validasi silang pada data latih. Setelah model dipilih, evaluasi akhir dilakukan satu kali pada data uji. Tabel perbandingan berikut merupakan hasil evaluasi data uji semua kandidat; model terpilih dan metrik akhirnya perlu disebutkan secara terpisah sesuai output sel validasi silang. Jangan mengisi tabel dengan angka perkiraan.

## 7. Kesimpulan dan Saran

**Catatan reproduksibilitas:** angka pada tabel diperoleh dengan menjalankan pipeline menggunakan pembagian data 80:20 dan `random_state=42`. Jalankan kembali notebook pada lingkungan pengumpulan untuk memastikan hasil konsisten.

Pada pembagian data yang digunakan, Random Forest menghasilkan MAE 3,041, RMSE 3,804, dan R² 0,294 pada data uji, serta memiliki RMSE rata-rata validasi silang sekitar 3,930. Ini menunjukkan performa lebih baik daripada baseline dan Linear Regression pada eksperimen ini, tetapi kemampuan prediksinya masih terbatas. R² 0,294 berarti model hanya menjelaskan sebagian variasi nilai akhir pada data uji. Fitur terpenting harus ditulis sesuai output permutation importance yang dihasilkan notebook, dan ditafsirkan sebagai kontribusi prediktif, bukan penyebab nilai siswa. Tegaskan bahwa hasil merupakan analisis akademik pada satu dataset dan bukan dasar tunggal untuk keputusan tentang siswa.

Saran pengembangan: evaluasi pada data eksternal, uji sensitivitas pemilihan fitur, bandingkan metode yang telah dipelajari di praktikum, serta perhatikan aspek privasi dan potensi bias sebelum penggunaan lebih lanjut.

## 8. Batasan dan Etika

Dataset bersifat observasional, konteksnya terbatas, dan belum tentu merepresentasikan populasi siswa lain. Model dapat mempelajari pola pada sampel tanpa mengungkap sebab-akibat. Prediksi tidak seharusnya digunakan untuk memberi stigma atau membatasi kesempatan siswa. Identitas siswa tidak menjadi fokus proyek dan hasil disampaikan secara agregat.

## 9. Referensi

Cortez, P. (2008). *Student Performance* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T.

UCI Machine Learning Repository. *Student Performance dataset page*. https://archive.ics.uci.edu/dataset/320/student%2Bperformance/
