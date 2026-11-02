---
id: TC-FA-CAT-E2E-196-kolom-tag-sort-3-state-dan-filter-multi-select
title: "Kolom TAG Tabel Assets: Sort 3-State dan Filter Multi-Select dengan Logika OR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-653
coverage:
  web: automated
---

# Kolom TAG Tabel Assets: Sort 3-State dan Filter Multi-Select dengan Logika OR

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): tag aktif `Laptop Dell - 1` RFID dan QR, `Laptop Dell - 2` NFC, `Laptop Dell - 4` pairing BARCODE berstatus nonaktif, aset lain tanpa tag.
- Data Pre-setup #58 (CatMain, node `Furniture`, seed API): `Office Chair - 1` tag `NFC`; `Office Chair - 2` tag `NFC` dan `QR`; `Office Chair - 3` tag `QR`; `Office Chair - 4` dan `Office Chair - 5` tanpa tag. Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik elipsis (⋯) pada baris `Furniture` > `Detail`
2. Klik header kolom TAG satu kali
3. Verifikasi Ascending alfabetis atas label ikon: `Office Chair - 1` (`NFC`), `Office Chair - 2` (`NFC, QR`), `Office Chair - 3` (`QR`), lalu baris `—` di akhir mengikuti `prd-conventions.md` §9.7
4. Klik header kolom TAG satu kali lagi
5. Verifikasi Descending kebalikan penuh (`QR`, `NFC, QR`, `NFC`) dengan baris `—` di awal
6. Klik header kolom TAG satu kali lagi
7. Verifikasi urutan kembali Netral ke default Name A-Z
8. Klik icon close (✕) pada Popup Detail
9. Pilih node `Electronics` di Sidebar Category Tree
10. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
11. Klik icon Filter
12. Verifikasi field berlabel `TAG` dengan placeholder `All tags` tampil di Filter Panel
13. Buka dropdown field `TAG`
14. Verifikasi field `TAG` berupa multi-select searchable
15. Verifikasi opsi dropdown hanya tipe tag distinct dari data tabel: `RFID`, `QR`, `NFC`
16. Verifikasi opsi `BARCODE` tidak ada karena pairing nonaktif
17. Pilih `RFID`, lalu klik `[Apply]`
18. Verifikasi tabel menyisakan `Laptop Dell - 1`
19. Klik icon Filter, tambahkan `NFC` sehingga `RFID` dan `NFC` terpilih, lalu klik `[Apply]`
20. Verifikasi tabel menyisakan `Laptop Dell - 1` dan `Laptop Dell - 2` (OR dalam field)

## Notes

- Mode: FE+BE. Langkah penghubung (S-03, S-09): langkah menutup Popup Detail `Furniture`, memilih node `Electronics`, dan membuka Popup Detail `Laptop`. Popup Detail `Furniture` dibuka dari node bawaan `All Categories` yang terpilih pada awal spec (layar awal hook `beforeEach` suite).
- Temuan untuk QA:
  - TC-FA-CAT-653 Expected a menyebut baris `—` di akhir/awal "mengikuti `prd-conventions.md` §9.7" tanpa menegaskan teks aturannya; spec mengasersi posisi baris `—` sesuai Expected.
  - TC-FA-CAT-653 langkah 5 memilih `RFID` dan `NFC` tanpa menyebut apakah pilihan `RFID` dari langkah 4 masih ada; spec menambahkan `NFC` ke pilihan yang ada.
