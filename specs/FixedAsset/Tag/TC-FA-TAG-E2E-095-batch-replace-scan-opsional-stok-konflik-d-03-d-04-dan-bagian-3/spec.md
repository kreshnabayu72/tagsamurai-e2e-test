---
id: TC-FA-TAG-E2E-095-batch-replace-scan-opsional-stok-konflik-d-03-d-04-dan-bagian-3
title: "Batch Replace TAG: Tag Pengganti yang Sudah Dipakai Aset Sebelumnya Ditolak (Bagian 3)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-410
  - TC-FA-TAG-1382
coverage:
  web: automated
---

# Batch Replace TAG: Tag Pengganti yang Sudah Dipakai Aset Sebelumnya Ditolak (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Available; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset sesi 1 sampai 3 | 'Excavator 20 Ton - 220' (AST-0220, `RF-00330`), 'Excavator 20 Ton - 221' (AST-0221, `RF-00140`), 'Excavator 20 Ton - 23' (AST-0023, `RF-00141`), masing-masing satu Tag RFID Paired, Group Plant A | `aset220`, `aset221`, `aset23` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokRfid` |

- State yang diubah dan pemulihannya: Tag `RF-00330` diganti `RF-00412` pada TC-FA-TAG-410; hook `after` memulihkan Tag `RF-00330` Paired dan stok Available seperti awal lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 13); entri TAG Log Global (langkah 13).

## Test Steps

### Tag pengganti dari aset yang di-Skip (TC-FA-TAG-1382)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
3. Klik Bulk `Batch Replace TAG`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Skip]
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
7. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada slot `RFID TAG` aset 2
8. Verifikasi Tag `RF-00412` tidak terisi dan tidak terverifikasi di slot aset 2

### Tag pengganti dari aset yang sudah Done (TC-FA-TAG-410)

9. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
10. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
11. Klik Bulk `Batch Replace TAG`
12. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
13. Klik [Submit & next]
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
15. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada slot `RFID TAG` aset 2
16. Verifikasi Tag `RF-00412` tidak terisi dan tidak terverifikasi di slot aset 2

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-410, 1382). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik scan opsional, stok, dan konflik Batch ada di spec 093 (TC-FA-TAG-400 s.d. 403) dan spec 094 (TC-FA-TAG-404, 408, 409).
- Urutan TC di dalam spec: TC-1382 (aset 1 di-Skip, tidak menyimpan) mendahului TC-410 (aset 1 disimpan lewat [Submit & next]) supaya keadaan awal tidak perlu dipulihkan di antaranya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 (memuat ulang halaman, yang juga mengakhiri sesi TC-1382, dan membuka popup dari keadaan bersih).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 13); entri TAG Log Global (langkah 13).
- Temuan untuk QA:
  - TC-FA-TAG-410 dan TC-FA-TAG-1382 tidak memberi cara menutup sesi di akhir; spec mengandalkan F5 pada langkah 9 untuk TC-1382 dan hook suite untuk TC-410 (sesi tanpa isian aset 2 yang tersimpan).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-410 dan TC-1382 ("Aset 1 Done dengan Tag `RF-00412` Paired", "Tag `RF-00412` tetap Available") tanpa langkah observasi di TC tidak diasersi.
