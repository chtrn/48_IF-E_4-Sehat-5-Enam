# Prediksi Dini Nilai Akhir Matematika Siswa Sekolah Menengah melalui Pemodelan Regresi Berbasis Faktor Demografis, Sosial, dan Sekolah
Nama Kelompok: 4 Sehat 5 Enam <br>
Nomor Kelompok: 48 <br>
Anggota Kelompok: <br>
- Tazkya Syakieb Dwiningtyas (123240029)
- Aisyah Yasmine Kirana (123240064)
- Chatarina Giftadiyana (123240183)
- Amalya Kumalasari (123240198)

## Ringkasan

Proyek ini membahas **prediksi dini nilai akhir Matematika siswa (`G3`)** menggunakan faktor demografis, sosial, keluarga, dan sekolah dari dataset **Student Performance — Mathematics** milik UCI Machine Learning Repository.

Repositori disusun sebagai portofolio Data Science yang mencakup **Business Understanding, Data Gathering, Exploratory Data Analysis (EDA), Cleaning, Preprocessing, Feature Selection, Modeling, Evaluation, Clustering eksploratif, reprodusibilitas, dan rencana deployment**.

Analisis utama dibagi ke dalam tiga notebook:

1. `01_business_data_understanding.ipynb` — Business Understanding, Data Gathering, EDA, dan Cleaning.
2. `02_preparation_model_evaluation.ipynb` — Preprocessing, Feature Selection, Modeling, dan Evaluasi.
3. `03_clustering_profil_siswa.ipynb` — Clustering profil siswa sebagai eksplorasi tambahan.

Selain notebook, folder `src/` menyediakan skrip yang dapat digunakan untuk menjalankan eksperimen model secara terpisah dan lebih terstruktur melalui konfigurasi `config.yaml`.

**Penting:** model pada proyek ini merupakan prototipe akademik. Prediksi tidak dimaksudkan sebagai keputusan otomatis mengenai kelulusan, kenaikan kelas, hukuman, atau perlakuan terhadap siswa. Hasil model hanya diposisikan sebagai alat bantu analisis dan penapisan awal yang tetap memerlukan peninjauan manusia.

## Dataset

Dataset utama berada pada:

```text
data/raw/student-mat.csv
```

Karakteristik dataset:

- **395 baris** data siswa.
- **33 variabel**.
- Target `G3`, yaitu nilai akhir Matematika pada skala 0–20.
- Variabel mencakup faktor demografis, keluarga, sekolah, aktivitas, perilaku, kehadiran, dan riwayat akademik.

Sumber dataset:

> Cortez, P. (2008). *Student Performance*. UCI Machine Learning Repository.  
> https://doi.org/10.24432/C5TG7T

Lisensi dataset: **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

## Temuan Awal dari Dataset

Berdasarkan notebook yang tersedia:

- Ukuran dataset: **395 × 33**.
- Tidak ditemukan missing value pada pemeriksaan awal.
- Tidak ditemukan baris duplikat penuh.
- Target `G3` berada pada rentang valid 0–20.
- Sebanyak **130 siswa (32,9%)** memiliki `G3 < 10`.
- Terdapat **38 siswa (9,6%)** dengan `G3 = 0`.
- Pada pemeriksaan IQR, terdapat **15 kandidat outlier** pada variabel `absences`.
- Nilai ekstrem `absences` tidak langsung dihapus karena masih dapat merupakan observasi yang valid.
- `G1` dan `G2` dikeluarkan dari pemodelan pada Notebook 02 agar model tidak bergantung pada nilai periode sebelumnya.
- Random Forest menjadi model terbaik pada eksperimen Notebook 02 berdasarkan RMSE validasi silang.
- Hasil evaluasi akhir Notebook 02 menunjukkan **MAE 3,041**, **RMSE 3,804**, dan **R² 0,294**.
- Notebook 03 menghasilkan **2 klaster** sebagai jumlah klaster terbaik berdasarkan silhouette score pada eksplorasi K-Means.

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
│   ├── 01_business_data_understanding.ipynb
│   ├── 02_preparation_model_evaluation.ipynb
│   └── 03_clustering_profil_siswa.ipynb
├── src/
│   ├── common.py
│   ├── train.py
│   ├── merge_metrics.py
│   └── predict.py
├── laporan/
└── outputs/
    └── dibuat otomatis setelah training
```

## Peta Komponen Analisis Berdasarkan Notebook

### 1. Business Understanding — Notebook 01

**File:** `notebooks/01_business_data_understanding.ipynb`

Mencakup:

- latar belakang proyek;
- rumusan masalah;
- tujuan proyek;
- target dan metrik;
- batasan dan etika;
- konteks penggunaan model.

Notebook ini menjadi titik awal pemahaman masalah sebelum analisis data dilakukan.

### 2. Data Gathering — Notebook 01

**File:** `notebooks/01_business_data_understanding.ipynb`

Mencakup:

- pemuatan `student-mat.csv`;
- penggunaan path relatif proyek;
- mekanisme pengunduhan dataset UCI apabila file lokal belum tersedia;
- pemeriksaan jumlah baris dan kolom;
- pemeriksaan nama variabel;
- pemeriksaan tipe data;
- statistik deskriptif awal.

Dataset yang digunakan:

```text
data/raw/student-mat.csv
```

### 3. Exploratory Data Analysis (EDA) — Notebook 01

**File:** `notebooks/01_business_data_understanding.ipynb`

Mencakup:

- pemeriksaan missing value;
- pemeriksaan duplikasi;
- distribusi target `G3`;
- proporsi siswa dengan `G3 < 10`;
- distribusi fitur numerik dan ordinal;
- korelasi Pearson antara fitur numerik/ordinal dan `G3`;
- perbandingan distribusi `G3` pada beberapa fitur kategorikal;
- visualisasi histogram, korelasi, dan boxplot.

Hubungan yang ditemukan pada tahap ini diperlakukan sebagai **asosiasi**, bukan hubungan sebab-akibat.

### 4. Cleaning — Notebook 01 dan Notebook 02

**Notebook 01:** `notebooks/01_business_data_understanding.ipynb`

Mencakup:

- pembuatan salinan data agar data asli tetap tersedia;
- konversi `G3` ke numerik;
- pemeriksaan target di luar rentang 0–20;
- pemeriksaan missing value;
- pemeriksaan duplikasi;
- pemeriksaan kandidat outlier `absences` menggunakan aturan IQR.

Hasil cleaning:

```text
Sebelum cleaning : 395 × 33
Sesudah cleaning : 395 × 33
Target tidak valid yang dihapus : 0
Missing value sesudah cleaning : 0
Duplikat sesudah cleaning : 0
```

**Notebook 02:** `notebooks/02_preparation_model_evaluation.ipynb`

Notebook kedua mengulang pemeriksaan cleaning agar pemodelan dapat dijalankan secara mandiri tanpa bergantung pada state Notebook 01.

## Notebook 02 — Preprocessing, Feature Selection, Modeling, dan Evaluasi

**File:** `notebooks/02_preparation_model_evaluation.ipynb`

Notebook ini merupakan tahap pemodelan utama dalam alur notebook.

### Feature Selection

Target:

```text
G3
```

Fitur yang dikeluarkan:

```text
G1
G2
G3
```

Setelah penghapusan tersebut, jumlah fitur yang digunakan adalah **30 fitur**.

Pada Notebook 02, `absences` **masih digunakan** sebagai salah satu fitur numerik.

Data dibagi menjadi:

- **316 data latih**
- **79 data uji**

dengan proporsi 80:20 dan `random_state = 42`.

### Preprocessing

Fitur numerik:

- imputasi median;
- standardisasi menggunakan `StandardScaler`.

Fitur kategorikal:

- imputasi nilai paling sering;
- `OneHotEncoder(handle_unknown="ignore")`.

Seluruh preprocessing ditempatkan di dalam `Pipeline` dan `ColumnTransformer`.

### Model

Notebook 02 membandingkan:

1. **Dummy Regressor**
2. **Linear Regression**
3. **Random Forest Regressor**

Random Forest menggunakan:

```text
n_estimators = 300
random_state = 42
min_samples_leaf = 2
```

### Evaluasi

Metrik yang digunakan:

- MAE
- RMSE
- R²

Notebook juga menggunakan **5-fold cross validation** pada data latih dengan `KFold(shuffle=True, random_state=42)`.

Model dipilih berdasarkan nilai rata-rata RMSE validasi silang.

### Hasil Notebook 02

Model yang terpilih:

```text
Random Forest
```

Hasil evaluasi akhir pada data uji:

| Metrik | Nilai |
|---|---:|
| MAE | 3,041 |
| RMSE | 3,804 |
| R² | 0,294 |

Interpretasinya, rata-rata kesalahan absolut prediksi berada di sekitar **3,04 poin** pada skala nilai G3.

### Feature Importance

Notebook 02 menggunakan **Permutation Importance** dengan:

```text
n_repeats = 15
scoring = neg_mean_absolute_error
```

Feature importance digunakan untuk melihat seberapa besar model bergantung pada suatu fitur, bukan untuk membuktikan hubungan sebab-akibat.

## Notebook 03 — Clustering Profil Siswa

**File:** `notebooks/03_clustering_profil_siswa.ipynb`

Notebook ini merupakan **eksplorasi tambahan** dan tidak menjadi bagian langsung dari model regresi prediksi `G3`.

Tujuannya adalah mengelompokkan siswa berdasarkan profil numerik/ordinal menggunakan **K-Means**.

### Fitur Clustering

Fitur yang digunakan:

```text
studytime
failures
absences
freetime
goout
Dalc
Walc
health
famrel
```

`G3` tidak digunakan dalam pembentukan klaster agar clustering tidak sekadar mengelompokkan siswa berdasarkan nilai akhir.

### Preprocessing Clustering

- missing value numerik diisi menggunakan median;
- seluruh fitur distandardisasi menggunakan `StandardScaler`.

### Pemilihan Jumlah Klaster

Nilai K diuji dari:

```text
K = 2 sampai 6
```

Metode evaluasi:

- inertia / elbow method;
- silhouette score.

Hasil silhouette:

| K | Silhouette |
|---:|---:|
| 2 | 0,210 |
| 3 | 0,141 |
| 4 | 0,129 |
| 5 | 0,128 |
| 6 | 0,120 |

Berdasarkan silhouette tertinggi, dipilih:

```text
K = 2
```

Jumlah siswa:

- Klaster 0: **275 siswa**
- Klaster 1: **120 siswa**

Clustering bersifat eksploratif dan tidak digunakan untuk memberikan label resmi atau diagnosis terhadap siswa.

## Ringkasan Cepat

| Komponen | File utama |
|---|---|
| Business Understanding | `01_business_data_understanding.ipynb` |
| Data Gathering | `01_business_data_understanding.ipynb` |
| EDA | `01_business_data_understanding.ipynb` |
| Cleaning | Notebook 01 dan 02 |
| Feature Selection | `02_preparation_model_evaluation.ipynb` |
| Preprocessing | `02_preparation_model_evaluation.ipynb` |
| Modeling | `02_preparation_model_evaluation.ipynb` |
| Evaluation | `02_preparation_model_evaluation.ipynb` |
| Feature Importance | `02_preparation_model_evaluation.ipynb` |
| Clustering | `03_clustering_profil_siswa.ipynb` |
| Konfigurasi eksperimen script | `config.yaml` |
| Validasi data | `src/common.py` |
| Training script | `src/train.py` |
| Penggabungan metrik | `src/merge_metrics.py` |
| Inferensi | `src/predict.py` |

## Hubungan Notebook dengan Folder `src`

Notebook dan folder `src/` menggunakan **dataset dan tujuan proyek yang sama**, tetapi keduanya merupakan dua jalur eksekusi yang berbeda.

### Jalur Notebook

```text
data/raw/student-mat.csv
        ↓
Notebook 01
        ↓
Notebook 02
        ↓
Model + Evaluasi
```

Notebook 03 merupakan cabang eksplorasi tambahan:

```text
data/raw/student-mat.csv
        ↓
Notebook 03
        ↓
Clustering Profil Siswa
```

### Jalur Script

```text
data/raw/student-mat.csv
        +
config.yaml
        ↓
src/common.py
        ↓
src/train.py
        ↓
model.joblib + metrics
        ↓
src/merge_metrics.py / src/predict.py
```

Dengan demikian, Notebook 02 **tidak memanggil `src/train.py`**, dan `src/train.py` juga tidak membaca hasil Notebook 02.

Keduanya dapat digunakan untuk tujuan yang berbeda:

- notebook untuk dokumentasi proses analisis dan presentasi;
- `src/` untuk menjalankan eksperimen yang lebih terstruktur dan dapat direproduksi.

## Perbedaan Penting antara Notebook 02 dan `src/train.py`

Terdapat beberapa perbedaan yang perlu dicatat agar hasil tidak dianggap identik.

### Model Linear

Notebook 02 menggunakan:

```text
Linear Regression
```

Sedangkan `src/train.py` menggunakan:

```text
Ridge Regression
```

### Penggunaan `absences`

Notebook 02:

```text
absences digunakan
```

Pada skenario `early_all` di `src/train.py`:

```text
absences dikeluarkan
```

Hal ini karena pipeline script membedakan prediksi awal tahun dan pertengahan periode.

### Validasi

Notebook 02 menggunakan:

```text
train-test split 80:20
+
5-fold KFold pada data latih
```

Pipeline `src/train.py` menggunakan skenario validasi yang dikendalikan melalui `config.yaml`.

Oleh karena itu, hasil Notebook 02 dan `src/train.py` **tidak harus menghasilkan angka yang sama**.

## Konfigurasi Eksperimen Script

**File:** `config.yaml`

Konfigurasi digunakan oleh pipeline `src/` untuk menyimpan:

- path dataset;
- separator CSV;
- checksum SHA-256;
- jumlah baris dan kolom yang diharapkan;
- target `G3`;
- threshold risiko;
- threshold warning;
- fitur yang dikeluarkan;
- parameter validasi;
- parameter Ridge Regression;
- parameter Random Forest;
- lokasi output.

Contoh:

```yaml
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

## Skenario pada `src/train.py`

### `early_all`

Prediksi awal:

- `G1` dikeluarkan;
- `G2` dikeluarkan;
- `absences` dikeluarkan;
- `G3 = 0` dipertahankan.

### `midperiod_all`

Prediksi pertengahan periode:

- `G1` dikeluarkan;
- `G2` dikeluarkan;
- `absences` digunakan;
- `G3 = 0` dipertahankan.

### `early_without_g3_zero`

Analisis sensitivitas:

- `G1` dikeluarkan;
- `G2` dikeluarkan;
- `absences` dikeluarkan;
- observasi `G3 = 0` dikeluarkan.

## Menjalankan Proyek

Disarankan menggunakan Python **3.10–3.12**.

### Clone Repository

```bash
git clone https://github.com/chtrn/48_IF-E_4-Sehat-5-Enam.git
cd 48_IF-E_4-Sehat-5-Enam
```

### Membuat Virtual Environment

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

### Instal Dependensi

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Menjalankan Notebook

```bash
jupyter lab
```

Jalankan notebook berdasarkan urutan berikut:

```text
01_business_data_understanding.ipynb
        ↓
02_preparation_model_evaluation.ipynb
```

Notebook clustering dapat dijalankan secara terpisah:

```text
03_clustering_profil_siswa.ipynb
```

Ketiga notebook membaca dataset yang sama dari `data/raw/student-mat.csv`, sehingga secara teknis masing-masing dapat dijalankan secara mandiri selama dataset tersedia.

## Menjalankan Pipeline Script

Skenario utama:

```bash
python src/train.py --config config.yaml --scenario early_all
```

Skenario pertengahan periode:

```bash
python src/train.py --config config.yaml --scenario midperiod_all
```

Analisis sensitivitas:

```bash
python src/train.py --config config.yaml --scenario early_without_g3_zero
```

Setelah seluruh skenario selesai:

```bash
python src/merge_metrics.py
```

Contoh inferensi:

```bash
python src/predict.py --model outputs/model.joblib --input data_baru.csv --sep ";"
```

## Requirements

Dependensi utama disimpan di:

```text
requirements.txt
```

Paket yang digunakan:

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

Komponen utama untuk menjalankan ulang proyek:

```text
data/raw/student-mat.csv
+
notebooks/
+
config.yaml
+
requirements.txt
+
src/
```

Notebook dapat digunakan untuk menelusuri proses analisis secara visual dan bertahap, sedangkan `src/` menyediakan pipeline eksperimen yang lebih terstruktur.

Random state `42` digunakan pada proses pemodelan dan clustering untuk membantu menjaga konsistensi hasil.

## Data, Privasi, dan Etika

Dataset tidak memuat identitas langsung seperti nama atau nomor induk siswa, tetapi tetap memiliki atribut yang sensitif, antara lain:

- jenis kelamin;
- usia;
- pendidikan dan pekerjaan orang tua;
- kesehatan;
- konsumsi alkohol;
- hubungan romantis;
- kondisi keluarga.

Karena itu:

- data tidak digabungkan dengan sumber identitas lain;
- hasil tidak digunakan untuk memberi stigma kepada siswa;
- model tidak menggantikan penilaian guru atau konselor;
- feature importance tidak ditafsirkan sebagai sebab-akibat;
- klaster tidak digunakan sebagai label resmi siswa;
- hasil dari dataset Portugal tidak langsung digeneralisasi ke sekolah Indonesia.

## Rencana Deployment

Deployment dirancang secara proporsional karena proyek masih berada pada tahap akademik.

### Tahap 1 — Reproducibility Offline

Notebook dan pipeline script dijalankan kembali pada data historis untuk memastikan seluruh proses dapat direproduksi.

### Tahap 2 — Validasi Data Lokal

Sebelum digunakan pada konteks sekolah nyata, model perlu diuji menggunakan data sekolah sasaran.

### Tahap 3 — Batch Prediction

Jika validasi lokal memadai, model dapat digunakan secara internal dan periodik untuk menghasilkan daftar siswa yang perlu ditinjau.

### Tahap 4 — Human-in-the-Loop

Guru atau konselor tetap menjadi pengambil keputusan akhir.

### Tahap 5 — Monitoring

Performa perlu dipantau berdasarkan:

- RMSE;
- MAE;
- R²;
- recall dan precision jika digunakan untuk penapisan;
- perubahan distribusi data;
- perbedaan error antar kelompok.

Model harus dievaluasi kembali apabila konteks data atau sistem pendidikan berubah.

## Batasan Utama

- Dataset hanya terdiri atas **395 siswa**.
- Data berasal dari dua sekolah di Portugal.
- Konteks dataset berbeda dengan sistem pendidikan Indonesia.
- Model bersifat prediktif dan asosiatif, bukan kausal.
- `G3 = 0` memiliki pola khusus yang perlu dianalisis secara hati-hati.
- Notebook 02 dan pipeline `src/` menggunakan konfigurasi pemodelan yang tidak sepenuhnya identik.
- Clustering bersifat eksploratif dan tidak digunakan sebagai dasar keputusan.
- Performa pada dataset ini tidak menjamin performa yang sama pada sekolah lain.

## Catatan Penggunaan

Repositori ini dibuat sebagai **portofolio dan dokumentasi reprodusibilitas proyek Data Science**.

Alur utama notebook:

```text
Data
  ↓
Notebook 01
Business Understanding
Data Gathering
EDA
Cleaning
  ↓
Notebook 02
Preprocessing
Feature Selection
Modeling
Evaluation
  ↓
Hasil Model
```

Eksplorasi tambahan:

```text
Data
  ↓
Notebook 03
K-Means Clustering
  ↓
Profil Klaster Siswa
```

Pipeline reprodusibilitas:

```text
Data + Config
     ↓
common.py
     ↓
train.py
     ↓
Model + Metrics
     ↓
merge_metrics.py / predict.py
```

Model dan clustering harus dipahami sebagai **alat analisis akademik**, bukan sistem keputusan otomatis.

