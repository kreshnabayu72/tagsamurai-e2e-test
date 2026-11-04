---
id: TC-FA-TDC-E2E-006-tampilan-kolom-allowed-methods-used-by-effective-from-dan-regulation-reference
title: "Tampilan Kolom Allowed Methods, Used By, Effective From, dan Regulation Reference"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-21
  - TC-FA-TDC-22
  - TC-FA-TDC-23
  - TC-FA-TDC-24
  - TC-FA-TDC-25
  - TC-FA-TDC-26
  - TC-FA-TDC-27
coverage:
  web: automated
---

# Tampilan Kolom Allowed Methods, Used By, Effective From, dan Regulation Reference

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data: Allowed Methods NB-1 `Straight Line · Declining Balance`, BLD-P `Straight Line`, LAND `—`; Used By NB-1 5, BLD-P 1, NB-4 0; Effective From NB-1 `Jan 2026`, NB-4 `Jan 2026`, NB-2 `—`; BLD-NP memiliki satu versi Scheduled dengan Effective From Jan 2027.
- Data tambahan untuk TC-FA-TDC-26 (mengubah data Pre-setup BLD-NP): versi Scheduled kedua Effective From Jan 2028 pada BLD-NP ditambahkan lewat seeding API sebagai precondition (tidak diasersi) dan dihapus kembali lewat seeding API di langkah akhir blok serta di hook `after`; Last Updated BLD-NP dapat berubah dan dipulihkan oleh seeding (S-06).
- Data TC-FA-TDC-27: tujuh class seed bawaan (NB-1 dengan Regulation Reference seed `UU HPP 7/2021; PMK 72/2023`), kunci `seedClasses`; tabel diganti ke tujuh class seed lewat seeding API sebelum TC itu.
- Kemampuan teknis: seeding class, versi Scheduled, dan pemulihannya lewat API (`suite.md`); mengarahkan kursor untuk tooltip; Overlay Column Visibility; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom tabel (Regulation Reference di-unhide lalu disembunyikan kembali dalam spec), versi Scheduled BLD-NP, dan isi tabel (diganti ke tujuh seed). Dipulihkan di hook `after` (hapus preferensi kolom di browser, hapus versi Scheduled tambahan, pulihkan tujuh seed).

## Test Steps

### TC-FA-TDC-21: Kolom Allowed Methods: urutan tetap dan strip untuk Land

1. Verifikasi Allowed Methods NB-1 `Straight Line · Declining Balance`
2. Verifikasi Allowed Methods BLD-P `Straight Line`
3. Verifikasi Allowed Methods LAND `—`

### TC-FA-TDC-22: Kolom Used By: angka lebih dari 0 berupa link, angka 0 teks biasa

4. Verifikasi Used By NB-1 `5` dan BLD-P `1` tampil sebagai link (clickable)
5. Verifikasi Used By NB-4 `0` tampil sebagai teks biasa (not clickable)

### TC-FA-TDC-24: Kolom Effective From: format MMM YYYY dan strip untuk versi pertama

6. Verifikasi Effective From NB-1 `Jan 2026` dengan format MMM YYYY, tanpa tanggal hari, dan tidak mengikuti format tanggal General Settings
7. Verifikasi Effective From NB-4 `Jan 2026`
8. Verifikasi Effective From NB-2 `—` (versi Current adalah versi pertama tanpa Effective From)

### TC-FA-TDC-25: Tooltip kolom Effective From untuk class dengan versi Scheduled

9. Arahkan kursor ke sel Effective From baris BLD-NP
10. Verifikasi tooltip `Next version starts Jan 2027.` tampil pada sel BLD-NP
11. Arahkan kursor ke sel Effective From baris NB-1
12. Verifikasi tidak ada tooltip pada sel NB-1

### TC-FA-TDC-23: Klik angka Used By 0 tidak membuka modal

13. Klik angka `0` pada baris NB-4
14. Verifikasi sedikitnya satu baris tabel tampil
15. Verifikasi tidak ada Popup Used By yang terbuka dan tidak ada perubahan pada halaman

### TC-FA-TDC-26: Tooltip Effective From merujuk versi Scheduled paling awal bila ada lebih dari satu

16. Tambahkan versi Scheduled Jan 2028 pada BLD-NP lewat seeding API hingga tersimpan, lalu muat ulang halaman
17. Arahkan kursor ke sel Effective From baris BLD-NP
18. Verifikasi tooltip `Next version starts Jan 2027.` tampil dan tidak menyebut Jan 2028
19. Hapus versi Scheduled Jan 2028 pada BLD-NP lewat seeding API hingga tersimpan, lalu muat ulang halaman

### TC-FA-TDC-27: Kolom Regulation Reference tampil setelah di-unhide

20. Ganti isi tabel menjadi tujuh class seed lewat seeding API, lalu muat ulang halaman
21. Klik header Actions `⋯`
22. Centang kolom Regulation Reference
23. Verifikasi kolom Regulation Reference tampil setelah dicentang
24. Verifikasi Regulation Reference NB-1 `UU HPP 7/2021; PMK 72/2023` (nilai seed)
25. Verifikasi nilai kolom Regulation Reference tidak pernah kosong
26. Hapus centang kolom Regulation Reference
27. Tutup Overlay Column Visibility

## Notes

- Urutan TC dalam spec: TC-FA-TDC-21, 22, 24, 25, 23, 26, 27 (bukan 21 sampai 27). TC-FA-TDC-23 diletakkan sesudah TC tooltip karena membuka kondisi klik yang tidak berefek; TC-FA-TDC-26 memakai data tambahan BLD-NP dan TC-FA-TDC-27 mengganti isi tabel sehingga keduanya di akhir (prinsip 3, data berubah di akhir).
- Langkah penghubung (S-03): langkah 16 dan 19 (precondition TC-FA-TDC-26 dan pemulihannya, tidak diasersi; "dipakai sebagai precondition TC, tidak diasersi"), langkah 20 (mengganti isi tabel ke tujuh seed untuk TC-FA-TDC-27), langkah 26 dan 27 (pemulihan Setup Column Regulation Reference: hapus centang lalu tutup panel; 8b.14, R-24 — TC tidak menyebut `[Save]` sehingga tidak ditulis). Hook `after` hanya cadangan.
- Asersi absence langkah 12 didahului anchor positif langkah 10 (tooltip BLD-NP tampil). Langkah 15 didahului anchor langkah 14 (baris pembanding pada surface yang sama).
- Temuan untuk QA:
  - TC-FA-TDC-25 mensyaratkan satu versi Scheduled pada BLD-NP, sedangkan TC-FA-TDC-26 mensyaratkan dua (Jan 2027 dan Jan 2028) pada class yang sama; spec menjalankan keduanya berurutan dengan seeding versi tambahan.
  - TC-FA-TDC-27 memakai tujuh class seed (Regulation Reference NB-1 `UU HPP 7/2021; PMK 72/2023`), sedangkan TC lain di spec ini memakai sembilan Example Data; TC tidak menyebut nilai Regulation Reference NB-1 pada Example Data. Spec mengganti isi tabel ke tujuh seed sebelum TC-FA-TDC-27.
  - TC-FA-TDC-27 tidak menyebut `[Save]` pada Overlay Column Visibility; spec mengikuti TC.
  - Email akun Total Control tidak tertulis di TC.
