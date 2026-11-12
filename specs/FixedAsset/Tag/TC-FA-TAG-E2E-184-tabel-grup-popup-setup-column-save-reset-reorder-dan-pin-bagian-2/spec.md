---
id: TC-FA-TAG-E2E-184-tabel-grup-popup-setup-column-save-reset-reorder-dan-pin-bagian-2
title: "Tabel Grup: Popup Setup Column, Reorder dan Pin (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-758
  - TC-FA-TAG-759
coverage:
  web: automated
---

# Tabel Grup: Popup Setup Column, Reorder dan Pin (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Pengubahan ukuran viewport browser (mempersempit lalu memulihkan). Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel grup (urutan dan pin) di cache browser; penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini. Viewport dipulihkan oleh langkah penghubung.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 4, 10).

## Test Steps

### TC-FA-TAG-758

1. Klik header kolom terakhir `⋯` pada tabel grup
2. Klik `Setup Column...`
3. Seret kolom Group ke posisi sebelum Asset Name
4. Klik `[Save]`
5. Verifikasi urutan kolom tabel grup menjadi Group lalu Asset Name

### TC-FA-TAG-759

6. Persempit viewport sehingga tabel grup perlu scroll horizontal
7. Klik header kolom terakhir `⋯` pada tabel grup
8. Klik `Setup Column...`
9. Pin kolom Asset Name
10. Klik `[Save]`
11. Scroll tabel grup secara horizontal
12. Verifikasi kolom Asset Name tetap di posisinya saat scroll
13. Pulihkan ukuran viewport

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-758, TC-FA-TAG-759). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column tabel grup ada di spec 183 (TC-FA-TAG-752 s.d. 756), spec 192 (TC-FA-TAG-757), dan spec 184 (TC-FA-TAG-758 s.d. 759).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 6, 13 (mempersempit dan memulihkan viewport).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 4, 10).
- Temuan untuk QA:
  - Pin pada TC-FA-TAG-759 dilakukan sesudah reorder TC-FA-TAG-758 (urutan Group lalu Asset Name tetap tersimpan).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
