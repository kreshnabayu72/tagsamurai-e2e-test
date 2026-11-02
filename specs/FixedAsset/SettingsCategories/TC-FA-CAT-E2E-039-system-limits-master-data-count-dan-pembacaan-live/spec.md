---
id: TC-FA-CAT-E2E-039-system-limits-master-data-count-dan-pembacaan-live
title: "System Limits: Dialog D-03 Master Data Count Limit, Plan Enterprise, dan Pembacaan Live"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-126
  - TC-FA-CAT-128
  - TC-FA-CAT-489
coverage:
  web: automated
---

# System Limits: Dialog D-03 Master Data Count Limit, Plan Enterprise, dan Pembacaan Live

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatCountLimit (Pre-setup #29, plan Enterprise, Master Data Count Limit 1.000 dengan 1.000 kategori L1 `Limit 0001` sampai `Limit 1000`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain).
- Pelaku kedua: Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) untuk mengubah Master Data Count Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- State global yang diubah: Master Data Count Limit CatCountLimit (1.000, dinaikkan ke 2.000 di langkah 9 dan 16, dikembalikan ke 1.000 di langkah 13). Hook `after` memulihkan Master Data Count Limit CatCountLimit ke 1.000. Seed 1.000 kategori dan pemulihan disediakan tim FE/BE (butir hook suite di `suite.md`). Suite berjalan serial.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-126: Master Data Count Limit tercapai, dialog D-03

1. Klik `[+] Category` pada sidebar
2. Verifikasi dialog 🔒 `Cannot Add Category` dengan body `You've reached the platform limit of 1000 records. Contact support if you need a higher limit.` dan tombol `[OK]` tampil
3. Verifikasi dialog tidak memiliki tombol Upgrade
4. Verifikasi popup New Category tidak terbuka
5. Klik `[OK]`

### TC-FA-CAT-128: Plan Enterprise tidak diblok cap plan, tetap tunduk batas platform

6. Klik `[+] Category` pada sidebar
7. Verifikasi dialog yang tampil adalah D-03 (batas platform), bukan D-01 (cap plan)
8. Klik `[OK]`
9. Principal Automation menaikkan Master Data Count Limit CatCountLimit dari 1.000 menjadi 2.000 hingga tersimpan
10. Klik `[+] Category` pada sidebar
11. Verifikasi popup New Category terbuka tanpa dialog
12. Klik `✕` pada popup

### TC-FA-CAT-489: System Limits dibaca live

13. Principal Automation mengembalikan Master Data Count Limit CatCountLimit menjadi 1.000 hingga tersimpan
14. Klik menu Fixed Asset > Settings > Categories untuk membuka ulang halaman
15. Verifikasi Breadcrumb halaman Categories tampil
16. Principal Automation menaikkan Master Data Count Limit CatCountLimit dari 1.000 menjadi 2.000 hingga tersimpan
17. Tunggu aksi selesai
18. Klik `[+] Category` pada sidebar tanpa memuat ulang halaman
19. Verifikasi popup New Category terbuka tanpa dialog D-03
20. Klik `✕` pada popup

## Notes

- Kelas e (volume data): TC-126, 128, 489 bergantung pada 1.000 kategori seed.
- Pelaku kedua lewat sesi API bukan konteks kedua (tanpa `P-2`). Langkah 9, 13, 16 ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (S-03): langkah 5, 8, 12, 20 (menutup dialog/popup), 13 (pemulihan limit), 14 (membuka ulang halaman; Breadcrumb sebagai anchor), 17 (tunggu aksi selesai sebelum aksi aktor, 8b butir 8).
- Temuan untuk QA:
  - TC-128 Expected b ("Setelah Principal menaikkan limit") tidak punya langkah di bagian langkah TC; spec menambahkan langkah 9 sampai 11 sebagai aksi Principal dan observasi popup.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
