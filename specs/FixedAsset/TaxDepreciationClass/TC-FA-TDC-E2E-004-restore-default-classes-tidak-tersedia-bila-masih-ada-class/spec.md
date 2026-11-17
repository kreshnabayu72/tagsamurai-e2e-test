---
id: TC-FA-TDC-E2E-004-restore-default-classes-tidak-tersedia-bila-masih-ada-class
title: "Restore Default Classes Tidak Tersedia Selama Masih Ada Class"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-13
  - TC-FA-TDC-316
  - TC-FA-TDC-317
  - TC-FA-TDC-318
sourceRules: ["§4.1.1#p5", "§7.1#p3", "§4.4#r11", "§4.1.1#p3", "ST-23", "FATDC-LOGIC-02k", "§4.1.1#b7", "FATDC-LOGIC-14b", "§3.6#r12"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#p5": [1, 25]
  "§7.1#p3": [1, 3, 9, 25, 27, 33]
  "§4.4#r11": 3
  "§4.1.1#p3": [6, 30]
  "ST-23": [13, 20, 40]
  "FATDC-LOGIC-02k": [14, 21, 40]
  "§4.1.1#b7": 22
  "FATDC-LOGIC-14b": 33
  "§3.6#r12": 39
coverage:
  web: automated
---

# Restore Default Classes Tidak Tersedia Selama Masih Ada Class

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset khusus automation, state tabel diatur tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data uji per blok (keempat blok memakai isi tabel berbeda, diatur lewat seeding API sebagai langkah penghubung; seeding disediakan tim FE/BE, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada):
  - TC-FA-TDC-13: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; kunci `exampleData`. Dibaca, tidak diubah.
  - TC-FA-TDC-316: tujuh class seed (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND); kunci `seedClasses`. Search `ZZZ-TIDAK-ADA`; Filter Asset Type `Land` dan Active `Inactive`. Dibaca, tidak diubah.
  - TC-FA-TDC-317: tabel memuat tepat satu class `NB-1` (seed lain tidak ada); kunci `onlyNb1`.
  - TC-FA-TDC-318: tabel memuat tepat satu class milik spec tanpa Used By dan tanpa Last Posted Tax Year dengan Class Code `KHS-D1-{runId}-004` (Class Code dasar `KHS-D1` dari TC; suffix S-12, lihat Temuan untuk QA). Dibuat lewat seeding di langkah penghubung blok ini dan dihapus oleh aksi `Delete` spec ini (cleanup di hook `after` hanya bila masih ada).
- Kemampuan teknis: seeding isi tabel (7 seed, 9 Example Data, satu class) dan pemulihan tujuh class seed lewat API; di hook `after` tujuh class seed dipulihkan.
- State global yang diubah: isi tabel Tax Depreciation Class pada company uji; dipulihkan ke tujuh class seed di hook `after`. Spec berjalan serial (`parallel: false`, `suite.md`).

## Test Steps

### TC-FA-TDC-13: Restore default classes tidak tersedia selama minimal satu class ada

1. Verifikasi toolbar menampilkan Search, Filter, Download, Changelog, dan `+ Class` tanpa tombol atau menu `Restore default classes`
2. Klik header kolom Actions `⋯`
3. Verifikasi panel Column Visibility tampil tanpa `Restore default classes`
4. Tutup panel Column Visibility
5. Klik ikon `⋯` pada baris NB-1
6. Verifikasi menu row action hanya `Edit` dan `Delete`
7. Tutup menu row action
8. Klik icon Filter
9. Verifikasi Filter Panel tampil tanpa `Restore default classes`
10. Tutup Filter Panel

### TC-FA-TDC-316: Empty State hasil Search atau Filter tidak memuat Restore default classes

11. Ganti isi tabel menjadi tujuh class seed lewat seeding API, lalu muat ulang halaman
12. Ketik Search `ZZZ-TIDAK-ADA`, tekan Enter
13. Verifikasi Title "No results found" dan Description "Try adjusting your search or filter."
14. Verifikasi tombol `Restore default classes` tidak ada
15. Klik `(←)` pada kotak Search
16. Klik icon Filter
17. Pilih Asset Type `Land`
18. Pilih Active `Inactive`
19. Klik `[Apply]`
20. Verifikasi Title "No results found" dan Description "Try adjusting your search or filter."
21. Verifikasi tombol `Restore default classes` tidak ada
22. Verifikasi chip filter dan `Clear all` tersedia
23. Klik `Clear all` pada chip filter

### TC-FA-TDC-317: Selama minimal satu class ada, tidak ada jalur UI untuk Restore default classes

24. Ganti isi tabel menjadi tepat satu class `NB-1` lewat seeding API, lalu muat ulang halaman
25. Verifikasi toolbar menampilkan Search, Filter, Download, Changelog, dan `+ Class` tanpa `Restore default classes`
26. Klik ikon `⋯` header kolom Actions
27. Verifikasi overlay `⋯` header tampil tanpa `Restore default classes`
28. Tutup overlay `⋯` header
29. Klik ikon `⋯` pada baris `NB-1`
30. Verifikasi row action tampil `Edit` dan `Delete` tanpa `Restore default classes`
31. Tutup menu row action
32. Centang baris `NB-1`
33. Verifikasi Bulk Action Bar tampil tanpa `Restore default classes`
34. Klik `Unselect All` pada Bulk Action Bar

### TC-FA-TDC-318: Restore default classes tersedia lagi setelah tabel kembali tanpa class

35. Ganti isi tabel menjadi tepat satu class `KHS-D1-{runId}-004` lewat seeding API, lalu muat ulang halaman
36. Klik ikon `⋯` pada baris `KHS-D1-{runId}-004`
37. Klik `Delete`
38. Klik `[Delete]` pada dialog Delete
39. Verifikasi toast sukses: "Success, tax depreciation class has been deleted."
40. Verifikasi Empty State tampil dengan tombol `Restore default classes`

## Notes

- Urutan TC dalam spec mengikuti nomor TC; kasus yang menghapus class (TC-FA-TDC-318) di akhir (prinsip 5 sampai 7 bagian 3).
- Langkah penghubung (S-03): langkah 4, 7, 10, 28, dan 31 (menutup panel atau menu sebelum aksi berikutnya), langkah 11, 24, dan 35 (mengganti isi tabel lewat seeding API karena tiap TC mensyaratkan isi tabel berbeda), langkah 15 (mengosongkan Search sebelum Filter), langkah 23 (menghapus chip filter), dan langkah 34 (`Unselect All`).
- Anchor positif absence (8b.2): tiap `Verifikasi` "tanpa Restore default classes" pada langkah 1, 3, 6, 9, 25, 27, 30, 33 memuat daftar elemen lain pada surface yang sama (toolbar, panel, menu, bar) sehingga surface terbukti termuat. Langkah 14 dan 21 didahului Empty State pada langkah 13 dan 20.
- Spec ini sekitar 40 langkah, di atas ~35 langkah. Alasan: keempat TC satu topik (jalur `Restore default classes` hanya muncul bila tabel kosong) dan satu kelas harness (fungsional); tiap blok dimulai dari seeding sendiri (langkah 11, 24, 35) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan memecahnya hanya menambah hook, login, dan seeding tanpa kelas atau harness berbeda.- Temuan untuk QA:
  - TC-FA-TDC-13 memakai sembilan class Example Data, TC-FA-TDC-316 tujuh seed, TC-FA-TDC-317 satu class `NB-1`, TC-FA-TDC-318 satu class `KHS-D1`; keempat isi tabel berbeda sehingga spec menyediakan seeding ulang antar blok.
  - TC-FA-TDC-317 menulis precondition "seed lain dihapus" tanpa menyebut Used By `NB-1`; spec memakai `NB-1` hanya dibaca dan memilih (tidak dihapus).
  - TC-FA-TDC-318 menulis Class Code `KHS-D1` tanpa suffix; TC tidak menyebut batas panjang Class Code sehingga suffix `-{runId}-004` mungkin melampaui batas. Perlu konfirmasi QA.
  - TC-FA-TDC-13 langkah 2 dan TC-FA-TDC-317 langkah 2 menyebut nama panel "Column Visibility" dan "overlay ⋯" untuk elemen yang sama; spec mengikuti penamaan tiap TC.
  - Email akun Total Control tidak tertulis di TC.
