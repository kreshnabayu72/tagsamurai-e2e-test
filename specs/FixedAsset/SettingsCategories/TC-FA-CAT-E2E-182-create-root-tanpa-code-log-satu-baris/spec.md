---
id: TC-FA-CAT-E2E-182-create-root-tanpa-code-log-satu-baris
title: "Create Root Tanpa Code: Code Hasil Generate dan Changelog Satu Baris per Kategori"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-166
  - TC-FA-CAT-169
coverage:
  web: automated
---

# Create Root Tanpa Code: Code Hasil Generate dan Changelog Satu Baris per Kategori

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Dinamis (dibuat spec): `Log Gen Cat {runId}-182` (tanpa Code) dan `Code Log Cat` (Code hasil generate `CLC`, literal karena Code diturunkan dari nama). Hook `before` menghapus sisa kategori L1 `Code Log Cat`; hook `after` menghapus kedua kategori. Seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Changelog kategori bersuffix unik sehingga baseline jumlah baris adalah nol (S-12); `Code Log Cat` dipilih lewat filter Category Name yang sama dan baseline dicatat di langkah 9 sebelum aksi.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-166: Satu baris log per kategori

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Log Gen Cat {runId}-182` dan biarkan Code kosong
3. Klik `[Submit]`
4. Buka Modal Changelog
5. Filter Category Name `Log Gen Cat {runId}-182`
6. Verifikasi Changelog memuat tepat satu baris Create dengan Field `Category Name` Old `—` New `Log Gen Cat {runId}-182`
7. Tutup Modal Changelog

### TC-FA-CAT-169: Create tanpa Code menulis Code hasil generate

8. Buka Modal Changelog, filter Category Name `Code Log Cat`, dan catat jumlah baris (baseline), lalu tutup Modal Changelog
9. Klik `[+] Category` pada sidebar
10. Isi Category Name `Code Log Cat` dan biarkan Code kosong
11. Klik `[Submit]`
12. Buka Detail kategori `Code Log Cat`
13. Verifikasi Popup Detail menampilkan Code hasil generate `CLC`
14. Tutup Popup Detail
15. Buka Modal Changelog dan filter Category Name `Code Log Cat`
16. Verifikasi Changelog memuat baris Create Field `Category Name` untuk `Code Log Cat` (anchor)
17. Verifikasi jumlah baris Changelog untuk `Code Log Cat` hanya bertambah satu dari baseline dan tidak ada baris Field `Code`
18. Tutup Modal Changelog

## Notes

- Langkah penghubung (S-03): langkah 7, 14, 18 (menutup modal/popup), langkah 8 (mencatat baseline).
- Asersi "tidak ada baris Field `Code`" (TC-166, TC-169) dipenuhi sebagai asersi jumlah: TC-166 memeriksa tepat satu baris (Field `Category Name`) dan TC-169 memeriksa kenaikan satu baris dari baseline dengan anchor baris Create yang tampil (langkah 16). Spec absence kelas g tidak memuat TC ini (S-05); asersi dipertahankan di sini sebagai asersi jumlah (prinsip 13).
- Nama `Code Log Cat` literal tanpa suffix karena Expected Code `CLC` diturunkan dari nama; pembersihan dijamin hook `before` dan `after`.
- Temuan untuk QA:
  - TC-169 tidak menyebut Changelog di langkah; Expected b dipenuhi lewat langkah 15 sampai 17 yang ditambahkan mengikuti TC-166 (cara membuka Changelog).
  - TC-169 memuat kalimat "lalu Submit" tanpa menyebut tombol; spec mengklik `[Submit]`.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
