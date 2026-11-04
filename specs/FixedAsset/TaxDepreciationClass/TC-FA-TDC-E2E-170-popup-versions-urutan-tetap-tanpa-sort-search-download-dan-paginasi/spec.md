---
id: TC-FA-TDC-E2E-170-popup-versions-urutan-tetap-tanpa-sort-search-download-dan-paginasi
title: "Popup Versions: Urutan Tetap, Tanpa Sort, Search, Download, dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-607
  - TC-FA-TDC-608
  - TC-FA-TDC-609
  - TC-FA-TDC-610
coverage:
  web: automated
---

# Popup Versions: Urutan Tetap, Tanpa Sort, Search, Download, dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), dua isi versi berurutan:
  - Isi versi A (TC-FA-TDC-607, 608, 609), kunci `exampleDataBldNpVersions`: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom sesuai Example Data kecuali BLD-NP yang memakai fixture khusus. BLD-NP memiliki 5 versi: Jan 2028 Scheduled (UL 12, SL 8.33%, Straight Line, `PMK 72/2023`, Rina P); Jan 2027 Cancelled (UL 15, SL 6.67%, Straight Line, `PMK 72/2023`, Rina P); Jan 2026 Current (UL 10, SL 10%, Straight Line, `PMK 72/2023`, Rina P); Jan 2025 Past (UL 8, SL 12.5%, Straight Line, `PMK 72/2023`, Rina P); versi pertama tanpa Effective From Past (UL 10, SL 10%, Straight Line, `UU HPP 7/2021; PMK 72/2023`, System).
  - Isi versi B (TC-FA-TDC-610), kunci `exampleDataBldNp12Versions`: sama dengan isi versi A, tetapi BLD-NP memiliki 12 versi (detail versi tidak disebut TC). Isi versi B diterapkan lewat seeding API pada langkah 15.
- Kemampuan teknis: membuka Drawer class dengan klik Class Code dan membuka Popup Versions dengan `View versions`; Pagination popup.
- State global yang diubah: tidak ada. Versi BLD-NP dikembalikan ke isi versi A lewat seeding API di hook `after`.

## Test Steps

### TC-FA-TDC-607: Urutan tetap Popup Versions: Effective From terbaru di atas, versi pertama paling bawah

1. Klik Class Code BLD-NP
2. Klik `View versions`
3. Verifikasi urutan baris: Jan 2028, Jan 2027, Jan 2026, Jan 2025, lalu versi pertama tanpa Effective From

### TC-FA-TDC-608: Popup Versions tanpa sort per kolom dan tanpa Setup Column

4. Klik header kolom Effective From
5. Klik header kolom Status
6. Verifikasi urutan baris tidak berubah
7. Verifikasi header tidak memiliki ikon sort
8. Cari Column Visibility pada header kolom
9. Verifikasi tidak ada ikon Column Visibility `⋯` maupun `Setup Column`
10. Verifikasi kolom Effective From, Status, Useful Life (years), Straight Line Rate, Declining Balance Rate, Allowed Methods, Regulation Reference, Modified By, Last Updated, dan Action selalu tampil

### TC-FA-TDC-609: Popup Versions tanpa Search dan Download

11. Amati toolbar Popup
12. Verifikasi tidak ada icon Search dan tidak ada Download pada Popup Versions

### TC-FA-TDC-610: Pagination Popup Versions

13. Tutup Popup Versions lewat ikon Close `(X)`
14. Tutup Drawer BLD-NP lewat `[×]`
15. Ganti isi versi menjadi isi versi B (BLD-NP 12 versi) lewat seeding API
16. Muat ulang halaman
17. Klik Class Code BLD-NP
18. Klik `View versions`
19. Verifikasi halaman 1 menampilkan 10 versi dengan page size default 10
20. Verifikasi footer menampilkan opsi page size `10`, `25`, `50`, `100`
21. Klik halaman berikutnya
22. Verifikasi halaman 2 menampilkan 2 versi
23. Verifikasi versi pertama tanpa Effective From berada di baris terakhir halaman 2
24. Ganti page size menjadi 25
25. Verifikasi page size 25 menampilkan 12 versi di halaman 1
26. Tutup Popup Versions lewat ikon Close `(X)`
27. Tutup Drawer BLD-NP lewat `[×]`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-607, 608, 609, 610. TC-FA-TDC-607 sampai 609 memakai Popup Versions BLD-NP (5 versi) yang sama sehingga dibuka sekali (langkah 1 dan 2); TC-FA-TDC-610 memakai BLD-NP dengan 12 versi sehingga diletakkan paling akhir dan isi versi diganti pada langkah 15.
- Langkah penghubung (S-03): langkah 11 (mengamati toolbar; TC tanpa Expected terpisah), langkah 13 dan 26 (menutup popup), langkah 14 dan 27 (menutup Drawer tanpa perubahan lewat `[×]`), langkah 15 dan 16 (seeding API dan muat ulang). Tabel utama memuat sembilan baris pada satu halaman; baris BLD-NP tidak perlu dicari lewat Search (8b.13).
- Asersi absence langkah 7, 9, dan 12 didahului anchor positif langkah 3 (baris versi tampil di tabel yang sama; 8b.2), dan langkah 10 (kolom tampil pada header yang sama).
- Temuan untuk QA:
  - TC-FA-TDC-608 langkah 4 ("Cari Column Visibility pada header kolom") adalah observasi tanpa aksi; spec menulisnya sebagai langkah penghubung diikuti `Verifikasi` Expected b.
  - TC-FA-TDC-608 Expected a tidak menyebut keadaan sebelum klik header; spec mengasersi urutan baris sama dengan keadaan langkah 3.
  - TC-FA-TDC-610 hanya menyebut "12 versi" tanpa detail Effective From, Status, dan nilai tiap versi.
  - Email akun Total Control dan user penyunting `Rina P` tidak tertulis di TC.
