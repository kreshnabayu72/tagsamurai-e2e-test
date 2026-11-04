---
id: TC-FA-TDC-E2E-160-download-isi-berkas-kolom-tampil-teks-active-strip-format-effective-from-dan-angka
title: "Download Isi Berkas: Kolom Tampil, Teks Active, Strip, Format Effective From, dan Angka"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-569
  - TC-FA-TDC-570
  - TC-FA-TDC-571
  - TC-FA-TDC-572
  - TC-FA-TDC-573
coverage:
  web: automated
---

# Download Isi Berkas: Kolom Tampil, Teks Active, Strip, Format Effective From, dan Angka

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData`: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Nilai yang diasersi: NB-1 Active On, Useful Life 4, Straight Line Rate 25%, Used By 5, Effective From `Jan 2026`; NB-4 Effective From `Jan 2026`; NB-OLD Active Off; LAND Useful Life, Straight Line Rate, Declining Balance Rate, Allowed Methods, dan Effective From kosong (`—` di UI); NB-2 Effective From kosong. Format tanggal General Settings company `dd/MM/yy`.
- Kemampuan teknis: membuka berkas unduhan CSV dan XLSX (isi sel, tipe sel) disediakan tim FE; Overlay Column Visibility; Overlay Download; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: kolom Used By disembunyikan lalu ditampilkan kembali dalam spec (langkah 1 sampai 10). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-569: Download hanya memuat kolom yang sedang tampil dan kembali memuat setelah ditampilkan

1. Klik header Actions `⋯`
2. Hapus centang kolom Used By
3. Tutup Overlay Column Visibility
4. Klik icon Download
5. Klik `Download as CSV` lalu buka berkas
6. Verifikasi berkas pertama tidak memuat kolom Used By
7. Klik header Actions `⋯`
8. Centang kolom Used By
9. Tutup Overlay Column Visibility
10. Klik icon Download
11. Klik `Download as CSV` lalu buka berkas
12. Verifikasi berkas kedua memuat kolom Used By

### TC-FA-TDC-570: Download menulis kolom Active sebagai teks Active atau Inactive

13. Klik icon Download
14. Klik `Download as CSV` lalu buka berkas
15. Verifikasi kolom Active baris NB-1 berisi `Active`
16. Verifikasi kolom Active baris NB-OLD berisi `Inactive`

### TC-FA-TDC-571: Download menulis nilai kosong sebagai tanda hubung

17. Klik icon Download
18. Klik `Download as CSV` lalu buka berkas
19. Verifikasi baris LAND: Useful Life, Straight Line Rate, Declining Balance Rate, Allowed Methods, dan Effective From berisi `-`
20. Verifikasi baris NB-2: Effective From berisi `-`
21. Verifikasi sel Effective From baris NB-2 tidak kosong, bukan `—`, dan bukan `null`

### TC-FA-TDC-572: Download menulis Effective From dengan format MMM YYYY bukan format tanggal General Settings

22. Klik icon Download
23. Klik `Download as CSV`
24. Buka berkas dan baca kolom Effective From
25. Verifikasi Effective From baris NB-1 dan NB-4 berisi `Jan 2026`
26. Verifikasi Effective From baris NB-1 dan NB-4 bukan tanggal berformat General Settings seperti `01/01/26`
27. Verifikasi Effective From baris NB-2 berisi `-`

### TC-FA-TDC-573: Download XLSX menulis angka sebagai sel angka tanpa simbol

28. Klik icon Download
29. Klik `Download as XLSX` lalu buka berkas
30. Verifikasi Useful Life baris NB-1 berisi angka `4` bertipe number
31. Verifikasi Used By baris NB-1 berisi angka `5` bertipe number
32. Verifikasi Straight Line Rate baris NB-1 berisi `25` tanpa simbol `%`

## Notes

- Langkah penghubung (S-03): langkah 3 dan 9 (menutup Overlay Column Visibility), langkah 7 sampai 9 (menampilkan kembali kolom Used By; pemulihan Setup Column 8b.14, R-24; TC tidak menyebut `[Save]` sehingga tidak ditulis). Kolom Used By tampil kembali pada langkah 8 sehingga TC berikutnya memakai kolom default.
- Tabel Example Data memuat sembilan baris pada satu halaman; baris target tidak perlu dicari lewat Search (8b.13).
- Seluruh `Verifikasi` isi berkas (kelas f) membaca berkas yang diunduh pada langkah sebelumnya dalam TC yang sama.
- Temuan untuk QA:
  - TC-FA-TDC-569 tidak menyebut cara menyembunyikan dan menampilkan kolom Used By; spec memakai Overlay Column Visibility lewat header Actions `⋯` sesuai pola TC kolom lain.
  - TC-FA-TDC-571 butir a menulis nilai kosong sebagai `-` (tanda hubung berkas) sedangkan UI tabel menulis `—`; spec mengikuti TC. Butir b menyebut baris NB-2 tanpa Effective From, sedangkan butir a tidak mencakup NB-2 pada kolom lain.
  - TC-FA-TDC-572 butir a menyebut `01/01/26` sebagai contoh format tanggal General Settings dd/MM/yy; spec mengasersi bahwa nilai bukan format tanggal tersebut.
  - TC-FA-TDC-573 tidak menyebut nilai Declining Balance Rate NB-1 pada berkas; spec tidak mengasersinya.
  - Email akun Total Control tidak tertulis di TC.
