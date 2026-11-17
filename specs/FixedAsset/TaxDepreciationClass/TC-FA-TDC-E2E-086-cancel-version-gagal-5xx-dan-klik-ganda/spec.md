---
id: TC-FA-TDC-E2E-086-cancel-version-gagal-5xx-dan-klik-ganda
title: "Cancel Version: Gagal 5xx Mempertahankan D-10 dan Klik Ganda Hanya Membatalkan Satu Kali"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-305
  - TC-FA-TDC-312
sourceRules: ["T-07", "D-10", "R-07", "ST-13"]
smoke: []
dependsOn: []
trace:
  "T-07": [6, 13]
  "D-10": 7
  "R-07": 7
  "ST-13": [8, 14]
coverage:
  web: automated
---

# Cancel Version: Gagal 5xx Mempertahankan D-10 dan Klik Ganda Hanya Membatalkan Satu Kali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`): class `KHS-C1-{runId}-086` (Class Name `Kelompok cancel uji`), Active, Used By 0, versi Current tanpa Effective From (Useful Life 8, Straight Line dan Declining Balance) dan satu versi Scheduled Effective From Jan 2027 (Useful Life 10, Straight Line dan Declining Balance). Tabel berisi tujuh class seed bawaan dan class itu; baris dibuka tanpa Search.
- Kemampuan intercept jaringan (`Spectra.intercept()`) di atas backend nyata (Mode FE+BE karena asersi memuat state server) untuk mengembalikan 500 pada endpoint pembatalan versi Scheduled (TC-305). Nama endpoint tidak tertulis di TC dan disediakan tim FE/BE (S-13). Intercept dilepas segera setelah pemicu selesai (langkah 5).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-305: Cancel version gagal 5xx

1. Klik link Class Code `KHS-C1-{runId}-086` pada tabel
2. Klik `[Cancel scheduled version]` pada Alert
3. Atur endpoint pembatalan versi mengembalikan 500 (intercept jaringan)
4. Klik `[Cancel version]`
5. Lepas intercept endpoint pembatalan versi
6. Verifikasi toast error "Error, failed to cancel scheduled version."
7. Verifikasi dialog D-10 tetap terbuka
8. Verifikasi tombol `[Cancel version]` enabled kembali
9. Klik `[Back]`
10. Dismiss toast error

### TC-FA-TDC-312: Klik ganda cepat pada Cancel version hanya membatalkan satu kali

11. Klik `[Cancel scheduled version]` pada Alert
12. Klik `[Cancel version]` dua kali dengan cepat
13. Verifikasi satu toast sukses "Success, scheduled version has been cancelled."
14. Verifikasi tidak ada toast error tambahan
15. Klik `[×]` pada header Drawer

## Notes

- P-5 (butir b): TC-305 adalah satu TC objek-uji ringan kelas b (satu kegagalan 5xx pada pembatalan versi) pada permukaan yang sama dengan TC-312 (Cancel version D-10); tanpa harness eksternal dan tanpa state berat sendiri.
- Langkah penghubung (S-03): langkah 9 (`[Back]` menutup D-10 yang tetap terbuka; Drawer tetap berisi class yang sama untuk TC-312), langkah 10 (R-12: toast error bersifat persisten, jadi di-dismiss sebelum hitungan toast TC-312), langkah 15 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Intercept dilepas di langkah 5 segera setelah pemicu (S-09); langkah 6 sampai 8 mengasersi hasil respons yang sudah diproses.
- Langkah 14 (absence toast error) berpegang pada anchor positif langkah 13 (toast sukses); jendela waktu antara dua toast tidak ditentukan TC.
- Post Condition TC-305 (versi tetap Scheduled; tidak ada entri log) dan TC-312 (tepat satu entri L-09) tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan L-09 ada di spec pencatatan log.
- Temuan untuk QA:
  - Post Condition TC-305 dan TC-312 tanpa langkah observasi di TC.
  - TC-305 memakai versi Jan 2027 yang tetap Scheduled setelah gagal; TC-312 pada TC sumber memulai dari class dan Drawer baru, sedangkan spec melanjutkan class yang sama dengan Drawer yang masih terbuka (versi tetap Scheduled setelah kegagalan).
  - Class Code `KHS-C1` ditulis tanpa suffix di TC; spec memakai `-{runId}-086` (S-12).
  - Email akun Total Control tidak tertulis di TC.
