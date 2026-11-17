---
id: TC-FA-TDC-E2E-049-create-validasi-regulation-reference-asset-type-dan-useful-life-kosong
title: "Create - Validasi Regulation Reference, Asset Type, dan Useful Life Kosong"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-152
  - TC-FA-TDC-153
  - TC-FA-TDC-154
  - TC-FA-TDC-155
  - TC-FA-TDC-156
sourceRules: ["V-09", "§4.1.2#r1", "V-10", "F-FATDC-01.k4d", "V-11", "F-FATDC-01.k4f", "§4.1.2#p4", "T-01"]
smoke: []
dependsOn: []
trace:
  "V-09": 3
  "§4.1.2#r1": [5, 25]
  "V-10": 9
  "F-FATDC-01.k4d": [10, 11]
  "V-11": 15
  "F-FATDC-01.k4f": [16, 18]
  "§4.1.2#p4": 17
  "T-01": 23
coverage:
  web: automated
---

# Create - Validasi Regulation Reference, Asset Type, dan Useful Life Kosong

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; sesudah satu Create tabel berisi 8 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-R2` (tersimpan); `KHS-A1` dan `KHS-U1` tidak disimpan. Data Uji dasar: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok uji validasi`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`. Nilai uji: Regulation Reference 256 karakter `A`, 255 karakter `A`, dan `  PMK 72/2023  ` (dua spasi di awal dan akhir). Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Pemulihan: hook `after` menghapus `KHS-R2` lewat API (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-152: Create - Regulation Reference 256 karakter ditolak saat mengetik

1. Klik `+ Class` di toolbar
2. Tempel 256 karakter `A` pada Regulation Reference
3. Verifikasi caption "Max. 255 characters" muncul pada Regulation Reference

### TC-FA-TDC-153: Create - Regulation Reference tepat 255 karakter diterima

4. Ganti isi Regulation Reference dengan 255 karakter `A`
5. Verifikasi tidak ada caption error pada Regulation Reference

### TC-FA-TDC-155: Create - Asset Type belum dipilih ditolak

6. Klik `[Clear Field]`
7. Isi Regulation Reference, Class Code `KHS-A1`, dan Class Name sesuai Data Uji; biarkan Asset Type belum dipilih
8. Klik `[Submit]`
9. Verifikasi caption "Asset type must not be empty" muncul pada Asset Type
10. Verifikasi Drawer tetap terbuka
11. Verifikasi tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru (tidak ada data tersimpan)

### TC-FA-TDC-156: Create - Useful Life kosong pada Asset Type Non-building ditolak

12. Klik `[Clear Field]`
13. Isi field lain sesuai Data Uji dengan Class Code `KHS-U1`; biarkan Useful Life kosong
14. Klik `[Submit]`
15. Verifikasi caption "Useful life must not be empty" muncul pada Useful Life
16. Verifikasi Drawer tetap terbuka
17. Verifikasi dialog Save Changes tidak muncul
18. Verifikasi tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru (tidak ada data tersimpan)

### TC-FA-TDC-154: Create - Regulation Reference dengan spasi tepi disimpan ter-trim

19. Klik `[Clear Field]`
20. Isi field lain sesuai Data Uji dengan Class Code `KHS-R2`
21. Ketik `  PMK 72/2023  ` pada Regulation Reference
22. Klik `[Submit]`
23. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
24. Klik link Class Code `KHS-R2`
25. Verifikasi pada Drawer Edit `KHS-R2`, Regulation Reference tampil "PMK 72/2023" tanpa spasi tepi
26. Tutup Drawer Edit dengan klik ikon ✕

## Notes

- Langkah penghubung (S-03): langkah 6, 12, dan 19 (`[Clear Field]` mengosongkan form dan caption sebelum kasus berikutnya; S-09), langkah 4 ("Ganti isi" Regulation Reference menggantikan 256 karakter sebelumnya), langkah 26 (menutup Drawer Edit yang bersih).
- Urutan TC: TC-FA-TDC-154 (aksi sukses dan membuka Drawer Edit) diletakkan paling akhir, sesudah semua validasi yang diblokir (S-10); urutan TC lain mengikuti satu pembukaan Drawer untuk kasus tanpa submit (prinsip 3).
- Tabel berisi 8 baris pada langkah 24 sehingga `KHS-R2` tampil tanpa Search (8b.13, R-23).
- Asersi absence langkah 5 didahului anchor caption pada langkah 3; asersi absence langkah 17 didahului anchor positif langkah 16 (Drawer masih terbuka pada permukaan yang sama; 8b.2).
- Pembagian TC lintas spec: validasi Useful Life batas dan Allowed Methods kosong (TC-FA-TDC-157 sampai 159) ada di spec `TC-FA-TDC-E2E-050-create-validasi-useful-life-batas-dan-allowed-methods-kosong`; validasi Regulation Reference kosong (TC-FA-TDC-151) ada di spec `TC-FA-TDC-E2E-048-create-class-name-trim-duplikat-diizinkan-dan-regulation-reference-kosong`.
- Temuan untuk QA:
  - TC-FA-TDC-156 Expected b menyebut "dialog Save Changes tidak muncul"; dialog itu mode Edit (D-09), sedangkan Drawer Create tidak punya dialog tersebut. Spec mengasersinya sesuai TC.
  - TC-FA-TDC-154 Expected b membuka Drawer Edit tanpa langkah di LK TC; spec menambah klik link Class Code (langkah 24) karena Expected b menyebutnya.
  - Post Condition TC-FA-TDC-152, 153, 155, dan 156 ("Tidak ada data berubah dan tidak ada entri log") tidak punya langkah observasi di TC; spec mengasersi data lewat jumlah baris tabel pada Expected TC-FA-TDC-155 b dan TC-FA-TDC-156 b dan tidak mengasersi entri log (S-01). Post Condition TC-FA-TDC-154 ("Regulation Reference tersimpan ter-trim") sudah diasersi di Expected b.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
