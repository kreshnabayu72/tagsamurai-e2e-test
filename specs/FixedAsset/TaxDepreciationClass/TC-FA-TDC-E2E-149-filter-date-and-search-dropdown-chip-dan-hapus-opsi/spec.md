---
id: TC-FA-TDC-E2E-149-filter-date-and-search-dropdown-chip-dan-hapus-opsi
title: "Filter: Date Range, Logika AND, Search Dropdown, Chip, dan Hapus Opsi"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-516
  - TC-FA-TDC-517
  - TC-FA-TDC-518
  - TC-FA-TDC-519
  - TC-FA-TDC-520
  - TC-FA-TDC-521
sourceRules: ["§4.1.1#r10", "ST-23", "§4.1.1#r13", "§4.1.1#r4", "§4.1.1#r9", "§4.7#r5", "§4.1.1#b7"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r10": [4, 5]
  "ST-23": 9
  "§4.1.1#r13": 13
  "§4.1.1#r4": [18, 22, 24, 27, 29, 35, 36, 38]
  "§4.1.1#r9": 18
  "§4.7#r5": 18
  "§4.1.1#b7": [32, 33]
coverage:
  web: automated
---

# Filter: Date Range, Logika AND, Search Dropdown, Chip, dan Hapus Opsi

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. NB-1 dan NB-4 memiliki Effective From `Jan 2026`, class lain `—`. NB-SL terakhir diubah 18/08/26 dan class lain pada tanggal berbeda (format tanggal General Settings company sudah diatur; nilai formatnya dari fixture). Used By NB-1 `5`, NB-SL `4`, NB-2 `3`, class lain `0` atau `1`. Asset Type: NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL `Non-building`, BLD-NP dan BLD-P `Building`, LAND `Land`.
- Data uji (literal TC): rentang Effective From yang memuat 1 Jan 2026 lalu 1 Feb 2026 sampai 31 Des 2026; rentang Last Updated 18/08/26 sampai 18/08/26; Asset Type `Non-building` dengan Used By Min `3`; keyword dropdown `bui` dan `zzz`; opsi Asset Type `Land` dan `Building`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); memilih rentang tanggal pada date range picker.
- State global yang diubah: Filter pada tabel (dilepas oleh langkah di spec dan oleh `beforeEach` suite).

## Test Steps

### Filter Effective From dengan date range (TC-FA-TDC-516)

1. Klik icon Filter
2. Pilih rentang Effective From yang memuat 1 Jan 2026
3. Klik `[Apply]`
4. Verifikasi tabel menampilkan tepat dua baris: NB-1 dan NB-4
5. Verifikasi class dengan Effective From `—` tidak tampil
6. Klik `[Clear Field]`
7. Pilih rentang Effective From 1 Feb 2026 sampai 31 Des 2026
8. Klik `[Apply]`
9. Verifikasi tabel menampilkan `No results found`

### Filter Last Updated dengan satu hari (TC-FA-TDC-517)

10. Klik `[Clear Field]`
11. Pilih rentang Last Updated 18/08/26 sampai 18/08/26
12. Klik `[Apply]`
13. Verifikasi tabel hanya menampilkan baris NB-SL (batas tanggal inklusif)

### Logika AND antar field filter berbeda (TC-FA-TDC-518)

14. Klik `[Clear Field]`
15. Pilih Asset Type `Non-building`
16. Isi Used By Min `3`
17. Klik `[Apply]`
18. Verifikasi tabel menampilkan tepat tiga baris: NB-1, NB-2, dan NB-SL (memenuhi kedua kriteria)

### Search di dalam dropdown filter (TC-FA-TDC-519)

19. Klik `[Clear Field]`
20. Buka dropdown Asset Type
21. Ketik `bui` pada kotak search dropdown
22. Verifikasi daftar opsi menyempit menjadi `Building` dan `Non-building` (substring, tidak case-sensitive)
23. Ganti isi kotak search dropdown dengan `zzz`
24. Verifikasi dropdown menampilkan teks `No results found`

### Chip opsi terpilih muncul di dalam field (TC-FA-TDC-520)

25. Kosongkan kotak search dropdown
26. Centang `Land`
27. Verifikasi chip `Land` tampil pada field Asset Type
28. Centang `Building`
29. Verifikasi chip `Building` muncul di samping chip `Land` (tidak menimpa)
30. Tutup dropdown Asset Type

### Hapus opsi lewat (✕) pada chip menyinkronkan checkbox (TC-FA-TDC-521)

31. Klik `(✕)` pada chip `Land`
32. Verifikasi chip `Building` tetap ada
33. Verifikasi chip `Land` hilang
34. Buka dropdown Asset Type
35. Verifikasi checkbox `Land` ter-uncheck
36. Verifikasi checkbox `Building` tetap tercentang
37. Klik `[Apply]`
38. Verifikasi tabel menampilkan tepat dua baris: BLD-NP dan BLD-P
39. Klik `[Clear Field]`
40. Klik `[Apply]`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-516 sampai 521. Langkah 1 TC-FA-TDC-521 ("Pilih Asset Type `Land` dan `Building` (chip tampil)") sudah terpenuhi oleh keadaan akhir TC-FA-TDC-520 (chip `Land` dan `Building` tampil pada field Asset Type), sehingga tidak diulang.
- Langkah penghubung (S-03, S-09): langkah 6, 10, 14, dan 19 (membersihkan field Filter sebelum TC berikutnya; TC tidak menyebut pembersihan), langkah 25 (mengosongkan kotak search dropdown sebelum memilih opsi), langkah 30 (menutup dropdown Asset Type sebelum langkah 31 mengklik `(✕)` pada chip dan langkah 34 membuka dropdown lagi; tanpa penutupan, "Buka dropdown" bisa menutup dropdown yang masih terbuka), langkah 39 dan 40 (melepas Filter di akhir spec).
- Filter Panel dibuka sekali pada langkah 1 dan tetap terbuka sesudah `[Apply]` (8b.9): langkah 6, 10, 14, 19, dan 39 langsung memakai `[Clear Field]` tanpa klik icon Filter (klik icon itu menutup panel).
- Asersi tidak tampil langkah 5 didahului anchor positif langkah 4 (baris NB-1 dan NB-4 tampil pada tabel yang sama; 8b.2); asersi chip hilang langkah 33 didahului anchor langkah 32 (chip `Building` tetap ada pada field yang sama).
- Spec ini 40 langkah, di atas ~35 langkah. Alasan: satu topik (kontrol Filter Panel tabel utama) pada dataset Example Data yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan S-01 mengharuskan satu `Verifikasi` per klausa.
- Temuan untuk QA:
  - TC-FA-TDC-516 langkah 1 "rentang yang memuat 1 Jan 2026" tidak menyebut tanggal awal dan akhir persis; spec mengikuti TC.
  - TC-FA-TDC-520 Expected a ("Closed-state field menampilkan chip `Land`") tidak menyebut apakah dropdown ditutup; spec mengasersi chip pada langkah 27 dan 29 saat dropdown masih terbuka, lalu menutup dropdown pada langkah 30 (langkah penghubung).
  - TC-FA-TDC-519 langkah 3 ("Ketik `zzz`") tidak menyebut apakah `bui` dihapus lebih dulu; spec mengganti isi kotak search dropdown.
  - Email akun Total Control tidak tertulis di TC.
