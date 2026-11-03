---
id: TC-FA-FAAM-E2E-151-changelog-setup-column-kelas-date
title: "Modal Changelog Setup Column: Kelas Date (Ceklis, Geser, Pin)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-484
  - TC-FA-FAAM-485
  - TC-FA-FAAM-486
coverage:
  web: automated
---

# Modal Changelog Setup Column: Kelas Date (Ceklis, Geser, Pin)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28) berisi sedikitnya satu entri sehingga kolom tabel Changelog tampil. Konfigurasi kolom bawaan: `Date | Action | Asset Name | Field | Old Value | New Value | Modified By`.
- Kemampuan teknis: drag and drop pada popup Setup Column dan hapus preferensi kolom Changelog di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom Changelog (preferensi di browser) diubah spec ini. Pemulihan: langkah 13, 22, dan 34 menghapus preferensi kolom di browser, dan hook `after` melakukannya sebagai cadangan (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAM-484: Setup Column Changelog ceklis dan unceklis kelas Date

2. Klik header Actions (⋯), lalu klik `Setup Column...`
3. Uncheck `Date` pada popup Setup Column
4. Verifikasi Live Preview hanya memuat kolom `Action | Asset Name | Field | Old Value | New Value | Modified By`
5. Check `Date` pada popup Setup Column
6. Verifikasi Live Preview memuat kolom `Date | Action | Asset Name | Field | Old Value | New Value | Modified By`
7. Uncheck `Date` pada popup Setup Column
8. Klik `[Save]`
9. Verifikasi tabel Changelog hanya memuat kolom `Action | Asset Name | Field | Old Value | New Value | Modified By | Actions (⋯)`
10. Tekan F5
11. Klik icon Changelog
12. Verifikasi konfigurasi tersimpan: tabel Changelog hanya memuat kolom `Action | Asset Name | Field | Old Value | New Value | Modified By | Actions (⋯)`
13. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5, lalu klik icon Changelog

### TC-FA-FAAM-485: Setup Column Changelog geser urutan kelas Date

14. Klik header Actions (⋯), lalu klik `Setup Column...`
15. Geser kolom `Date` ke posisi terakhir (sesudah `Modified By`)
16. Verifikasi Live Preview berurutan `Action | Asset Name | Field | Old Value | New Value | Modified By | Date`
17. Klik `[Save]`
18. Verifikasi tabel Changelog berurutan `Action | Asset Name | Field | Old Value | New Value | Modified By | Date`
19. Tekan F5
20. Klik icon Changelog
21. Verifikasi konfigurasi tersimpan: tabel Changelog berurutan `Action | Asset Name | Field | Old Value | New Value | Modified By | Date`
22. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5, lalu klik icon Changelog

### TC-FA-FAAM-486: Setup Column Changelog pin dan unpin kelas Date

23. Klik header Actions (⋯), lalu klik `Setup Column...`
24. Pin kolom `Date`
25. Verifikasi Live Preview menampilkan kolom `Date` ter-pin
26. Unpin kolom `Date`
27. Verifikasi Live Preview menampilkan kolom `Date` tanpa pin
28. Pin kolom `Date`
29. Klik `[Save]`
30. Verifikasi tabel Changelog menampilkan kolom `Date` ter-pin
31. Tekan F5
32. Klik icon Changelog
33. Verifikasi konfigurasi tersimpan: tabel Changelog menampilkan kolom `Date` ter-pin
34. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka kembali Changelog sesudah F5 (langkah 11, 20, 32), memulihkan konfigurasi kolom ke bawaan sebelum TC berikutnya (langkah 13, 22, 34), dan menyimpan perubahan sebelum asersi tabel (langkah 8, 17, 29). Memulihkan lewat penghapusan preferensi mencegah form dirty tertinggal (S-09).
- Spec ini mencapai 34 langkah; setiap TC ditulis dalam siklus ceklis atau geser atau pin lalu Save, F5, dan verifikasi persistensi.
- Verifikasi daftar kolom pada langkah 4, 9, dan 12 menyebut daftar utuh; ketiadaan kolom `Date` dibuktikan oleh daftar yang sama-sama memuat kolom lain (anchor positif, bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-484, 485, dan 486 Expected b memuat kurung "(pin maksimal tiga kolom)", yang tidak relevan untuk ceklis dan geser dan tidak dapat diuji dengan satu kolom ter-pin pada TC pin; spec tidak mengasersinya.
  - Kolom Date (kelas Date) pada TC-FA-FAAM-486 hanya satu kolom, sehingga batas pin tiga kolom diuji di spec 154 pada kelas teks.
