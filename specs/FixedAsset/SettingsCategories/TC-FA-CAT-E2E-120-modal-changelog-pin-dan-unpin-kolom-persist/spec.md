---
id: TC-FA-CAT-E2E-120-modal-changelog-pin-dan-unpin-kolom-persist
title: "Modal Changelog: Pin dan Unpin Tujuh Kolom Lewat Popup Setup Column dengan Persist"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-545
coverage:
  web: automated
---

# Modal Changelog: Pin dan Unpin Tujuh Kolom Lewat Popup Setup Column dengan Persist

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.
- Lebar viewport diatur cukup sempit sehingga tabel Changelog dapat di-scroll horizontal (langkah 1); tanpa itu asersi kolom tetap di kiri saat scroll tidak bermakna.
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

### TC-FA-CAT-545: Pin dan unpin kolom Changelog lewat popup dan persist

1. Atur lebar viewport sehingga tabel Changelog dapat di-scroll horizontal
2. Klik icon Changelog di Table Tools
Untuk setiap baris pada tabel "Parameter kolom" (langkah 3 sampai 9):

3. Buka Column Visibility > `Setup Column...`, klik icon Pin pada kolom baris tabel, lalu klik `[Save]`
4. Scroll tabel horizontal
5. Verifikasi kolom baris tabel tetap di kiri saat scroll horizontal
6. Tekan F5, klik icon Changelog di Table Tools, lalu scroll tabel horizontal
7. Verifikasi Pin bertahan setelah F5: kolom baris tabel tetap di kiri saat scroll horizontal
8. Buka Setup Column, klik icon Pin pada kolom baris tabel sekali lagi (unpin), klik `[Save]`, lalu scroll tabel horizontal
9. Verifikasi kolom baris tabel ikut scroll setelah unpin
10. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Alasan di atas sekitar 35 langkah: langkah 3 sampai 9 diulang pada tujuh kolom (ekspansi 49 langkah, total 52 langkah) dengan parameter di tabel Prerequisites; tiap kolom berdiri sendiri sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna (8b butir 7).
- Expected TC-FA-CAT-545 butir a sampai g (satu per kolom) dipecah menjadi tiga Verifikasi per iterasi: tetap di kiri saat scroll, Pin bertahan setelah F5, dan ikut scroll setelah unpin.
- Langkah penghubung (S-03, S-11): langkah 1 (viewport) dan langkah terakhir menutup modal. Setiap iterasi diakhiri dengan unpin sehingga iterasi berikutnya mulai dari keadaan tanpa kolom ter-pin.
- Temuan untuk QA:
  - TC-FA-CAT-545 menyebut Pin "bertahan setelah F5" tanpa menyebut cara mengamatinya; spec mengasersi lewat perilaku kolom tetap di kiri saat scroll horizontal setelah F5.
  - Pre-setup #23 hanya 12 baris dan tujuh kolom; scroll horizontal hanya bermakna bila lebar tabel melebihi viewport. TC tidak menyebut lebar viewport; spec memakai langkah 1 dan kemampuan itu dicatat sebagai kebutuhan tim FE.
