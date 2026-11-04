---
id: TC-FA-LBL-E2E-001-screening-daftar-label-state-hasil-kosong-dan-changelog
title: "Screening tab Labels: daftar, state hasil kosong, dan Changelog"
priority: Critical
caseType: Positive
status: draft
sourceRules:
  - F-FALB-01
  - F-FALB-08.k1
  - F-FALB-09.k2
coverage:
  web: automated
---

# Screening tab Labels: daftar, state hasil kosong, dan Changelog

## Prerequisites

- Mode: FE+BE
- Akun: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-07` (Population Labels List 6 baris pre-setup, dibaca saja dan tidak diubah; kolom Total Asset mengikuti Example Data PRD §4.1.1 yang menjadi sumber `DU-07`), `DU-08` (kata kunci Search tanpa hasil).
- Spec ini hanya membaca: tidak membuat data dan tidak mengubah state global, sehingga tidak ada cleanup selain menutup modal Changelog (langkah 22).

## Test Steps

### F-FALB-01: List Labels

1. Verifikasi Labels List menampilkan chip badge pada kolom Label untuk keenam label `DU-07`, dengan latar chip berwarna hex baris itu
2. Verifikasi kolom Color Hex menampilkan kode `#RRGGBB` tiap label sesuai `DU-07`
3. Verifikasi kolom Total Asset menampilkan jumlah aset tiap label sebagai angka bulat rata kanan berbentuk link
4. Klik ikon Filter di toolbar
5. Verifikasi Filter Panel tampil di bawah toolbar dengan tombol `[Clear Field]` dan `[Apply]`
6. Isi field Total Asset `Min` dengan nilai yang memisahkan Finance Department dari Executive Asset menurut kolom Total Asset `DU-07`, klik `[Apply]`
7. Verifikasi baris Finance Department tampil di Labels List
8. Verifikasi baris Executive Asset tidak tampil di Labels List
9. Klik `[Clear Field]`, klik `[Apply]`
10. Verifikasi kontrol Pagination tampil dengan jumlah baris per halaman bawaan 10
11. Buka pilihan jumlah baris per halaman
12. Verifikasi pilihan jumlah baris per halaman adalah 10, 25, 50, dan 100
13. Tutup pilihan jumlah baris per halaman dengan Esc

### F-FALB-08.k1: Pencarian tanpa hasil di Labels List

14. Ketik Search `DU-08`, tekan Enter
15. Verifikasi empty state Labels List menampilkan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
16. Klik `(←)` pada kotak Search

### F-FALB-09.k2: Pencarian tanpa hasil di Modal Changelog

17. Klik ikon Changelog pada toolbar tabel
18. Verifikasi Modal Changelog: Labels tampil dengan judul `Changelog: Labels`
19. Ketik Search `DU-08` di toolbar Modal Changelog, tekan Enter
20. Verifikasi empty state Modal Changelog menampilkan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
21. Klik `(←)` pada kotak Search Modal Changelog
22. Klik `[✕]` pada header Modal Changelog

## Notes

- Langkah penghubung (S-03): langkah 4, 9, 11, 13, 16, 17, 21, dan 22. Langkah 9 mengosongkan Filter sebelum blok berikutnya mengandalkan tabel penuh (S-09). Langkah 16 mengosongkan Search sebelum modal dibuka (S-09). Langkah 11 dan 13 hanya membuka dan menutup pilihan jumlah baris tanpa mengubahnya.
- Anchor positif (bagian 8b butir 2): langkah 7 membuktikan Labels List sudah termuat sebelum absence di langkah 8; langkah 18 membuktikan Modal Changelog sudah terbuka sebelum asersi hasil kosong.
- Search dan Filter dipakai sebagai alat uji klausa, bukan untuk membuka baris target (R-16 tidak berlaku).
- Klausa di luar E2E: `F-FALB-01` menyebut daftar katalog beserta chip, kode hex, jumlah aset, filter, dan pagination; isi opsi tiap field Filter, Setup Column, Search per kolom, Sort, dan Download dimiliki baris tabel `T-ALB-01` yang tidak punya ID leaf di PRD ini, sehingga tidak diasersi di spec ini.
- Nilai batas langkah 6 diturunkan dari kolom Total Asset Example Data PRD §4.1.1 (Finance Department 120, Executive Asset 14), sumber `DU-07`.
