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

Repositori saat ini memuat data mentah, notebook untuk **Business Understanding, Data Gathering, EDA, dan Cleaning**, serta skrip pendukung untuk validasi data, training model, penggabungan metrik, dan inferensi.

Nilai `G1` dan `G2` tidak digunakan sebagai fitur pada rancangan prediksi dini karena keduanya merupakan nilai periode sebelumnya. Pada pipeline di folder `src/`, `absences` juga dapat dikeluarkan pada skenario prediksi awal tahun.

**Penting:** model pada proyek ini merupakan prototipe akademik. Hasil prediksi tidak dimaksudkan sebagai keputusan otomatis mengenai kelulusan, kenaikan kelas, atau perlakuan terhadap siswa. Hasil model hanya dapat diposisikan sebagai alat bantu penapisan awal yang tetap memerlukan peninjauan manusia.

## Dataset

Dataset utama berada pada:

```text
data/raw/student-mat.csv
```

Dataset memuat:

- **395 baris** data siswa.
- **33 variabel**.
- Target `G3`, yaitu nilai akhir Matematika pada skala 0–20.
- Variabel demografis, keluarga, aktivitas, dukungan sekolah, perilaku, kehadiran, dan nilai akademik.

Sumber dataset:

> Cortez, P. (2008). *Student Performance*. UCI Machine Learning Repository.  
> https://doi.org/10.24432/C5TG7T

Dataset Student Performance menggunakan lisensi **CC BY 4.0**.

## Temuan Awal

Berdasarkan pemeriksaan pada notebook yang tersedia:

- Dataset berhasil dibaca dengan ukuran **395 × 33**.
- Tidak ditemukan missing value pada pemeriksaan awal.
- Tidak ditemukan baris duplikat penuh.
- Target `G3` berada pada rentang yang valid 0–20.
- Terdapat **15 kandidat outlier** pada `absences` berdasarkan aturan IQR.
- Nilai ekstrem `absences` tidak langsung dihapus karena masih dapat merupakan observasi yang valid.
- `failures` menunjukkan hubungan negatif yang relatif paling kuat terhadap `G3` di antara variabel numerik/ordinal yang diperiksa pada notebook.
- Hubungan antarvariabel pada tahap EDA diperlakukan sebagai hubungan asosiatif, bukan hubungan sebab-akibat.

## Struktur Repositori

Struktur utama yang digunakan pada proyek:

```text
48_IF-E_4-Sehat-5-Enam/
├── README.md
├── requirements.txt
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
└── laporan/
    └── berkas dokumentasi/laporan proyek
```

Folder `laporan/` digunakan untuk menyimpan dokumentasi laporan proyek. Notebook dan kode utama tidak bergantung langsung pada berkas di folder tersebut.

## Peta Komponen Proyek

| Komponen | File utama |
|---|---|---|
| Business Understanding | `notebooks/01_business_data_understanding.ipynb` | 
| Data Gathering | `notebooks/01_business_data_understanding.ipynb` | 
| Data Understanding / EDA | `notebooks/01_business_data_understanding.ipynb` | 
| Cleaning | `notebooks/01_business_data_understanding.ipynb` | 
| Dataset mentah | `data/raw/student-mat.csv` | 
| Validasi data dan checksum | `src/common.py` |
| Training model | `src/train.py` | 
| Penggabungan metrik | `src/merge_metrics.py` | 
| Inferensi | `src/predict.py` | 
| Dependensi Python | `requirements.txt` | 
| Konfigurasi eksperimen | `config.yaml` | 
| Artefak model/hasil | `outputs/` | 

## 1. Notebook Business Understanding, Data Gathering, EDA, dan Cleaning

**File:**

```text
notebooks/01_business_data_understanding.ipynb
```

Notebook ini menjadi artefak analisis utama yang saat ini dapat ditinjau langsung.

Isi notebook mencakup:

- latar belakang proyek;
- rumusan masalah;
- tujuan dan metrik;
- batasan dan aspek etika;
- sumber dataset UCI;
- pemuatan `student-mat.csv`;
- pemeriksaan ukuran, nama kolom, dan tipe data;
- data dictionary;
- pemeriksaan kualitas data;
- analisis distribusi target `G3`;
- EDA variabel numerik dan kategorikal;
- pemeriksaan korelasi;
- pemeriksaan missing value dan duplikasi;
- cleaning target;
- pemeriksaan kandidat outlier pada `absences`.

Notebook menggunakan path proyek:

```text
data/raw/student-mat.csv
```

Jika dataset belum tersedia, kode notebook memiliki mekanisme untuk mencoba mengunduh arsip Student Performance dari UCI dan menyimpan `student-mat.csv` ke `data/raw/`.

### Catatan

Notebook saat ini berhenti pada tahap **Cleaning dan pemeriksaan outlier**. Walaupun beberapa kelas model sudah diimpor pada bagian awal notebook, training dan evaluasi model belum dijalankan di notebook tersebut.

Dengan demikian, pemodelan pada kondisi repo saat ini berada pada jalur terpisah melalui `src/train.py`.

## 2. Validasi Data — `src/common.py`

File:

```text
src/common.py
```

Fungsi utamanya adalah:

- membaca konfigurasi YAML;
- menyelesaikan path relatif;
- menghitung SHA-256 dataset;
- membandingkan checksum dataset;
- memeriksa jumlah baris dan kolom.

`common.py` digunakan oleh `src/train.py`.

### Ketergantungan

File ini membutuhkan:

```text
PyYAML
pandas
```

`pandas` sudah tersedia di `requirements.txt`, tetapi **PyYAML belum tercantum**.

## 3. Training Model — `src/train.py`

File:

```text
src/train.py
```

Skrip ini menyediakan pipeline pemodelan yang lebih lengkap dibanding notebook saat ini.

Model yang digunakan pada skrip:

1. `DummyRegressor` sebagai baseline rata-rata.
2. `Ridge Regression`.
3. `RandomForestRegressor`.

Preprocessing:

- fitur kategorikal menggunakan `OneHotEncoder`;
- fitur numerik menggunakan `StandardScaler`;
- seluruh preprocessing ditempatkan di dalam `Pipeline`.

Evaluasi menggunakan:

- RMSE;
- MAE;
- R²;
- recall siswa berisiko;
- precision peringatan.

Skrip menyediakan tiga skenario:

### `early_all`

Prediksi awal menggunakan seluruh observasi.

- `G1` dan `G2` dikeluarkan.
- `absences` dikeluarkan.
- observasi `G3 = 0` dipertahankan.

### `midperiod_all`

Skenario ketika informasi kehadiran sudah tersedia.

- `G1` dan `G2` dikeluarkan.
- `absences` digunakan.
- observasi `G3 = 0` dipertahankan.

### `early_without_g3_zero`

Analisis sensitivitas.

- `G1` dan `G2` dikeluarkan.
- `absences` dikeluarkan.
- observasi dengan `G3 = 0` dikeluarkan.

Validasi dilakukan menggunakan `RepeatedStratifiedKFold`. Stratifikasi dibentuk dari kombinasi status risiko `G3 < threshold` dan indikator `G3 = 0`.

### Ketergantungan terhadap file lain

`train.py` menggunakan:

```text
src/common.py
config.yaml
data/raw/student-mat.csv
```

Skrip juga membutuhkan paket:

```text
joblib
PyYAML
```

Pada kondisi repo saat ini, `config.yaml` belum tersedia di root dan `joblib` serta `PyYAML` belum tercantum pada `requirements.txt`.

Karena itu, **pipeline `src/train.py` belum dapat dianggap sepenuhnya reproducible dari clone bersih tanpa melengkapi komponen tersebut terlebih dahulu**.

## 4. Penggabungan Metrik — `src/merge_metrics.py`

File:

```text
src/merge_metrics.py
```

Skrip ini menggabungkan tiga file hasil:

```text
outputs/metrics_early_all.json
outputs/metrics_midperiod_all.json
outputs/metrics_early_without_g3_zero.json
```

menjadi:

```text
outputs/metrics.json
```

Dengan demikian, `merge_metrics.py` bergantung langsung pada keberhasilan tiga proses training sebelumnya.

Jika salah satu file metrik belum tersedia, skrip akan menghentikan proses dengan `FileNotFoundError`.

## 5. Inferensi — `src/predict.py`

File:

```text
src/predict.py
```

Skrip digunakan untuk menghasilkan prediksi `G3` pada data baru menggunakan model yang telah disimpan.

Secara default skrip mengharapkan:

```text
outputs/model.joblib
```

Output prediksi berisi tambahan:

- `predicted_G3`;
- `warning_flag`.

`warning_flag` bernilai benar ketika prediksi berada di bawah ambang peringatan.

### Ketergantungan

`predict.py` bergantung pada artefak model yang dihasilkan oleh `train.py`.

Alurnya adalah:

```text
train.py
   ↓
outputs/model.joblib
   ↓
predict.py
   ↓
outputs/predictions.csv
```

Karena artefak `model.joblib` belum tersedia di root repo saat ini, inferensi baru dapat dilakukan setelah pipeline training berhasil dijalankan.

## Keterkaitan Antarfile

Alur konseptual repositori saat ini adalah:

```text
data/raw/student-mat.csv
        │
        ├───────────────→ notebooks/01_business_data_understanding.ipynb
        │                    │
        │                    └── Business Understanding
        │                        Data Gathering
        │                        EDA
        │                        Cleaning
        │
        └──→ config.yaml ──→ src/common.py
                              │
                              ↓
                         src/train.py
                              │
              ┌───────────────┼────────────────┐
              ↓               ↓                ↓
       metrics_early    metrics_midperiod   metrics_without_zero
              │               │                │
              └───────────────┼────────────────┘
                              ↓
                   src/merge_metrics.py
                              ↓
                      outputs/metrics.json

                         src/train.py
                              ↓
                     outputs/model.joblib
                              ↓
                       src/predict.py
                              ↓
                  outputs/predictions.csv
```

Bagian kiri, yaitu notebook, sudah dapat digunakan untuk analisis data awal. Bagian kanan, yaitu pipeline skrip, secara desain saling berkaitan tetapi saat ini masih memerlukan `config.yaml` dan dependensi tambahan.

## Hubungan Notebook dan Skrip

Notebook dan skrip membahas proyek serta dataset yang sama, tetapi keduanya **belum merupakan satu pipeline yang sepenuhnya terintegrasi**.

Perbedaannya:

| Aspek | Notebook 01 | `src/train.py` |
|---|---|---|
| Dataset | `data/raw/student-mat.csv` | Ditentukan melalui `config.yaml` |
| Fokus | Business Understanding, EDA, Cleaning | Modeling dan evaluasi |
| Baseline | Dicantumkan pada rencana notebook | `DummyRegressor` |
| Model linear | Notebook menyebut `LinearRegression` | Menggunakan `Ridge` |
| Random Forest | Diimpor, belum dilatih di notebook | Digunakan |
| Validasi | Belum masuk tahap modeling | Repeated Stratified K-Fold |
| Output model | Tidak ada | Dirancang menghasilkan `model.joblib` |

Karena itu, README ini tidak menyatakan bahwa hasil modeling dari `src/train.py` sudah direproduksi oleh notebook.

## Menjalankan Notebook

Disarankan menggunakan Python 3.10–3.12.

Clone repositori:

```bash
git clone https://github.com/chtrn/48_IF-E_4-Sehat-5-Enam.git
cd 48_IF-E_4-Sehat-5-Enam
```

Buat virtual environment:

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Instal dependensi:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Jalankan Jupyter:

```bash
jupyter lab
```

Kemudian buka:

```text
notebooks/01_business_data_understanding.ipynb
```

dan jalankan sel dari atas ke bawah.

## Status Reprodusibilitas Saat Ini

### Sudah dapat dijalankan

Notebook:

```text
notebooks/01_business_data_understanding.ipynb
```

beserta dataset:

```text
data/raw/student-mat.csv
```

sudah saling terhubung melalui path relatif proyek.

### Belum lengkap untuk pipeline skrip

Agar `src/train.py`, `src/merge_metrics.py`, dan `src/predict.py` dapat membentuk alur end-to-end dari clone bersih, repo masih perlu melengkapi:

1. `config.yaml`;
2. `joblib` pada `requirements.txt`;
3. `PyYAML` pada `requirements.txt`;
4. folder `outputs/` akan dihasilkan setelah training, sehingga tidak harus disimpan sejak awal;
5. model dan file metrik harus dihasilkan ulang sebelum `predict.py` dan `merge_metrics.py` digunakan.

## Dependensi

Isi `requirements.txt` saat ini:

```text
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
scikit-learn>=1.3
jupyterlab>=4.0
notebook>=7.0
```

Untuk menjalankan seluruh kode pada folder `src/`, tambahkan:

```text
joblib
PyYAML
```

## Data, Privasi, dan Etika

Dataset tidak memuat nama atau identitas langsung siswa, tetapi tetap mengandung atribut demografis, keluarga, kesehatan, konsumsi alkohol, dan hubungan pribadi.

Karena itu:

- data tidak sebaiknya digabungkan dengan sumber identitas lain;
- hasil model tidak digunakan untuk memberi stigma pada siswa;
- prediksi tidak menggantikan penilaian guru atau konselor;
- feature importance tidak boleh dibaca sebagai hubungan sebab-akibat;
- generalisasi ke sekolah di Indonesia memerlukan validasi menggunakan data lokal.

## Rencana Deployment

Deployment yang proporsional untuk konteks proyek ini adalah **batch/offline internal**, bukan aplikasi keputusan otomatis.

Tahapan yang disarankan:

1. **Reproducibility lokal**  
   Pastikan notebook dan pipeline training dapat dijalankan dari clone bersih.

2. **Validasi pada data sekolah sasaran**  
   Model perlu diuji menggunakan data lokal dan hanya menggunakan atribut yang benar-benar tersedia pada saat prediksi.

3. **Batch prediction**  
   Data siswa diproses secara periodik untuk menghasilkan daftar prioritas peninjauan.

4. **Human-in-the-loop**  
   Guru atau konselor meninjau hasil sebelum tindakan apa pun dilakukan.

5. **Monitoring**  
   Pantau RMSE, MAE, R², recall, precision, perubahan distribusi data, serta perbedaan error antar kelompok.

Model tidak direkomendasikan untuk deployment operasional sebelum validasi lokal dilakukan.

## Batasan Utama

- Dataset hanya terdiri dari 395 siswa.
- Data berasal dari dua sekolah di Portugal.
- Konteks dataset tidak otomatis mewakili sekolah di Indonesia.
- Data bersifat observasional sehingga hubungan yang ditemukan tidak membuktikan kausalitas.
- `G3 = 0` memiliki pola khusus yang perlu diperiksa lebih lanjut.
- Waktu ketersediaan `absences` harus dipastikan jika model digunakan untuk prediksi awal.
- Notebook dan pipeline `src/` belum sepenuhnya terintegrasi.
- Pipeline training belum dapat dijalankan dari clone bersih sebelum `config.yaml`, `joblib`, dan `PyYAML` dilengkapi.

## Catatan Repositori

README ini disusun mengikuti file yang benar-benar dapat diverifikasi pada repositori saat ini. File atau output yang belum tersedia di GitHub tidak dicantumkan sebagai artefak yang sudah ada.

Setelah `config.yaml` dan dependensi pipeline dilengkapi, dokumentasi dapat diperbarui kembali dengan hasil training, metrik final, feature importance, dan contoh inferensi yang benar-benar dihasilkan dari repositori.
