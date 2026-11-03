---
id: TC-FA-CAT-E2E-108-download-tabel-utama-menu-nama-berkas-cakupan-hasil-nol-dan-node-leaf
title: "Download Tabel Utama: Menu CSV dan XLSX, Nama Berkas, Cakupan Baris dan Kolom, Hasil Nol, Urutan Sort, dan Node Leaf"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-367
  - TC-FA-CAT-368
  - TC-FA-CAT-369
  - TC-FA-CAT-373
  - TC-FA-CAT-374
  - TC-FA-CAT-615
coverage:
  web: automated
---

# Download Tabel Utama: Menu CSV dan XLSX, Nama Berkas, Cakupan Baris dan Kolom, Hasil Nol, Urutan Sort, dan Node Leaf

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke Total Control client CatMain (Pre-setup #20, password `Spectra.env.FA_TC_PASSWORD`) hanya pada langkah 33 sampai 35 untuk TC-615. Hook `after` mengembalikan sesi ke akun default suite (CatMain).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (Total Asset 0 sampai 29). Data Pre-setup #20 (CatMain), hanya dibaca: node `Monitor` (Code `ELEC-MN`, leaf, Total Asset 0) di bawah `Electronics`. Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Kemampuan membaca berkas CSV dan XLSX yang terunduh (nama berkas, jumlah baris, baris header) disediakan tim FE; asersi isi sel, BOM, dan tipe sel ada di spec berkelas binary buffer (spec 109).
- State yang diubah spec: Column Visibility tabel utama (langkah 15 dan 19). Hook `after` memulihkan preferensi kolom dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-367: Menu Download dan nama berkas

1. Klik icon Download
2. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`
3. Klik `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas `Categories.csv` terunduh
6. Klik icon Download lalu `Download as XLSX`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas `Categories.xlsx` terunduh

### TC-FA-CAT-368: Cakupan baris export

9. Klik icon Download lalu `Download as CSV` (tanpa Search/Filter, pagination 10)
10. Verifikasi berkas memuat seluruh 30 baris node terpilih, bukan hanya 10 baris halaman aktif
11. Ketik Search `Seed Cat 1`, tekan Enter
12. Klik icon Download lalu `Download as CSV`
13. Verifikasi berkas hanya memuat 11 baris yang cocok (`Seed Cat 1` dan `Seed Cat 10` sampai `Seed Cat 19`)
14. Klik `✕` pada Search, tekan Enter

### TC-FA-CAT-369: Cakupan kolom export mengikuti Column Visibility

15. Klik header Actions (⋯) lalu hilangkan centang kolom `Code` pada overlay
16. Klik icon Download lalu `Download as CSV`
17. Verifikasi tidak ada toast atau peringatan
18. Verifikasi berkas tidak memuat kolom `Code`
19. Klik header Actions (⋯) lalu centang kembali kolom `Code` pada overlay
20. Klik icon Download lalu `Download as CSV`
21. Verifikasi berkas memuat kembali kolom `Code`

### TC-FA-CAT-373: Download pada hasil nol baris

22. Ketik Search `tidak-ada-xyz`, tekan Enter
23. Verifikasi Title `No results found` tampil
24. Verifikasi tombol Download tetap aktif
25. Klik icon Download lalu `Download as CSV`
26. Verifikasi tidak ada toast
27. Verifikasi berkas hanya berisi baris header kolom yang visible tanpa baris data
28. Klik `✕` pada Search, tekan Enter

### TC-FA-CAT-374: Urutan baris berkas mengikuti Sort aktif

29. Klik header Total Asset dua kali (Descending)
30. Klik icon Download lalu `Download as CSV`
31. Verifikasi baris berkas berurut Total Asset menurun mengikuti tabel
32. Klik header Total Asset ketiga kali (Netral)

### TC-FA-CAT-615: Node leaf (genuine empty)

33. Logout dari akun Total Control client CatMany
34. Login sebagai Total Control client CatMain (Pre-setup #20)
35. Buka Fixed Asset > Settings > Categories
36. Klik node `Monitor` (leaf) di Sidebar Category Tree
37. Verifikasi tabel menampilkan empty state dengan title `No subcategory yet`
38. Verifikasi empty state menampilkan description `This category does not have any subcategories.`
39. Verifikasi Search, Filter, dan Download tetap tampil
40. Klik Download > `Download as CSV`
41. Verifikasi tidak ada toast
42. Verifikasi berkas `Categories.csv` hanya berisi baris header kolom yang visible, tanpa baris data
43. Klik icon Filter lalu buka dropdown Modified By
44. Verifikasi dropdown Modified By menampilkan teks `No options available`

## Notes

- Langkah penghubung (S-03): langkah 14, 28, 32 (mengembalikan Search dan Sort ke default, S-09); langkah 33 sampai 35 (ganti akun eksplisit ke client CatMain, S-07).
- Ambang sekitar 35 langkah terlampaui (44 langkah). Alasan: seluruh TC berupa fungsi Download tabel utama pada satu halaman dan satu kelas harness (fungsional; asersi berkas terbatas pada nama, baris, dan header); tiap TC berdiri sendiri dan kegagalan satu TC tidak membuat TC lain kehilangan makna. TC-615 memakai client CatMain karena node leaf `Monitor` hanya ada di Pre-setup #20.
- Asersi "tidak ada toast" (langkah 4, 7, 17, 26, 41) diletakkan segera setelah pemicu dan sebelum asersi berkas (butir 8b.11).
- Temuan untuk QA:
  - TC-368 menyebut "Seed Cat 1 dan Seed Cat 10 sampai Seed Cat 19" sebagai isi berkas; spec mengasersi jumlah dan kecocokan baris, sedangkan nilai sel berkas ada di kelas binary buffer.
  - TC-615 tidak menyebut cara memastikan dropdown Modified By dimuat sebelum dibaca; spec membuka dropdown lalu mengasersi teksnya.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
