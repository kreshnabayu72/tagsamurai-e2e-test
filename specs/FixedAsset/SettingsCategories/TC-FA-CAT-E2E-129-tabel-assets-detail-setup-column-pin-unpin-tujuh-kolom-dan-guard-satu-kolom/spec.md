---
id: TC-FA-CAT-E2E-129-tabel-assets-detail-setup-column-pin-unpin-tujuh-kolom-dan-guard-satu-kolom
title: "Tabel Assets pada Popup Detail: Pin dan Unpin Tujuh Kolom lewat Setup Column dengan Persist serta Guard Satu Kolom Tersisa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-550
  - TC-FA-CAT-553
coverage:
  web: automated
---

# Tabel Assets pada Popup Detail: Pin dan Unpin Tujuh Kolom lewat Setup Column dengan Persist serta Guard Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Pre-setup #40 (label aset; dipakai bila kolom curated Label diuji) dan #56 (kolom Custom Field grup General yang Active) disediakan tim FE sebagai fixture backend; spec ini hanya membaca.
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.
- Lebar viewport diatur cukup sempit sehingga tabel Assets pada popup Detail dapat di-scroll horizontal (langkah 1); tanpa itu asersi kolom tetap di kiri saat scroll tidak bermakna.
- Parameter kolom pada TC-FA-CAT-550 (dipakai pada langkah perulangan):

| Baris | Kolom |
|---|---|
| 1 | `Name` |
| 2 | `Asset ID` |
| 3 | `Brand` |
| 4 | `Model/Type` |
| 5 | `Group` |
| 6 | `Status` |
| 7 | `Last Updated` |

## Test Steps
1. Atur lebar viewport sehingga tabel Assets pada popup Detail dapat di-scroll horizontal
2. Klik node `Electronics` di Sidebar Category Tree
3. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-550: Pin dan unpin kolom tabel Assets lewat popup dan persist

Untuk setiap baris pada tabel "Parameter kolom pada TC-FA-CAT-550" (langkah 4 sampai 10):

4. Klik header Actions (⋯) > `Setup Column...`, klik icon Pin pada kolom baris tabel, lalu klik `[Save]`
5. Scroll tabel horizontal
6. Verifikasi kolom baris tabel tetap di kiri saat scroll horizontal
7. Tekan F5, klik node `Electronics` di Sidebar Category Tree, klik elipsis (⋯) pada baris `Laptop` > `Detail`, lalu scroll tabel horizontal
8. Verifikasi Pin bertahan setelah F5: kolom baris tabel tetap di kiri saat scroll horizontal
9. Klik header Actions (⋯) > `Setup Column...`, klik icon Pin pada kolom baris tabel sekali lagi (unpin), klik `[Save]`, lalu scroll tabel horizontal
10. Verifikasi kolom baris tabel ikut scroll setelah unpin

### TC-FA-CAT-553: Guard satu kolom tersisa tabel Assets

11. Klik header Actions (⋯) > `Setup Column...`
12. Hilangkan centang semua kolom kecuali `Name`
13. Hover checkbox kolom `Name`
14. Verifikasi checkbox kolom `Name` disabled
15. Verifikasi tooltip `At least one column must remain visible.` tampil
16. Klik icon close (✕) pada popup Setup Column, lalu klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Alasan di atas sekitar 35 langkah: langkah 4 sampai 10 diulang pada tujuh kolom (ekspansi 49 langkah, total 58 langkah dengan perulangan diekspansi) dengan parameter di tabel Prerequisites; tiap kolom berdiri sendiri sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna (8b butir 7).
- Expected TC-FA-CAT-550 butir a sampai g (satu per kolom) dipecah menjadi tiga Verifikasi per iterasi: tetap di kiri saat scroll, Pin bertahan setelah F5 (langkah sesudah 7), dan ikut scroll setelah unpin.
- Langkah penghubung (S-03, S-11): langkah 1 (viewport); langkah 7 membuka ulang popup karena F5 menutupnya; langkah terakhir menutup Setup Column tanpa Save dan menutup popup. Tiap iterasi diakhiri unpin sehingga iterasi berikutnya mulai tanpa kolom ter-pin.
- Temuan untuk QA:
  - TC-FA-CAT-550 menyebut Pin "bertahan setelah F5" tanpa menyebut cara mengamatinya; spec mengasersi lewat perilaku kolom tetap di kiri saat scroll horizontal setelah F5.
  - TC-FA-CAT-553 langkah 3 ("semua kolom kecuali `Name`") tidak menyebut apakah kolom curated ikut dihitung; spec hanya menghilangkan centang kolom Visible default.
