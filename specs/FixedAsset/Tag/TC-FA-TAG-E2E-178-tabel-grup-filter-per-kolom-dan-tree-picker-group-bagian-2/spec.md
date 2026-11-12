---
id: TC-FA-TAG-E2E-178-tabel-grup-filter-per-kolom-dan-tree-picker-group-bagian-2
title: "Tabel Grup: Tree Picker Group dan Filter pada Kolom Tersembunyi (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-727
  - TC-FA-TAG-728
  - TC-FA-TAG-729
  - TC-FA-TAG-730
coverage:
  web: automated
---

# Tabel Grup: Tree Picker Group dan Filter pada Kolom Tersembunyi (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Struktur Group: Plant A memiliki child Line 1 dan grandchild Zone 1. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Struktur Group | Plant A > Line 1 > Zone 1 (Plant A memiliki child Line 1 dan grandchild Zone 1) | `strukturPlantA` |

- State yang diubah dan pemulihannya: kolom Asset Name disembunyikan di TC-FA-TAG-730 dan ditampilkan kembali oleh langkah penghubung (konfigurasi kolom di cache browser); hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`, sebagai cadangan bila spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 25, 29), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-727

1. Klik ikon Filter
2. Klik tombol field `Group` ("All groups")
3. Verifikasi Modal Tree Picker menampilkan tree Group dalam scope dengan checkbox per node, Search node, serta footer `[Cancel]` dan `[Select]`
4. Centang node `Plant A`
5. Verifikasi centang `Plant A` mencentang semua turunannya (Line 1, Zone 1)
6. Klik `[Select]`
7. Verifikasi nilai Group tampil sebagai chip
8. Klik `[Apply]`
9. Verifikasi hanya baris grup Plant A (dan descendant) yang tampil: Excavator 20 Ton / Plant A dan Forklift Manual / Plant A

### TC-FA-TAG-728

10. Klik `[Clear Field]`
11. Klik tombol field `Group`
12. Centang node `Plant A`
13. Klik `[Cancel]`
14. Verifikasi Modal Tree Picker tertutup
15. Verifikasi field Group tetap kosong ("All groups")

### TC-FA-TAG-729

16. Klik tombol field `Group`
17. Ketik `Plant` pada Search node
18. Verifikasi hanya node yang namanya memuat `Plant` tampil (dengan ancestor-nya)
19. Klik `[Cancel]`

### TC-FA-TAG-730

20. Klik `[Clear Field]`
21. Pilih Asset Name 'Forklift Manual'
22. Klik `[Apply]`
23. Klik ikon Filter (menutup Filter Panel)
24. Klik header kolom terakhir `⋯` pada tabel grup
25. Hilangkan centang kolom Asset Name
26. Klik ikon Filter
27. Verifikasi filter tetap ter-Apply: hanya satu baris grup tampil (Group Plant A, TAG Type Non TAG)
28. Verifikasi field `Asset Name` tetap ada di Filter Panel
29. Klik header kolom terakhir `⋯` pada tabel grup, lalu centang kembali kolom Asset Name

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-727, TC-FA-TAG-728, TC-FA-TAG-729, TC-FA-TAG-730). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Filter per kolom dan Tree Picker Group ada di spec 177 (TC-FA-TAG-720 s.d. 726) dan spec 178 (TC-FA-TAG-727 s.d. 730).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 10, 19, 20, 23, 29 (membersihkan draft Filter Panel, menutup modal Tree Picker dan Filter Panel, serta memulihkan kolom Asset Name).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 25, 29), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - Di TC-FA-TAG-730, kolom Asset Name sedang disembunyikan sehingga hasil filter tidak dapat dibaca dari nama; spec membaca hasil dari kolom Group dan TAG Type baris tunggal Forklift Manual / Plant A (Non TAG).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
