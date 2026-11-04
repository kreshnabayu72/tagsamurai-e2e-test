---
id: TC-FA-TDC-E2E-048-create-class-name-trim-duplikat-diizinkan-dan-regulation-reference-kosong
title: "Create - Class Name Ter-trim, Duplikat Diizinkan, dan Regulation Reference Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-149
  - TC-FA-TDC-150
  - TC-FA-TDC-151
coverage:
  web: automated
---

# Create - Class Name Ter-trim, Duplikat Diizinkan, dan Regulation Reference Kosong

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND; `NB-1` ber-Class Name "Bukan bangunan – Kelompok 1". Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; sesudah dua Create tabel berisi 9 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-N3` dan `KHS-N4` belum ada (tersimpan); `KHS-R1` tidak disimpan. Data Uji dasar (field selain yang diuji): Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok uji validasi` (hanya TC-FA-TDC-151), Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`. Class Name uji: `  Kelompok trim  ` (dua spasi di awal dan akhir) dan `Bukan bangunan – Kelompok 1`; Regulation Reference uji: kosong dan tiga spasi. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Pemulihan: hook `after` menghapus `KHS-N3` dan `KHS-N4` lewat API (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-151: Create - Regulation Reference kosong atau hanya spasi ditolak

1. Klik `+ Class` di toolbar
2. Isi field lain sesuai Data Uji dan Class Code `KHS-R1`; biarkan Regulation Reference kosong
3. Klik `[Submit]`
4. Verifikasi caption "Regulation reference must not be empty" muncul pada Regulation Reference (kosong)
5. Isi Regulation Reference dengan tiga spasi
6. Klik `[Submit]`
7. Verifikasi caption "Regulation reference must not be empty" muncul pada Regulation Reference (tiga spasi)
8. Verifikasi Drawer tetap terbuka
9. Verifikasi tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru (tidak ada data tersimpan)
10. Klik `[Clear Field]`

### TC-FA-TDC-149: Create - Class Name dengan spasi tepi disimpan ter-trim

11. Isi field lain sesuai Data Uji dasar dan Class Code `KHS-N3`
12. Ketik `  Kelompok trim  ` pada Class Name
13. Klik `[Submit]`
14. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
15. Verifikasi baris tabel menampilkan Class Name "Kelompok trim" tanpa spasi tepi

### TC-FA-TDC-150: Create - Class Name sama dengan class lain diizinkan

16. Tunggu toast lama hilang otomatis
17. Klik `+ Class` di toolbar
18. Isi field lain sesuai Data Uji dasar dan Class Code `KHS-N4`
19. Isi Class Name `Bukan bangunan – Kelompok 1`
20. Verifikasi tidak ada caption error pada Class Name
21. Klik `[Submit]`
22. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
23. Verifikasi tabel memuat dua baris dengan Class Name "Bukan bangunan – Kelompok 1" (`NB-1` dan `KHS-N4`)

## Notes

- Langkah penghubung (S-03): langkah 10 (`[Clear Field]` mengosongkan form dan caption sebelum kasus berikutnya; S-09), langkah 16 (menunggu toast sukses hilang otomatis).
- Urutan TC: TC-FA-TDC-151 (validasi diblokir) diletakkan lebih dulu, lalu TC-FA-TDC-149 dan TC-FA-TDC-150 (aksi sukses), mengikuti prinsip validasi yang diblokir sebelum aksi sukses (S-10); satu Drawer dipakai untuk TC-FA-TDC-151 dan TC-FA-TDC-149.
- Tabel berisi 8 baris pada langkah 15 dan 9 baris pada langkah 23, sehingga tidak didahului Search (8b.13, R-23).
- Langkah 20 diletakkan sebelum `[Submit]` karena caption error diasersi pada keadaan form sebelum disimpan (8b.5).
- Pembagian TC lintas spec: validasi Class Name lain (kosong, panjang, emoji) ada di spec `TC-FA-TDC-E2E-047-create-validasi-class-name-kosong-panjang-dan-emoji`; validasi Regulation Reference lain ada di spec `TC-FA-TDC-E2E-049-create-validasi-regulation-reference-asset-type-dan-useful-life-kosong`.
- Temuan untuk QA:
  - Langkah 11 dan 18 mengikuti TC ("field lain sesuai Data Uji dasar"); TC-FA-TDC-149 dan 150 tidak menyebut Class Name pada Data Uji dasar, sedangkan Class Name diuji pada langkah 12 dan 19.
  - TC-FA-TDC-150 Expected c menyebut dua baris ber-Class Name sama tanpa menyebut Search; spec tidak memakai Search karena tabel memuat satu halaman.
  - Post Condition TC-FA-TDC-149 ("Class Name tersimpan ter-trim"), TC-FA-TDC-150 ("duplikat tersimpan tanpa penolakan"), dan TC-FA-TDC-151 ("Tidak ada data berubah dan tidak ada entri log") tidak punya langkah observasi tersendiri di TC; spec tidak mengasersi entri log (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
