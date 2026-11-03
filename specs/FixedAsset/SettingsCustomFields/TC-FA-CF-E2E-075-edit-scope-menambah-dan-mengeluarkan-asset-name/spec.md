---
id: TC-FA-CF-E2E-075-edit-scope-menambah-dan-mengeluarkan-asset-name
title: "Edit Scope: Menambah dan Mengeluarkan Asset Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-268
  - TC-FA-CF-269
  - TC-FA-CF-270
  - TC-FA-CF-271
  - TC-FA-CF-272
coverage:
  web: automated
---

# Edit Scope: Menambah dan Mengeluarkan Asset Name

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General; Max custom fields per asset name 20): dipakai `Storage Capacity` (Numeric 0 Decimal Places, Scope {Generator, Pump}, tanpa nilai aset pada Asset Name `Pump`) dan `Rated Power` (Numeric 1 Decimal Place, Scope {Generator, Pump}, bernilai `12.5` pada aset A1 = Asset Name `Pump`). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Storage Capacity` dan `Rated Power` beserta nilai A1) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE, termasuk pemulihan kedua field di tengah spec (lihat Notes).
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-268: Menambah Asset Name ke Scope tanpa nilai yang dibuang disimpan tanpa dialog

2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Tambahkan chip `Compressor` pada Scope
4. Klik `[Save]`
5. Verifikasi dialog `Change Scope` tidak tampil
6. Verifikasi toast sukses `Success, custom field has been updated.` tampil
7. Verifikasi kolom Scope baris `Storage Capacity` menampilkan badge `Compressor`, badge `Generator`, dan chip `+1 more`

### TC-FA-CF-272: Mengubah Scope Specific ke General pada field bernilai aset

8. Klik row action `⋯` > `Edit` pada baris `Rated Power`
9. Pilih Scope `General`
10. Tunggu toast lama hilang otomatis
11. Klik `[Save]`
12. Verifikasi dialog `Change Scope` tidak tampil karena tidak ada nilai aset di luar cakupan baru dan tidak ada nilai Global yang dibuang
13. Verifikasi toast sukses `Success, custom field has been updated.` tampil
14. Verifikasi kolom Scope baris `Rated Power` menampilkan `General`
15. Buka Detail aset `A1`
16. Verifikasi nilai aset `A1` untuk field `Rated Power` tetap ada
17. Kembali ke Fixed Asset > Settings > Custom Fields (tab General)
18. Pulihkan `Storage Capacity` dan `Rated Power` ke baseline (Scope {Generator, Pump}; nilai `12.5` pada aset `A1`) lewat seed API
19. Muat ulang halaman (F5)
20. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-271: Mengeluarkan Asset Name tanpa nilai aset tidak menampilkan dialog

21. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
22. Hapus chip `Pump` dari Scope
23. Klik `[Save]`
24. Verifikasi dialog `Change Scope` tidak tampil
25. Verifikasi toast sukses `Success, custom field has been updated.` tampil

### TC-FA-CF-269: Mengeluarkan Asset Name yang aset-nya bernilai menampilkan dialog Change Scope

26. Klik row action `⋯` > `Edit` pada baris `Rated Power`
27. Hapus chip `Pump` dari Scope
28. Klik `[Save]`
29. Verifikasi dialog warning `Change Scope` dengan teks `Switching scope will discard the values currently stored for assets outside the new scope. This action cannot be undone.` serta tombol `[Cancel]` dan `[Change Scope]` tampil

### TC-FA-CF-270: Confirm Change Scope membuang nilai aset di luar cakupan baru

30. Tunggu toast lama hilang otomatis
31. Klik `[Change Scope]`
32. Verifikasi toast sukses `Success, custom field has been updated.` tampil
33. Verifikasi kolom Scope baris `Rated Power` menampilkan `Generator`
34. Buka Detail aset `A1` (Asset Name `Pump`)
35. Verifikasi nilai aset `A1` untuk field `Rated Power` dibuang

## Notes

- Urutan TC di spec: 268, 272, 271, 269, 270. TC-FA-CF-268 dan 272 mengubah Scope `Storage Capacity` dan `Rated Power`, padahal TC-FA-CF-271, 269, dan 270 membutuhkan Scope {Generator, Pump}; karena itu kedua field dipulihkan lewat seed di antara keduanya. TC-FA-CF-269 dan 270 berantai pada dialog `Change Scope` yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 20 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 17 sampai 19 (kembali dari Detail aset, memulihkan kedua field lewat seed, dan memuat ulang halaman supaya tabel mencerminkan seed), langkah 31 (mengonfirmasi dialog `Change Scope` yang menjadi aksi TC-FA-CF-270).
- Langkah penghubung toast (S-03, R-22): langkah 10 dan 30 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-271 menyebut "Save sukses" tanpa toast; spec mengasersi toast sukses sebagai bukti Save sukses.
  - Halaman Detail aset `A1` dan cara membukanya tidak dijelaskan di TC; spec menulisnya persis seperti TC.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
