# Prediksi Dini Nilai Akhir Matematika Siswa Sekolah Menengah melalui Pemodelan Regresi Berbasis Faktor Demografis, Sosial, dan Sekolah
Nama Kelompok: 4 Sehat 5 Enam <br>
Nomor Kelompok: 48 <br>
Anggota Kelompok: <br>
- Tazkya Syakieb Dwiningtyas (123240029)
- Aisyah Yasmine Kirana (123240064)
- Chatarina Giftadiyana (123240183)
- Amalya Kumalasari (123240198)

## Ringkasan

Proyek ini membahas **prediksi dini nilai akhir Matematika siswa (`G3`)** menggunakan faktor demografis, keluarga, sosial, dan sekolah dari dataset **Student Performance — Mathematics** milik UCI Machine Learning Repository.

Repositori disusun sebagai portofolio Data Science yang dapat ditelusuri dari data mentah, notebook analisis, konfigurasi eksperimen, skrip pemodelan, sampai artefak hasil prediksi. Folder `notebooks/` berisi **tiga notebook** yang menjadi dokumentasi proses analisis, sedangkan folder `src/` menyediakan skrip yang mendukung reprodusibilitas training, evaluasi, penggabungan hasil, dan inferensi.

Tujuan utama proyek adalah memperkirakan nilai akhir Matematika sebelum nilai periode pertama (`G1`) dan periode kedua (`G2`) tersedia. Oleh karena itu, `G1` dan `G2` tidak digunakan sebagai fitur pada skenario prediksi dini. Variabel `absences` juga dikeluarkan pada skenario awal karena waktu ketersediaannya perlu dibedakan dari fitur yang sudah tersedia sejak awal periode pembelajaran.

**Penting:** model pada proyek ini merupakan prototipe akademik. Prediksi tidak digunakan sebagai keputusan otomatis mengenai kelulusan, kenaikan kelas, hukuman, atau perlakuan terhadap siswa. Keluaran model hanya diposisikan sebagai alat bantu penapisan awal yang tetap memerlukan peninjauan guru atau konselor.

## Dataset

Dataset utama berada pada:

```text
data/raw/student-mat.csv
```

Karakteristik dataset:

- **395 baris** data siswa.
- **33 variabel**.
- Variabel target adalah `G3`, yaitu nilai akhir Matematika pada skala 0–20.
- Data mencakup faktor demografis, keluarga, sekolah, aktivitas, perilaku, kehadiran, dan riwayat akademik.

Sumber:

> Cortez, P. (2008). *Student Performance*. UCI Machine Learning Repository.  
> https://doi.org/10.24432/C5TG7T

Lisensi dataset: **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

## Temuan Awal

Berdasarkan analisis proyek:

- Dataset berukuran **395 × 33**.
- Tidak ditemukan missing value pada pemeriksaan awal.
- Tidak ditemukan baris duplikat penuh.
- Nilai `G3` berada pada rentang 0–20.
- Sebanyak **130 siswa (32,9%)** memiliki `G3 < 10`.
- Terdapat **38 siswa (9,6%)** dengan `G3 = 0`.
- `failures` menjadi salah satu variabel yang menunjukkan hubungan negatif paling kuat dengan `G3`.
- `absences` menunjukkan pola khusus terhadap kelompok `G3 = 0`, sehingga penggunaannya dibedakan antara skenario awal dan pertengahan periode.
- Hubungan antarvariabel diperlakukan sebagai hubungan **asosiatif**, bukan hubungan sebab-akibat.

## Struktur Repositori

```text
48_IF-E_4-Sehat-5-Enam/
├── README.md
├── requirements.txt
├── config.yaml
├── data/
│   └── raw/
│       └── student-mat.csv
├── notebooks/
│   ├── Notebook 01
│   ├── Notebook 02
│   └── Notebook 03
├── src/
│   ├── common.py
│   ├── train.py
│   ├── merge_metrics.py
│   └── predict.py
├── laporan/
└── outputs/
    └── dibuat otomatis setelah training
```

> Folder `notebooks/` berisi tiga file notebook pada repositori. Notebook dijalankan sesuai urutan penomoran file agar proses analisis dapat diikuti secara bertahap.

## Peta Komponen Proyek

| Komponen | Lokasi utama |
|---|---|
| Dataset mentah | `data/raw/student-mat.csv` |
| Business Understanding | Notebook 01 |
| Data Gathering | Notebook 01 |
| Data Understanding dan EDA | Notebook 01 dan notebook lanjutan |
| Cleaning dan Data Preparation | Notebook pada folder `notebooks/` |
| Eksperimen / analisis lanjutan | Notebook 02 dan Notebook 03 |
| Konfigurasi eksperimen | `config.yaml` |
| Validasi data dan utilitas | `src/common.py` |
| Training dan evaluasi model | `src/train.py` |
| Penggabungan metrik | `src/merge_metrics.py` |
| Inferensi | `src/predict.py` |
| Dependensi | `requirements.txt` |
| Dokumentasi laporan | `laporan/` |
| Artefak hasil | `outputs/` |

## Notebook

Folder:

```text
notebooks/
```

berisi **tiga notebook** yang digunakan untuk mendokumentasikan proses analisis secara bertahap.

### Notebook 01 — Business dan Data Understanding

Notebook pertama menjadi tahap awal proyek dan mencakup komponen utama seperti:

- latar belakang dan konteks proyek;
- rumusan masalah;
- tujuan proyek;
- stakeholder;
- metrik keberhasilan;
- sumber dataset;
- pemeriksaan struktur data;
- data dictionary;
- pemeriksaan kualitas data;
- eksplorasi distribusi target `G3`;
- analisis awal variabel prediktor;
- pemeriksaan missing value;
- pemeriksaan duplikasi;
- pemeriksaan kandidat outlier;
- analisis awal terhadap pola `G3 = 0`.

Notebook membaca dataset dari:

```text
data/raw/student-mat.csv
```

### Notebook 02 — Tahap Analisis Lanjutan

Notebook kedua digunakan sebagai kelanjutan dari notebook pertama. Notebook ini tetap menggunakan dataset dan konteks proyek yang sama, sehingga hasil dari tahap pemahaman dan pembersihan data dapat diteruskan ke proses analisis berikutnya.

Notebook kedua sebaiknya dijalankan setelah Notebook 01 agar keputusan data yang digunakan tetap konsisten.

### Notebook 03 — Tahap Eksperimen / Evaluasi Lanjutan

Notebook ketiga merupakan tahap lanjutan dari rangkaian notebook proyek.

Notebook ini melengkapi dokumentasi analisis yang tidak hanya bergantung pada kode di folder `src/`, sehingga proses dan hasil eksperimen dapat ditinjau melalui Jupyter Notebook.

Untuk menjaga reprodusibilitas, jalankan notebook berdasarkan urutan file:

```text
Notebook 01
    ↓
Notebook 02
    ↓
Notebook 03
```

## Konfigurasi Eksperimen

File:

```text
config.yaml
```

digunakan untuk menyimpan parameter eksperimen agar konfigurasi tidak ditulis langsung di dalam kode.

Konfigurasi utama mencakup:

```yaml
project:
  name: "Prediksi Dini Nilai Akhir Matematika"
  random_seed: 42

data:
  path: "data/raw/student-mat.csv"
  separator: ";"
  expected_rows: 395
  expected_columns: 33

target:
  column: "G3"
  actual_risk_threshold: 10
  predicted_warning_threshold: 11
```

Konfigurasi juga menyimpan:

- checksum dataset;
- fitur yang dikeluarkan;
- jumlah fold validasi;
- jumlah pengulangan;
- parameter Ridge Regression;
- parameter Random Forest;
- lokasi penyimpanan output.

## Validasi Data

File:

```text
src/common.py
```

menyediakan fungsi pendukung untuk:

- membaca `config.yaml`;
- mengatur path relatif terhadap root proyek;
- menghitung SHA-256 dataset;
- memvalidasi checksum;
- memvalidasi jumlah baris;
- memvalidasi jumlah kolom.

Hubungan file:

```text
config.yaml
    ↓
src/common.py
    ↓
src/train.py
```

## Preprocessing dan Modeling

File:

```text
src/train.py
```

menjadi pipeline training yang dapat dijalankan ulang melalui terminal.

### Preprocessing

Pipeline melakukan:

- pemisahan `G3` sebagai target;
- penghapusan fitur yang tidak digunakan sesuai skenario;
- `OneHotEncoder` untuk fitur kategorikal;
- `StandardScaler` untuk fitur numerik;
- preprocessing di dalam `Pipeline` agar transformasi tidak bocor dari data validasi.

### Model

Model yang dibandingkan:

1. **DummyRegressor** sebagai baseline.
2. **Ridge Regression**.
3. **RandomForestRegressor**.

### Metrik

Evaluasi mencakup:

- RMSE;
- MAE;
- R²;
- Recall siswa berisiko;
- Precision warning.

## Skenario Eksperimen

### `early_all`

Skenario utama prediksi dini.

- `G1` dikeluarkan.
- `G2` dikeluarkan.
- `absences` dikeluarkan.
- Observasi `G3 = 0` dipertahankan.

### `midperiod_all`

Skenario tambahan ketika informasi kehadiran sudah tersedia.

- `G1` dikeluarkan.
- `G2` dikeluarkan.
- `absences` digunakan.
- Observasi `G3 = 0` dipertahankan.

### `early_without_g3_zero`

Analisis sensitivitas.

- `G1` dikeluarkan.
- `G2` dikeluarkan.
- `absences` dikeluarkan.
- Observasi `G3 = 0` dikeluarkan.

## Penggabungan Hasil Eksperimen

File:

```text
src/merge_metrics.py
```

digunakan setelah tiga skenario training selesai.

Skrip membaca:

```text
outputs/metrics_early_all.json
outputs/metrics_midperiod_all.json
outputs/metrics_early_without_g3_zero.json
```

dan menggabungkannya menjadi:

```text
outputs/metrics.json
```

Alur:

```text
early_all
     │
midperiod_all
     │
early_without_g3_zero
     ↓
src/merge_metrics.py
     ↓
outputs/metrics.json
```

## Inferensi

File:

```text
src/predict.py
```

menggunakan model hasil training:

```text
outputs/model.joblib
```

untuk memprediksi nilai `G3` pada data baru.

Keluaran utama:

- `predicted_G3`;
- `warning_flag`.

Secara default hasil prediksi disimpan sebagai:

```text
outputs/predictions.csv
```

Alur:

```text
src/train.py
     ↓
outputs/model.joblib
     ↓
src/predict.py
     ↓
outputs/predictions.csv
```

## Keterkaitan Antar Komponen

```text
                       ┌───────────────────────────┐
                       │ data/raw/student-mat.csv │
                       └─────────────┬─────────────┘
                                     │
                 ┌───────────────────┴───────────────────┐
                 │                                       │
                 ↓                                       ↓
          notebooks/                               config.yaml
     ┌───────────────────┐                              │
     │ Notebook 01       │                              ↓
     │ Notebook 02       │                        src/common.py
     │ Notebook 03       │                              │
     └─────────┬─────────┘                              ↓
               │                                  src/train.py
               │                                    /      \
               │                                   /        \
               │                                  ↓          ↓
               │                             metrics      model.joblib
               │                                  │          │
               │                                  ↓          ↓
               │                       src/merge_metrics.py  src/predict.py
               │                                  │          │
               └──────────────────────────────────┴──────────┘
                                                  ↓
                                               outputs/
```

Secara fungsi:

- `data/` menyediakan dataset sumber.
- `notebooks/` mendokumentasikan proses analisis dalam tiga tahap.
- `config.yaml` menyimpan parameter eksperimen.
- `src/common.py` menangani konfigurasi dan validasi data.
- `src/train.py` menjalankan training dan evaluasi.
- `src/merge_metrics.py` menggabungkan hasil beberapa skenario.
- `src/predict.py` menggunakan model tersimpan untuk inferensi.
- `outputs/` menampung artefak yang dihasilkan.
- `laporan/` menyimpan dokumentasi tertulis proyek.

## Menjalankan Proyek

Disarankan menggunakan Python **3.10–3.12**.

### 1. Clone repository

```bash
git clone https://github.com/chtrn/48_IF-E_4-Sehat-5-Enam.git
cd 48_IF-E_4-Sehat-5-Enam
```

### 2. Membuat virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Instal dependensi

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Menjalankan Notebook

Jalankan:

```bash
jupyter lab
```

Kemudian buka folder:

```text
notebooks/
```

dan jalankan ketiga notebook secara berurutan berdasarkan nomor file:

```text
01 → 02 → 03
```

## Menjalankan Training

### Skenario prediksi awal

```bash
python src/train.py --config config.yaml --scenario early_all
```

### Skenario pertengahan periode

```bash
python src/train.py --config config.yaml --scenario midperiod_all
```

### Analisis sensitivitas tanpa G3 = 0

```bash
python src/train.py --config config.yaml --scenario early_without_g3_zero
```

## Menggabungkan Metrik

Setelah ketiga skenario training selesai:

```bash
python src/merge_metrics.py
```

## Menjalankan Prediksi

Setelah model tersedia:

```bash
python src/predict.py --model outputs/model.joblib --input data_baru.csv --sep ";"
```

## Requirements

Dependensi proyek disimpan pada:

```text
requirements.txt
```

Paket utama:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib
- PyYAML
- jupyterlab
- notebook

## Reprodusibilitas

Komponen utama yang digunakan untuk menjalankan ulang proyek adalah:

```text
data/raw/student-mat.csv
+
3 notebook pada notebooks/
+
config.yaml
+
requirements.txt
+
src/
```

`config.yaml` menjaga konfigurasi eksperimen tetap eksplisit, sedangkan `requirements.txt` mendokumentasikan environment Python yang diperlukan.

Validasi checksum pada dataset membantu memastikan training menggunakan file data yang sama dengan data yang diharapkan.

## Data, Privasi, dan Etika

Walaupun dataset tidak menyimpan identitas langsung seperti nama atau nomor siswa, dataset tetap memiliki beberapa atribut yang bersifat sensitif, seperti:

- jenis kelamin;
- usia;
- pendidikan orang tua;
- pekerjaan orang tua;
- kesehatan;
- konsumsi alkohol;
- hubungan romantis;
- kondisi keluarga.

Karena itu:

- dataset tidak digabungkan dengan sumber identitas lain;
- model tidak digunakan untuk memberi stigma kepada siswa;
- prediksi tidak menggantikan penilaian guru atau konselor;
- feature importance tidak ditafsirkan sebagai hubungan sebab-akibat;
- hasil dari dataset Portugal tidak langsung digeneralisasi ke sekolah Indonesia.

## Rencana Deployment

Deployment dirancang secara proporsional dengan konteks proyek akademik.

### Tahap 1 — Reproducibility Offline

Notebook dan skrip dijalankan pada data historis untuk memastikan alur analisis, preprocessing, training, dan evaluasi dapat direproduksi.

### Tahap 2 — Validasi Data Lokal

Sebelum dipakai pada konteks sekolah nyata, pipeline perlu diuji menggunakan data historis sekolah sasaran.

### Tahap 3 — Batch Prediction

Jika validasi lokal memadai, model dapat digunakan secara internal dan periodik untuk menghasilkan daftar siswa yang perlu ditinjau.

### Tahap 4 — Human-in-the-Loop

Guru atau konselor tetap menjadi pengambil keputusan akhir.

### Tahap 5 — Monitoring

Model perlu dipantau terhadap:

- perubahan distribusi data;
- RMSE;
- MAE;
- R²;
- recall;
- precision;
- false warning;
- siswa berisiko yang terlewat;
- perbedaan error antar kelompok.

Jika konteks atau distribusi data berubah, model perlu dievaluasi kembali sebelum digunakan.

## Batasan Utama

- Dataset hanya terdiri atas **395 siswa**.
- Data berasal dari dua sekolah di Portugal.
- Konteks data tidak secara langsung mewakili sistem pendidikan Indonesia.
- Model bersifat prediktif dan asosiatif, bukan kausal.
- `G3 = 0` memiliki pola khusus yang perlu dianalisis secara hati-hati.
- Waktu ketersediaan `absences` harus diperhatikan dalam konteks prediksi dini.
- Model tidak digunakan sebagai satu-satunya dasar keputusan terhadap siswa.
- Performa pada dataset ini tidak menjamin performa yang sama pada sekolah atau periode lain.

## Catatan Penggunaan

Repositori ini dibuat sebagai **portofolio dan dokumentasi reprodusibilitas proyek Data Science**.

Alur keseluruhan proyek dapat diringkas sebagai:

```text
Data
  ↓
Notebook 01
  ↓
Notebook 02
  ↓
Notebook 03
  ↓
Konfigurasi Eksperimen
  ↓
Training dan Evaluasi
  ↓
Model dan Metrics
  ↓
Prediction
```

Model harus dipahami sebagai **alat bantu penapisan awal**, bukan sistem keputusan akademik otomatis.

