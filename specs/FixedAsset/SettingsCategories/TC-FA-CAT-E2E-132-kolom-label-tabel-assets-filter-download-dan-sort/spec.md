---
id: TC-FA-CAT-E2E-132-kolom-label-tabel-assets-filter-download-dan-sort
title: "Kolom Curated Label pada Tabel Assets: Filter Label, Download Hanya Saat Label Ditampilkan, dan Sort 3-State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-562
  - TC-FA-CAT-563
  - TC-FA-CAT-564
coverage:
  web: automated
---

# Kolom Curated Label pada Tabel Assets: Filter Label, Download Hanya Saat Label Ditampilkan, dan Sort 3-State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Label aset (Pre-setup #40, dibuat di Settings > Asset Master > Labels, disediakan tim FE): `Laptop Dell - 1` label `Fragile`; `Laptop Dell - 2` label `Fragile` dan `Priority`; `Laptop Dell - 3` label `Fragile`, `Priority`, `Insured`, dan `Outdoor`; `Laptop HP - 1` label `Bulky`; aset lain tanpa label (termasuk `Laptop Dell - 4`).
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`).
- Berkas hasil Download dibaca dari buffer unduhan browser (kolom dan isi sel); kemampuan membaca berkas unduhan disediakan tim FE.

## Test Steps
1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-563: Filter Label, field multi-select searchable, opsi DISTINCT dari tabel, logika OR

3. Klik icon Filter
4. Verifikasi field `Label` multi-select searchable dengan placeholder `All labels` tampil di Filter Panel walau kolom Label tersembunyi
5. Buka dropdown Label
6. Verifikasi opsi hanya label yang ada pada baris tabel node ini (`Fragile`, `Priority`, `Insured`, `Outdoor`, `Bulky`)
7. Pilih `Fragile` dan `Bulky` lalu klik `[Apply]`
8. Verifikasi hasil memuat aset yang memiliki `Fragile` atau `Bulky` (OR dalam field)
9. Klik icon Filter, klik `[Clear Field]` pada tiap field, lalu klik `[Apply]`

### TC-FA-CAT-564: Download tabel Assets memuat kolom Label hanya saat Label ditampilkan

10. Klik Download > `Download as XLSX`
11. Verifikasi berkas pertama tidak memuat kolom Label
12. Klik header Actions (⋯) > `Setup Column...`, centang kolom `Label`, lalu klik `[Save]`
13. Klik Download > `Download as XLSX`
14. Verifikasi berkas kedua memuat kolom Label
15. Verifikasi sel `Laptop Dell - 3` pada berkas kedua memuat keempat nama label `Fragile`, `Priority`, `Insured`, `Outdoor`

### TC-FA-CAT-562: Sort 3-state kolom Label, jumlah label terkecil dulu, tie-breaker label pertama A-Z

16. Klik header Label satu kali
17. Verifikasi Ascending: jumlah label terkecil dulu; di antara aset satu label `Laptop HP - 1` (`Bulky`) sebelum `Laptop Dell - 1` (`Fragile`), lalu `Laptop Dell - 2`, lalu `Laptop Dell - 3`
18. Klik header Label kedua kali
19. Verifikasi Descending kebalikan penuh dari Ascending
20. Klik header Label ketiga kali
21. Verifikasi Netral kembali ke default Name A-Z
22. Klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan dalam spec: TC-FA-CAT-563 dan bagian pertama TC-FA-CAT-564 memerlukan kolom Label tersembunyi, sedangkan TC-FA-CAT-562 memerlukan kolom Label tampil; karena itu TC-FA-CAT-562 diletakkan terakhir, sesudah Label ditampilkan pada TC-FA-CAT-564 (S-10).
- Langkah penghubung (S-03/S-09, tanpa `Verifikasi`): membersihkan Filter sesudah TC-FA-CAT-563 dan menutup popup di akhir. Konfigurasi Setup Column dipulihkan di hook `after` dengan menghapus preferensi kolom di browser.
- TC-FA-CAT-564 berHINT `f` (buffer biner): berkas unduhan dibaca lewat kemampuan tim FE; sisa spec tidak membutuhkan buffer.
- Expected TC-FA-CAT-564 butir b dipecah menjadi dua Verifikasi (kolom Label dan isi sel `Laptop Dell - 3`).
- Temuan untuk QA:
  - TC-FA-CAT-564 mencantumkan Data `Laptop Dell - 3` hanya untuk berkas kedua; spec mengasersi isi sel pada berkas kedua.
