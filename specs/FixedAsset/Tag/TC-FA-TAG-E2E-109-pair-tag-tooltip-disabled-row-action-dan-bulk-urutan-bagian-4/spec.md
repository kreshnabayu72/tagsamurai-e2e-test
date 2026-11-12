---
id: TC-FA-TAG-E2E-109-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-4
title: "Pair TAG: Bulk Pair TAG Status Aset Didahulukan atas Stok (Bagian 4)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1494
coverage:
  web: automated
---

# Pair TAG: Bulk Pair TAG Status Aset Didahulukan atas Stok (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Asset Status aset, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset target | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset In Disposal Process | 'Excavator 20 Ton - 53' (AST-0053, Group Plant A, TAG Type RFID, Asset Status In Disposal Process), Not Paired Yet | `aset53` |
| Stok Available | tidak ada Tag RFID Available di stok Global | `stokRfidKosong` |

- State yang diubah dan pemulihannya: stok Available RFID dikosongkan lewat fixture backend; hook `after` memulihkan stok seperti awal.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1) yang menyiapkan atau memulihkan state.

## Test Steps

1. Kosongkan stok Tag RFID Available dan pastikan reader tersambung serta 'Excavator 20 Ton - 51' Not Paired Yet dan 'Excavator 20 Ton - 53' In Disposal Process Not Paired Yet lewat fixture backend hingga tersimpan
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
3. Klik `Show` di samping `Not Paired Yet`
4. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 53'
5. Arahkan kursor ke Bulk `Pair TAG`
6. Verifikasi Bulk `Pair TAG` tetap tampil namun Disabled
7. Verifikasi tooltip "This asset can't be paired while it is in disposal."
8. Verifikasi tooltip bukan "No available RFID TAG in stock."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1494). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik tooltip Disabled Pair TAG ada di spec 106 (TC-FA-TAG-449 s.d. 452), spec 107 (TC-FA-TAG-454 s.d. 458), spec 108 (TC-FA-TAG-1455, 1491 s.d. 1493), dan spec 116 (TC-FA-TAG-453).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (mengatur stok, reader, dan aset lewat fixture backend hingga tersimpan).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur reader tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
