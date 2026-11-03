---
id: TC-FA-CAT-E2E-090-wizard-pra-t0-seleksi-dibuang-atau-diubah-sebelum-t0-kategori-dihapus-dan-ditambah
title: "Wizard Pra-T-0: Seleksi Dibuang atau Diubah Sebelum T-0 karena Kategori Dihapus atau Ditambah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-601
  - TC-FA-CAT-602
  - TC-FA-CAT-603
coverage:
  web: automated
---

# Wizard Pra-T-0: Seleksi Dibuang atau Diubah Sebelum T-0 karena Kategori Dihapus atau Ditambah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPreT0 (Pre-setup #32), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #32 (CatPreT0, downgrade terjadwal dari plan aktif Professional cap 100 ke plan baru Starter cap 5, T-0 belum tiba, belum ada seleksi tersimpan): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Data Dinamis (dibuat spec): kategori root `Late Cat {runId}-090` pada langkah 24 sampai 26; dihapus oleh pemulihan seed Pre-setup #32.
- Waktu: T-0 dibaca dari data downgrade terjadwal client lewat API seeding (8b.3); jam server dan jam browser diatur bersama ke T-0 pada langkah 8, 28, dan 45 (bagian 6 konvensi). Kemampuan mengatur jam dan memicu penerapan T-0 disediakan tim FE/BE.
- State yang diubah spec: jam server, seleksi tersimpan, dan kategori client CatPreT0 (penghapusan pada langkah 6 dan 43, penambahan pada langkah 26). Pemulihan seed Pre-setup #32 dan jam dilakukan fixture backend (disediakan tim FE/BE) pada langkah 17 dan 37 serta di hook `after`. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog per Action sebelum aksi (baseline NM untuk `Marked as Excess (Category Consolidation)`, NR untuk `Restored from Excess (Category Consolidation)`, S-12).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-601: Seleksi tersimpan dibuang di T-0 bila jumlah Category sudah <= cap plan baru

1. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
2. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, dan `Delta Supply`
3. Klik `[Save Selection]`
4. Tunggu aksi selesai
5. Buka Fixed Asset > Settings > Categories
6. Hapus `Epsilon Gear`, `Zeta Vehicle`, dan `Eta Furniture` lewat row action Delete sehingga jumlah kategori menjadi 5
7. Catat baseline NM dan NR jumlah baris Changelog
8. Majukan jam server dan jam browser ke T-0 (cap plan baru 5 berlaku) hingga tersimpan
9. Buka Fixed Asset > Settings > Categories
10. Verifikasi `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Theta Heavy` berstatus usable
11. Verifikasi tidak ada node Excess
12. Verifikasi Alert Category Consolidation tidak tampil
13. Buka Modal Changelog
14. Verifikasi jumlah baris `Marked as Excess (Category Consolidation)` sama dengan NM
15. Verifikasi jumlah baris `Restored from Excess (Category Consolidation)` sama dengan NR
16. Tutup Modal Changelog

### TC-FA-CAT-602: Category dibuat setelah Submit seleksi diperlakukan tidak dicentang dan menjadi Excess di T-0 bila jumlah > cap

17. Pulihkan seed Pre-setup #32 dan jam lewat fixture, lalu muat ulang halaman Categories
18. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
19. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
20. Klik `[Save Selection]`
21. Tunggu aksi selesai
22. Buka Fixed Asset > Settings > Categories
23. Klik `[+] Category` pada sidebar
24. Isi Category Name `Late Cat {runId}-090`
25. Klik `[Submit]`
26. Verifikasi toast `Success, category has been created.` tampil
27. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
28. Majukan jam server dan jam browser ke T-0 (cap plan baru 5 berlaku) hingga tersimpan
29. Buka Fixed Asset > Settings > Categories
30. Verifikasi `Late Cat {runId}-090` berstatus Excess (jumlah 9 melebihi cap 5) walau dibuat setelah seleksi disimpan
31. Verifikasi `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear` berstatus usable
32. Verifikasi `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess
33. Buka Modal Changelog
34. Verifikasi Changelog bertambah tepat empat baris `Marked as Excess (Category Consolidation)` (NM + 4) untuk `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`, dan `Late Cat {runId}-090`
35. Verifikasi Modified By tiap baris baru adalah aktor Total Control yang men-submit
36. Tutup Modal Changelog

### TC-FA-CAT-603: Category tercentang yang dihapus sebelum T-0 keluar dari seleksi dan slotnya tidak diisi otomatis

37. Pulihkan seed Pre-setup #32 dan jam lewat fixture, lalu muat ulang halaman Categories
38. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
39. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, dan `Epsilon Gear`
40. Klik `[Save Selection]`
41. Tunggu aksi selesai
42. Buka Fixed Asset > Settings > Categories
43. Hapus `Delta Supply` lewat row action Delete
44. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
45. Majukan jam server dan jam browser ke T-0 (cap plan baru 5 berlaku) hingga tersimpan
46. Buka Fixed Asset > Settings > Categories
47. Verifikasi hanya `Alpha Tech`, `Beta Tools`, `Gamma Parts`, dan `Epsilon Gear` yang berstatus usable (slot `Delta Supply` tidak diisi kategori lain)
48. Verifikasi `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy` berstatus Excess
49. Buka Modal Changelog
50. Verifikasi Changelog bertambah tepat tiga baris `Marked as Excess (Category Consolidation)` (NM + 3) untuk `Zeta Vehicle`, `Eta Furniture`, dan `Theta Heavy`
51. Verifikasi Modified By tiap baris baru adalah aktor Total Control
52. Verifikasi Changelog memuat satu baris `Delete` untuk `Delta Supply`
53. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (53 langkah nominal). Alasan: seluruh blok satu kelas (harness eksternal: time-travel T-0) pada satu client CatPreT0, dan tiap blok memulai dari seed yang dipulihkan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; sekitar 18 langkah per blok hanyalah pembentukan state (Wizard, hapus atau buat kategori, pemicu T-0) yang diwajibkan TC.
- Urutan TC: TC-FA-CAT-601, TC-FA-CAT-602, lalu TC-FA-CAT-603; tiap TC mengubah seleksi dan kategori sehingga didahului pemulihan seed (S-09).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4, 21, 41 (menunggu aksi selesai), 5, 9, 22, 29, 42, 46 (navigasi), 7, 27, 44 (baseline), 8, 28, 45 (pemicu T-0), 16, 36, 53 (menutup Modal Changelog), 17 dan 37 (pemulihan seed).
- Asersi absence langkah 11, 12, 14, dan 15 memakai langkah 10 (kategori usable tampil pada halaman yang sama) dan selisih terhadap baseline sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-601 Expected a menyebut `Theta Heavy` sebagai salah satu dari kelima kategori yang tersisa; spec mengasersinya apa adanya.
  - TC-FA-CAT-603 Expected c menyebut satu baris `Delete` untuk `Delta Supply` tanpa Field, Old Value, dan New Value; spec hanya mengasersi Action `Delete` dan Category Name.
