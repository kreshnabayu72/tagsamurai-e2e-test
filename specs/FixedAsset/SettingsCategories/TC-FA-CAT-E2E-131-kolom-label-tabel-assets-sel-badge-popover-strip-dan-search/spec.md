---
id: TC-FA-CAT-E2E-131-kolom-label-tabel-assets-sel-badge-popover-strip-dan-search
title: "Kolom Curated Label pada Tabel Assets: Sel Badge dengan Ringkasan +N more, Popover Labels, Sel Kosong, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-558
  - TC-FA-CAT-559
  - TC-FA-CAT-560
  - TC-FA-CAT-561
coverage:
  web: automated
---

# Kolom Curated Label pada Tabel Assets: Sel Badge dengan Ringkasan +N more, Popover Labels, Sel Kosong, dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Label aset (Pre-setup #40, dibuat di Settings > Asset Master > Labels, disediakan tim FE): `Laptop Dell - 1` label `Fragile`; `Laptop Dell - 2` label `Fragile` dan `Priority`; `Laptop Dell - 3` label `Fragile`, `Priority`, `Insured`, dan `Outdoor`; `Laptop HP - 1` label `Bulky`; aset lain tanpa label (termasuk `Laptop Dell - 4`).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`).

## Test Steps
1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Klik header Actions (⋯) > `Setup Column...`, centang kolom `Label`, lalu klik `[Save]`

### TC-FA-CAT-558: Sel Label, satu atau dua badge berwarna dan sisanya diringkas +N more

4. Perhatikan sel Label pada `Laptop Dell - 1`, `Laptop Dell - 2`, dan `Laptop Dell - 3`
5. Verifikasi `Laptop Dell - 1` menampilkan 1 badge `Fragile` tanpa `+N more`
6. Verifikasi `Laptop Dell - 2` menampilkan 2 badge `Fragile` dan `Priority` tanpa `+N more`
7. Verifikasi `Laptop Dell - 3` menampilkan 2 badge lalu chip `+2 more`
8. Verifikasi badge berwarna sesuai warna hex label

### TC-FA-CAT-559: Chip +N more membuka popover Labels berisi seluruh label aset

9. Klik chip `+2 more` pada `Laptop Dell - 3`
10. Verifikasi popover `Labels` terbuka dan memuat keempat label `Fragile`, `Priority`, `Insured`, `Outdoor`
11. Tekan `Esc` untuk menutup popover

### TC-FA-CAT-560: Sel Label kosong menampilkan strip

12. Perhatikan sel Label pada `Laptop Dell - 4` yang tidak memiliki label
13. Verifikasi sel Label `Laptop Dell - 4` menampilkan `—`

### TC-FA-CAT-561: Search tabel Assets pada kolom Label

14. Klik icon Search, ketik `fragile`, lalu tekan `Enter`
15. Verifikasi `fragile` menemukan `Laptop Dell - 1`, `Laptop Dell - 2`, dan `Laptop Dell - 3` (substring case-insensitive pada nama label)
16. Ketik `outdoor` pada Search lalu tekan `Enter`
17. Verifikasi `outdoor` menemukan `Laptop Dell - 3` walau label itu tidak tampil sebagai badge
18. Ketik `tidak-ada-lbl` pada Search lalu tekan `Enter`
19. Verifikasi `tidak-ada-lbl` menampilkan `No results found`
20. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong, kemudian klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Kolom `Label` ditampilkan sekali di awal untuk keempat TC (precondition identik); konfigurasi dipulihkan di hook `after` (S-06).
- Langkah penghubung (S-03/S-09, tanpa `Verifikasi`): menampilkan kolom `Label`, menutup popover dengan `Esc`, dan mengosongkan Search lalu menutup popup di akhir.
- Expected TC-FA-CAT-558 butir c dipecah menjadi tiga Verifikasi (2 badge, chip `+2 more`, warna hex).
- Temuan untuk QA:
  - TC-FA-CAT-558 butir c tidak menyebut kode hex tiap label; spec mengasersi warna badge sama dengan warna label di Settings > Asset Master > Labels.
  - TC-FA-CAT-560 berjudul "menampilkan strip" sedangkan Expected menyebut `—`; spec mengikuti Expected.
