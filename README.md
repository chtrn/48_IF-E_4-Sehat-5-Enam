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

Repositori disusun mengikuti alur kerja Data Science berbasis CRISP-DM. Komponen proyek mencakup **Business Understanding, Data Gathering, Data Understanding, EDA, Cleaning, Preprocessing, Modeling, Evaluation, Reproducibility, dan rencana deployment**.

Tujuan utama proyek adalah memperkirakan nilai akhir Matematika sebelum nilai periode pertama (`G1`) dan periode kedua (`G2`) tersedia. Oleh karena itu, `G1` dan `G2` tidak digunakan sebagai fitur pada skenario utama. Variabel `absences` juga dikeluarkan dari skenario prediksi awal karena waktu ketersediaannya tidak cukup jelas untuk konteks deteksi dini.

**Penting:** model pada proyek ini merupakan prototipe akademik. Prediksi tidak digunakan sebagai keputusan otomatis mengenai kelulusan, kenaikan kelas, hukuman, maupun perlakuan terhadap siswa. Keluaran model hanya diposisikan sebagai alat bantu penapisan awal yang tetap membutuhkan peninjauan guru atau konselor.

## Dataset

Dataset utama berada pada:

```text
data/raw/student-mat.csv
```

Karakteristik dataset:

- **395 baris** data siswa.
- **33 variabel**.
- Target `G3`, yaitu nilai akhir Matematika pada skala **0–20**.
- Variabel mencakup faktor demografis, keluarga, sekolah, aktivitas, perilaku, kehadiran, dan riwayat akademik.

Sumber:

> Cortez, P. (2008). *Student Performance*. UCI Machine Learning Repository.  
> https://doi.org/10.24432/C5TG7T

Lisensi dataset: **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

## Temuan Awal

Berdasarkan analisis pada notebook dan laporan:

- Dataset memiliki ukuran **395 × 33**.
- Tidak ditemukan missing value pada pemeriksaan awal.
- Tidak ditemukan baris duplikat penuh.
- Nilai `G3` berada pada rentang 0–20.
- Sebanyak **130 siswa (32,9%)** memiliki `G3 < 10`.
- Terdapat **38 siswa (9,6%)** dengan `G3 = 0`.
- `failures` menjadi salah satu prediktor yang menunjukkan hubungan negatif paling kuat dengan `G3`.
- `absences` menunjukkan pola khusus terhadap kelompok `G3 = 0`, sehingga tidak digunakan pada skenario prediksi awal.
- Hubungan antarvariabel diperlakukan sebagai hubungan **asosiatif**, bukan kausal.

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
│   └── 01_business_data_understanding.ipynb
├── src/
│   ├── common.py
│   ├── train.py
│   ├── merge_metrics.py
│   └── predict.py
├── laporan/
└── outputs/
    └── dibuat otomatis setelah training
```

Folder `outputs/` tidak harus disimpan sejak awal. Folder tersebut akan dibuat oleh pipeline saat training dijalankan.

## Peta Komponen Proyek

| Komponen | File utama |
|---|---|
| Business Understanding | `notebooks/01_business_data_understanding.ipynb` |
| Data Gathering | `notebooks/01_business_data_understanding.ipynb` |
| Data Understanding | `notebooks/01_business_data_understanding.ipynb` |
| EDA | `notebooks/01_business_data_understanding.ipynb` |
| Cleaning | `notebooks/01_business_data_understanding.ipynb` |
| Dataset | `data/raw/student-mat.csv` |
| Konfigurasi eksperimen | `config.yaml` |
| Validasi data | `src/common.py` |
| Training dan evaluasi | `src/train.py` |
| Penggabungan hasil | `src/merge_metrics.py` |
| Inferensi | `src/predict.py` |
| Dependensi | `requirements.txt` |
| Dokumentasi | `laporan/` |

## 1. Business Understanding, Data Gathering, EDA, dan Cleaning

**File:**

```text
notebooks/01_business_data_understanding.ipynb
```

Notebook ini mencakup:

- latar belakang proyek;
- rumusan masalah;
- tujuan penelitian;
- stakeholder;
- metrik keberhasilan;
- batasan dan risiko;
- sumber dataset;
- pemuatan dataset;
- data dictionary;
- pemeriksaan kualitas data;
- analisis distribusi `G3`;
- analisis variabel numerik dan kategorikal;
- korelasi;
- pemeriksaan missing value;
- pemeriksaan duplikasi;
- pemeriksaan kandidat outlier;
- analisis awal terhadap `G3 = 0`.

Notebook membaca dataset melalui:

```text
data/raw/student-mat.csv
```

Dengan demikian, notebook dan dataset sudah menggunakan path relatif proyek.

## 2. Konfigurasi Eksperimen

**File:**

```text
config.yaml
```

File konfigurasi menyimpan parameter yang digunakan oleh pipeline, antara lain:

- path dataset;
- separator CSV;
- ukuran data yang diharapkan;
- checksum SHA-256;
- target `G3`;
- threshold risiko;
- threshold warning;
- fitur yang harus dikeluarkan;
- jumlah fold dan repeat validasi;
- parameter Ridge Regression;
- parameter Random Forest;
- lokasi output.

Contoh bagian penting:

```yaml
data:
  path: "data/raw/student-mat.csv"
  separator: ";"

target:
  column: "G3"
  actual_risk_threshold: 10
  predicted_warning_threshold: 11
```

Penggunaan file konfigurasi membuat eksperimen lebih mudah dijalankan ulang tanpa mengubah kode sumber.

## 3. Validasi Data

**File:**

```text
src/common.py
```

File ini menyediakan fungsi untuk:

- membaca `config.yaml`;
- mengatur path relatif proyek;
- menghitung SHA-256 dataset;
- memvalidasi checksum;
- memvalidasi jumlah baris;
- memvalidasi jumlah kolom.

Alur:

```text
config.yaml
    ↓
src/common.py
    ↓
src/train.py
```

## 4. Preprocessing dan Modeling

**File:**

```text
src/train.py
```

Pipeline training menggunakan:

### Preprocessing

- fitur kategorikal → `OneHotEncoder`;
- fitur numerik → `StandardScaler`;
- seluruh transformasi berada di dalam `Pipeline` untuk mengurangi risiko data leakage.

### Model

1. `DummyRegressor`
2. `Ridge Regression`
3. `RandomForestRegressor`

### Evaluasi

- RMSE
- MAE
- R²
- Recall siswa berisiko
- Precision warning

## 5. Skenario Eksperimen

Pipeline menyediakan tiga skenario.

### `early_all`

Skenario utama prediksi awal.

- `G1` dikeluarkan.
- `G2` dikeluarkan.
- `absences` dikeluarkan.
- `G3 = 0` dipertahankan.

### `midperiod_all`

Skenario ketika informasi ketidakhadiran sudah tersedia.

- `G1` dikeluarkan.
- `G2` dikeluarkan.
- `absences` digunakan.
- `G3 = 0` dipertahankan.

### `early_without_g3_zero`

Analisis sensitivitas.

- `G1` dikeluarkan.
- `G2` dikeluarkan.
- `absences` dikeluarkan.
- observasi `G3 = 0` dikeluarkan.

Ketiga skenario digunakan untuk melihat pengaruh waktu ketersediaan fitur dan pola khusus pada target.

## 6. Penggabungan Hasil

**File:**

```text
src/merge_metrics.py
```

Skrip ini menggabungkan:

```text
outputs/metrics_early_all.json
outputs/metrics_midperiod_all.json
outputs/metrics_early_without_g3_zero.json
```

menjadi:

```text
outputs/metrics.json
```

Alur:

```text
train.py
   ↓
3 file metrics
   ↓
merge_metrics.py
   ↓
metrics.json
```

## 7. Inferensi

**File:**

```text
src/predict.py
```

Skrip ini menggunakan model hasil training:

```text
outputs/model.joblib
```

untuk menghasilkan:

- `predicted_G3`
- `warning_flag`

Output default:

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

## Keterkaitan Antarfile

Struktur pipeline:

```text
data/raw/student-mat.csv
        │
        ├──────────→ notebooks/01_business_data_understanding.ipynb
        │                    │
        │                    ├─ Business Understanding
        │                    ├─ Data Gathering
        │                    ├─ EDA
        │                    └─ Cleaning
        │
        └──→ config.yaml
                  │
                  ↓
            src/common.py
                  │
                  ↓
             src/train.py
                  │
          ┌───────┴─────────────┐
          ↓                     ↓
      metrics files         model.joblib
          │                     │
          ↓                     ↓
src/merge_metrics.py       src/predict.py
          │                     │
          ↓                     ↓
    metrics.json         predictions.csv
```

Dengan struktur ini, komponen data, notebook, konfigurasi, training, evaluasi, dan inferensi sudah memiliki hubungan yang jelas.

## Menjalankan Proyek

Disarankan menggunakan Python **3.10–3.12**.

### 1. Clone Repository

```bash
git clone https://github.com/chtrn/48_IF-E_4-Sehat-5-Enam.git
cd 48_IF-E_4-Sehat-5-Enam
```

### 2. Membuat Virtual Environment

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

### 3. Instal Dependensi

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Menjalankan Notebook

```bash
jupyter lab
```

Kemudian buka:

```text
notebooks/01_business_data_understanding.ipynb
```

Jalankan seluruh sel secara berurutan dari atas ke bawah.

## Menjalankan Training

### Skenario utama

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

## Menggabungkan Hasil Evaluasi

Setelah seluruh skenario selesai:

```bash
python src/merge_metrics.py
```

Hasil gabungan:

```text
outputs/metrics.json
```

## Menjalankan Prediksi

Setelah model tersedia:

```bash
python src/predict.py --model outputs/model.joblib --input data_baru.csv --sep ";"
```

Hasil:

```text
outputs/predictions.csv
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

Eksperimen dirancang agar dapat dijalankan ulang melalui kombinasi:

```text
student-mat.csv
+
config.yaml
+
requirements.txt
+
src/
+
notebooks/
```

`config.yaml` menyimpan parameter eksperimen sehingga nilai konfigurasi tidak perlu ditulis langsung di dalam kode.

Checksum SHA-256 pada dataset digunakan untuk memastikan file yang digunakan sesuai dengan dataset yang diharapkan.

Random seed juga ditentukan melalui konfigurasi untuk membantu menjaga konsistensi hasil eksperimen.

## Data, Privasi, dan Etika

Walaupun dataset tidak menyimpan identitas langsung seperti nama atau nomor siswa, dataset tetap memuat beberapa informasi yang sensitif, seperti:

- jenis kelamin;
- usia;
- pendidikan orang tua;
- pekerjaan orang tua;
- konsumsi alkohol;
- kesehatan;
- hubungan romantis;
- kondisi keluarga.

Karena itu:

- dataset tidak digabungkan dengan sumber identitas lain;
- model tidak digunakan untuk memberi stigma;
- prediksi tidak menggantikan keputusan guru;
- feature importance tidak ditafsirkan sebagai penyebab;
- hasil tidak langsung digeneralisasi ke sekolah Indonesia.

## Rencana Deployment

Deployment yang direncanakan bersifat proporsional dengan konteks proyek akademik.

### Tahap 1 — Offline Reproducibility

Notebook dan pipeline dijalankan pada data historis untuk memverifikasi preprocessing, training, dan evaluasi.

### Tahap 2 — Pilot Data Lokal

Sebelum digunakan di sekolah, pipeline perlu diuji pada data historis sekolah sasaran.

### Tahap 3 — Validasi

Model dievaluasi berdasarkan:

- RMSE;
- MAE;
- R²;
- recall;
- precision;
- performa antar kelompok;
- perubahan distribusi data.

### Tahap 4 — Batch Internal

Jika validasi lokal memadai, model dapat digunakan secara batch untuk membuat daftar siswa yang membutuhkan peninjauan.

### Tahap 5 — Human-in-the-Loop

Guru atau konselor tetap menjadi pengambil keputusan akhir.

### Tahap 6 — Monitoring

Jika digunakan secara berkelanjutan, perlu dilakukan pemantauan terhadap:

- data drift;
- penurunan performa;
- false warning;
- siswa berisiko yang tidak terdeteksi;
- perbedaan error antar kelompok;
- perubahan kurikulum atau kebijakan.

## Batasan Utama

- Dataset hanya terdiri atas **395 siswa**.
- Data berasal dari dua sekolah di Portugal.
- Konteks data berbeda dengan sistem pendidikan Indonesia.
- Model bersifat prediktif dan asosiatif, bukan kausal.
- `G3 = 0` memiliki pola khusus yang perlu dianalisis hati-hati.
- `absences` tidak digunakan pada skenario awal karena waktu ketersediaannya tidak jelas.
- Model tidak boleh digunakan sebagai satu-satunya dasar pengambilan keputusan.
- Performa pada dataset ini tidak menjamin performa yang sama pada sekolah lain.

## Catatan Penggunaan

Repositori ini dibuat untuk keperluan akademik, portofolio, dan dokumentasi reprodusibilitas proyek Data Science.

Struktur proyek dirancang agar alur berikut dapat ditelusuri:

```text
Data
  ↓
Business & Data Understanding
  ↓
EDA & Cleaning
  ↓
Configuration
  ↓
Preprocessing
  ↓
Model Training
  ↓
Evaluation
  ↓
Model Artifact
  ↓
Prediction
```
Model harus dipahami sebagai **alat bantu penapisan awal**, bukan sistem keputusan akademik otomatis.
