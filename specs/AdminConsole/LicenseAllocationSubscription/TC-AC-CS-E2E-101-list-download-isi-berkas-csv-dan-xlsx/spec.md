---
id: TC-AC-CS-E2E-101-list-download-isi-berkas-csv-dan-xlsx
title: "List Download: Isi Berkas CSV dan XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-389
  - TC-AC-CS-390
  - TC-AC-CS-391
  - TC-AC-CS-472
coverage:
  web: automated
---

# List Download: Isi Berkas CSV dan XLSX

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #82 (120 baris term di tab Current dan 60 baris di tab History; Plan Owner PT Maju Bersama dan CV Karya Mandiri) bersifat baca-saja; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data seed Pre-setup #85: Client `Toko "Maju, Jaya"` (binaan langsung PT Maju Bersama; nama memuat koma dan tanda kutip) dengan term FAMS Growth Active, dibaca baca-saja untuk TC-AC-CS-391.
- Data seed Pre-setup #61: baris `SUBS-20260101-00001` (Client PT Sejahtera, FAMS, plan Professional, status Active, tanggal 01/01/26 / 31/12/26) dibaca baca-saja untuk TC-AC-CS-472.
- Kemampuan membaca isi berkas unduhan pada tingkat byte dan sel (BOM, pemisah, kutip, tipe sel, nama sheet) disediakan tim FE; kelas binary buffer (f).
- State global General Settings Principal PT ABC: Date Format bawaan `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00`. Blok TC-AC-CS-472 mengubah Date Format menjadi `M/d/yy` lewat fixture backend (disediakan tim FE/BE, langkah 16) dan memulihkannya ke `dd/MM/yy` pada langkah 24 dan di hook `after`; suite berjalan serial.

## Test Steps

### TC-AC-CS-389: Transformasi nilai sel pada berkas ekspor

1. Klik ikon Download lalu pilih `Download as XLSX` dan buka berkas
2. Verifikasi kolom Status berisi label teks apa adanya (`Waiting for Approval`, `Expired`, dan `Active`) tanpa warna badge
3. Verifikasi tanggal berformat mengikuti General Settings (`dd/MM/yy`)
4. Verifikasi nilai tanggal kosong ditulis `-` (hyphen tunggal)
5. Verifikasi kolom Plan Owner berisi `[Nama] (Type)` sebagai teks
6. Verifikasi sheet bernama `Sheet1`

### TC-AC-CS-390: Sel Plan berbadge pada ekspor memuat nama diikuti label badge

7. Klik ikon Download lalu pilih `Download as CSV` dan buka berkas
8. Verifikasi baris Trial menulis nama plan diikuti `Trial` (`Growth Trial`)
9. Verifikasi baris Custom Plan menulis nama diikuti `Custom` (`Mitra Premium Custom`)
10. Verifikasi baris Paid biasa menulis nama plan saja

### TC-AC-CS-391: Struktur berkas CSV: UTF-8 dengan BOM dan kutip ganda

11. Klik ikon Download lalu pilih `Download as CSV` dan periksa berkas pada tingkat byte
12. Verifikasi pemisah berkas adalah koma
13. Verifikasi encoding berkas UTF-8 dengan BOM
14. Verifikasi nilai yang mengandung koma, kutip, atau baris baru dibungkus kutip ganda dengan kutip di dalamnya digandakan
15. Verifikasi sel Client Pre-setup #85 ditulis `"Toko ""Maju, Jaya"""`

### TC-AC-CS-472: Format tanggal pada Subscription Detail dan berkas ekspor

16. Ubah Date Format General Settings Principal PT ABC menjadi `M/d/yy` lewat fixture backend
17. Ketik Search `SUBS-20260101-00001`, tekan Enter
18. Klik baris `SUBS-20260101-00001` untuk membuka Detail
19. Verifikasi Start Date `1/1/26` di Subscription Info
20. Verifikasi End Date `12/31/26` di Subscription Info
21. Klik crumb `Client Subscription` untuk kembali ke List
22. Klik ikon Download lalu pilih `Download as CSV` dan buka berkas
23. Verifikasi berkas ekspor memakai format tanggal yang sama (`1/1/26` dan `12/31/26`)
24. Pulihkan Date Format General Settings Principal PT ABC menjadi `dd/MM/yy` lewat fixture backend

## Notes

- Nama berkas, nama kolom, dan jumlah baris berkas (TC-AC-CS-383 sampai 388 dan 392) dicakup spec lain suite ini.
- Langkah penghubung (S-03): langkah 16 dan 24 (mengubah dan memulihkan Date Format lewat fixture), Search `SUBS-20260101-00001` (langkah 17) agar baris seed itu tampil sebelum diklik, dan klik crumb `Client Subscription` untuk kembali ke List.
- Urutan blok mengikuti bagian 3: blok TC-AC-CS-472 yang mengubah state global General Settings berada di akhir.
- Pembagian TC lintas spec: format tanggal List pada layar (selain Detail dan berkas) ada di spec Format Tanggal General Settings, bukan di spec ini.
- Temuan untuk QA:
  - TC-AC-CS-389 menyebut baris Waiting for Approval, Expired, Active, dan Custom Plan "tersedia" tanpa nomor Pre-setup baris; spec memakai dataset #82 apa adanya dan tidak menyebut Subscription ID baris tertentu.
  - TC-AC-CS-390 menyebut `Growth Trial` dan `Mitra Premium Custom` tanpa nomor Pre-setup baris; baris Custom Plan `Mitra Premium` ada di Pre-setup #51.
  - TC-AC-CS-472 Precondition menyebut baris #61 tanpa langkah mengubah Date Format; spec menambah langkah fixture 16 (pemulihan 24).
