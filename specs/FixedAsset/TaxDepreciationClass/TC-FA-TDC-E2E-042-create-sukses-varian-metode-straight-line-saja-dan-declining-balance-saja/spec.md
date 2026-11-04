---
id: TC-FA-TDC-E2E-042-create-sukses-varian-metode-straight-line-saja-dan-declining-balance-saja
title: "Create Sukses - Varian Metode Straight Line Saja dan Declining Balance Saja"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-108
  - TC-FA-TDC-109
coverage:
  web: automated
---

# Create Sukses - Varian Metode Straight Line Saja dan Declining Balance Saja

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; setelah dua Create tabel berisi 9 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-02` dan `KHS-03` belum ada. Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`); Class Name `Kelompok khusus uji 2` dan `Kelompok khusus uji 3`. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Pemulihan: hook `after` menghapus `KHS-02` dan `KHS-03` lewat API (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-108: Submit Create class Non-building dengan Straight Line saja

1. Klik `+ Class` di toolbar
2. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
3. Isi Class Code `KHS-02`
4. Isi Class Name `Kelompok khusus uji 2`
5. Pilih Asset Type `Non-building`
6. Isi Useful Life `16`
7. Pilih Allowed Methods `Straight Line`
8. Klik `[Submit]`
9. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
10. Verifikasi baris `KHS-02`: Straight Line Rate "6.25%", Declining Balance Rate "—", Allowed Methods "Straight Line"

### TC-FA-TDC-109: Submit Create class Non-building dengan Declining Balance saja

11. Tunggu toast lama hilang otomatis
12. Klik `+ Class` di toolbar
13. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
14. Isi Class Code `KHS-03`
15. Isi Class Name `Kelompok khusus uji 3`
16. Pilih Asset Type `Non-building`
17. Isi Useful Life `10`
18. Pilih Allowed Methods `Declining Balance`
19. Klik `[Submit]`
20. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
21. Verifikasi baris `KHS-03`: Straight Line Rate "—", Declining Balance Rate "20%", Allowed Methods "Declining Balance"

## Notes

- Langkah penghubung (S-03): langkah 11 (menunggu toast sukses sebelumnya hilang otomatis supaya toast berikutnya tidak lulus semu).
- Tabel berisi 8 baris pada langkah 10 dan 9 baris pada langkah 21 (7 seed ditambah class milik spec), sehingga baris target tampil tanpa Search (8b.13, R-23).
- Pembagian TC lintas spec: TC-FA-TDC-110 (Create berhasil mereset Search, Filter, dan sort pada tabel lebih dari 10 class) ada di spec `TC-FA-TDC-E2E-233-create-berhasil-mengosongkan-search-clear-filter-dan-sort-default-di-halaman-dua`.
- Temuan untuk QA:
  - Post Condition TC-FA-TDC-108 a dan TC-FA-TDC-109 a (rate metode lain tidak disimpan pada versi pertama) tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01). Sisi tampilan tabel ("—") sudah diasersi di Expected.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
