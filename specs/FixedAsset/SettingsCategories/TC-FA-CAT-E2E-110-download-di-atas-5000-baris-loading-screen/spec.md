---
id: TC-FA-CAT-E2E-110-download-di-atas-5000-baris-loading-screen
title: "Download di Atas 5.000 Baris: Loading Screen Tanpa Job Background"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-375
coverage:
  web: automated
---

# Download di Atas 5.000 Baris: Loading Screen Tanpa Job Background

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatBig (Pre-setup #37), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Kelas harness: volume data (kelas e). Data Pre-setup #37 (CatBig, plan Enterprise, Master Data Count Limit default): 5.001 kategori L1, dibaca saja dan tidak diubah. Data disediakan tim FE/BE lewat seed API (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Kemampuan membaca jumlah baris berkas CSV yang terunduh disediakan tim FE.
- Kemampuan membaca notifikasi in-app dan jendela 24 jam (untuk asersi tidak ada job background) disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-375: Download di atas 5.000 baris

1. Catat jumlah notifikasi in-app awal (baseline)
2. Klik Download > `Download as CSV`
3. Verifikasi loading screen tampil
4. Verifikasi tidak ada job background
5. Verifikasi tidak ada jendela 24 jam
6. Verifikasi berkas langsung terunduh memuat seluruh 5.001 baris
7. Verifikasi jumlah notifikasi in-app sama dengan baseline langkah 1

## Notes

- Langkah penghubung (S-03): langkah 1 (mencatat baseline notifikasi in-app).
- Asersi loading screen (langkah 3) dan absence job background serta jendela 24 jam (langkah 4 dan 5) diletakkan segera setelah pemicu dan sebelum asersi berkas (butir 8b.11); berkas terunduh pada langkah 6 menjadi anchor positif bahwa respons sudah diproses.
- Temuan untuk QA:
  - TC-375 butir b ("tidak ada job background, tidak ada notifikasi in-app, tidak ada jendela 24 jam") tidak menyebut cara mengamati job background; spec memakai baseline notifikasi in-app dan kemampuan baca yang disediakan tim FE.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
