---
id: TC-FA-COA-E2E-047-kombinasi-search-filter-sort-paginasi-pada-tabel
title: "Kombinasi Search, Filter, Sort, dan Paginasi pada Tabel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-79
  - TC-FA-COA-325
  - TC-FA-COA-326
  - TC-FA-COA-327
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Paginasi pada Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hanya dibaca, tidak diubah; disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`): akun P1 sampai P5 (P1 `5-6001` Depreciation Expense – Admin, Active; P2 `6-2001` Repairs & Maintenance Expense, Active; P3 `4-7001` Gain on Disposal, Inactive; P4 `1-1002` Equipment – Legacy Code, Inactive; P5 `CAP-6100` Capitalization Clearing – Repairs, Active).
- Data untuk TC-FA-COA-325: tabel berisi lebih dari 10 akun Active yang Account Name-nya memuat `Depreciation`, ukuran halaman 10 (asumsi pre-setup; seed P1 sampai P115 disediakan tim FE), sehingga halaman 2 hasil Search dan Filter terisi. Search `Depreciation` dan Filter Active = Active memiliki sedikitnya satu akun Active dan satu akun bukan Active di seed sehingga saringan terbukti membedakan (S-11).
- State yang diubah spec: Search, Filter Panel, sort, dan halaman tabel; tiap TC dipulihkan dengan langkah eksplisit (langkah 9, 20, 29, 38). Tidak ada data yang ditulis. Hook `after` menghapus preferensi tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-79: Search dan Filter Panel berlaku bersamaan (AND) dan Clear all hanya melepas filter

1. Ketik Search `Depreciation`, tekan Enter
2. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
3. Verifikasi sedikitnya satu baris tampil di tabel
4. Verifikasi setiap baris tabel memuat `Depreciation`
5. Verifikasi setiap baris tabel berstatus Active
6. Klik `Clear all`
7. Verifikasi chip filter Active dilepas
8. Verifikasi Search tetap `Depreciation`
9. Klik `(←)` pada kotak Search

### TC-FA-COA-325: Kombinasi Search, Filter, Sort, dan Paginasi berlaku bersamaan

10. Ketik Search `Depreciation`, tekan Enter
11. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
12. Klik header Account Name satu kali
13. Verifikasi sedikitnya satu baris tampil di tabel
14. Verifikasi setiap baris tabel berstatus Active
15. Verifikasi setiap baris tabel memuat `Depreciation`
16. Verifikasi baris tabel berurut Account Name A-Z
17. Pindah ke halaman 2
18. Verifikasi info paginasi mengikuti jumlah hasil Search dan Filter
19. Verifikasi halaman 2 berisi lanjutan hasil yang sama
20. Klik `(←)` pada kotak Search, klik `Clear all`, lalu klik header Account Name dua kali sampai netral

### TC-FA-COA-326: Clear Filter saat Search dan Sort aktif hanya melepas filter

21. Ketik Search `Depreciation`, tekan Enter
22. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
23. Klik header Account Name satu kali
24. Klik `Clear all`
25. Verifikasi sedikitnya satu baris tampil di tabel
26. Verifikasi chip filter Active dilepas
27. Verifikasi Search tetap `Depreciation`
28. Verifikasi sort Account Name naik (↑) tetap aktif
29. Klik `(←)` pada kotak Search, lalu klik header Account Name dua kali sampai netral

### TC-FA-COA-327: Mengosongkan Search saat Filter dan Sort aktif hanya melepas Search

30. Ketik Search `Depreciation`, tekan Enter
31. Buka Filter Panel, pilih Active = Active, klik `[Apply]`
32. Klik header Account Name satu kali
33. Klik `(✕)` di kotak Search, lalu tekan Enter pada input kosong
34. Verifikasi sedikitnya satu baris tampil di tabel
35. Verifikasi Search dikosongkan
36. Verifikasi filter Active tetap aktif
37. Verifikasi sort Account Name naik (↑) tetap aktif
38. Klik `Clear all`, lalu klik header Account Name dua kali sampai netral

## Notes

- Alasan spec di atas sekitar 35 langkah (38 langkah): empat TC kombinasi Search, Filter, dan Sort pada satu layar dan satu dataset, semuanya kelas fungsional yang sama dan berdiri sendiri; pembeda tiap blok adalah aksi pelepas yang diuji. Asersi universal ("setiap baris ...") didahului pembanding sedikitnya satu baris (8b.2) dan Expected dipecah satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (S-03, S-09): langkah 9, 20, 29, dan 38 (mengosongkan Search, melepas filter, dan mengembalikan sort ke netral sebelum TC berikutnya).
- Langkah 33 mengosongkan Search lewat `(✕)` lalu Enter sesuai TC-FA-COA-327; Search pada langkah lain memakai `(←)` (8b.9).
- Spec ini hanya memuat TC-FA-COA-79, 325, 326, 327 (TC-FA-COA-79 menjadi sumber kombinasi AND dan Clear all).
- Temuan untuk QA:
  - TC-FA-COA-325 butir b ("halaman 2 berisi lanjutan hasil yang sama") mensyaratkan lebih dari 10 hasil Active berisi `Depreciation`, padahal precondition TC hanya menulis "lebih dari 10 akun Active"; spec menulis asumsi itu di Prerequisites.
  - TC-FA-COA-79 butir a ("hanya akun Depreciation yang Active") tidak menyebut apakah `Depreciation` dicocokkan pada Account Name saja; spec mengasersi baris memuat `Depreciation` pada baris yang tampil.
  - TC-FA-COA-325 butir b tidak menyebut format teks info paginasi; spec mengasersi jumlah mengikuti hasil tanpa teks literal.
