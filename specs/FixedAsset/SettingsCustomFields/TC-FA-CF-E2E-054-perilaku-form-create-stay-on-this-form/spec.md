---
id: TC-FA-CF-E2E-054-perilaku-form-create-stay-on-this-form
title: "Perilaku Form Create: Checkbox Stay on this Form Dicentang, Tidak Dicentang, dan Create Berulang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-171
  - TC-FA-CF-172
  - TC-FA-CF-173
coverage:
  web: automated
---

# Perilaku Form Create: Checkbox Stay on this Form Dicentang, Tidak Dicentang, dan Create Berulang

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); Asset Name `Pump` sudah ada di baseline.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-054`): `Stay Off {runId}-054` (Text), `Stay One {runId}-054` (Numeric, Decimal Places 2, Scope `Pump`, Required Yes), `Batch 1 {runId}-054`, `Batch 2 {runId}-054`, dan `Batch 3 {runId}-054` (Text).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-054`.
- Kemampuan teknis: pembacaan state checkbox, isi input, dan default kontrol modal Create.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-172: Checkbox Stay tidak dicentang menutup modal dan me-refresh tabel

1. Klik [+ Custom Field]
2. Isi Field Name `Stay Off {runId}-054` dan Data Type `Text`
3. Klik [Submit]
4. Verifikasi modal tertutup
5. Verifikasi toast "Success, custom field has been created." tampil
6. Ketik Search `Stay Off {runId}-054`, tekan Enter
7. Verifikasi tabel ter-refresh dan memuat baris `Stay Off {runId}-054`
8. Klik `(←)` pada kotak Search

### TC-FA-CF-171: Checkbox Stay on this form dicentang mempertahankan modal dan mereset input ke default

9. Klik [+ Custom Field]
10. Isi Field Name `Stay One {runId}-054`, Data Type `Numeric`, Decimal Places `2 (.00)`, Scope `Specific Asset Name` dengan `Pump`, Required Yes
11. Centang `Stay on this form after submitting`
12. Tunggu toast lama hilang otomatis
13. Klik [Submit]
14. Verifikasi toast "Success, custom field has been created." tampil
15. Verifikasi modal tetap terbuka
16. Verifikasi Field Name kosong
17. Verifikasi Data Type belum dipilih
18. Verifikasi Scope `General`
19. Verifikasi Value Type `Specific`
20. Verifikasi Required No
21. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
22. Hapus centang `Stay on this form after submitting`
23. Klik `[✕]`

### TC-FA-CF-173: Create berulang dengan Stay menghasilkan tiga field berturut-turut

24. Klik [+ Custom Field]
25. Centang `Stay on this form after submitting`
26. Tunggu toast lama hilang otomatis
27. Isi Field Name `Batch 1 {runId}-054` dan Data Type `Text`, lalu klik [Submit]
28. Verifikasi toast "Success, custom field has been created." tampil
29. Tunggu toast lama hilang otomatis
30. Isi Field Name `Batch 2 {runId}-054` dan Data Type `Text`, lalu klik [Submit]
31. Verifikasi toast "Success, custom field has been created." tampil
32. Tunggu toast lama hilang otomatis
33. Isi Field Name `Batch 3 {runId}-054` dan Data Type `Text`, lalu klik [Submit]
34. Verifikasi toast "Success, custom field has been created." tampil
35. Verifikasi modal tetap terbuka
36. Hapus centang `Stay on this form after submitting`
37. Klik `[✕]`

### Baris tabel hasil Create

38. Ketik Search `{runId}-054`, tekan Enter
39. Verifikasi tabel menampilkan 5 baris: `Batch 1 {runId}-054`, `Batch 2 {runId}-054`, `Batch 3 {runId}-054`, `Stay Off {runId}-054`, dan `Stay One {runId}-054`
40. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 172, 171, 173 (urutan sumber 171, 172, 173). TC-FA-CF-172 dijalankan lebih dulu karena memakai modal dengan checkbox Stay tidak dicentang (kondisi awal); TC-FA-CF-171 dan TC-FA-CF-173 mencentang checkbox itu.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 6, 8, 9, 11, 22, 23, 24, 25, 36, 37, 38, 40, serta pengisian form dan klik tombol sebagai bagian langkah TC. Langkah 22 dan 36 (hapus centang `Stay on this form after submitting`) mengembalikan form ke kondisi awal sebelum `[✕]` pada langkah 23 dan 37; form identik dengan kondisi awal dianggap bersih (TC-FA-CF-181) sehingga dialog `Unsaved Changes` tidak diharapkan (lihat Temuan untuk QA).
- Expected "tabel di latar belakang ter-refresh dan memuat baris `Stay One`" (TC-FA-CF-171) dan "ketiga baris tampil pada tabel" (TC-FA-CF-173) diasersi pada langkah 39 sesudah modal ditutup, karena tabel berada di belakang modal. Langkah 39 memuat lima baris sehingga sekaligus menjadi pembanding bagi baris `Stay Off`.
- Spec melewati sekitar 35 langkah (40 langkah): tiga TC satu topik (checkbox Stay) dengan satu dataset, dan tiap Create memakai nama field sendiri sehingga kegagalan satu TC tidak menghilangkan makna TC lain.
- Langkah penghubung toast (S-03, R-22): langkah 12, 26, 29 dan 32 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-171: Expected b ("seluruh input kembali ke default") diuraikan per input mengikuti daftar default di Expected b (Field Name kosong, Data Type belum dipilih, Scope `General`, Value Type `Specific`, Required No); Decimal Places yang terisi `2 (.00)` tidak diasersi kembali ke default karena kontrol itu tidak tampil sebelum Data Type dipilih.
  - TC-FA-CF-172: Expected b ("tabel ter-refresh seketika") diasersi lewat Search nama field karena TC tidak menyebut posisi baris baru pada tabel.
  - Nama field memakai suffix `{runId}-054` (S-12) sehingga tidak sama dengan `Stay One`, `Stay Off`, dan `Batch 1` sampai `Batch 3` pada Data Uji TC.
  - TC-FA-CF-171 dan TC-FA-CF-173 menutup form dengan `[✕]` sesudah checkbox Stay tercentang tanpa menyebut apakah centang itu membuat form dirty; spec menghapus centang lebih dulu (langkah 22 dan 36) agar form identik dengan kondisi awal dan tidak ada dialog `Unsaved Changes`. Bila PRD menetapkan checkbox Stay bukan bagian kondisi dirty, langkah itu tidak diperlukan.
