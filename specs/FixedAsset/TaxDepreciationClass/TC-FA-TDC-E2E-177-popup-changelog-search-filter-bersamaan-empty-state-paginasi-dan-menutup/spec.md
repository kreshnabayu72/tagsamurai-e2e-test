---
id: TC-FA-TDC-E2E-177-popup-changelog-search-filter-bersamaan-empty-state-paginasi-dan-menutup
title: "Popup Changelog: Search dan Filter Bersamaan, Empty State, Paginasi, dan Menutup Popup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-635
  - TC-FA-TDC-636
  - TC-FA-TDC-637
  - TC-FA-TDC-638
  - TC-FA-TDC-639
coverage:
  web: automated
---

# Popup Changelog: Search dan Filter Bersamaan, Empty State, Paginasi, dan Menutup Popup

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah kecuali langkah 35; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD (9 baris `Edit`, dua di antaranya Edit NB-4; halaman 2 pada page size 10 memuat 6 entri terlama dari 18/08/26 sampai 01/01/26). Format tanggal General Settings `dd/MM/yy HH:mm`. Data Dinamis: tidak ada.
- Data uji TC-FA-TDC-635: Action `Edit`; Keyword `NB-4`, `Delete`. TC-FA-TDC-636: Keyword `zzzz`.
- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); kondisi seed gagal untuk TC-FA-TDC-637 (J-01 belum berhasil sehingga tabel tanpa class dan belum ada entri Changelog), diatur dan dipulihkan lewat seeding API suite (`suite.md`); mengganti page size Popup.
- State global yang diubah: seed class dan riwayat Changelog diubah ke kondisi seed gagal di langkah 35 dan dipulihkan ke Example Data di langkah 40 (hook `after` memulihkannya lagi sebagai cadangan); Search, Filter, dan page size Popup dilepas di langkah 4, 14, 26, 27, dan 39.

## Test Steps

1. Klik icon Changelog

### TC-FA-TDC-636: Empty State hasil pencarian kosong

2. Ketik Search `zzzz`, tekan Enter
3. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
4. Klik `(←)` pada kotak Search

### TC-FA-TDC-638: Pagination Popup Changelog

5. Verifikasi halaman 1 menampilkan 10 entri
6. Verifikasi page size default 10
7. Buka dropdown page size
8. Verifikasi opsi page size `10`, `25`, `50`, `100`
9. Tutup dropdown page size
10. Klik halaman berikutnya
11. Verifikasi halaman 2 menampilkan 6 entri terlama (dari 18/08/26 sampai 01/01/26)
12. Ganti page size menjadi 25
13. Verifikasi halaman 1 menampilkan 16 entri
14. Ganti page size kembali menjadi 10

### TC-FA-TDC-635: Search dan Filter bersamaan serta pemulihan hasil kosong

15. Klik icon Filter pada toolbar Popup
16. Pilih Action `Edit`
17. Klik `[Apply]`
18. Ketik Search `NB-4`, tekan Enter
19. Verifikasi Popup menampilkan 2 baris Edit NB-4
20. Ganti isi kotak search dengan `Delete`, tekan Enter
21. Verifikasi Popup menampilkan `No results found` (irisan kosong)
22. Kosongkan isi kotak search, tekan Enter
23. Verifikasi 9 baris `Edit` kembali tampil
24. Klik icon Filter pada toolbar Popup
25. Verifikasi Action `Edit` tetap terpilih di Filter Panel
26. Klik `[Clear Field]`
27. Klik `[Apply]`

### TC-FA-TDC-639: Menutup Popup Changelog

28. Klik area gelap di luar Popup
29. Verifikasi Popup tetap terbuka setelah klik backdrop
30. Klik ikon Close `(X)`
31. Verifikasi Popup tertutup setelah klik Close
32. Klik icon Changelog
33. Tekan Esc
34. Verifikasi Popup tertutup setelah Esc

### TC-FA-TDC-637: Empty State saat belum ada entri

35. Atur kondisi seed gagal (J-01 belum berhasil): tabel tanpa class dan belum ada entri Changelog
36. Muat ulang halaman (F5)
37. Klik icon Changelog
38. Verifikasi Illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
39. Tutup Popup Changelog lewat ikon Close `(X)`
40. Pulihkan seed ke Example Data (sembilan class dan 16 entri Changelog)

## Notes

- Urutan TC dalam spec: TC-FA-TDC-636, TC-FA-TDC-638, TC-FA-TDC-635, TC-FA-TDC-639, lalu TC-FA-TDC-637. TC-FA-TDC-635 meninggalkan Filter aktif sehingga diletakkan sesudah TC pencarian dan paginasi yang membutuhkan tabel penuh; TC-FA-TDC-637 membutuhkan state seed yang berbeda (tabel tanpa class, tanpa entri Changelog) sehingga diletakkan di akhir dan state dipulihkan di langkah 40 (S-10).
- Alasan lebih dari sekitar 35 langkah: satu topik (Popup Changelog), satu kelas harness, dan data Pre-setup yang sama; kelima TC hanya mengamati dan menyaring tanpa mengubah data sehingga satu pembukaan Popup dipakai bersama (prinsip 13, halaman yang sama dipakai berulang), dan blok TC-FA-TDC-637 berdiri sendiri di akhir spec.
- Langkah 1 TC-FA-TDC-635, TC-FA-TDC-636, dan TC-FA-TDC-638 ("Klik icon Changelog") tidak diulang karena Popup Changelog tetap terbuka sejak langkah 1; TC-FA-TDC-639 membuka Popup kembali pada langkah 32 sesuai langkah 4 TC.
- Langkah penghubung (S-03): langkah 4 (mengosongkan Search lewat `(←)`), langkah 7 dan 9 (membuka dan menutup dropdown page size untuk mengamati opsi), langkah 12 dan 14 (ganti page size), langkah 26 dan 27 (melepas Filter), langkah 35 sampai 36 dan 40 (kondisi seed gagal dan pemulihannya), langkah 39 (menutup Popup).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-635 menomori Expected "setelah langkah 2", "setelah langkah 3", "setelah langkah 4" bergeser satu terhadap langkah TC (langkah 3 menghasilkan 2 baris, langkah 4 hasil kosong, langkah 5 pemulihan); spec mengikuti urutan aksinya. TC tidak menyebut cara mengamati "filter Action tetap aktif"; spec membuka Filter Panel dan mengamati opsi terpilih.
  - TC-FA-TDC-638 tidak menyebut cara mengamati opsi page size; spec membuka dropdown page size.
  - TC-FA-TDC-637 tidak menyebut cara mengatur kondisi seed gagal; mekanismenya disediakan tim FE/BE (S-13).
  - Isi Popup Changelog memakai jumlah entri absolut (10, 6, dan 16 entri) pada audit trail permanen; Lampiran A konvensi tidak memuat pengecualian untuk modul ini. Spec mengikuti TC dan membutuhkan kemampuan Fixture BE yang menimpa riwayat Changelog dengan 16 entri Example Data (tidak disebut TC, PRD, atau LLD).
