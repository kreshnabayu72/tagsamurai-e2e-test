---
id: TC-FA-CAT-E2E-193-modal-changelog-dropdown-filter-pencarian-internal-dan-sinkronisasi-chip
title: "Modal Changelog: Pencarian Internal Dropdown Filter dan Sinkronisasi Chip dengan Checkbox"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-586
coverage:
  web: automated
---

# Modal Changelog: Pencarian Internal Dropdown Filter dan Sinkronisasi Chip dengan Checkbox

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Parameter dropdown (dipakai pada langkah perulangan):

| Baris | Dropdown | Keyword internal | Hasil yang diharapkan |
|---|---|---|---|
| 1 | Action | `excess` | dua Action `Marked as Excess (Category Consolidation)` dan `Restored from Excess (Category Consolidation)` |
| 2 | Category Name | `Electronics` | opsi yang path-nya memuat `Electronics` |
| 3 | Field | `Code` | Field `Code` |
| 4 | Modified By | `sar` | `Sarah T` |

## Test Steps

### TC-FA-CAT-586: Pencarian internal dropdown Filter dan sinkronisasi chip dengan checkbox

1. Klik icon Changelog di Table Tools
2. Klik icon Filter
Untuk setiap baris pada tabel "Parameter dropdown" (langkah 3 sampai 12):

3. Pada dropdown baris tabel ketik keyword internal pada kotak cari dalam dropdown
4. Verifikasi opsi dropdown menyempit ke hasil yang diharapkan pada baris tabel
5. Pada kotak cari dalam dropdown ketik `zzz`
6. Verifikasi dropdown menampilkan teks `No results found` tanpa ilustrasi
7. Hapus keyword lalu centang dua opsi (atau satu bila hanya satu yang cocok) dan tutup dropdown
8. Verifikasi opsi yang dicentang tampil sebagai chip pada field dropdown
9. Klik (✕) pada salah satu chip lalu buka kembali dropdown
10. Verifikasi chip itu hilang dan checkbox opsinya ter-uncheck di dropdown
11. Uncheck satu opsi dari dalam dropdown yang masih terbuka lalu tutup dropdown
12. Verifikasi chip opsi itu hilang dari field
13. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Spec ini memuat TC-FA-CAT-586 saja agar spec 114 tidak melewati batas.
- Alasan di atas sekitar 35 langkah: langkah 3 sampai 12 diulang pada empat dropdown (ekspansi 40 langkah, total 44 langkah) dengan parameter di tabel Prerequisites; tiap dropdown berdiri sendiri sehingga kegagalan satu dropdown tidak membuat dropdown lain kehilangan makna (8b butir 7).
- Langkah penghubung (S-03/S-09): langkah 2 membuka Filter Panel, langkah 7 menghapus keyword dalam dropdown sebelum mencentang opsi, langkah akhir menutup modal.
- Expected TC-FA-CAT-586 butir a sampai e dipetakan ke Verifikasi: a ke langkah 4, b ke 6, c ke 8, d ke 10, e ke 12 (diulang per dropdown).
- Temuan untuk QA:
  - TC-FA-CAT-586 butir a untuk dropdown Category Name hanya menyebut "opsi yang path-nya memuat `Electronics`" tanpa daftar opsi pasti; spec mengasersi bahwa semua opsi tersisa memuat `Electronics`.
  - Langkah 5 TC (uncheck dari dalam dropdown) mengandalkan dropdown masih terbuka; spec menutup dropdown setelah langkah itu untuk iterasi berikutnya.
