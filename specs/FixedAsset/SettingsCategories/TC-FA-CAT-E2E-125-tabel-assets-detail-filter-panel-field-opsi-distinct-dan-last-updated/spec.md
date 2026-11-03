---
id: TC-FA-CAT-E2E-125-tabel-assets-detail-filter-panel-field-opsi-distinct-dan-last-updated
title: "Tabel Assets pada Popup Detail: Screening Filter Panel, Opsi DISTINCT, Logika OR dan AND, serta Date Range Last Updated Inklusif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-428
  - TC-FA-CAT-429
  - TC-FA-CAT-430
  - TC-FA-CAT-431
  - TC-FA-CAT-554
coverage:
  web: automated
---

# Tabel Assets pada Popup Detail: Screening Filter Panel, Opsi DISTINCT, Logika OR dan AND, serta Date Range Last Updated Inklusif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).

## Test Steps
1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-428: Screening Filter Panel tabel Assets

3. Klik icon Filter
4. Verifikasi Name (`All asset names`), TAG (`All tags`), Brand (`All brands`), Model/Type (`All models`), Measurement (`All units`), Group (`All groups`), Label (`All labels`), Status (`All statuses`), dan Transactional Policy (`All transactions`) semuanya multi-select searchable
5. Verifikasi Last Scanned, Warranty Expiry, dan Last Updated berupa date range dengan placeholder `Select date`
6. Verifikasi Asset Value berupa range dengan placeholder `Min` / `Max`
7. Verifikasi tidak ada field Category
8. Verifikasi maksimal 4 field per baris
9. Verifikasi field kolom curated (Measurement, Label, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry) tampil walau kolomnya tersembunyi
10. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-FA-CAT-429: Filter Brand, Model/Type, dan Group dengan opsi DISTINCT dari data tabel

11. Buka dropdown Brand
12. Verifikasi opsi Brand hanya nilai yang ada pada baris tabel node ini (`Dell`, `HP`, `Hewlett Packard Enterprise Indonesia`)
13. Buka dropdown Model/Type
14. Verifikasi opsi Model/Type hanya nilai yang ada pada baris tabel (`Latitude 5420`, `Elite Dragonfly G3 Notebook PC`)
15. Buka dropdown Group
16. Verifikasi opsi Group hanya nilai yang ada pada baris tabel (`Head Office > Floor 1 > Room 301`, `Region Jawa > Jakarta Selatan Distribution Center`)
17. Pilih Brand `Dell`, Model/Type `Latitude 5420`, dan Group `Head Office > Floor 1 > Room 301` lalu klik `[Apply]`
18. Verifikasi hasil adalah aset ber-Brand `Dell` DAN Model/Type `Latitude 5420` DAN Group terpilih (AND antar field)

### TC-FA-CAT-430: Filter Name memakai nama aset distinct tanpa Increment

19. Klik icon Filter, klik `[Clear Field]` pada tiap field, lalu buka dropdown Name
20. Verifikasi opsi berupa nama aset tanpa Increment (`Laptop Dell`, `Laptop HP`)
21. Pilih `Laptop Dell` lalu klik `[Apply]`
22. Verifikasi hasil menampilkan seluruh unit bernama `Laptop Dell`

### TC-FA-CAT-431: Filter Status multi-select tabel Assets (logika OR dalam field)

23. Klik icon Filter, klik `[Clear Field]` pada tiap field, pilih Status `Available` dan `Borrowed`, lalu klik `[Apply]`
24. Verifikasi hasil memuat baris ber-Status `Available` atau `Borrowed` (OR dalam field)
25. Verifikasi aset ber-sel multi-badge `Borrowed` + `Damaged` ikut tampil saat Status `Borrowed` dipilih
26. Klik icon Filter, ganti pilihan Status menjadi hanya `Damaged`, lalu klik `[Apply]`
27. Verifikasi aset ber-sel multi-badge `Borrowed` + `Damaged` ikut tampil saat hanya `Damaged` dipilih

### TC-FA-CAT-554: Filter Last Updated tabel Assets (date range inklusif)

28. Klik icon Filter, klik `[Clear Field]` pada tiap field, pilih rentang Last Updated yang mencakup sebagian baris, lalu klik `[Apply]`
29. Verifikasi baris dengan Last Updated di dalam rentang (inklusif di kedua tanggal) tampil
30. Klik icon Filter, pilih rentang satu hari (Start sama dengan End), lalu klik `[Apply]`
31. Verifikasi rentang satu hari menampilkan baris yang diperbarui pada hari itu
32. Klik icon Filter, klik `[Clear Field]` pada tiap field, klik `[Apply]`, lalu klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Spec read-only.
- Langkah penghubung (S-03/S-09, tanpa `Verifikasi`): membersihkan Filter (`[Clear Field]`, `[Apply]`) di antara TC dan menutup popup di akhir.
- Expected TC-FA-CAT-428 butir a dipecah menjadi lima Verifikasi (jenis field), butir b menjadi dua, butir c satu. Field Filter kolom Custom Field menurut Data Type diasersi pada TC-FA-CAT-689 sampai TC-FA-CAT-693, bukan di spec ini.
- Temuan untuk QA:
  - TC-FA-CAT-554 tidak menyebut nilai rentang tanggal; spec memakai tanggal Last Updated baris seed Pre-setup #22 yang dibaca dari tabel sebelum Filter.
  - TC-FA-CAT-431 tidak menyebut apakah aset ber-Status `Available` ada pada Pre-setup #22; spec mengasersi baris yang tampil sesuai pilihan.
