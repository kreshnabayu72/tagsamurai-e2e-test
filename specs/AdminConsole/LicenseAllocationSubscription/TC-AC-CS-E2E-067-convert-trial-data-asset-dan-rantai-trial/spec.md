---
id: TC-AC-CS-E2E-067-convert-trial-data-asset-dan-rantai-trial
title: "Convert Trial: Data Asset dan Rantai Trial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-249
  - TC-AC-CS-250
  - TC-AC-CS-251
coverage:
  web: automated
---

# Convert Trial: Data Asset dan Rantai Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Distributor PT Maju Bersama, Eko Saputra (Pre-setup #9), `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_DIST_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Subscription ID dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed A untuk trial dan seed B untuk term paid): Client `PT Sejahtera+{runId}-067` dengan trial Active FAMS plan Enterprise (badge Trial; Subscription ID seed A; Trial Asset Quota 100 dan Trial Concurrent User Quota 5, Plan Owner PT ABC (Principal); padanan Pre-setup #60), Data Asset Client pada produk FAMS sebanyak 37 Asset (padanan #77), dan term paid Active pada Client dan Product yang sama tanpa successor pending sehingga Convert memakai mode Renewal (Subscription ID seed B; padanan #61); Client `Klinik Harapan Bunda+{runId}-067` dengan trial Active SAMS Growth tanpa term paid SAMS (padanan #71). Tanggal acuan uji `19/08/26`.
- Data Dinamis: Hasil Convert hanya mengenai Client seed dan dipulihkan oleh fixture backend pemulihan state (disediakan tim FE/BE) di hook `before` dan sebagai langkah penghubung antar blok TC; seed dihapus di hook `after`. Efeknya (Last Updated dan entri audit trail) dicatat di sini.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (status trial Active bergantung pada hari ini), dipulihkan di hook `after`; membaca daftar Asset Client `PT Sejahtera+{runId}-067` pada produk FAMS (jumlah Asset).

## Test Steps

### TC-AC-CS-249: Data Asset Client tidak disentuh saat Convert

1. Ketik Search `PT Sejahtera+{runId}-067`, tekan Enter, lalu catat jumlah Asset Client `PT Sejahtera+{runId}-067` pada produk FAMS sebagai baseline (37)
2. Klik ikon `⋯` pada baris trial Subscription ID seed A lalu pilih `Convert`
3. Pilih Plan `Enterprise`, isi Duration `1` lalu klik `[Submit]` dan `[Convert]`
4. Tunggu aksi selesai (dialog/modal tertutup)
5. Buka daftar Asset Client `PT Sejahtera+{runId}-067`
6. Verifikasi seluruh 37 Asset tetap ada tanpa dihapus, diarsipkan, atau disalin ulang
7. Buka Detail term paid baru
8. Verifikasi term paid baru memakai data Asset yang sama: daftar Asset Client tetap menampilkan 37 Asset yang sama

### TC-AC-CS-250: Jumlah Asset Client tidak memblokir Convert

9. Pulihkan trial Subscription ID seed A ke Active tanpa successor lewat fixture backend, lalu buka Allocation > Client Subscription tab Current dan ketik Search `PT Sejahtera+{runId}-067`, tekan Enter
10. Buka Detail baris trial Subscription ID seed A
11. Verifikasi baris `Asset` pada tabel License Quota: Total 100, Used 37, Remaining 63
12. Kembali ke List, klik ikon `⋯` pada baris trial lalu pilih `Convert`
13. Pilih Plan `Enterprise`, isi Duration `1` lalu klik `[Submit]` dan `[Convert]`
14. Tunggu aksi selesai (dialog/modal tertutup)
15. Verifikasi Convert diproses dan term paid baru dibuat tanpa diblokir jumlah Asset 37
16. Verifikasi Data Asset Client tetap 37 Asset dan tidak berubah

### TC-AC-CS-251: Rantai trial dan rantai paid terpisah serta Plan Owner term paid adalah aktor Convert

17. Ganti akun: Logout lalu login sebagai Total Control Distributor (`Eko Saputra`)
18. Buka menu Allocation > Client Subscription
19. Ketik Search `Klinik Harapan Bunda+{runId}-067`, tekan Enter
20. Klik ikon `⋯` pada baris trial Active SAMS Growth lalu pilih `Convert`
21. Selesaikan Convert: pilih Plan `Professional`, isi Duration `1` lalu klik `[Submit]` dan `[Convert]`
22. Tunggu aksi selesai (dialog/modal tertutup)
23. Buka Detail term paid baru
24. Verifikasi Previous Subscription term paid "—" dan tidak menunjuk baris trial
25. Verifikasi Plan Owner term paid `PT Maju Bersama (Distributor)` (aktor Convert) dan bukan `CV Karya Mandiri (Partner)`

## Notes

- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); `Tunggu aksi selesai (dialog/modal tertutup)` setelah Convert sebelum berpindah surface (8b.8); pemulihan trial lewat fixture; ganti akun eksplisit (S-07) diikuti `Buka menu Allocation > Client Subscription` sebelum Search (S-14).
- Temuan untuk QA: (1) TC-AC-CS-249 dan TC-AC-CS-250 tidak menyebut layar daftar Asset Client; spec memakai kemampuan baca daftar Asset yang disediakan tim FE/BE. (2) TC-AC-CS-251 langkah 2 ("Selesaikan Convert") tidak menyebut Plan dan Duration; spec memakai Plan `Professional` dan Duration `1`.
