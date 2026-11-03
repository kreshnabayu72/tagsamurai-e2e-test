---
id: TC-AC-DS-E2E-135-usage-filter-kombinasi-and-search-dan-tanpa-hasil
title: "Usage: Filter AND, Search Lalu Filter dan Sebaliknya, serta Empty State Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-439
  - TC-AC-DS-561
  - TC-AC-DS-562
  - TC-AC-DS-563
coverage:
  web: automated
---

# Usage: Filter AND, Search Lalu Filter dan Sebaliknya, serta Empty State Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris dan jaringan entitas (#32, #24): `PT Arunika Prima` (Principal) 55, `PT Cakra Distribusi` (Distributor) 25, `PT Delta Retail` (Client) 5, `PT Mitra Lintas Nusa` (Distributor dan Client) 20, `PT Surya Logistik` (Client) 15. Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil
3. Verifikasi tabel Usage memuat sedikitnya satu baris

### TC-AC-DS-439: Empty state Usage by Company saat Search atau Filter tidak menghasilkan baris

4. Klik ikon Search pada popup, ketik Search `tidak-ada-company`, tekan Enter
5. Verifikasi area tabel menampilkan judul "No results found" dan deskripsi "Try adjusting your search or filter."

### Pemulihan state antar TC

6. Klik `(←)` pada kotak Search

### TC-AC-DS-562: Search lalu Filter pada Usage menghasilkan irisan dan melepas Filter memulihkan tabel

7. Klik ikon Search pada popup, ketik Search `Mitra`, tekan Enter
8. Klik ikon Filter pada popup
9. Verifikasi Filter Panel popup tampil
10. Pada field Entity Type pilih `Principal`
11. Klik `[Apply]` pada Filter Panel popup
12. Verifikasi tabel menampilkan "No results found" dan "Try adjusting your search or filter." karena irisan kosong
13. Verifikasi penerapan Filter tidak mereset kata kunci Search `Mitra`
14. Klik `[Clear Field]`, klik `[Apply]`
15. Verifikasi tabel pulih menampilkan `PT Mitra Lintas Nusa`
16. Verifikasi Search `Mitra` tetap aktif

### Pemulihan state antar TC

17. Klik `(←)` pada kotak Search

### TC-AC-DS-563: Filter lalu Search pada Usage menghasilkan irisan yang identik

18. Pada field Entity Type pilih `Client`
19. Klik `[Apply]` pada Filter Panel popup
20. Ketik Search `Surya`, tekan Enter
21. Verifikasi tabel memuat `PT Surya Logistik` saja
22. Verifikasi kriteria Entity Type `Client` tetap aktif pada pencarian `Surya`
23. Ganti isi kotak search dengan `Cakra`, tekan Enter
24. Verifikasi tabel menampilkan "No results found" karena `PT Cakra Distribusi` bukan Client
25. Verifikasi kriteria Entity Type `Client` tetap aktif pada pencarian `Cakra`

### Pemulihan state antar TC

26. Klik `(←)` pada kotak Search; klik `[Clear Field]`

### TC-AC-DS-561: Beberapa field Filter Usage digabung AND

27. Pada field Entity Type pilih `Client`
28. Isi Total Stock Min `10` dan Max `20`
29. Klik `[Apply]` pada Filter Panel popup
30. Verifikasi tabel hanya memuat baris Entity Type `Client` dengan Total Stock 10 sampai 20: `PT Mitra Lintas Nusa` (20) dan `PT Surya Logistik` (15)
31. Verifikasi `PT Delta Retail` (Client, 5) dan `PT Cakra Distribusi` (Distributor, 25) tidak tampil

### Pemulihan state akhir

32. Klik `[Clear Field]`, klik `[Apply]`, lalu tutup popup dengan ikon close `[✕]`

## Notes

- Langkah 1 sampai 3 adalah pembuka bersama (popup `HHR-ARC-100` dibuka sekali). Langkah 3 adalah pembanding generik sebelum asersi Search dan Filter (8b butir 2).
- Urutan TC dalam spec: 439, 562, 563, 561 (bukan urutan nomor). Alasan: Filter Panel dibuka sekali pada TC-AC-DS-562 dan tetap terbuka sesudah `[Apply]` (TC 448, 562 langsung `[Clear Field]` tanpa membuka ulang), sehingga TC berikutnya tidak mengklik ikon Filter lagi dan Search tidak diketik saat panel belum ada. Tiap TC tetap dimulai dari keadaan Search dan Filter kosong (langkah 6, 17, 26 membersihkan; S-09).
- Langkah penghubung tanpa `Verifikasi`: langkah 6, 14 (bagian TC 562), 17, 26, dan 32 (S-03).
- Expected 562 butir a, b, c ditulis langkah 12, 13, 15, 16; Expected 563 butir c dipecah menjadi langkah 22 dan 25 (kriteria `Client` per pencarian).
- Temuan untuk QA:
  - S-15: TC tidak menyatakan apakah Filter Panel tertutup sesudah `[Apply]`; spec mengikuti TC (panel tetap terbuka). Bila panel menutup otomatis, langkah 18 dan 27 perlu membuka ulang ikon Filter.
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
