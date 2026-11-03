---
id: TC-FA-FAAM-E2E-153-changelog-setup-column-kelas-teks-ceklis-dan-geser
title: "Modal Changelog Setup Column: Kelas Action, Asset Name, Field, Old-New Value (Ceklis dan Geser)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-487
  - TC-FA-FAAM-488
coverage:
  web: automated
---

# Modal Changelog Setup Column: Kelas Action, Asset Name, Field, Old-New Value (Ceklis dan Geser)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28) berisi sedikitnya satu entri sehingga kolom tabel Changelog tampil. Konfigurasi kolom bawaan: `Date | Action | Asset Name | Field | Old Value | New Value | Modified By`. Kolom kelas ini: `Action`, `Asset Name`, `Field`, `Old Value`, `New Value`.
- Kemampuan teknis: drag and drop pada popup Setup Column dan hapus preferensi kolom Changelog di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom Changelog (preferensi di browser) diubah spec ini. Pemulihan: langkah 13 dan 22 menghapus preferensi kolom di browser, dan hook `after` melakukannya sebagai cadangan (bukan `[Reset to Default]`; kemampuan disediakan tim FE; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAM-487: Setup Column Changelog ceklis dan unceklis kelas Action, Asset Name, Field, Old Value, New Value

2. Klik header Actions (⋯), lalu klik `Setup Column...`
3. Uncheck `Action`, `Asset Name`, `Field`, `Old Value`, dan `New Value` pada popup Setup Column
4. Verifikasi Live Preview hanya memuat kolom `Date | Modified By`
5. Check `Action`, `Asset Name`, `Field`, `Old Value`, dan `New Value` pada popup Setup Column
6. Verifikasi Live Preview memuat kolom `Date | Action | Asset Name | Field | Old Value | New Value | Modified By`
7. Uncheck `Action`, `Asset Name`, `Field`, `Old Value`, dan `New Value` pada popup Setup Column
8. Klik `[Save]`
9. Verifikasi tabel Changelog hanya memuat kolom `Date | Modified By | Actions (⋯)`
10. Tekan F5
11. Klik icon Changelog
12. Verifikasi konfigurasi tersimpan: tabel Changelog hanya memuat kolom `Date | Modified By | Actions (⋯)`
13. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5, lalu klik icon Changelog

### TC-FA-FAAM-488: Setup Column Changelog geser urutan kelas Action, Asset Name, Field, Old Value, New Value

14. Klik header Actions (⋯), lalu klik `Setup Column...`
15. Geser kolom `New Value`, `Old Value`, `Field`, `Asset Name`, lalu `Action` berurutan ke posisi sesudah `Date` sehingga urutan lima kolom terbalik
16. Verifikasi Live Preview berurutan `Date | New Value | Old Value | Field | Asset Name | Action | Modified By`
17. Klik `[Save]`
18. Verifikasi tabel Changelog berurutan `Date | New Value | Old Value | Field | Asset Name | Action | Modified By`
19. Tekan F5
20. Klik icon Changelog
21. Verifikasi konfigurasi tersimpan: tabel Changelog berurutan `Date | New Value | Old Value | Field | Asset Name | Action | Modified By`
22. Pulihkan konfigurasi kolom ke bawaan: hapus preferensi kolom di browser, tekan F5

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membuka kembali Changelog sesudah F5 (langkah 11 dan 20), memulihkan konfigurasi kolom ke bawaan (langkah 13 dan 22), serta menyimpan perubahan sebelum asersi tabel (langkah 8 dan 17).
- Langkah 22 memulihkan konfigurasi tanpa membuka kembali Changelog karena spec berakhir di sana; langkah 13 membuka kembali karena TC berikutnya dimulai dari Changelog.
- Kelima kolom diuji bersama dalam satu urutan akhir: Live Preview dan tabel disebut sebagai daftar utuh (S-01), dengan kolom `Date` dan `Modified By` sebagai anchor positif bagi ketiadaan lima kolom lain (bagian 8b butir 2). Pada langkah 15, urutan akhir membalik kelima kolom sehingga tiap kolom berpindah posisi.
- Pin kelas yang sama ada di spec 154 (TC-FA-FAAM-489).
- Temuan untuk QA: TC-FA-FAAM-487 dan 488 Expected tiap kolom memuat kurung "(pin maksimal tiga kolom)", yang tidak relevan untuk ceklis dan geser; spec tidak mengasersinya.
