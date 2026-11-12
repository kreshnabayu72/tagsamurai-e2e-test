---
id: TC-AC-LA-E2E-112-download-list-volume-lebih-5000-baris
title: "Download List: Volume Lebih dari 5.000 Baris"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-348
coverage:
  web: automated
---

# Download List: Volume Lebih dari 5.000 Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data Dinamis (kelas volume data): 5.100 baris alokasi pada scope Total Control Principal #1, di-seed lewat API di hook `before`. Hook `after` menghapus data seed itu lewat kemampuan pembersihan yang disediakan tim FE (modul tidak punya aksi hapus alokasi di UI; pemulihan juga dijamin baseline automation, Catatan TC).
- Kemampuan teknis: membaca berkas hasil unduhan peramban (nama berkas dan jumlah baris), dan membaca ada tidaknya job latar atas aksi Download, disediakan tim FE tanpa endpoint karangan (S-13). Berkas unduhan dihapus di hook `after`.
- Jendela absence notifikasi in-app: pilihan spec (bukan nilai TC atau PRD), langkah penghubung "Tunggu 5 detik tanpa memuat ulang halaman" sebelum asersi absence notifikasi (konvensi bagian 6).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-348: Download dengan lebih dari 5.000 baris

1. Download as CSV
2. Verifikasi loading screen tampil sampai berkas siap
3. Verifikasi berkas CSV langsung terunduh
4. Verifikasi berkas memuat seluruh baris (jumlah baris sama dengan N tab Current: 5.100 baris seed ditambah baris tab Current seed #54)
5. Verifikasi tidak ada job background
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Verifikasi tidak ada notifikasi in-app

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Langkah `Download as CSV` berarti: klik ikon Download lalu pilih opsi dengan nama itu.
- Langkah 2 diasersi segera setelah pemicu sebelum berkas selesai (konvensi bagian 8b butir 5); absence notifikasi (langkah 7) mengikuti berkas terunduh sebagai anchor positif (butir 11).
- Langkah penghubung (S-03): langkah 6 (jendela 5 detik sebelum absence notifikasi in-app, bagian 6).
- Temuan untuk QA:
  - TC-AC-LA-348 tidak menyebut status alokasi seed 5.100 baris (tab Current atau History); spec mengasumsikan tab Current dan N tab Current dari seeding.
  - TC-AC-LA-348 Expected b ("Tidak ada job background") tidak menyebut cara mengamatinya; spec memakai kemampuan baca job latar "disediakan tim FE".
  - Modul tidak punya aksi hapus alokasi; pembersihan 5.100 baris bergantung baseline automation dan kemampuan tim FE.
