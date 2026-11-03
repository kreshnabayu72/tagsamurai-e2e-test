---
id: TC-FA-CAT-E2E-123-tabel-assets-detail-screening-search-guard-last-updated-dan-placeholder
title: "Tabel Assets pada Popup Detail: Screening Kolom dan Default Sort, Search Kolom Teks dan Badge, Guard Last Updated, dan Placeholder Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-419
  - TC-FA-CAT-420
  - TC-FA-CAT-421
  - TC-FA-CAT-422
  - TC-FA-CAT-423
  - TC-FA-CAT-439
coverage:
  web: automated
---

# Tabel Assets pada Popup Detail: Screening Kolom dan Default Sort, Search Kolom Teks dan Badge, Guard Last Updated, dan Placeholder Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).

## Test Steps

### TC-FA-CAT-419: Screening tabel Assets pada Popup Detail

1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Verifikasi toolbar tabel Assets berurutan Search | Filter | Download
4. Verifikasi kolom Visible berurutan Name (sortable) | Asset ID | TAG | Brand | Model/Type | Group | Status | Last Updated | Column Visibility (⋯)
5. Verifikasi default sort Name A-Z
6. Verifikasi kolom curated (Measurement, Label, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry, dan kolom Custom Field) tidak tampil
7. Verifikasi kolom Category tidak ada
8. Verifikasi nama aset berformat `[Asset Name] - [Increment]` (mis. `Laptop Dell - 8`)
9. Verifikasi urutan Increment numerik natural (`Laptop Dell - 2` sebelum `Laptop Dell - 10`)

### TC-FA-CAT-420: Search tabel Assets pada Name dan Asset ID

10. Klik icon Search, ketik `laptop dell - 3`, lalu tekan `Enter`
11. Verifikasi Search mencocokkan teks lengkap `[Asset Name] - [Increment]` secara substring case-insensitive
12. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong
13. Klik icon Search, ketik ID aset `Laptop Dell - 3`, lalu tekan `Enter`
14. Verifikasi Search mencocokkan Asset ID secara substring case-insensitive

### TC-FA-CAT-421: Search tabel Assets pada kolom badge Brand, Model/Type, dan Group

15. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong
16. Klik icon Search, ketik `dell`, lalu tekan `Enter`
17. Verifikasi `dell` menemukan aset ber-Brand `Dell`
18. Ketik `5420` pada Search lalu tekan `Enter`
19. Verifikasi `5420` menemukan aset ber-Model `Latitude 5420`
20. Ketik `Floor 1` pada Search lalu tekan `Enter`
21. Verifikasi `Floor 1` menemukan aset ber-Group `Head Office > Floor 1 > Room 301`

### TC-FA-CAT-422: Search kolom Status mencocokkan label badge pada sel multi-badge

22. Ketik `damaged` pada Search lalu tekan `Enter`
23. Verifikasi baris ber-Status `Damaged` ditemukan
24. Verifikasi baris multi-badge `Borrowed` + `Damaged` ditemukan (cocok bila salah satu badge cocok)

### TC-FA-CAT-423: Guard kolom Last Updated tidak dapat dicari lewat Search

25. Ketik nilai tanggal Last Updated baris pertama pada Search lalu tekan `Enter`
26. Verifikasi tidak ada hasil

### TC-FA-CAT-439: Placeholder Search tabel Assets

27. Klik (✕) pada input Search lalu tekan `Enter` pada input kosong, kemudian klik icon Close (✕) pada popup
28. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
29. Klik icon Search di toolbar tabel Assets
30. Verifikasi placeholder input Search `Search asset name, asset ID, brand...`
31. Klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec read-only; tidak ada konfigurasi yang disimpan.
- Langkah penghubung (S-03/S-09, tanpa `Verifikasi`): mengosongkan Search di antara TC dan menutup popup di akhir.
- Expected TC-FA-CAT-419 butir a dipecah menjadi lima Verifikasi (toolbar, kolom Visible, default sort, kolom curated, kolom Category) dan butir b menjadi dua Verifikasi (format nama, urutan Increment).
- Temuan untuk QA:
  - Langkah sumber ketiga TC-FA-CAT-420 ("Search ID aset `Laptop Dell - 3` pada Asset ID") memakai keyword yang sama dengan langkah sumber kedua; spec memakai keyword itu dan mengasersi pencocokan Asset ID.
  - TC-FA-CAT-423 tidak menyebut format nilai tanggal baris pertama; spec memakai teks tanggal persis seperti tampil di sel Last Updated.
  - Langkah sumber TC-FA-CAT-421 tidak membersihkan Search di antaranya; spec menimpa keyword pada input yang sama.
