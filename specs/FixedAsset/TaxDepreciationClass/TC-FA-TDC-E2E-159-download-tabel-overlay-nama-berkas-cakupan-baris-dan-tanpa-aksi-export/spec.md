---
id: TC-FA-TDC-E2E-159-download-tabel-overlay-nama-berkas-cakupan-baris-dan-tanpa-aksi-export
title: "Download Tabel: Overlay, Nama Berkas, Cakupan Baris, dan Tanpa Aksi Export"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-564
  - TC-FA-TDC-565
  - TC-FA-TDC-566
  - TC-FA-TDC-567
  - TC-FA-TDC-568
  - TC-FA-TDC-914
coverage:
  web: automated
---

# Download Tabel: Overlay, Nama Berkas, Cakupan Baris, dan Tanpa Aksi Export

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), dua isi tabel berurutan:
  - Isi tabel A (TC-FA-TDC-564, 565, 566, 914), kunci `exampleData`: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-4 berstatus Active.
  - Isi tabel B (TC-FA-TDC-567 dan 568), kunci `exampleDataPlus17`: 26 class, yaitu sembilan class Example Data ditambah 17 class Active TDC-01 sampai TDC-17 (Asset Type Building, Allowed Methods Straight Line, Class Name `Kelas uji 01` sampai `Kelas uji 17`); urutan default Class Code A-Z: sembilan class Example Data lalu TDC-01 sampai TDC-17.
- Kemampuan teknis: seeding isi tabel lewat API; membuka berkas unduhan CSV dan XLSX (jumlah baris, sheet) disediakan tim FE; Overlay Download, Filter, dan Search tabel utama.
- State global yang diubah: isi tabel diganti ke isi tabel B pada langkah 27. Isi tabel dipulihkan ke isi tabel A lewat seeding API di hook `after`.

## Test Steps

### TC-FA-TDC-564: Screening Overlay Download

1. Klik icon Download
2. Verifikasi Overlay tampil menempel pada icon Download tanpa backdrop
3. Verifikasi Overlay memuat dua opsi `Download as CSV` dan `Download as XLSX`
4. Tutup Overlay Download

### TC-FA-TDC-565: Download CSV: nama berkas dan tanpa toast sukses

5. Klik icon Download
6. Klik `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas `Tax-Depreciation-Class.csv` terunduh

### TC-FA-TDC-566: Download XLSX: nama berkas, sheet Sheet1, dan tanpa toast sukses

9. Klik icon Download
10. Klik `Download as XLSX` lalu buka berkas
11. Verifikasi tidak ada toast sukses
12. Verifikasi berkas `Tax-Depreciation-Class.xlsx` terunduh
13. Verifikasi berkas memiliki satu sheet bernama `Sheet1`

### TC-FA-TDC-914: Tidak ada aksi Export pada Bulk Action Bar, menu baris, maupun toolbar

14. Centang baris NB-4 (Active)
15. Verifikasi Bulk Action Bar memuat `Deactivate` dan `Delete`
16. Verifikasi Bulk Action Bar tidak memuat aksi `Export`
17. Klik tombol `⋯` pada baris NB-4
18. Verifikasi menu baris NB-4 memuat `Edit` dan `Delete`
19. Verifikasi menu baris NB-4 tidak memuat `Export`
20. Tutup menu baris NB-4
21. Verifikasi toolbar tabel dari kiri ke kanan memuat Search, Filter, Download, Changelog, dan `+ Class`
22. Verifikasi toolbar tidak memuat tombol `Export`
23. Klik icon Download
24. Verifikasi unduhan daftar hanya tersedia lewat Download: Overlay memuat `Download as CSV` dan `Download as XLSX`
25. Tutup Overlay Download
26. Hapus centang baris NB-4

### TC-FA-TDC-567: Download tanpa Search dan Filter memuat seluruh baris lintas halaman

27. Ganti isi tabel menjadi isi tabel B (26 class) lewat seeding API, lalu muat ulang halaman
28. Pastikan tidak ada Search dan Filter aktif dan tabel berada di halaman 1 (10 baris)
29. Klik icon Download
30. Klik `Download as CSV` lalu buka berkas
31. Verifikasi berkas memuat 26 baris data ditambah baris header (bukan hanya 10 baris halaman aktif)

### TC-FA-TDC-568: Download dengan Search dan Filter aktif hanya memuat baris yang cocok

32. Ketik Search `TDC`, tekan Enter
33. Terapkan Filter Asset Type `Building`
34. Klik icon Download
35. Klik `Download as CSV` lalu buka berkas
36. Verifikasi berkas hanya memuat 17 baris TDC-01 sampai TDC-17 ditambah baris header

## Notes

- Urutan TC dalam spec: TC-FA-TDC-564, 565, 566, 914, 567, 568. Empat TC pertama memakai isi tabel A (sembilan class); TC-FA-TDC-567 dan 568 memakai isi tabel B (26 class) sehingga diletakkan sesudahnya dan isi tabel diganti pada langkah 27.
- P-10: spec ini mencampur TC yang mengasersi UI Download (TC-FA-TDC-564 dan 914) dengan TC yang mengasersi isi berkas (butir sheet TC-FA-TDC-566, TC-FA-TDC-567, TC-FA-TDC-568) pada alur Download tabel yang sama. Dalam tiap TC klausa UI diletakkan sebelum klausa isi berkas, dan tiap klausa punya `Verifikasi` sendiri (S-01). Alur klik Download lalu buka berkas tidak dapat dipisah dari asersi UI di sampingnya.
- Alasan lebih dari sekitar 35 langkah (36 langkah): satu topik (Download tabel utama), semua blok memakai alur Download yang sama dengan tabel yang sama, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak menghapus makna blok lain.
- Urutan `Verifikasi` pada langkah 7 dan 8, serta 11 sampai 13: asersi tidak ada toast sukses diletakkan segera setelah pemicu (klik pilihan format) dan sebelum asersi berkas terunduh yang menjadi anchor positif bahwa respons sudah diproses (8b.11).
- Langkah penghubung (S-03): langkah 4, 20, 25 (menutup Overlay atau menu), langkah 26 (menghapus centang baris NB-4), langkah 27 (mengganti isi tabel lewat seeding API), dan langkah 28 (memastikan tabel tanpa Search, Filter, dan di halaman 1; langkah TC tanpa Expected). Tabel isi A memuat sembilan baris pada satu halaman; baris NB-4 tidak perlu dicari lewat Search (8b.13).
- Asersi absence langkah 16, 19, dan 22 didahului anchor positif langkah 15, 18, dan 21 (aksi, opsi, atau ikon lain pada permukaan yang sama tampil; 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-565 dan 566 Expected "tidak ada toast sukses" tidak memberi langkah observasi spesifik; spec mengasersinya sesudah pemicu klik pilihan format (8b.11).
  - TC-FA-TDC-566, 567, dan 568: TC tidak menyebut cara membuka berkas (aplikasi atau pembaca) maupun lokasi unduhan; spec memakai kemampuan membuka berkas yang disediakan tim FE.
  - TC-FA-TDC-914 butir d ("unduhan daftar hanya tersedia lewat Download") tidak memberi asersi negatif untuk jalur unduh lain selain butir a, b, dan c; spec mengasersi bahwa Overlay Download memuat dua opsi.
  - Email akun Total Control tidak tertulis di TC.
