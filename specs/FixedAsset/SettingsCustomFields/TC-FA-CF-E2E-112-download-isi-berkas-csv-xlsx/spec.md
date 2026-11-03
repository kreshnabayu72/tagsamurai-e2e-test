---
id: TC-FA-CF-E2E-112-download-isi-berkas-csv-xlsx
title: "Download: Isi Sel, BOM, dan Sheet Berkas CSV dan XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-426
  - TC-FA-CF-427
  - TC-FA-CF-428
  - TC-FA-CF-430
  - TC-FA-CF-431
coverage:
  web: automated
---

# Download: Isi Sel, BOM, dan Sheet Berkas CSV dan XLSX

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`). Kelas harness: binary buffer (isi berkas unduhan).
- Akun aktor pertama: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (langkah 15 dan 16, Ganti akun untuk TC-FA-CF-430): Total Control Company Nama Khusus (Pre-setup #37) dengan email mengikuti pola `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Nama Khusus (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_TC_NAMAKHUSUS_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11, General Settings Date Format `dd/MM/yy` dan Time Format 24 jam) dengan baseline tab General (Pre-setup #12) yang dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` (fixture belum ada, disediakan tim FE); baris yang dipakai: `Asset Serial Tag` (Active, Required Yes, Modified By Budi Santoso, Last Updated 17/10/26 10:45), `Storage Capacity` (Required No), `Equipment Class` (Dropdown `Class A`, `Class B`, `Class C`, Scope `Compressor`, `Generator`, `Pump`), `Depreciated Ratio` (Percentage 2 Decimal Places, Inactive), dan `Total Cost` (Formula, Placeholder, Value Type, dan Required kosong). Company Nama Khusus (Pre-setup #37) dengan field `Cap, "Pump"` pada tab General, dirujuk lewat fixture baru `Fixture.faCustomFields.namaKhusus`. Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data custom field.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: penangkapan berkas unduhan dan pembacaan buffer berkas (encoding dan BOM CSV, nilai sel CSV, daftar sheet XLSX), disediakan tim FE.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CF-426: Transformasi sel berkas Download per tipe kolom

1. Klik icon Download > `Download as CSV`
2. Verifikasi kolom Active ditulis `Active` pada baris `Asset Serial Tag` dan `Inactive` pada baris `Depreciated Ratio`
3. Verifikasi kolom Required ditulis `Yes` pada baris `Asset Serial Tag` dan `No` pada baris `Storage Capacity`
4. Verifikasi Scope baris `Equipment Class` ditulis seluruh nama dipisah `, ` termasuk yang di balik `+N more`: `Compressor, Generator, Pump`
5. Verifikasi Value Setting baris `Equipment Class` ditulis `Class A, Class B, Class C` (seluruh opsi, bukan `+1 more`)
6. Verifikasi Value Setting baris `Depreciated Ratio` ditulis `2 Decimal Places`
7. Verifikasi nilai kosong (`—`) ditulis `-` pada Placeholder, Value Type, dan Required baris `Total Cost`
8. Verifikasi warna badge tidak ikut ter-export (sel Active hanya berisi teks `Active` atau `Inactive`)

### TC-FA-CF-427: Sel Modified By berkas Download berisi nama lengkap user

9. Klik icon Download > `Download as CSV`
10. Verifikasi sel Modified By baris `Asset Serial Tag` berisi `Budi Santoso`

### TC-FA-CF-428: Sel Last Updated berkas Download mengikuti format General Settings

11. Klik icon Download > `Download as CSV`
12. Verifikasi sel Last Updated baris `Asset Serial Tag` berisi `17/10/26, 10:45`

### TC-FA-CF-431: XLSX berkas Download berisi satu sheet bernama Sheet1

13. Klik icon Download > `Download as XLSX`
14. Verifikasi berkas memuat satu sheet bernama `Sheet1`

### TC-FA-CF-430: CSV berkas Download memakai UTF-8 dengan BOM dan meng-escape koma serta tanda kutip

15. Ganti akun: Logout dari akun Total Control Company Alpha
16. Login sebagai Total Control Company Nama Khusus (Pre-setup #37) dengan `Spectra.env.FA_TC_NAMAKHUSUS_PASSWORD`
17. Buka Fixed Asset > Settings > Custom Fields lewat menu sidebar
18. Klik icon Download > `Download as CSV`
19. Verifikasi berkas CSV berenkoding UTF-8 dengan BOM
20. Verifikasi nilai field `Cap, "Pump"` di berkas dibungkus tanda kutip ganda dengan tanda kutip di dalamnya digandakan (`"Cap, ""Pump"""`)

## Notes

- Spec memuat 20 langkah, di bawah ambang sekitar 35 langkah. Satu kelas harness (binary buffer), satu topik (isi berkas Download), dua Company.
- Urutan TC di spec: 426, 427, 428, 431, lalu 430. TC-FA-CF-430 berada di akhir karena memakai akun lain (Ganti akun, langkah 15 dan 16); akun aktor pertama dan hook `before` adalah Total Control Company Alpha sehingga empat TC pertama tidak butuh ganti akun (S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 17 (membuka halaman setelah ganti akun).
- Kelas harness f (binary buffer) hanya mencakup isi berkas; nama berkas, header kolom, dan jumlah baris diasersi di spec Download fungsional.
- Temuan untuk QA:
  - Email akun Total Control Company Nama Khusus tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1 dengan `{namaCompany}` = Company Nama Khusus, dan akunnya disediakan tim FE.
  - TC-FA-CF-426 Data Uji hanya menyebut baris `Asset Serial Tag`, `Equipment Class`, `Depreciated Ratio`, dan `Total Cost`; Expected b memakai nilai `No` yang tidak ada pada keempat baris itu (Required `Asset Serial Tag` Yes, `Total Cost` kosong). Spec memakai baris `Storage Capacity` (Required No, Pre-setup #12) untuk nilai `No`.
  - TC-FA-CF-426 Expected f ("warna badge tidak ikut ter-export") tidak menyatakan cara memeriksa pada berkas CSV; spec memeriksa bahwa sel Active hanya berisi teks.
  - TC-FA-CF-426 Expected a sampai e tidak menyebut baris untuk tiap klausa; spec memakai baris Data Uji dan Pre-setup #12 (`Asset Serial Tag`, `Depreciated Ratio`, `Equipment Class`, `Total Cost`).
  - TC-FA-CF-430 Langkah Uji tidak menyebut cara mengamati encoding berkas; kemampuan pembacaan buffer disediakan tim FE (Prerequisites).
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
