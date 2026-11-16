---
id: TC-FA-TDC-E2E-144-search-kolom-hidden-regulation-reference-modified-by-dan-class-name
title: "Search: Kolom Hidden Mengikuti Visibilitas Kolom"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-493
  - TC-FA-TDC-494
  - TC-FA-TDC-495
sourceRules: ["§4.1.1#r2", "§4.1.1#r11", "§4.1.1#b2", "§4.1.1#r12", "§4.1.1#r3"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r2": [1, 21]
  "§4.1.1#r11": 2
  "§4.1.1#b2": [4, 7, 24]
  "§4.1.1#r12": [11, 13]
  "§4.1.1#r3": [22, 28, 30]
coverage:
  web: automated
---

# Search: Kolom Hidden Mengikuti Visibilitas Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. Regulation Reference NB-SL `PMK 99/2099` dan class lain `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`). NB-SL terakhir diubah oleh `Rina P` dan class lain berstatus `System` (user penyunting disediakan tim FE). Class Name LAND `Tanah`. Kolom Regulation Reference dan Modified By Hidden (default).
- Data uji (keyword Search, literal TC): `PMK 99/2099`, `Rina`, `Tanah`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Overlay Column Visibility; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: Search pada tabel dan konfigurasi kolom (Modified By dan Class Name disembunyikan atau ditampilkan lalu dikembalikan oleh langkah di spec). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Search mencocokkan Regulation Reference walau kolomnya Hidden (TC-FA-TDC-493)

1. Verifikasi kolom Class Code tampil di tabel
2. Verifikasi kolom Regulation Reference tidak tampil di tabel
3. Ketik Search `PMK 99/2099`, tekan Enter
4. Verifikasi tabel hanya menampilkan baris NB-SL

### Search Modified By terikat visibilitas kolom (TC-FA-TDC-494)

5. Klik `(←)` pada kotak Search
6. Ketik Search `Rina`, tekan Enter
7. Verifikasi (saat kolom Hidden) tabel menampilkan `No results found`
8. Klik header Actions `⋯`
9. Centang kolom Modified By
10. Tutup Overlay Column Visibility
11. Verifikasi kolom Modified By tampil
12. Ganti isi kotak search dengan `Rina`, tekan Enter
13. Verifikasi (saat kolom tampil) tabel hanya menampilkan baris NB-SL
14. Klik `(←)` pada kotak Search
15. Klik header Actions `⋯`
16. Hapus centang kolom Modified By
17. Tutup Overlay Column Visibility

### Search kolom yang di-hide tidak mencocokkan, setelah di-unhide mencocokkan (TC-FA-TDC-495)

18. Klik header Actions `⋯`
19. Hapus centang kolom Class Name
20. Tutup Overlay Column Visibility
21. Verifikasi kolom Class Code tampil di tabel
22. Verifikasi kolom Class Name tidak tampil
23. Ketik Search `Tanah`, tekan Enter
24. Verifikasi tabel menampilkan `No results found`
25. Klik header Actions `⋯`
26. Centang kolom Class Name
27. Tutup Overlay Column Visibility
28. Verifikasi kolom Class Name tampil kembali
29. Ganti isi kotak search dengan `Tanah`, tekan Enter
30. Verifikasi tabel hanya menampilkan baris LAND
31. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 5, 14, dan 31 (menutup kotak Search dan mereset tabel; S-09), langkah 10, 17, 20, dan 27 (menutup Overlay Column Visibility), langkah 8 sampai 9 dan 25 sampai 26 (menampilkan kolom lewat Overlay yang diuji TC), langkah 15 sampai 17 (pemulihan Setup Column agar kolom Modified By kembali Hidden; 8b.14, R-24). Langkah 18 sampai 20 menyembunyikan Class Name sebagai aksi TC-FA-TDC-495; langkah 25 sampai 27 menampilkannya kembali sehingga kolom pulih tanpa langkah tambahan. Hook `after` hanya cadangan.
- Langkah 12 dan 29 menulis "ganti isi kotak search" karena TC menyebut "ketik" ulang sesudah kolom diubah dan kotak Search masih berisi keyword sebelumnya (8b.9).
- Asersi absence langkah 2 dan 22 punya anchor positif pada `Verifikasi` kolom lain pada tabel yang sama (langkah 1 dan 21; 8b.2). Asersi `No results found` langkah 7 dan 24 adalah Empty State hasil Search yang diproses, anchor positif yang sah.
- Temuan untuk QA:
  - TC-FA-TDC-494 dan 495: "Kosongkan Search" sebelum mengetik ulang tidak menyebut cara mengosongkan; spec memakai "ganti isi kotak search".
  - TC-FA-TDC-494 langkah 2 tidak menyebut `[Save]` pada Overlay Column Visibility; spec mengikuti TC (perubahan langsung).
  - Email akun Total Control dan nama lengkap user penyunting NB-SL tidak tertulis di TC.
