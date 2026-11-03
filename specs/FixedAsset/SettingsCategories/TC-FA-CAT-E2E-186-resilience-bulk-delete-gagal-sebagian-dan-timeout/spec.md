---
id: TC-FA-CAT-E2E-186-resilience-bulk-delete-gagal-sebagian-dan-timeout
title: "Resilience Bulk Delete: Gagal Sebagian dan Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-262
  - TC-FA-CAT-271
coverage:
  web: automated
---

# Resilience Bulk Delete: Gagal Sebagian dan Timeout

## Prerequisites

- Mode: FE+BE. Backend nyata; kegagalan 500 dan timeout dipaksa lewat `Spectra.intercept()` di atas backend nyata (bagian 6 konvensi), bukan mock penuh.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; kategori `Heavy Tools` Pre-setup #39 diganti node milik spec.
- Data milik spec (seed API di hook `before` lewat jalur Create resmi, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Bulk Root {runId}-186` | `E186ROOT` | L1; dipilih di sidebar |
  | TC-262 | `Vehicle B {runId}-186` | `E186VB` | anak `Bulk Root`, leaf; menggantikan `Vehicle`; terhapus |
  | TC-262 | `Peripheral {runId}-186` | `E186PERI` | anak `Bulk Root`, internal; terhapus bersama anak |
  | Anak `Peripheral` | `Keyboard {runId}-186` | `E186KB` | leaf |
  | Anak `Peripheral` | `Mouse {runId}-186` | `E186MS` | leaf |
  | TC-262 dan TC-271 | `Heavy Tools {runId}-186` | `E186HT` | anak `Bulk Root`, leaf, tidak ditunjuk Asset Name; menggantikan `Heavy Tools`; gagal terhapus di TC-262 dan dipakai ulang di TC-271 |
  | TC-271 | `Vehicle C {runId}-186` | `E186VC` | anak `Bulk Root`, leaf; menggantikan `Vehicle` |

- Kemampuan intercept jaringan (disediakan tim FE): memaksa respons Delete 500 untuk baris tertentu (`Heavy Tools`), memutus respons Delete (timeout), dan melepas intercept. Intercept dilepas segera setelah pemicu selesai dan di hook `after` (S-09).
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-262: Bulk Delete gagal sebagian karena server: satu toast ringkasan T-14 dan baris gagal tetap terpilih

1. Klik node `Bulk Root {runId}-186` di sidebar
2. Centang checkbox baris `Vehicle B {runId}-186`, `Heavy Tools {runId}-186`, dan `Peripheral {runId}-186`
3. Paksa respons Delete baris `Heavy Tools {runId}-186` gagal 500 lewat intercept jaringan
4. Klik `[Delete]` pada Bulk Action Bar
5. Klik `[Delete]` pada dialog
6. Verifikasi toast error `Error, failed to delete some categories.` tanpa tombol aksi
7. Verifikasi hanya satu toast yang tampil (bukan satu toast per baris)
8. Verifikasi `Vehicle B {runId}-186` terhapus: baris tidak lagi tampil di tabel
9. Verifikasi `Peripheral {runId}-186` terhapus beserta `Keyboard {runId}-186` dan `Mouse {runId}-186`: baris tidak tampil di tabel dan node tidak tampil di sidebar
10. Verifikasi `Heavy Tools {runId}-186` gagal terhapus: baris tetap tampil dan tetap terpilih (checkbox tercentang)
11. Verifikasi daftar di-refresh: tabel memuat `Heavy Tools {runId}-186` dan `Vehicle C {runId}-186` sebagai baris tersisa
12. Hapus intercept
13. Hilangkan centang baris `Heavy Tools {runId}-186`

### TC-FA-CAT-271: Bulk Delete tanpa respons (timeout jaringan): bar dan seleksi dipertahankan

14. Centang checkbox baris `Vehicle C {runId}-186` dan `Heavy Tools {runId}-186`
15. Putus respons Delete lewat intercept jaringan
16. Klik `[Delete]` pada Bulk Action Bar
17. Klik `[Delete]` pada dialog
18. Verifikasi toast error baku `Connection problem. Please try again.` tanpa tombol aksi
19. Verifikasi Bulk Action Bar dipertahankan
20. Verifikasi seleksi dipertahankan (`Vehicle C {runId}-186` dan `Heavy Tools {runId}-186` tetap tercentang)
21. Verifikasi list di-refresh sehingga keadaan nyata terlihat
22. Verifikasi dialog konfirmasi Bulk Delete tetap terbuka
23. Verifikasi tombol `[Delete]` pada dialog kembali enabled setelah toast timeout
24. Hapus intercept
25. Klik `[Cancel]` pada dialog
26. Hilangkan centang kedua baris

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-262 dan TC-271 ada di spec ini; TC-207, TC-211, TC-236, dan TC-240 ada di spec 060.
- Kelas b (fault injection) untuk Bulk Delete, memakai Bulk Action Bar dan data seleksi sendiri.
- Penyesuaian data (S-06, S-12): TC memakai kategori Pre-setup #20 dan #39 (`Vehicle`, `Heavy Tools`, `Peripheral`); spec memakai node milik spec bersuffix `{runId}-186`. `Vehicle B` dan `Vehicle C` memisahkan target TC-262 yang terhapus dari target TC-271.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node `Bulk Root` di sidebar; menghapus intercept; membatalkan dialog lewat `[Cancel]`; menghilangkan centang seleksi (S-09).
- Langkah 11 mengasumsikan `Vehicle C` tampil sebagai baris tersisa karena disiapkan oleh `before` dan tidak termasuk seleksi TC-262.
- Temuan untuk QA:
  - TC-262 Expected b menyebut "daftar di-refresh" tanpa merinci isi; spec mengasersi baris tersisa.
  - TC-271 tidak menyatakan apakah permintaan yang diputus sampai ke server; spec tidak mengasersi state server pasca-timeout.
  - TC-271 Expected b ("list di-refresh agar keadaan nyata terlihat") dan Expected c (dialog tetap terbuka) dinyatakan bersamaan; urutan keduanya di UI tidak dijelaskan, spec mengasersi keduanya tanpa urutan.
