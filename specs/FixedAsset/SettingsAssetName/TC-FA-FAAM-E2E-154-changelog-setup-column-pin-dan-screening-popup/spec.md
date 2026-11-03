---
id: TC-FA-FAAM-E2E-154-changelog-setup-column-pin-dan-screening-popup
title: "Modal Changelog Setup Column: Pin Kelas Teks dan Screening Overlay-Popup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-489
  - TC-FA-FAAM-493
coverage:
  web: automated
---

# Modal Changelog Setup Column: Pin Kelas Teks dan Screening Overlay-Popup

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28) berisi sedikitnya satu entri sehingga kolom tabel Changelog tampil. Konfigurasi kolom bawaan: `Date | Action | Asset Name | Field | Old Value | New Value | Modified By`.
- Kemampuan teknis: hover pada header kolom, drag and drop pada popup Setup Column, dan hapus preferensi kolom Changelog di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom Changelog (preferensi di browser) diubah spec ini. Pemulihan: langkah 29 menghapus preferensi kolom di browser, dan hook `after` melakukannya sebagai cadangan (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAM-493: Screening overlay dan popup Setup Column Changelog

2. Arahkan kursor ke header Actions (⋯)
3. Verifikasi tooltip `Column Visibility`
4. Klik header Actions (⋯)
5. Verifikasi overlay memuat 7 kolom data
6. Klik `Setup Column...`
7. Verifikasi popup `Setup Column` memuat Live Preview, `[Reset to Default]`, dan `[Save]`

### TC-FA-FAAM-489: Setup Column Changelog pin dan unpin kelas Action, Asset Name, Field, Old Value, New Value

8. Ronde 1: pin kolom `Action`, `Asset Name`, dan `Field`
9. Verifikasi Live Preview menampilkan kolom `Action`, `Asset Name`, dan `Field` ter-pin
10. Klik `[Save]`
11. Verifikasi tabel Changelog menampilkan kolom `Action`, `Asset Name`, dan `Field` ter-pin
12. Tekan F5
13. Klik icon Changelog
14. Verifikasi konfigurasi tersimpan: tabel Changelog menampilkan kolom `Action`, `Asset Name`, dan `Field` ter-pin
15. Klik header Actions (⋯), lalu klik `Setup Column...`
16. Unpin kolom `Action`, `Asset Name`, dan `Field`
17. Klik `[Save]`
18. Ronde 2: klik header Actions (⋯), lalu klik `Setup Column...`
19. Pin kolom `Old Value` dan `New Value`
20. Verifikasi Live Preview menampilkan kolom `Old Value` ter-pin
21. Verifikasi Live Preview menampilkan kolom `New Value` ter-pin
22. Klik `[Save]`
23. Verifikasi tabel Changelog menampilkan kolom `Old Value` ter-pin
24. Verifikasi tabel Changelog menampilkan kolom `New Value` ter-pin
25. Tekan F5
26. Klik icon Changelog
27. Verifikasi konfigurasi tersimpan: tabel Changelog menampilkan kolom `Old Value` ter-pin
28. Verifikasi konfigurasi tersimpan: tabel Changelog menampilkan kolom `New Value` ter-pin
29. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5

## Notes

- Urutan di spec: screening overlay dan popup (TC-FA-FAAM-493) lebih dulu karena membuka popup yang dipakai TC-FA-FAAM-489 (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): menyimpan perubahan sebelum asersi tabel (langkah 10 dan 22), membuka kembali Changelog sesudah F5 (langkah 13 dan 26), memulihkan pin ronde 1 lewat `Setup Column...` dan `[Save]` (langkah 15 sampai 17), membuka `Setup Column...` untuk ronde 2 (langkah 18), dan memulihkan konfigurasi kolom (langkah 29).
- Batas pin maksimal tiga kolom membuat kelima kolom tidak dapat ter-pin bersamaan; pin dilakukan dalam dua ronde: ronde 1 `Action`, `Asset Name`, dan `Field` (langkah 8 sampai 14) dipulihkan sebelum ronde 2 `Old Value` dan `New Value` (langkah 19 sampai 28).
- Daftar kolom pada Verifikasi ronde 1 disebut utuh (S-01); Verifikasi ronde 2 dipisah per kolom sesuai butir Expected d dan e.
- Temuan untuk QA:
  - Kelas Date dan Modified By untuk pin ada di spec 151 dan 152.
