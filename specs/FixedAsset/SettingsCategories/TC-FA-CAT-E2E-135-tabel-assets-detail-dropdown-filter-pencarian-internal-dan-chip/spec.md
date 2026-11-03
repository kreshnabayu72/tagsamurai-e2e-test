---
id: TC-FA-CAT-E2E-135-tabel-assets-detail-dropdown-filter-pencarian-internal-dan-chip
title: "Tabel Assets Popup Detail: Dropdown Filter Pencarian Internal dan Sinkronisasi Chip dengan Checkbox"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-591
coverage:
  web: automated
---

# Tabel Assets Popup Detail: Dropdown Filter Pencarian Internal dan Sinkronisasi Chip dengan Checkbox

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Dropdown Filter yang diuji (parameter langkah 5 sampai 17):

| Field Filter | Keyword pada kotak cari dalam dropdown | Opsi yang tersisa |
|---|---|---|
| Name | `dell` | `Laptop Dell` |
| Brand | `hew` | `Hewlett Packard Enterprise Indonesia` |
| Model/Type | `elite` | `Elite Dragonfly G3 Notebook PC` |
| Group | `jakarta` | `Region Jawa > Jakarta Selatan Distribution Center` |
| Status | `avail` | `Available` |

- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Klik icon Filter
4. Untuk setiap baris tabel "Dropdown Filter yang diuji" pada Prerequisites, lakukan langkah 5 sampai 17
5. Buka dropdown field Filter yang diuji lalu ketik keyword pada kotak cari dalam dropdown
6. Verifikasi opsi dropdown menyempit ke opsi yang tersisa pada tabel
7. Ganti isi kotak cari dalam dropdown dengan `zzz`
8. Verifikasi teks `No results found` (tanpa ilustrasi) tampil pada dropdown
9. Ganti isi kotak cari dalam dropdown dengan keyword pada tabel, centang opsi yang cocok (satu bila hanya satu yang cocok), lalu tutup dropdown
10. Verifikasi opsi yang dicentang tampil sebagai chip pada field
11. Klik (✕) pada salah satu chip di field
12. Buka kembali dropdown field
13. Verifikasi chip itu terhapus dari field
14. Verifikasi checkbox opsi itu ter-uncheck di dropdown
15. Centang kembali satu opsi di dropdown yang masih terbuka lalu uncheck opsi itu dari dalam dropdown
16. Verifikasi chip opsi itu terhapus dari field
17. Tutup dropdown

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah dengan ekspansi (langkah 5 sampai 17 diulang untuk lima field Filter; nominal 17). Alasan: satu TC sumber yang langkahnya identik per field, parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat (bagian 8b butir 7).
- Langkah penghubung (S-03): langkah 1 dan 2 (membuka Popup Detail), langkah 3 (membuka Filter Panel), langkah 17 (menutup dropdown), dan pencentangan kembali satu opsi pada langkah 15 supaya "uncheck dari dalam dropdown" punya opsi yang tercentang.
- Temuan untuk QA:
  - TC-FA-CAT-591 langkah 6 ("uncheck satu opsi dari dalam dropdown yang masih terbuka") tidak menyebut opsi mana yang masih tercentang setelah langkah 5; spec mencentang kembali satu opsi sebagai langkah penghubung.
  - TC-FA-CAT-591 langkah 4 menyebut "centang dua opsi (atau satu bila hanya satu yang cocok)" sedangkan keyword menyisakan satu opsi per field (Expected a); spec mencentang opsi yang cocok.
