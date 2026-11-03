---
id: TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all
title: "Bulk Action Bar: Screening 1 Baris Dicentang, Counter Singular/Plural, Checkbox Header, Select All Lintas Halaman, dan Uncheck dari 100%"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-246
  - TC-FA-GRP-247
  - TC-FA-GRP-248
  - TC-FA-GRP-249
  - TC-FA-GRP-250
coverage:
  web: automated
---

# Bulk Action Bar: Screening 1 Baris Dicentang, Counter Singular/Plural, Checkbox Header, Select All Lintas Halaman, dan Uncheck dari 100%

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): 12 group level 1 kosong `Bulk K01` sampai `Bulk K12` (nama distinct, semuanya memuat huruf `K`) sehingga tabel memuat lebih dari satu halaman (page size default 10). N = jumlah total baris tabel Groups List pada tampilan All Groups (Pre-setup level 1 ditambah 12 group seed), dibaca lewat fixture BE sebelum uji dan bukan dari satu halaman tabel (8b butir 10).
- Spec tidak mengubah data; seleksi dibersihkan antar TC dengan (X) (S-09). Cleanup di `after`: hapus 12 group seed lewat API.

## Test Steps

### TC-FA-GRP-246: Screening Bulk Action Bar saat 1 baris dicentang

1. Centang baris pertama pada halaman 1
2. Verifikasi bar tampil dengan urutan Bulk Action, counter `1 group selected`, Select All ([N] records), dan (X)
3. Klik Bulk Action
4. Verifikasi Bulk Action berisi satu aksi: Delete
5. Tutup menu Bulk Action, lalu klik (X)

### TC-FA-GRP-247: Counter singular/plural dan (X)

6. Centang baris 1
7. Verifikasi counter `1 group selected`
8. Centang baris 2
9. Verifikasi counter `2 groups selected`
10. Uncheck baris 2
11. Verifikasi counter `1 group selected`
12. Centang baris 2 lagi
13. Klik (X)
14. Verifikasi seluruh seleksi dibersihkan
15. Verifikasi bar bulk action tertutup

### TC-FA-GRP-248: Checkbox header

16. Klik checkbox header
17. Verifikasi seluruh baris halaman aktif checked
18. Uncheck checkbox header
19. Verifikasi seluruh baris halaman unchecked
20. Verifikasi bar bulk action hilang
21. Centang 1 baris
22. Verifikasi checkbox header berstatus indeterminate [-]
23. Klik (X)

### TC-FA-GRP-249: Select All lintas halaman dan Unselect All

24. Centang 1 baris, lalu klik Select All ([N] records)
25. Verifikasi counter sama dengan N (seluruh baris yang cocok terseleksi)
26. Klik tombol halaman 2
27. Verifikasi seluruh baris halaman 2 tercentang (seleksi lintas halaman)
28. Verifikasi tombol berubah menjadi Unselect All
29. Klik Unselect All
30. Verifikasi seleksi dibersihkan
31. Verifikasi bar bulk action tertutup

### TC-FA-GRP-250: Uncheck 1 baris dari kondisi 100% terseleksi

32. Klik tombol halaman 1
33. Klik checkbox header lalu Select All ([N] records)
34. Uncheck 1 baris
35. Verifikasi bar bulk action tetap tampil
36. Verifikasi tombol kembali menjadi Select All (N-1 records)
37. Klik (X)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 5, 23, 32, 37: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Seleksi tiap TC dimulai dari keadaan bersih (langkah penghubung klik (X), S-09). TC-249 memakai satu pembukaan layar yang sama dengan TC lain (hook `beforeEach` suite).
- Spec berisi lebih dari 35 langkah. Alasan: lima TC screening Bulk Action Bar satu topik, satu dataset, dan satu kelas (fungsional UI), tiap blok berdiri sendiri; semuanya satu dataset (bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC-246 tidak menyebut cara membuka daftar aksi Bulk Action; spec mengklik Bulk Action untuk membaca isinya.
  - TC-250 Precondition tidak menyebut data; spec memakai dataset 12 group yang sama dengan TC lain pada spec ini.
