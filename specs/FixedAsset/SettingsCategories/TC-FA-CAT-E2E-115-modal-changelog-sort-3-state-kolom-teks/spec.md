---
id: TC-FA-CAT-E2E-115-modal-changelog-sort-3-state-kolom-teks
title: "Modal Changelog: Sort 3-State pada Kolom Action, Category Name, Field, Old Value, dan New Value"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-397
coverage:
  web: automated
---

# Modal Changelog: Sort 3-State pada Kolom Action, Category Name, Field, Old Value, dan New Value

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Changelog CatMain bertambah oleh spec lain dan tidak pernah dikosongkan. Asersi isi dan urutan hanya atas baris seed Pre-setup #23, dibatasi Filter Date 20 Jun 2026 sampai 1 Jul 2026 (rentang tanggal Example Data PRD §4.1, tanggal baris spec lain berada di luar rentang itu; S-14). Filter dipasang lewat langkah penghubung.
- Parameter kolom (dipakai pada langkah perulangan):

| Baris | Kolom | Aturan Ascending (↑) |
|---|---|---|
| 1 | Action | alfabet A-Z case-insensitive |
| 2 | Category Name | alfabet A-Z case-insensitive |
| 3 | Field | alfabet A-Z case-insensitive |
| 4 | Old Value | alfabet A-Z; nilai kosong `—` di akhir |
| 5 | New Value | alfabet A-Z; nilai kosong `—` di akhir |

## Test Steps

### TC-FA-CAT-397: Sort 3-state Changelog kolom Action, Category Name, Field, Old Value, New Value

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di toolbar modal, pilih rentang tanggal 20 Jun 2026 sampai 1 Jul 2026 pada field Date, lalu klik `[Apply]`
Untuk setiap baris pada tabel "Parameter kolom" (langkah 3 sampai 8):

3. Klik header kolom baris tabel satu kali
4. Verifikasi kolom terurut Ascending (↑) sesuai aturan pada baris tabel
5. Klik header kolom baris tabel kedua kali
6. Verifikasi kolom terurut Descending (↓) kebalikan penuh dari Ascending
7. Klik header kolom baris tabel ketiga kali
8. Verifikasi kolom kembali Netral dengan urutan default Date Newest First
9. Klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-FA-CAT-398 dan TC-FA-CAT-399 ada di spec 194.
- Alasan di atas sekitar 35 langkah: langkah 3 sampai 8 diulang pada lima kolom (ekspansi 30 langkah, total 33 langkah) dengan parameter di tabel Prerequisites; tiap kolom berdiri sendiri (8b butir 7).
- Expected TC-FA-CAT-397 butir a sampai e satu per kolom, masing-masing dipecah per klik (Klik #1, #2, #3) menjadi tiga Verifikasi (S-01).
- Langkah penghubung (S-03, S-14): langkah 2 membatasi Changelog ke rentang Date baris seed Pre-setup #23; langkah terakhir menutup modal.
- Temuan untuk QA:
  - TC-FA-CAT-397 tidak menyebut baris Pre-setup #23 mana yang dipakai membandingkan urutan; spec mengasersi urutan atas baris Changelog yang tampil setelah Filter Date seed (langkah 2).
  - Pre-setup #23 menyebut "rename ancestor setelah Create anak" tanpa tanggal; rentang Filter Date spec memakai tanggal Example Data PRD §4.1 (20 Jun 2026 sampai 1 Jul 2026). Mohon QA menambahkan tanggal seed pada Pre-setup #23.
