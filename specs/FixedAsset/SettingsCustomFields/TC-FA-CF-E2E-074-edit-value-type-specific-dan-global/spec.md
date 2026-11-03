---
id: TC-FA-CF-E2E-074-edit-value-type-specific-dan-global
title: "Edit Value Type: Specific ke Global dan Sebaliknya"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-262
  - TC-FA-CF-263
  - TC-FA-CF-264
  - TC-FA-CF-265
  - TC-FA-CF-266
coverage:
  web: automated
---

# Edit Value Type: Specific ke Global dan Sebaliknya

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Rated Power` (Numeric 1 Decimal Place {Generator, Pump} Specific, bernilai `12.5` pada aset A1), `Empty Metric` (Numeric 2 Decimal Places General Specific, tanpa nilai aset), dan `Voltage Spec` (Text {Generator, Pump} Global `220V` untuk `Generator` dan `110V` untuk `Pump`). Aset A1 = Asset Name `Pump`, A2 = Asset Name `Generator`. Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Rated Power`, `Empty Metric`, `Voltage Spec` beserta nilai aset) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-262: Value Type Specific ke Global pada field bernilai aset menampilkan dialog Change to Global Value

2. Klik row action `⋯` > `Edit` pada baris `Rated Power`
3. Pilih Value Type `Global` dan isi Value `Generator` dengan `10` dan `Pump` dengan `20`
4. Klik `[Save]`
5. Verifikasi dialog warning `Change to Global Value` dengan teks `Switching to a global value will discard the values currently stored for individual assets. This action cannot be undone.` serta tombol `[Cancel]` dan `[Change to Global]` tampil

### TC-FA-CF-263: Confirm Change to Global Value membuang nilai aset dan menyimpan nilai Global

6. Klik `[Change to Global]`
7. Verifikasi toast sukses `Success, custom field has been updated.` tampil
8. Verifikasi kolom Value Type baris `Rated Power` menampilkan `Global`
9. Buka Detail aset `A1`
10. Verifikasi nilai individual aset `A1` untuk field `Rated Power` dibuang
11. Verifikasi nilai Global baru tersimpan tanpa bercampur dengan nilai individual
12. Kembali ke Fixed Asset > Settings > Custom Fields (tab General)

### TC-FA-CF-264: Value Type Specific ke Global tanpa nilai aset tersimpan tanpa dialog

13. Klik row action `⋯` > `Edit` pada baris `Empty Metric`
14. Pilih Value Type `Global` dan isi Value dengan `7`
15. Tunggu toast lama hilang otomatis
16. Klik `[Save]`
17. Verifikasi dialog `Change to Global Value` tidak tampil
18. Verifikasi toast sukses `Success, custom field has been updated.` tampil
19. Verifikasi kolom Value Type baris `Empty Metric` menampilkan `Global`

### TC-FA-CF-265: Value Type Global ke Specific selalu menampilkan dialog Change to Specific Value

20. Atur ukuran halaman Pagination menjadi 100
21. Klik row action `⋯` > `Edit` pada baris `Voltage Spec`
22. Pilih Value Type `Specific`
23. Klik `[Save]`
24. Verifikasi dialog warning `Change to Specific Value` dengan teks `Switching to a specific value will discard the global value, and each asset will need its own value. This action cannot be undone.` serta tombol `[Cancel]` dan `[Change to Specific]` tampil

### TC-FA-CF-266: Confirm Change to Specific Value membuang seluruh nilai Global

25. Klik `[Change to Specific]`
26. Verifikasi kolom Value Type baris `Voltage Spec` menampilkan `Specific`
27. Buka Detail aset `A1` (Asset Name `Pump`)
28. Verifikasi nilai Global `110V` tidak lagi tampil pada Detail aset `A1` dan nilai aset dimulai kosong
29. Buka Detail aset `A2` (Asset Name `Generator`)
30. Verifikasi nilai Global `220V` tidak lagi tampil pada Detail aset `A2` dan nilai aset dimulai kosong

## Notes

- Urutan TC di spec: 262, 263, 264, 265, 266. TC-FA-CF-262 dan 263 berantai pada dialog yang sama (aksi `[Save]` yang menampilkan dialog dilanjutkan `[Change to Global]`); TC-FA-CF-265 dan 266 berantai dengan cara yang sama pada `Voltage Spec`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 20 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search; kembali dari Detail aset pada langkah 12 mengembalikan halaman ke ukuran bawaan, dan `Empty Metric` berada di halaman pertama), langkah 12 (kembali dari Detail aset ke halaman Custom Fields).
- Nilai Global yang diisi `10`, `20`, dan `7` serta nilai aset adalah nilai uji literal TC, bukan nama yang unik per run.
- Langkah penghubung toast (S-03, R-22): langkah 15 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-263 tidak menyebut nilai spesifik yang diharapkan pada Detail aset `A1` selain "nilai individual dibuang dan nilai Global baru tersimpan tanpa bercampur"; spec mengasersi kedua klausa itu tanpa menyebut nilai (A1 = `Pump`, Value Global `Pump` = `20`).
  - TC-FA-CF-266 menyebut "nilai aset dimulai kosong"; spec menggabungkannya dengan klausa nilai Global tidak tampil pada tiap Detail aset (S-01, satu butir Expected per aset).
  - Halaman Detail aset `A1` dan `A2` serta cara membukanya tidak dijelaskan di TC; spec menulisnya persis seperti TC.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
