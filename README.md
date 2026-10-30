# Prediksi Dini Nilai Akhir Matematika Siswa Sekolah Menengah melalui Pemodelan Regresi Berbasis Faktor Demografis, Sosial, dan Sekolah
Nama Kelompok: 4 Sehat 5 Enam <br>
Nomor Kelompok: 48 <br>
Anggota Kelompok: <br>
- Tazkya Syakieb Dwiningtyas (123240029)
- Aisyah Yasmine Kirana (123240064)
- Chatarina Giftadiyana (123240183)
- Amalya Kumalasari (123240198)
## Ringkasan
Proyek ini menganalisis dan membangun prototipe model untuk **memprediksi nilai akhir Matematika (`G3`) siswa sekolah menengah secara dini** menggunakan faktor demografis, sosial, keluarga, dan sekolah. Dataset yang digunakan adalah **Student Performance — Mathematics (`student-mat.csv`)** dari UCI Machine Learning Repository.

Fokus proyek mengikuti alur **CRISP-DM**, khususnya **Business Understanding**, **Data Understanding**, **Data Preparation**, pemodelan awal, evaluasi, serta penyusunan artefak yang dapat dijalankan ulang. Nilai `G1` dan `G2` sengaja tidak digunakan sebagai fitur karena baru tersedia setelah proses pembelajaran berjalan dan kurang sesuai untuk skenario prediksi dini.

**Penting:** model pada repositori ini adalah **prototipe akademik untuk penapisan awal**, bukan sistem yang menentukan kelulusan, penempatan kelas, atau keputusan akademik siswa secara otomatis. Prediksi hanya dimaksudkan sebagai sinyal awal bagi guru atau konselor untuk menentukan siswa yang perlu ditinjau lebih lanjut. Dataset hanya berasal dari dua sekolah di Portugal sehingga hasilnya tidak dapat langsung digeneralisasi ke sekolah di Indonesia tanpa validasi lokal.

## Temuan awal dari berkas yang diberikan
- Ukuran dataset: **395 baris × 33 kolom**.
- Variabel target: **`G3`**, nilai akhir Matematika pada skala 0–20.
- Sebanyak **130 siswa (32,9%)** memiliki `G3 < 10`.
- Terdapat **38 siswa (9,6%)** dengan `G3 = 0` yang membentuk pola khusus dan dipertahankan pada analisis utama, kemudian diuji kembali melalui analisis sensitivitas.
- Tidak ditemukan nilai kosong dan tidak ditemukan baris duplikat penuh pada pemeriksaan awal.
- `G1` dan `G2` tidak digunakan sebagai fitur model utama.
- `absences` tidak digunakan pada skenario **prediksi awal tahun**, tetapi disediakan pada skenario tambahan **pertengahan periode** karena waktu ketersediaannya tidak jelas untuk prediksi dini.
- SHA-256 file `student-mat.csv`: `e47f9ee225e1ee6e69b7564e6dac7123e80b8486677fe111f351964cef5dec80`.

Hasil validasi silang yang tersimpan pada repositori menunjukkan bahwa **Random Forest** pada skenario prediksi awal tanpa `absences` memperoleh **RMSE 4,294**, **MAE 3,243**, **R² 0,112**, **recall 0,744**, dan **precision 0,427**. Ketika `absences` digunakan pada skenario pertengahan periode, kinerjanya meningkat menjadi **RMSE 3,848** dan **R² 0,285**. Perbedaan ini harus ditafsirkan dengan hati-hati karena `absences` memiliki hubungan kuat dengan pola pencatatan kelompok `G3 = 0`.

Jalankan notebook dan skrip pada repositori untuk memverifikasi seluruh angka tersebut dari salinan data yang disertakan.

## Peta komponen analisis berdasarkan artefak

Bagian utama proyek disediakan dalam notebook, skrip, konfigurasi, dan keluaran eksperimen berikut.

### 1. Reprodusibilitas Analisis — Notebook 01

**File:** `notebooks/01_reproducibility.ipynb`

Mencakup:
- Pemuatan dan validasi dataset.
- Pemeriksaan ukuran data dan checksum.
- Pemeriksaan variabel target dan fitur yang dikecualikan.
- EDA ringkas yang mendukung keputusan pemodelan.
- Penyiapan preprocessing.
- Evaluasi model baseline, Ridge Regression, dan Random Forest.
- Pemeriksaan hasil skenario utama dan analisis sensitivitas.

Versi notebook yang telah dieksekusi juga tersedia pada:

`notebooks/01_reproducibility.executed.ipynb`

File tersebut dapat digunakan untuk meninjau keluaran terakhir tanpa harus menjalankan ulang seluruh sel terlebih dahulu.

### 2. Data Validation dan Utilitas — `src/common.py`

**File:** `src/common.py`

Mencakup:
- Pembacaan konfigurasi proyek.
- Pemeriksaan lokasi dan format data.
- Verifikasi SHA-256 dataset.
- Fungsi pendukung yang digunakan oleh skrip eksperimen.

### 3. Preprocessing dan Modeling — `src/train.py`

**File:** `src/train.py`

Mencakup:
- Penghapusan `G1` dan `G2` dari fitur prediktor.
- Penghapusan `absences` pada skenario prediksi awal.
- One-hot encoding untuk variabel kategorikal di dalam pipeline.
- Validasi silang **5-fold × 3 pengulangan**.
- Stratifikasi berdasarkan kombinasi status risiko `G3 < 10` dan indikator `G3 = 0`.
- Evaluasi baseline rata-rata, Ridge Regression, dan Random Forest.
- Perhitungan RMSE, MAE, R², recall, dan precision.
- Penyimpanan model serta feature importance.

### 4. Analisis Tiga Skenario

Tiga skenario utama dapat dijalankan secara terpisah:

#### `early_all`

Skenario utama untuk prediksi awal tahun.

- Menggunakan seluruh 395 siswa.
- `G1`, `G2`, dan `absences` tidak digunakan sebagai fitur.
- `G3 = 0` tetap dipertahankan.

#### `midperiod_all`

Skenario tambahan untuk kondisi ketika informasi ketidakhadiran sudah tersedia.

- Menggunakan seluruh 395 siswa.
- `G1` dan `G2` tetap dikeluarkan.
- `absences` digunakan.

#### `early_without_g3_zero`

Analisis sensitivitas untuk melihat kemampuan model ketika observasi `G3 = 0` dikeluarkan.

- Menggunakan 357 siswa.
- `G1`, `G2`, dan `absences` tidak digunakan sebagai fitur.
- Bukan skenario utama, tetapi digunakan untuk menguji sensitivitas hasil.

### 5. Penggabungan Hasil — `src/merge_metrics.py`

**File:** `src/merge_metrics.py`

Menggabungkan hasil ketiga skenario menjadi:

`outputs/metrics.json`

File ini memudahkan perbandingan performa setiap model dan skenario tanpa membuka keluaran eksperimen satu per satu.

### 6. Contoh Inferensi — `src/predict.py`

**File:** `src/predict.py`

Mencakup contoh penggunaan model yang telah disimpan untuk menghasilkan prediksi pada data baru dengan struktur fitur yang sesuai.

**Catatan:** fitur pada data input nyata harus benar-benar tersedia pada waktu prediksi. Skrip ini adalah demonstrasi teknis dan bukan aplikasi produksi.

### Ringkasan cepat

| Komponen | Artefak utama |
|---|---|
| Business/Data Understanding dan pemeriksaan reproducibility | `notebooks/01_reproducibility.ipynb` |
| Data validation dan checksum | `src/common.py` |
| Preprocessing dan Modeling | `src/train.py` |
| Penggabungan metrik | `src/merge_metrics.py` |
| Contoh prediksi | `src/predict.py` |
| Parameter eksperimen | `config.yaml` |
| Hasil eksperimen | `outputs/` |
| Rencana deployment | `deployment_plan.md` |

## Struktur repositori

```text
Lampiran_Portofolio_Reprodusibilitas/
├── README.md
├── requirements.txt
├── config.yaml
├── deployment_plan.md
├── data/
│   └── student-mat.csv
├── notebooks/
│   ├── 01_reproducibility.ipynb
│   └── 01_reproducibility.executed.ipynb
├── src/
│   ├── common.py
│   ├── train.py
│   ├── merge_metrics.py
│   └── predict.py
└── outputs/
    ├── metrics.json
    ├── metrics_early_all.json
    ├── metrics_midperiod_all.json
    ├── metrics_early_without_g3_zero.json
    ├── feature_importance.csv
    ├── model.joblib
    └── predictions_demo.csv
```

## Menjalankan di Mac/Linux/Windows

Disarankan menggunakan **Python 3.11**. Dari direktori proyek:

```bash
python -m venv .venv
```

Aktifkan virtual environment.

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Kemudian instal dependensi:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Untuk membuka notebook:

```bash
jupyter notebook notebooks/01_reproducibility.ipynb
```

Jalankan notebook dari sel pertama sampai terakhir.

## Menjalankan eksperimen dari skrip

### 1. Skenario prediksi awal

```bash
python src/train.py --config config.yaml --scenario early_all
```

### 2. Skenario pertengahan periode

```bash
python src/train.py --config config.yaml --scenario midperiod_all
```

### 3. Analisis sensitivitas tanpa G3 = 0

```bash
python src/train.py --config config.yaml --scenario early_without_g3_zero
```

### 4. Menggabungkan hasil

```bash
python src/merge_metrics.py
```

Hasil akhir dapat diperiksa pada:

```text
outputs/metrics.json
```

## Contoh menjalankan prediksi

Model hasil eksperimen disimpan pada:

```text
outputs/model.joblib
```

Contoh penggunaan:

```bash
python src/predict.py \
  --model outputs/model.joblib \
  --input data/student-mat.csv \
  --sep ";"
```

Pada Windows PowerShell perintah dapat ditulis dalam satu baris:

```powershell
python src/predict.py --model outputs/model.joblib --input data/student-mat.csv --sep ";"
```

Perintah tersebut hanya digunakan untuk demonstrasi pipeline. Untuk penggunaan sebenarnya, input seharusnya berupa data siswa baru dan tidak memuat target `G3` sebagai informasi yang digunakan untuk prediksi.

## Alur analisis

1. Memuat `student-mat.csv` dan memverifikasi ukuran serta checksum dataset.
2. Memisahkan `G3` sebagai target dan mengeluarkan `G1` serta `G2` dari fitur.
3. Membentuk indikator analisis untuk status risiko (`G3 < 10`) dan kelompok `G3 = 0`.
4. Menjalankan preprocessing di dalam pipeline agar transformasi tidak memanfaatkan data pada fold validasi.
5. Melakukan repeated stratified cross-validation sebanyak **5 fold × 3 pengulangan**.
6. Membandingkan baseline rata-rata, Ridge Regression, dan Random Forest.
7. Mengevaluasi RMSE, MAE, R², recall siswa berisiko, dan precision peringatan.
8. Menjalankan skenario utama prediksi awal, skenario pertengahan periode, dan analisis sensitivitas tanpa `G3 = 0`.
9. Menyimpan metrik, feature importance, model, serta contoh keluaran prediksi pada folder `outputs/`.

## Konfigurasi eksperimen

Parameter utama disimpan dalam `config.yaml` agar eksperimen dapat dijalankan ulang tanpa mengubah kode sumber secara langsung.

Konfigurasi utama meliputi:

- `random_seed: 42`
- target: `G3`
- ambang risiko aktual: `G3 < 10`
- ambang peringatan prediksi: prediksi `G3 < 11`
- validasi: 5 fold × 3 pengulangan
- Random Forest: 300 estimator
- fitur yang selalu dikeluarkan: `G1` dan `G2`
- fitur tambahan yang dikeluarkan pada prediksi awal: `absences`

## Data, privasi, dan lisensi

Sumber dataset:

**Cortez, P. (2008). Student Performance. UCI Machine Learning Repository.**  
DOI: https://doi.org/10.24432/C5TG7T

Dataset Student Performance tersedia dengan lisensi **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Penggunaan dan adaptasi diperbolehkan selama atribusi kepada sumber tetap diberikan.

Dataset tidak memuat nama, nomor induk siswa, atau kontak langsung. Namun, beberapa atribut seperti sekolah, usia, jenis kelamin, alamat, pekerjaan orang tua, konsumsi alkohol, kesehatan, dan hubungan romantis merupakan informasi yang perlu diperlakukan secara hati-hati. Data pada proyek ini tidak boleh digabungkan dengan sumber identitas lain untuk mencoba mengidentifikasi individu.

## Batasan utama

- Dataset hanya berisi **395 siswa** dari dua sekolah di Portugal.
- Data berasal dari konteks sekitar tahun ajaran 2005–2006 dan tidak mewakili kondisi sekolah Indonesia saat ini.
- Model bersifat **prediktif dan asosiatif**, bukan kausal.
- `G3 = 0` memiliki pola khusus yang tidak dijelaskan secara eksplisit oleh dokumentasi sumber.
- Waktu ketersediaan `absences` tidak cukup jelas untuk menjadikannya fitur prediksi awal tahun.
- Beberapa fitur demografis dan keluarga dapat bertindak sebagai atribut sensitif atau proksi kondisi sosial.
- Nilai feature importance tidak boleh ditafsirkan sebagai bukti bahwa suatu fitur menyebabkan nilai siswa naik atau turun.
- Model tidak boleh digunakan sebagai satu-satunya dasar untuk mengambil keputusan terhadap siswa.
- Validasi pada data sekolah sasaran wajib dilakukan sebelum penggunaan operasional.

## Rencana deployment

Deployment dirancang secara proporsional karena proyek ini masih berupa prototipe akademik.

Tahap yang direkomendasikan:

1. **Tahap reproducibility/offline** — model dijalankan melalui notebook atau skrip pada data yang telah disiapkan.
2. **Tahap pilot lokal** — pipeline diuji menggunakan data historis sekolah sasaran dan struktur fitur yang benar-benar tersedia pada awal tahun ajaran.
3. **Tahap validasi** — kinerja, recall siswa berisiko, precision, dan galat antarkelompok diperiksa sebelum digunakan oleh pengguna akhir.
4. **Tahap penggunaan terbatas** — bila hasil validasi memadai, model dapat ditempatkan sebagai proses batch internal yang menghasilkan daftar siswa untuk ditinjau oleh guru atau konselor.
5. **Human-in-the-loop** — seluruh keluaran tetap memerlukan pemeriksaan manusia dan tidak digunakan sebagai keputusan otomatis.
6. **Monitoring** — performa model, perubahan distribusi data, serta perbedaan galat antar kelompok perlu diperiksa secara berkala.

Rincian deployment tersedia pada `deployment_plan.md`.

## Catatan penggunaan

Repositori ini dibuat untuk **portofolio dan reprodusibilitas tugas Data Science**. Artefak di dalamnya memungkinkan pemeriksa menjalankan kembali alur eksperimen, memeriksa konfigurasi, membandingkan skenario, dan memverifikasi keluaran yang dilaporkan.

Hasil model harus dipahami sebagai **alat penapisan kasar untuk eksperimen akademik**, bukan sebagai pengganti penilaian guru, konselor, atau kebijakan sekolah.
