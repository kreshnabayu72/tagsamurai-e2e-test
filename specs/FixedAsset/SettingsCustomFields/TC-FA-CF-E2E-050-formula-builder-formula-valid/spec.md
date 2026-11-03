---
id: TC-FA-CF-E2E-050-formula-builder-formula-valid
title: "Formula Builder: Berakhir Operator Ditolak, Formula Valid Tersimpan, dan Konstanta Desimal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-154
  - TC-FA-CF-155
  - TC-FA-CF-156
coverage:
  web: automated
---

# Formula Builder: Berakhir Operator Ditolak, Formula Valid Tersimpan, dan Konstanta Desimal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Field standar numerik yang dirujuk Formula: `Purchase Price` (satu-satunya operan yang disebut PRD, NC-16).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-050`): `Formula End {runId}-050` (Formula `Purchase Price +`, tidak tersimpan), `Formula Valid {runId}-050` (Formula `Purchase Price + 10`, tersimpan), `Formula Const {runId}-050` (Formula `Purchase Price × 1.5`, tersimpan).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-050`.
- Kemampuan teknis: penyusunan token Formula Builder (token field, konstanta angka, operator `+`, `−`, `×`, `÷`); label kontrol builder tidak diasersi sampai Open Item OI-01 PRD dijawab.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]

### TC-FA-CF-154: Formula berakhir operator ditolak saat Submit

2. Isi Field Name `Formula End {runId}-050`, pilih Data Type `Formula`
3. Susun token field `Purchase Price` lalu operator `+`
4. Klik [Submit]
5. Verifikasi pesan inline "Formula cannot end with an operator" tampil saat Submit
6. Verifikasi field tidak tersimpan: modal tetap terbuka
7. Klik [Clear Field]

### TC-FA-CF-155: Formula valid Purchase Price + 10 tersimpan tanpa Placeholder, Value Type, dan Required

8. Isi Field Name `Formula Valid {runId}-050`, pilih Data Type `Formula`
9. Susun token field `Purchase Price`, operator `+`, konstanta `10`
10. Klik [Submit]
11. Verifikasi toast "Success, custom field has been created." tampil
12. Ketik Search `Formula Valid {runId}-050`, tekan Enter
13. Verifikasi baris `Formula Valid {runId}-050` menampilkan Data Type `Formula`
14. Verifikasi baris `Formula Valid {runId}-050` menampilkan Placeholder `—`
15. Verifikasi baris `Formula Valid {runId}-050` menampilkan Value Type `—`
16. Verifikasi baris `Formula Valid {runId}-050` menampilkan Required `—`
17. Klik `(←)` pada kotak Search

### TC-FA-CF-156: Konstanta angka non-negatif dengan titik desimal diterima dalam Formula

18. Klik [+ Custom Field]
19. Isi Field Name `Formula Const {runId}-050`, pilih Data Type `Formula`
20. Susun token field `Purchase Price`, operator `×`, konstanta `1.5`
21. Tunggu toast lama hilang otomatis
22. Klik [Submit]
23. Verifikasi toast "Success, custom field has been created." tampil

### Penutup: field yang ditolak tidak tersimpan

24. Ketik Search `{runId}-050`, tekan Enter
25. Verifikasi tabel menampilkan tepat 2 baris: `Formula Valid {runId}-050` dan `Formula Const {runId}-050` (field `Formula End {runId}-050` tidak tersimpan)
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (154, 155, 156). TC-FA-CF-154 diblokir dan memakai modal yang sama dengan TC-FA-CF-155 lewat [Clear Field] (langkah 7); TC-FA-CF-155 menutup modal dengan Submit sukses sehingga TC-FA-CF-156 membuka modal baru (langkah 18).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, 12 (Search untuk menemukan baris target, R-16), 17, 18, 24, 26, serta penyusunan token dan pengisian form sebagai bagian langkah TC. Langkah 24 sampai 26 membuktikan lewat dua baris tersimpan sebagai anchor positif bahwa field TC-FA-CF-154 tidak muncul.
- Langkah 13 sampai 16 memecah Expected b TC-FA-CF-155 per klausa (S-01).
- Langkah penghubung toast (S-03, R-22): langkah 21 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-155: Expected b mengasersi Placeholder, Value Type, dan Required `—` pada baris; TC tidak menyebut cara menemukan baris, sehingga spec mencari baris lewat Search nama field.
  - TC-FA-CF-156: Expected hanya toast sukses; nilai konstanta `1.5` yang tersimpan tidak diasersi.
  - Nama field memakai suffix `{runId}-050` (S-12) sehingga tidak sama dengan `Formula Test` pada Data Uji TC.
