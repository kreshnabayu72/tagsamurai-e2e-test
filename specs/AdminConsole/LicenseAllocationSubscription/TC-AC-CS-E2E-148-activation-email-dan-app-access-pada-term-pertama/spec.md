---
id: TC-AC-CS-E2E-148-activation-email-dan-app-access-pada-term-pertama
title: "Add: Activation Email dan App Access Hanya pada Term Pertama Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-156
coverage:
  web: automated
---

# Add: Activation Email dan App Access Hanya pada Term Pertama Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`, beserta dua term yang dibuat spec): Client `Client Tanpa Subscription+{runId}-148` (padanan Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term dan tanpa trial) dengan Default User beralamat email yang dibaca lewat `Fixture.license-allocation-subscription`; layanan email uji (mail-catcher) aktif.
- Jam (CLK): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before`, lalu diatur absolut ke `15/09/26` pada langkah 11 (kemampuan fixture waktu dan pemicu job Scheduled Flip disediakan tim FE/BE; tidak ada endpoint yang dinamai TC, PRD, atau LLD). Jam dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan mail-catcher untuk membaca jumlah email per alamat (baseline sebelum aksi, R-11); pembacaan status App Access Client; pemicu dan poll job Scheduled Flip hingga selesai (batas tunggu 2 menit dengan muat ulang tiap 5 detik).

## Test Steps

### TC-AC-CS-156: Activation Email dan App Access hanya pada term pertama Client yang menjadi Active

1. Catat baseline jumlah email ke alamat Default User Client `Client Tanpa Subscription+{runId}-148` lewat mail-catcher
2. Klik `[+ Subscription]`
3. Pilih Client `Client Tanpa Subscription+{runId}-148`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `15/09/26`
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, subscription has been added." muncul
6. Ketik Search `Client Tanpa Subscription+{runId}-148`, tekan Enter
7. Verifikasi baris SAMS berstatus Pending
8. Verifikasi Activation Email belum dikirim (jumlah email ke alamat Default User sama dengan baseline)
9. Verifikasi App Access belum dikirim (dibaca lewat fixture BE)
10. Klik `(←)` pada kotak Search
11. Atur jam server dan jam browser absolut ke `15/09/26`, lalu picu job Scheduled Flip hingga selesai
12. Ketik Search `Client Tanpa Subscription+{runId}-148`, tekan Enter
13. Verifikasi baris SAMS berstatus Active
14. Verifikasi Activation Email terkirim satu kali (jumlah email ke alamat Default User = baseline + 1)
15. Verifikasi App Access terkirim satu kali (dibaca lewat fixture BE)
16. Klik `(←)` pada kotak Search
17. Klik `[+ Subscription]`
18. Pilih Client `Client Tanpa Subscription+{runId}-148`, Product `FAMS`, Plan `Growth`, Duration `1`, Start Date `15/09/26`
19. Klik `[Submit]`
20. Verifikasi toast sukses "Success, subscription has been added." muncul
21. Ketik Search `Client Tanpa Subscription+{runId}-148`, tekan Enter
22. Verifikasi baris FAMS berstatus Active
23. Verifikasi Activation Email tidak dikirim lagi (jumlah email ke alamat Default User tetap baseline + 1)

## Notes

- Spec memuat satu TC dengan harness jam dan job (kelas d: harness eksternal) sebagai pemicu kondisi yang diuji, bukan objek uji (P-5); asersi email dan App Access adalah Expected TC.
- Langkah penghubung (S-03): baseline email (langkah 1), Search untuk menemukan baris target (R-16; langkah 6, 12, 21), `(←)` pada kotak Search (langkah 10, 16), dan pengaturan jam serta pemicu job (langkah 11).
- Tahap TC-AC-CS-156 Langkah 4 ("Start Date hari ini") ditulis Start Date `15/09/26` yang sama dengan hari berjalan setelah jam diatur pada langkah 11.
- Pada Expected a, absence email diperkuat anchor positif toast sukses dan baris Pending (langkah 5 dan 7); absence pada Expected c diperkuat toast dan baris Active (langkah 20 dan 22).
- Temuan untuk QA:
  - TC-AC-CS-156 Langkah 3 menyebut "tunggu scheduled flip pada `15/09/26`" tanpa menyatakan cara memicunya; ditulis sebagai kemampuan "disediakan tim FE/BE" (jam dan job).
  - TC-AC-CS-156 Langkah 4 menyebut "term FAMS kedua" tanpa menyebut Plan dan Duration; spec memakai Plan `Growth` dan Duration `1`.
  - TC-AC-CS-156 Expected b "App Access terkirim" tidak menyebut cara cek di UI; spec memakai pembacaan lewat fixture BE.
