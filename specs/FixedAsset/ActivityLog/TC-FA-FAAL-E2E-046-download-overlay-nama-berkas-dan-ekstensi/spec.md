---
id: TC-FA-FAAL-E2E-046-download-overlay-nama-berkas-dan-ekstensi
title: "Download: Overlay Format serta Nama Berkas CSV/XLSX di Kedua Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-161
  - TC-FA-FAAL-162
  - TC-FA-FAAL-163
  - TC-FA-FAAL-164
  - TC-FA-FAAL-165
  - TC-FA-FAAL-170
coverage:
  web: automated
---

# Download: Overlay Format serta Nama Berkas CSV/XLSX di Kedua Tab

## Prerequisites

- Mode: FE+BE (backend nyata; unduhan nyata tanpa intercept).
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka).
- Data Pre-setup: Data Log Tab Session SS-01 sampai SS-11 (#11) dan Tab User Action UA-01 sampai UA-15 (#12), disediakan lewat seed suite. Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE). Data Dinamis: tidak ada.
- Data Filter: kombinasi Filter Action `Delete` dan Object `Audit` di Tab User Action tidak memiliki baris pada data seed (kombinasi yang sama dengan TC-FA-FAAL-184).
- Kemampuan teknis (disediakan tim FE): penangkap unduhan browser yang membaca nama berkas terunduh.
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, pemulihan konfigurasi kolom) mengikuti `suite.md`. Spec ini tidak mengubah state global dan tidak menyimpan konfigurasi kolom.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### Tab Session: overlay format, unduh CSV, dan unduh XLSX

1. Klik icon Download di Tab Session
2. Verifikasi overlay Tab Session memuat tepat `Download as CSV` dan `Download as XLSX`
3. Pilih `Download as CSV`
4. Verifikasi tidak ada toast
5. Verifikasi berkas `Activity-Log-Session.csv` terunduh
6. Klik icon Download
7. Pilih `Download as XLSX`
8. Verifikasi tidak ada toast sukses maupun toast lain
9. Verifikasi berkas `Activity-Log-Session.xlsx` terunduh

### Tab User Action: overlay format, unduh CSV, dan unduh XLSX

10. Klik tab User Action
11. Klik icon Download
12. Verifikasi overlay Tab User Action memuat tepat `Download as CSV` dan `Download as XLSX`
13. Pilih `Download as CSV`
14. Verifikasi tidak ada toast
15. Verifikasi berkas `Activity-Log-User-Action.csv` terunduh
16. Klik icon Download
17. Pilih `Download as XLSX`
18. Verifikasi tidak ada toast sukses maupun toast lain
19. Verifikasi berkas `Activity-Log-User-Action.xlsx` terunduh

### Icon Download pada hasil Filter kosong

20. Terapkan Filter Action `Delete` dan Object `Audit` di Tab User Action
21. Verifikasi icon Download tetap aktif (tidak Disabled)
22. Bersihkan Filter Action dan Object lewat Clear Field

## Notes

- Mode: FE+BE (kelas f hanya untuk isi berkas; spec ini mengasersi nama berkas, ekstensi, dan overlay, yaitu asersi fungsional menurut bagian 3 prinsip 13f).
- Penggabungan alur: overlay TC-FA-FAAL-161 diamati pada langkah 2 dan 12, lalu overlay yang sama dipakai TC-FA-FAAL-162 sampai 165. Langkah 8 dan 9 (Tab Session) serta 18 dan 19 (Tab User Action) adalah pengamatan TC-FA-FAAL-170 (XLSX tanpa toast di kedua tab) sekaligus Expected TC-FA-FAAL-163 dan 165; Expected-nya identik sehingga tidak diulang.
- Urutan asersi pada langkah 4 dan 5, 8 dan 9, 14 dan 15, 18 dan 19: absence toast ditulis segera setelah pemicu (pilihan format) dan sebelum asersi berkas terunduh, sesuai bagian 8b butir 11; pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- Langkah penghubung (S-03): langkah 22 (membersihkan Filter agar tidak terbawa), langkah 10 (pindah tab).
- Temuan untuk QA:
  - TC-FA-FAAL-161 langkah 4 tidak menyebut nilai Filter yang menghasilkan 0 baris; spec memakai Action `Delete` dan Object `Audit` (kombinasi 0 baris dari TC-FA-FAAL-184).
  - TC-FA-FAAL-162 sampai 165 tidak memberi Post Condition; tidak ada yang diasersi.
