---
id: TC-FA-CAT-E2E-119-modal-changelog-setup-column-geser-urutan-dan-reset-to-default
title: "Modal Changelog: Geser Urutan Tujuh Kolom Lewat Popup dengan Persist dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-409
  - TC-FA-CAT-410
coverage:
  web: automated
---

# Modal Changelog: Geser Urutan Tujuh Kolom Lewat Popup dengan Persist dan Reset to Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.
- Parameter kolom (dipakai pada langkah perulangan):

| Baris | Kolom |
|---|---|
| 1 | `Date` |
| 2 | `Action` |
| 3 | `Category Name` |
| 4 | `Field` |
| 5 | `Old Value` |
| 6 | `New Value` |
| 7 | `Modified By` |

## Test Steps

### TC-FA-CAT-409: Geser urutan kolom Changelog lewat popup dan persist

1. Klik icon Changelog di Table Tools
2. Klik header Actions (⋯) > `Setup Column...`
Untuk setiap baris pada tabel "Parameter kolom" (langkah 3 sampai 4):

3. Geser kolom baris tabel ke posisi pertama
4. Verifikasi preview menempatkan kolom baris tabel sebagai kolom data pertama
5. Klik `[Save]`
6. Verifikasi urutan kolom data menjadi Modified By, New Value, Old Value, Field, Category Name, Action, Date
7. Tekan F5 lalu klik icon Changelog di Table Tools
8. Verifikasi urutan kolom data Modified By, New Value, Old Value, Field, Category Name, Action, Date bertahan setelah F5

### TC-FA-CAT-410: Reset to Default Setup Column Changelog mengembalikan tujuh kolom bawaan

9. Klik header Actions (⋯) > `Setup Column...`
10. Hilangkan centang `Old Value` dan geser `Modified By` ke posisi pertama
11. Klik `[Reset to Default]`
12. Verifikasi preview kembali ke tujuh kolom default berurutan Date, Action, Category Name, Field, Old Value, New Value, Modified By
13. Klik `[Save]`
14. Verifikasi tabel kembali ke tujuh kolom default berurutan Date, Action, Category Name, Field, Old Value, New Value, Modified By
15. Tekan F5 lalu klik icon Changelog di Table Tools
16. Verifikasi konfigurasi default bertahan setelah F5
17. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Alasan di atas sekitar 35 langkah: langkah 3 sampai 4 diulang pada tujuh kolom (ekspansi 14 langkah, total 29 langkah dengan perulangan diekspansi) dengan parameter di tabel Prerequisites; tiap kolom diasersi setelah digeser (8b butir 7).
- Expected TC-FA-CAT-409 butir a sampai g dipetakan ke Verifikasi langkah 4 pada tiap iterasi; butir h dipecah menjadi dua Verifikasi (urutan setelah Save, dan bertahan setelah F5 pada langkah 7 dan sesudahnya).
- Langkah penghubung (S-03): langkah terakhir menutup modal. Setelah F5 modal tertutup sehingga dibuka ulang sebelum Verifikasi.
- Temuan untuk QA:
  - TC-FA-CAT-409 dan TC-FA-CAT-410 tidak menyebut apakah modal Changelog tetap terbuka setelah F5; spec membukanya ulang.
  - TC-FA-CAT-410 dijalankan sesudah TC-FA-CAT-409 pada sesi yang sama sehingga konfigurasi awalnya adalah hasil TC-FA-CAT-409 (urutan terbalik); Reset to Default tetap mengembalikan tujuh kolom bawaan.
