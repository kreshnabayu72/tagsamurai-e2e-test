---
id: TC-AC-CS-E2E-031-form-add-validasi-duration
title: "Form Add: Validasi Duration"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-117
  - TC-AC-CS-118
  - TC-AC-CS-119
  - TC-AC-CS-120
coverage:
  web: automated
---

# Form Add: Validasi Duration

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-031` (padanan Pre-setup #48: tanpa term dan tanpa trial). Tidak ada Submit sukses pada spec ini.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah term Client seed lewat fixture BE.
- Data uji input Duration: kosong, `0`, `1`, `abc`, `1.5`.

## Test Steps

### TC-AC-CS-117: Validasi Duration kosong varian Add

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription+{runId}-031`, Product `SAMS`, Plan `Growth`, kosongkan Duration, isi Start Date `19/08/26`
3. Klik `[Submit]`
4. Verifikasi error inline "Duration must not be empty"
5. Verifikasi modal tetap terbuka

### TC-AC-CS-118: Validasi Duration kurang dari 1 tahun varian Add

6. Isi Duration `0`
7. Klik `[Submit]`
8. Verifikasi error inline "Duration must be at least 1 year"
9. Verifikasi jumlah term Client `Client Tanpa Subscription+{runId}-031` tetap 0 (dibaca lewat fixture BE)

### TC-AC-CS-119: Duration batas bawah 1 tahun diterima varian Add

10. Isi Duration `1`
11. Amati End Date pada Preview term baru
12. Verifikasi tidak ada error pada Duration
13. Verifikasi Preview term baru menampilkan tanggal akhir `18/08/27` (Start Date + 1 tahun - 1 hari, End Date inklusif)

### TC-AC-CS-120: Field Duration hanya menerima digit

14. Klik `[Clear Field]`
15. Ketik `abc` pada field Duration
16. Verifikasi huruf tidak masuk ke field Duration
17. Ketik `1.5` pada field Duration
18. Verifikasi nilai desimal tidak diterima sehingga Duration tetap bilangan bulat tahun
19. Klik `[Clear Field]` sehingga semua field kembali ke nilai awal
20. Klik `[✕]` pada header modal

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Form dibuka sekali untuk keempat TC (kasus tanpa Submit sukses memakai satu pembukaan dengan field diganti di antara kasus).
- Langkah penghubung (S-03): `[Clear Field]` antar kasus (langkah 14), mengganti isi field Duration (langkah 6, 10), dan `[Clear Field]` dan `[✕]` pada langkah 19 dan 20 (form kembali ke nilai awal sehingga clean dan tidak ada dialog Unsaved Changes).
- Temuan untuk QA:
  - TC-AC-CS-120 tidak menyatakan nilai Duration setelah mengetik `abc` dan `1.5` (kosong, `1`, atau `15`); spec hanya mengasersi Expected a dan b dan menutup form lewat `[Clear Field]` agar deterministik.
  - TC-AC-CS-119 Langkah 2 mengisi Start Date `19/08/26` dan Duration `1`; spec mengisi Start Date di langkah 2 TC-AC-CS-117 sehingga nilainya terbawa.
