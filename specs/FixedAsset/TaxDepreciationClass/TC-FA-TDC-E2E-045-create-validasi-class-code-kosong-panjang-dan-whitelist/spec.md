---
id: TC-FA-TDC-E2E-045-create-validasi-class-code-kosong-panjang-dan-whitelist
title: "Create - Validasi Class Code Kosong, Panjang, dan Whitelist Karakter"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-135
  - TC-FA-TDC-136
  - TC-FA-TDC-137
  - TC-FA-TDC-138
  - TC-FA-TDC-139
coverage:
  web: automated
---

# Create - Validasi Class Code Kosong, Panjang, dan Whitelist Karakter

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (semua Submit diblokir validasi). Data Uji dasar (field selain Class Code): Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok uji validasi`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`. Nilai Class Code uji: kosong, tiga spasi, `ABCDEFGHIJKLMNOP` (16 karakter), `ABCDEFGHIJKLMNO` (15 karakter), `NB 1`, `NB#1`, `NB/1`, `NB@1`, `NBé1`, `Ab-1_2.x`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-135: Create - Class Code kosong atau hanya spasi ditolak

1. Klik `+ Class` di toolbar
2. Isi field lain sesuai Data Uji dasar; biarkan Class Code kosong
3. Klik `[Submit]`
4. Verifikasi caption "Class code must not be empty" muncul pada Class Code (Class Code kosong)
5. Isi Class Code dengan tiga spasi
6. Klik `[Submit]`
7. Verifikasi caption "Class code must not be empty" muncul pada Class Code (tiga spasi)
8. Verifikasi Drawer tetap terbuka
9. Verifikasi tidak ada toast sukses
10. Verifikasi tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru (tidak ada data tersimpan)

### TC-FA-TDC-136: Create - Class Code 16 karakter ditolak saat mengetik

11. Klik `[Clear Field]`
12. Ketik `ABCDEFGHIJKLMNOP` pada Class Code
13. Verifikasi caption "Max. 15 characters" muncul pada Class Code
14. Klik `[Submit]`
15. Verifikasi tidak ada Submit yang berhasil: Drawer tetap terbuka dan tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru

### TC-FA-TDC-137: Create - Class Code tepat 15 karakter diterima

16. Ganti isi Class Code dengan `ABCDEFGHIJKLMNO`
17. Verifikasi tidak ada caption error pada Class Code
18. Verifikasi nilai tampil utuh 15 karakter di field Class Code

### TC-FA-TDC-138: Create - Class Code berisi karakter di luar whitelist ditolak

19. Ganti isi Class Code dengan `NB 1`
20. Verifikasi caption "Class code contains invalid characters" muncul segera (`NB 1`)
21. Ganti isi Class Code dengan `NB#1`
22. Verifikasi caption "Class code contains invalid characters" muncul segera (`NB#1`)
23. Ganti isi Class Code dengan `NB/1`
24. Verifikasi caption "Class code contains invalid characters" muncul segera (`NB/1`)
25. Ganti isi Class Code dengan `NB@1`
26. Verifikasi caption "Class code contains invalid characters" muncul segera (`NB@1`)
27. Ganti isi Class Code dengan `NBé1`
28. Verifikasi caption "Class code contains invalid characters" muncul segera (`NBé1`)

### TC-FA-TDC-139: Create - Class Code dengan huruf, angka, tanda hubung, underscore, dan titik diterima

29. Ganti isi Class Code dengan `Ab-1_2.x`
30. Verifikasi tidak ada caption error pada Class Code setelah jeda debounce
31. Verifikasi nilai `Ab-1_2.x` tampil utuh
32. Klik `[Clear Field]`
33. Klik ikon ✕ pada Drawer

## Notes

- Langkah penghubung (S-03): langkah 11 dan 32 (`[Clear Field]` mengosongkan form dan caption sebelum kasus berikutnya; S-09), langkah 16, 19, 21, 23, 25, 27, dan 29 ("Ganti isi" Class Code menggantikan nilai sebelumnya, mengikuti pola TC-FA-TDC-138), langkah 33 (menutup Drawer yang bersih sesudah Clear Field).
- Satu pembukaan Drawer dipakai untuk seluruh kasus tanpa submit yang berhasil (prinsip 3, halaman yang sama dipakai berulang); kasus yang diblokir Submit (TC-FA-TDC-135) diletakkan lebih dulu.
- Asersi absence pada langkah 9, 17, dan 30 didahului anchor positif: caption error sebelumnya ada pada Drawer yang sama (langkah 4, 7, 13, dan 28) dan nilai field tampil (langkah 18 dan 31); langkah 10 dan 15 memverifikasi jumlah baris seed (positif), bukan ketiadaan baris.
- Pembagian TC lintas spec: validasi Class Code duplikat (TC-FA-TDC-140 sampai 143) ada di spec `TC-FA-TDC-E2E-046-create-validasi-class-code-duplikat-debounce-dan-trim`.
- Temuan untuk QA:
  - TC-FA-TDC-136 Expected b menyebut "Submit/Save"; Drawer Create hanya memiliki `[Submit]` (`[Save]` ada di mode Edit). Spec memakai `[Submit]` dan menambah langkah klik `[Submit]` (langkah 14) karena LK TC tidak memuat klik tersebut sementara Expected b menyebutnya.
  - Post Condition TC-FA-TDC-135, 136, 137, 138, dan 139 ("Tidak ada data berubah dan tidak ada entri log") tidak punya langkah observasi di TC; spec hanya mengasersi data lewat jumlah baris tabel pada Expected TC-FA-TDC-135 c dan TC-FA-TDC-136 b dan tidak mengasersi entri log (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
