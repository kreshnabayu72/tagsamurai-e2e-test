---
id: TC-FA-CAT-E2E-124-tabel-assets-detail-sort-3-state-seluruh-kolom
title: "Tabel Assets pada Popup Detail: Sort 3-State pada Kolom Name, Asset ID, Brand, Model/Type, Group, Status, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-424
  - TC-FA-CAT-425
  - TC-FA-CAT-426
  - TC-FA-CAT-427
coverage:
  web: automated
---

# Tabel Assets pada Popup Detail: Sort 3-State pada Kolom Name, Asset ID, Brand, Model/Type, Group, Status, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Parameter kolom pada TC-FA-CAT-425 (dipakai pada langkah perulangan):

| Baris | Kolom |
|---|---|
| 1 | Asset ID |
| 2 | Brand |
| 3 | Model/Type |
| 4 | Group |

## Test Steps
1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-424: Sort 3-state tabel Assets kolom Name

3. Klik header Name satu kali
4. Verifikasi Ascending: alfabet nama aset lalu Increment numerik natural
5. Klik header Name kedua kali
6. Verifikasi Descending kebalikan penuh dari Ascending
7. Klik header Name ketiga kali
8. Verifikasi Netral kembali ke default Name A-Z

### TC-FA-CAT-425: Sort 3-state tabel Assets kolom Asset ID, Brand, Model/Type, Group

Untuk setiap baris pada tabel "Parameter kolom pada TC-FA-CAT-425" (langkah 9 sampai 14):

9. Klik header kolom baris tabel satu kali
10. Verifikasi Ascending (↑) alfabet A-Z case-insensitive
11. Klik header kolom baris tabel kedua kali
12. Verifikasi Descending (↓) kebalikan penuh
13. Klik header kolom baris tabel ketiga kali
14. Verifikasi Netral kembali ke default Name A-Z

### TC-FA-CAT-426: Sort 3-state tabel Assets kolom Status

15. Klik header Status satu kali
16. Verifikasi Ascending: alfabet berdasarkan label; sel multi-badge `Borrowed` + `Damaged` memakai badge pertama menurut urutan alfabetis dalam sel (`Borrowed`)
17. Klik header Status kedua kali
18. Verifikasi Descending kebalikan penuh
19. Klik header Status ketiga kali
20. Verifikasi Netral kembali ke default Name A-Z

### TC-FA-CAT-427: Sort 3-state tabel Assets kolom Last Updated

21. Klik header Last Updated satu kali
22. Verifikasi Ascending (↑) Oldest First (tanggal terlama di atas)
23. Klik header Last Updated kedua kali
24. Verifikasi Descending (↓) Newest First (kebalikan penuh)
25. Klik header Last Updated ketiga kali
26. Verifikasi Netral kembali ke default Name A-Z
27. Klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Alasan di atas sekitar 35 langkah: langkah 9 sampai 14 diulang pada empat kolom (ekspansi 24 langkah, total 45 langkah dengan perulangan diekspansi) dengan parameter di tabel Prerequisites; tiap kolom berdiri sendiri (8b butir 7). Seluruh TC memakai popup yang sama dan tiap TC mengakhiri sort pada keadaan Netral sehingga popup tidak dibuka ulang (S-09).
- Langkah penghubung (S-03): membuka popup di awal dan menutupnya di akhir.
- Expected tiap kolom dipecah per klik (Klik #1, #2, #3) menjadi tiga Verifikasi (S-01).
- Temuan untuk QA:
  - TC-FA-CAT-425 tidak menyebut header kolom lain (Name) sebagai acuan netral; spec mengasersi kembali ke default Name A-Z sesuai Expected.
