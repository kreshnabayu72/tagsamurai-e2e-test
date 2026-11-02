---
id: TC-FA-CAT-E2E-162-tabel-step-dropdown-filter-clear-field-dan-kombinasi
title: "Tabel Step Category Consolidation: Dropdown Filter (Pencarian Internal dan Sinkronisasi Chip), Clear Field, serta Kombinasi Search, Filter, dan Sort dengan Centang Keep usable Dipertahankan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-597
  - TC-FA-CAT-598
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Dropdown Filter (Pencarian Internal dan Sinkronisasi Chip), Clear Field, serta Kombinasi Search, Filter, dan Sort dengan Centang Keep usable Dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection) hanya dibaca: 8 kategori root `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`, dengan Modified By bergantian `Jane Smith`, `Alex Brown`, dan `System`. Kebutuhan data uji: sedikitnya satu baris `Usable` dan satu `Excess` (opsi Status `Usable` dan `Excess`); status tiap baris tidak tertulis di Pre-setup #33 dan disediakan tim FE/BE lewat seed (lihat Temuan untuk QA).
- Field Filter yang diuji pada langkah 3 sampai 10 (langkah diulang untuk setiap baris tabel):

  | Field | Keyword internal | Opsi tersisa | Opsi dicentang | Chip yang di-(✕) |
  |---|---|---|---|---|
  | Depth | `l1` | `L1` | `L1` | `L1` |
  | Status | `usa` | `Usable` | `Usable`, `Excess` | `Usable` |
  | Modified By | `jan` | `Jane S` | `Jane S`, `Alex B` | `Jane S` |

- State yang diubah spec: Filter, Search, dan Sort tabel Step serta centang `Keep usable` pada wizard (tidak disimpan ke server karena `[Save Selection]` tidak diklik). Dipulihkan dengan langkah penghubung (langkah 15, 32, 43, 44).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

1. Klik `[Choose Categories]` pada Alert Category Consolidation

### TC-FA-CAT-597: Dropdown Filter tabel Step, pencarian internal dan sinkronisasi chip (untuk setiap field pada tabel Field Filter, langkah 3 sampai 10)

2. Klik icon Filter
3. Buka dropdown field, lalu ketik keyword internal pada kotak cari dalam dropdown
4. Verifikasi opsi menyempit ke opsi tersisa sesuai tabel
5. Ganti isi kotak cari dalam dropdown dengan `zzz`
6. Verifikasi dropdown menampilkan teks `No results found` tanpa ilustrasi
7. Kosongkan kotak cari dalam dropdown, centang opsi yang dicentang sesuai tabel, lalu tutup dropdown
8. Verifikasi opsi yang dicentang tampil sebagai chip pada field
9. Klik (✕) pada chip yang di-(✕) sesuai tabel, lalu buka dropdown field
10. Verifikasi chip itu terhapus dan checkbox opsi itu ter-uncheck di dropdown
11. Buka dropdown Status, lalu uncheck opsi `Excess` dari dalam dropdown
12. Verifikasi chip `Excess` terhapus dari field Status
13. Buka dropdown Modified By, lalu uncheck opsi `Alex B` dari dalam dropdown
14. Verifikasi chip `Alex B` terhapus dari field Modified By
15. Klik `[Clear Field]` dan tutup Filter Panel

### TC-FA-CAT-598: Clear Field Filter serta kombinasi Search, Filter, dan Sort dengan centang Keep usable dipertahankan

16. Centang `Keep usable` pada `Alpha Tech`
17. Ketik Search `Alpha`, tekan `Enter`
18. Klik icon Filter, pilih Depth `L1`, lalu klik `[Apply]`
19. Klik header Code dua kali
20. Verifikasi hasil adalah irisan Search dan Filter, yaitu hanya `Alpha Tech`
21. Verifikasi titik indikator tampil pada icon Filter
22. Klik icon Filter, lalu klik `[Clear Field]`
23. Verifikasi seluruh field Filter kosong
24. Klik `[Apply]`
25. Verifikasi Filter lepas dan titik indikator pada icon Filter hilang
26. Verifikasi Search `Alpha` dipertahankan
27. Verifikasi Sort Code Descending dipertahankan
28. Klik icon Filter, pilih Depth `L1`, lalu klik `[Apply]`
29. Klik icon (✕) pada Search, lalu tekan `Enter`
30. Verifikasi Filter Depth `L1` dipertahankan (titik indikator tampil pada icon Filter)
31. Verifikasi Sort Code Descending dipertahankan
32. Reset semua kontrol: klik icon Filter, `[Clear Field]`, `[Apply]`, klik icon panah (←) pada Search, dan klik header Code sampai Netral
33. Klik icon Filter, pilih Depth `L1`, lalu klik `[Apply]`
34. Ketik Search `Alpha`, tekan `Enter`
35. Verifikasi hasil hanya `Alpha Tech` (dataset identik dengan urutan Search lalu Filter)
36. Verifikasi kotak Search tetap berisi `Alpha` (keyword tidak tertimpa saat Filter diterapkan)
37. Ganti isi kotak search dengan `zzzz`, tekan `Enter`
38. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
39. Klik icon (✕) pada Search, lalu tekan `Enter`
40. Verifikasi tabel memuat sedikitnya satu baris (pulih otomatis saat Search dikosongkan)
41. Verifikasi centang `Keep usable` pada `Alpha Tech` dipertahankan
42. Verifikasi counter `1 of 5 categories selected` dipertahankan
43. Hilangkan centang `Keep usable` pada `Alpha Tech`
44. Klik `[Cancel]` pada footer wizard Category Consolidation

## Notes

- Spec melewati sekitar 35 langkah (44 langkah nominal, dengan langkah 3 sampai 10 diulang tiga kali sehingga sekitar 62 langkah setelah ekspansi). Alasan: TC-FA-CAT-598 satu TC tak terbagi dengan enam butir Expected yang berurutan pada satu state (Search, Filter, Sort, centang), sedangkan TC-FA-CAT-597 satu alur identik per field dengan parameter di tabel `Field Filter` (bagian 8b butir 7); kedua TC menguji Filter Panel tabel Step yang sama dan berdiri sendiri. Langkah yang diulang: 3 sampai 10.
- Langkah penghubung (S-03, S-09): langkah 1 (membuka wizard), langkah 15 (membersihkan Filter dan menutup panel sebelum TC berikutnya), langkah 32 (reset semua kontrol sebelum urutan Filter lalu Search), langkah 43 dan 44 (centang `Keep usable` dilepas sehingga wizard tidak dirty, lalu `[Cancel]` menutup wizard tanpa menyimpan; spec tidak berakhir dengan form dirty, S-09).
- Urutan langkah TC-FA-CAT-597 mengelompokkan langkah per field (langkah 3 sampai 10), bukan per langkah TC lintas ketiga dropdown; hasil asersinya sama dengan Expected TC. Uncheck dari dalam dropdown (Expected e) dikerjakan untuk Status dan Modified By pada langkah 11 sampai 14.
- Expected TC-FA-CAT-598 butir f diverifikasi sekali pada akhir alur (langkah 41 dan 42) karena centang dan counter tidak berubah oleh langkah penghubung.
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-597 menyebut "centang dua opsi (atau satu bila hanya satu yang cocok)" tanpa opsi spesifik; spec memakai opsi di tabel `Field Filter`. Pre-setup #33 hanya berisi kategori root sehingga Depth hanya punya opsi `L1`; uncheck dari dalam dropdown (Expected e) untuk Depth tidak dapat dilakukan karena chip tunggal sudah dihapus pada langkah 9, sehingga hanya diuji untuk Status dan Modified By.
  - TC-FA-CAT-597 membutuhkan baris `Usable` dan `Excess` serta Modified By `Jane S` dan `Alex B` pada Pre-setup #33, yang tidak menyebut status tiap baris.
  - TC-FA-CAT-598 langkah 3 menyebut "Sort Code Descending" tanpa jumlah klik; spec memakai dua klik (Ascending lalu Descending) mengikuti siklus tiga state.
  - TC-FA-CAT-598 langkah 5 menyebut "Reset semua kontrol" tanpa merinci; spec mengartikannya sebagai Clear Field Filter, panah tutup Search, dan Sort Netral (langkah 32).
