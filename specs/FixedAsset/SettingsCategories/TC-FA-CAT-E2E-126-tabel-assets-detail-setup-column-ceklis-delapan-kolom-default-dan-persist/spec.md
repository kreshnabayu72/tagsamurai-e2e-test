---
id: TC-FA-CAT-E2E-126-tabel-assets-detail-setup-column-ceklis-delapan-kolom-default-dan-persist
title: "Tabel Assets pada Popup Detail: Ceklis dan Unceklis Delapan Kolom Default Visible lewat Setup Column dengan Persist"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-432
coverage:
  web: automated
---

# Tabel Assets pada Popup Detail: Ceklis dan Unceklis Delapan Kolom Default Visible lewat Setup Column dengan Persist

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Pre-setup #40 (label aset; dipakai bila kolom curated Label diuji) dan #56 (kolom Custom Field grup General yang Active) disediakan tim FE sebagai fixture backend; spec ini hanya membaca.
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.
- Parameter kolom (dipakai pada langkah perulangan):

| Baris | Kolom |
|---|---|
| 1 | `Name` |
| 2 | `Asset ID` |
| 3 | `Brand` |
| 4 | `Model/Type` |
| 5 | `Group` |
| 6 | `Status` |
| 7 | `Last Updated` |
| 8 | `TAG` |

## Test Steps

### TC-FA-CAT-432: Setup Column tabel Assets, ceklis dan unceklis tiap kolom default Visible, Save, dan persist

1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Klik header Actions (⋯) > `Setup Column...`
Untuk setiap baris pada tabel "Parameter kolom" (langkah 4 sampai 7):

4. Hilangkan centang kolom baris tabel
5. Verifikasi Live Preview menyembunyikan kolom baris tabel
6. Centang kembali kolom baris tabel
7. Verifikasi Live Preview menampilkan kembali kolom baris tabel
8. Hilangkan centang kolom `Brand` dan `Model/Type` lalu klik `[Save]`
9. Verifikasi kolom `Brand` dan `Model/Type` tidak ada di tabel
10. Tekan F5, klik node `Electronics` di Sidebar Category Tree, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
11. Verifikasi konfigurasi bertahan: kolom `Brand` dan `Model/Type` tidak ada di tabel setelah F5
12. Verifikasi kolom curated (Hidden default) tetap tidak tampil
13. Klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Alasan di atas sekitar 35 langkah: langkah 4 sampai 7 diulang pada delapan kolom (ekspansi 32 langkah, total 41 langkah dengan perulangan diekspansi) dengan parameter di tabel Prerequisites; tiap kolom berdiri sendiri (8b butir 7).
- Expected TC-FA-CAT-432 butir a sampai h (satu per kolom) dipetakan ke Verifikasi langkah langkah sesudahnya dan 7 pada tiap iterasi; butir i dipecah menjadi tiga Verifikasi (tidak ada di tabel, bertahan setelah F5 pada langkah 10 dan sesudahnya, kolom curated tetap tidak tampil).
- Langkah penghubung (S-03): langkah 10 membuka ulang popup karena F5 menutupnya; langkah terakhir menutup popup.
- Temuan untuk QA:
  - TC-FA-CAT-432 tidak menyebut cara membuka ulang popup setelah F5; spec membukanya lewat node `Electronics` dan baris `Laptop`.
