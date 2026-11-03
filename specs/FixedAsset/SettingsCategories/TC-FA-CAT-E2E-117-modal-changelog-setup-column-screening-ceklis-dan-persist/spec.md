---
id: TC-FA-CAT-E2E-117-modal-changelog-setup-column-screening-ceklis-dan-persist
title: "Modal Changelog: Kolom Actions, Screening Popup Setup Column, serta Ceklis dan Persist Tujuh Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-406
  - TC-FA-CAT-407
  - TC-FA-CAT-408
coverage:
  web: automated
---

# Modal Changelog: Kolom Actions, Screening Popup Setup Column, serta Ceklis dan Persist Tujuh Kolom

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

### TC-FA-CAT-406: Kolom Actions kosong sebagai trigger Column Visibility

1. Klik icon Changelog di Table Tools
2. Klik header kolom Actions (⋯) di ujung kanan tabel
3. Verifikasi kolom Actions tanpa konten tampil di ujung kanan tabel
4. Verifikasi overlay Column Visibility terbuka dengan tujuh kolom data: Date, Action, Category Name, Field, Old Value, New Value, Modified By

### TC-FA-CAT-407: Screening popup Setup Column Changelog

5. Klik `Setup Column...` pada overlay Column Visibility
6. Verifikasi Title `Setup Column` dan deskripsi tampil
7. Verifikasi tujuh kolom tampil dengan checkbox
8. Verifikasi drag handle dan icon Pin tampil pada tiap kolom
9. Verifikasi Live Preview tampil
10. Verifikasi `[Reset to Default]` dan `[Save]` tampil
11. Klik icon close (✕) pada popup Setup Column

### TC-FA-CAT-408: Ceklis dan unceklis kolom Changelog dan persist

12. Klik header Actions (⋯) > `Setup Column...`
Untuk setiap baris pada tabel "Parameter kolom" (langkah 13 sampai 16):

13. Hilangkan centang kolom baris tabel
14. Verifikasi Live Preview menyembunyikan kolom baris tabel
15. Centang kembali kolom baris tabel
16. Verifikasi Live Preview menampilkan kembali kolom baris tabel
17. Hilangkan centang kolom `Old Value` dan `New Value` lalu klik `[Save]`
18. Verifikasi kolom `Old Value` dan `New Value` tidak ada di tabel
19. Tekan F5 lalu klik icon Changelog di Table Tools
20. Verifikasi konfigurasi bertahan: kolom `Old Value` dan `New Value` tidak ada di tabel setelah F5
21. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Setup Column Changelog lanjutan ada di spec 118, 119, dan 120.
- Alasan di atas sekitar 35 langkah: langkah 13 sampai 16 diulang pada tujuh kolom (ekspansi 28 langkah, total 45 langkah) dengan parameter di tabel Prerequisites; tiap kolom berdiri sendiri dan Setup Column Changelog tidak dapat dipisah tanpa mengulang pembukaan modal (8b butir 7).
- Langkah penghubung (S-03): langkah 11 menutup popup Setup Column sebelum TC-FA-CAT-408 membuka ulang popup, dan langkah terakhir menutup modal. Setelah F5 modal tertutup sehingga modal dibuka ulang sebelum Verifikasi.
- Expected TC-FA-CAT-408 butir a sampai g (satu per kolom) dipetakan ke Verifikasi langkah 14 dan 16 pada tiap iterasi (hilangkan centang pada langkah 13, centang kembali pada langkah 15); butir h dipecah menjadi dua Verifikasi (tidak ada di tabel, bertahan setelah F5).
- Temuan untuk QA:
  - TC-FA-CAT-407 menyebut "deskripsi" tanpa teksnya; spec mengasersi bahwa deskripsi tampil tanpa mencocokkan teks.
  - TC-FA-CAT-408 butir h: tabel tersembunyi `Old Value` dan `New Value` diasersi setelah Save dan setelah F5; TC tidak menyebut apakah modal Changelog tetap terbuka setelah F5 (spec membukanya ulang).
