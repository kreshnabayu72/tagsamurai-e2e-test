---
id: TC-FA-FAAM-E2E-099-bulk-delete-sukses-homogen-continue-dan-klik-ganda
title: "Bulk Delete: Konfirmasi Homogen, Continue Campuran, dan Klik Ganda Menghapus Sekali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-284
  - TC-FA-FAAM-286
  - TC-FA-FAAM-673
coverage:
  web: automated
---

# Bulk Delete: Konfirmasi Homogen, Continue Campuran, dan Klik Ganda Menghapus Sekali

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (suffix `{runId}-099`, seed di hook `before`, cleanup di hook `after` untuk yang tersisa); Search `{runId}-099` menampilkan ketujuh baris dalam satu halaman:
  - `Bulk Clean A 284 {runId}-099` dan `Bulk Clean B 284 {runId}-099`: salinan Pre-setup #13c (Total Asset 0), dihapus TC-FA-FAAM-284.
  - `Bulk Clean A 286 {runId}-099` dan `Bulk Clean B 286 {runId}-099`: salinan Pre-setup #13c (Total Asset 0), dihapus TC-FA-FAAM-286.
  - `Bulk Used X {runId}-099`: salinan Pre-setup #14o (Total Asset 3), tetap setelah TC-FA-FAAM-286.
  - `Bulk Dbl A {runId}-099` dan `Bulk Dbl B {runId}-099`: salinan Pre-setup #13i (Total Asset 0), dihapus TC-FA-FAAM-673.
- Kemampuan teknis (disediakan tim BE/FE): membaca jumlah entri Changelog tanpa mengubahnya. Baseline N0 dicatat sekali sebelum aksi pertama; jumlah entri pada langkah berikutnya dibandingkan dengan N0 ditambah entri Delete dari TC sebelumnya (selisih terhadap baseline, S-12).
- State global: tidak ada yang diubah spec ini.

## Test Steps

1. Catat jumlah entri Changelog sebagai N0 lewat kemampuan baca
2. Ketik Search `{runId}-099`, tekan Enter

### TC-FA-FAAM-284: Konfirmasi Bulk Delete homogen menghapus semua dan mencatat satu entri Delete per item

3. Centang baris `Bulk Clean A 284 {runId}-099`, `Bulk Clean B 284 {runId}-099`
4. Klik `Bulk Action` lalu `Delete`
5. Klik `[Delete]`
6. Verifikasi toast `Success, asset name has been deleted.` tampil
7. Verifikasi kedua baris `Bulk Clean A 284 {runId}-099` dan `Bulk Clean B 284 {runId}-099` hilang
8. Verifikasi bar bulk menghilang
9. Verifikasi seleksi di-reset
10. Buka Changelog
11. Verifikasi dua baris teratas Changelog memiliki Action `Delete` dengan Old `Bulk Clean A 284 {runId}-099` dan `Bulk Clean B 284 {runId}-099`
12. Verifikasi kedua baris memiliki Date yang sama persis
13. Tutup Changelog

### TC-FA-FAAM-286: Continue pada Bulk Delete campuran menghapus yang bersih dan melewati in-use

14. Centang baris `Bulk Clean A 286 {runId}-099`, `Bulk Clean B 286 {runId}-099`, `Bulk Used X {runId}-099`
15. Klik `Bulk Action` lalu `Delete`
16. Klik `[Continue]`
17. Verifikasi toast `Success, asset name has been deleted. Some items were skipped.` tampil
18. Verifikasi `Bulk Clean A 286 {runId}-099` dan `Bulk Clean B 286 {runId}-099` hilang
19. Verifikasi `Bulk Used X {runId}-099` tetap
20. Buka Changelog
21. Verifikasi dua baris teratas Changelog memiliki Action `Delete` dengan Old `Bulk Clean A 286 {runId}-099` dan `Bulk Clean B 286 {runId}-099`
22. Verifikasi jumlah entri Changelog sama dengan N0 + 4 (dua entri dari TC-FA-FAAM-284 dan dua entri Delete dari TC ini; tidak ada baris untuk `Bulk Used X {runId}-099`)
23. Tutup Changelog

### TC-FA-FAAM-673: Klik ganda cepat pada [Delete] dialog Bulk Delete hanya menghapus sekali

24. Tunggu toast lama hilang otomatis
25. Centang baris `Bulk Dbl A {runId}-099`, `Bulk Dbl B {runId}-099`
26. Klik `Bulk Action` lalu `Delete`
27. Klik `[Delete]` pada dialog `Delete Asset Names` dua kali cepat
28. Verifikasi dialog tertutup
29. Verifikasi kedua baris `Bulk Dbl A {runId}-099` dan `Bulk Dbl B {runId}-099` hilang
30. Verifikasi tepat satu toast `Success, asset name has been deleted.` tampil
31. Buka Changelog
32. Verifikasi dua baris teratas Changelog memiliki Action `Delete` dengan Old `Bulk Dbl A {runId}-099` dan `Bulk Dbl B {runId}-099`
33. Verifikasi kedua baris memiliki Date yang sama
34. Verifikasi jumlah entri Changelog sama dengan N0 + 6 (tanpa baris ganda)
35. Tutup Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): baseline Changelog N0 (langkah 1, S-12), Search untuk menemukan baris target (R-16, langkah 2), membuka dan menutup Changelog (langkah 10, 13, 20, 23, 31, 35), dan menunggu toast lama hilang otomatis sebelum hitungan "tepat satu toast" (langkah 24, R-12).
- Asersi absence pada langkah 7, 18, dan 29 memakai toast sukses sebagai anchor (bagian 8b butir 2); absence bar pada langkah 8 memakai langkah 7 sebagai anchor.
- Seluruh record yang dihapus adalah salinan milik spec; Pre-setup #13c, #13i, dan #14o tidak diubah (S-06).
- Temuan untuk QA:
  - TC-FA-FAAM-284 dan TC-FA-FAAM-673 menulis "Date yang sama persis" tanpa menyebut ketelitian; kolom Date Changelog berketelitian menit sehingga asersi ini tidak membedakan dua penghapusan beda detik dalam menit yang sama.
  - TC-FA-FAAM-286 Expected d ("Changelog hanya memuat dua baris Delete untuk item yang terhapus") diasersi lewat selisih jumlah entri terhadap baseline N0.
