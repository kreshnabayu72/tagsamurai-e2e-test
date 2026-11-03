---
id: TC-FA-CAT-E2E-111-resilience-wizard-save-selection-dan-download-5xx-dan-timeout
title: "Resilience Wizard Save Selection dan Download (Tabel Utama, Changelog, Assets): Respons 5xx dan Timeout Jaringan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-300
  - TC-FA-CAT-313
  - TC-FA-CAT-370
  - TC-FA-CAT-413
  - TC-FA-CAT-286
coverage:
  web: automated
---

# Resilience Wizard Save Selection dan Download (Tabel Utama, Changelog, Assets): Respons 5xx dan Timeout Jaringan

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Submit Wizard dan respons Download dipaksa lewat `Spectra.intercept()`, sedangkan state kategori dan berkas yang terunduh diasersi pada backend nyata).
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun eksplisit: client CatMany (Pre-setup #24) pada langkah 32 sampai 34, lalu client CatMain (Pre-setup #20) pada langkah 40 sampai 42 (akun dan password sama, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (CatMain).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup yang dibaca, tidak diubah: #33 (CatPostT0: T-0 sudah lewat, Starter cap 5, 8 kategori termasuk `Alpha Tech` dan `Beta Tools`, belum pernah submit selection); #24 (CatMany: 30 kategori L1); #20 (CatMain: `Electronics` berisi `Laptop` dengan 12 aset); #21, #22 (Asset Name dan aset `Laptop`); #23 (Changelog CatMain). Seed client dan state T-0 disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()` di atas backend nyata; tidak ada endpoint karangan):
  - TC-FA-CAT-300: respons Submit Wizard dipaksa 500.
  - TC-FA-CAT-313: respons Submit Wizard tidak diberikan (timeout jaringan).
  - TC-FA-CAT-370: respons Download tabel utama dipaksa 500.
  - TC-FA-CAT-413: respons Download Changelog dipaksa 500 (pada percobaan kedua).
  - TC-FA-CAT-286: respons Download tabel Assets dipaksa 500.
  Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Kemampuan membaca jumlah entri Changelog client CatPostT0 sebelum dan sesudah aksi (baseline N, dipakai langkah 1 dan 12; selisih terhadap N, S-12) disediakan tim FE/BE; tidak ada endpoint karangan.
- Kemampuan membaca berkas yang terunduh (hanya untuk nama berkas pada langkah 46) disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-300: Save Selection gagal 5xx

1. Catat status Excess node `Alpha Tech` dan `Beta Tools` di tabel dan sidebar (baseline), dan baca jumlah entri Changelog client CatPostT0 lewat kemampuan baca (baseline N)
2. Klik `[Choose Categories]` pada Alert Category Consolidation
3. Centang `Keep usable` pada `Alpha Tech`
4. Centang `Keep usable` pada `Beta Tools`
5. Paksa respons Submit menjadi 500 lewat intercept jaringan
6. Klik `[Save Selection]`
7. Verifikasi toast error `Error, failed to update category consolidation.` tampil
8. Verifikasi toast error tanpa tombol aksi
9. Verifikasi popup tetap terbuka
10. Verifikasi centang `Keep usable` pada `Alpha Tech` dan `Beta Tools` dipertahankan
11. Verifikasi status Excess node `Alpha Tech` dan `Beta Tools` di tabel dan sidebar sama dengan baseline langkah 1
12. Verifikasi jumlah entri Changelog client CatPostT0 masih N (baseline langkah 1; tidak ada log baru)
13. Lepas intercept respons Submit

### TC-FA-CAT-313: Save Selection tanpa respons (timeout jaringan)

14. Klik icon Close (✕) pada popup
15. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]` tampil
16. Klik `[Leave]` pada dialog
17. Klik `[Choose Categories]` pada Alert Category Consolidation
18. Centang `Keep usable` pada `Alpha Tech`
19. Centang `Keep usable` pada `Beta Tools`
20. Putus respons Submit lewat intercept jaringan (tidak ada respons)
21. Klik `[Save Selection]`
22. Verifikasi toast error baku `Connection problem. Please try again.` tampil tanpa tombol aksi
23. Verifikasi tidak ada toast sukses `Success, category consolidation has been updated.`
24. Verifikasi tidak ada toast error `Error, failed to update category consolidation.`
25. Verifikasi popup tetap terbuka dan centang dipertahankan
26. Verifikasi tombol `[Save Selection]` kembali enabled
27. Verifikasi status Excess node di tabel dan sidebar sama dengan baseline langkah 1
28. Lepas intercept respons Submit
29. Klik icon Close (✕) pada popup
30. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]` tampil
31. Klik `[Leave]` pada dialog

### Ganti akun ke client CatMany

32. Logout dari akun Total Control client CatPostT0
33. Login sebagai Total Control client CatMany (Pre-setup #24)
34. Buka Fixed Asset > Settings > Categories

### TC-FA-CAT-370: Download tabel utama gagal

35. Paksa respons Download menjadi 500 lewat intercept jaringan
36. Klik icon Download lalu `Download as XLSX`
37. Verifikasi toast error `Error, failed to download Categories.` tampil (tanpa extension di pesan)
38. Verifikasi toast error tanpa tombol aksi
39. Lepas intercept respons Download

### Ganti akun ke client CatMain

40. Logout dari akun Total Control client CatMany
41. Login sebagai Total Control client CatMain (Pre-setup #20)
42. Buka Fixed Asset > Settings > Categories

### TC-FA-CAT-413: Download Changelog

43. Klik icon Changelog di Table Tools
44. Klik Download > `Download as CSV`
45. Verifikasi tidak ada toast sukses
46. Verifikasi berkas `Changelog-Category.csv` terunduh
47. Paksa respons Download menjadi 500 lewat intercept jaringan
48. Klik Download > `Download as XLSX`
49. Verifikasi toast error `Error, failed to download Changelog-Category.` tampil (tanpa extension di pesan)
50. Lepas intercept respons Download dan tutup Modal Changelog dengan icon Close (✕)

### TC-FA-CAT-286: Download tabel Assets gagal

51. Klik node `Electronics` di Sidebar Category Tree
52. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
53. Paksa respons Download menjadi 500 lewat intercept jaringan
54. Klik Download > `Download as XLSX`
55. Verifikasi toast error `Error, failed to download Category-Assets.` tampil
56. Verifikasi toast error tanpa tombol aksi
57. Lepas intercept respons Download dan tutup Popup Detail

## Notes

- Langkah penghubung (S-03, S-08): langkah 1 (baseline status Excess dan jumlah entri Changelog), 13 dan 28 (melepas intercept), 14 sampai 16 dan 29 sampai 31 (menutup popup dirty: ✕, dialog Unsaved Changes, `[Leave]`), 32 sampai 34 dan 40 sampai 42 (ganti akun eksplisit ke client lain, S-07), 50 dan 57 (melepas intercept dan menutup modal atau popup).
- Ambang sekitar 35 langkah terlampaui (57 langkah). Alasan: seluruh TC berkelas fault injection (kelas b) yang menurut bagian 3 cukup satu spec per kelas per modul; tiap TC berdiri sendiri dan kegagalan satu TC tidak membuat TC lain kehilangan makna. Tiga client berbeda diperlukan karena precondition TC (Pre-setup #33, #24, #20).
- Asersi absence toast pada langkah 23 dan 24 didahului toast `Connection problem. Please try again.` (langkah 22) sebagai anchor positif.
- P-1 (state berat): klausa "tidak ada log" TC-FA-CAT-300 butir b diasersi di spec ini (langkah 12, selisih terhadap baseline N langkah 1, S-05 dan S-12) karena bergantung pada state berat yang dibangun langkah 2 sampai 6 (client CatPostT0 pasca T-0 dengan Alert Consolidation dan respons Submit yang dipaksa 500); tidak ada spec absence yang memuat TC-300. Toast error langkah 7 menjadi anchor positif bahwa respons sudah diproses.
- Temuan untuk QA:
  - TC-300 butir b menyebut "tidak ada log" tanpa menyebut surface; spec hanya mengasersi Changelog (langkah 12). System Log dan Activity Log tidak diasersi karena TC tidak memberi langkah observasinya; perlu keputusan QA.
  - TC-313 mengulang Choose Categories setelah TC-300 tanpa menyebut cara menutup popup berisi centang yang belum tersimpan; spec memakai icon Close (✕) lalu memverifikasi dialog Unsaved Changes dan klik `[Leave]` (langkah 14 sampai 16 dan 29 sampai 31, S-08); teks dialog mengikuti TC-FA-CAT-298 dan TC-FA-CAT-576.
  - TC-413 butir b menyebut intercept gagal pada percobaan XLSX kedua; spec mengikuti urutan itu.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
