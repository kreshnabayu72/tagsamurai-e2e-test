---
id: TC-FA-TAG-E2E-086-replace-tooltip-disabled-dan-hidden-row-action-dan-bulk-bagian-1
title: "Replace TAG: Tooltip Disabled Row Action dan Bulk Batch Replace (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-330
  - TC-FA-TAG-331
  - TC-FA-TAG-371
  - TC-FA-TAG-372
  - TC-FA-TAG-373
  - TC-FA-TAG-374
  - TC-FA-TAG-380
coverage:
  web: automated
---

# Replace TAG: Tooltip Disabled Row Action dan Bulk Batch Replace (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB yang dapat diatur tersambung atau tidak tersambung (driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Asset Status aset, Tag per status registri, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 1 | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID), satu Tag RFID `RF-00330` Paired | `aset220` |
| Aset 2 | 'Excavator 20 Ton - 221' (AST-0221, Group Plant A), Tag RFID `RF-00140` Paired | `aset221` |
| Aset 3 | 'Excavator 20 Ton - 22' (AST-0022, Group Plant A), Tag RFID `RF-00142` Paired; Asset Status Disposed atau In Disposal Process sesuai bagian | `aset22` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500` | `stokAvailable` |

- State yang diubah dan pemulihannya: status reader, stok Available RFID, dan Asset Status 'Excavator 20 Ton - 22' diatur per bagian lewat fixture; hook `after` memulihkan reader tersambung, stok seperti awal, dan Asset Status aset.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 5, 16, 25, 32) yang menyiapkan atau memulihkan state.

## Test Steps

### Reader tidak tersambung dan stok 0 (TC-FA-TAG-331)

1. Atur reader tidak tersambung ke komputer, hapus semua Tag RFID Available dari stok Global, dan pastikan 'Excavator 20 Ton - 220' punya satu Tag RFID `RF-00330` Paired lewat fixture backend hingga tersimpan
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
4. Verifikasi row action Disabled dengan tooltip "Connect a TAG reader to replace."

### Reader tidak tersambung dan stok tersedia (TC-FA-TAG-371, TC-FA-TAG-380)

5. Tutup Popup Detail, isi stok Global dengan Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` Available (reader tetap tidak tersambung), dan pastikan 'Excavator 20 Ton - 221' punya Tag RFID `RF-00140` Paired lewat fixture backend hingga tersimpan
6. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
7. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
8. Verifikasi row action `Replace TAG` tetap tampil (visible) namun berstatus Disabled
9. Verifikasi tooltip "Connect a TAG reader to replace."
10. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
11. Verifikasi Dialog Replace TAG tidak terbuka
12. Centang baris 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
13. Arahkan kursor ke Bulk `Batch Replace TAG`
14. Verifikasi Bulk `Batch Replace TAG` tetap tampil namun Disabled
15. Verifikasi tooltip "Connect a TAG reader to replace."

### Reader tersambung dan stok RFID 0 (TC-FA-TAG-372, TC-FA-TAG-330)

16. Hapus centang kedua baris, tutup Popup Detail, sambungkan reader (driver terpasang, aktif, sudah disinkronkan), hapus semua Tag RFID Available dari stok Global, dan atur 'Excavator 20 Ton - 22' berstatus Disposed lewat fixture backend hingga tersimpan
17. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
18. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
19. Verifikasi row action `Replace TAG` tetap tampil (visible) namun berstatus Disabled
20. Verifikasi tooltip "No available RFID TAG in stock. Activate TAG in Global Settings > TAG."
21. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
22. Verifikasi Dialog Replace TAG tidak terbuka
23. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 22'
24. Verifikasi row action Disabled dengan tooltip "This asset is in disposal process or already disposed."

### Aset In Disposal Process dan Disposed dengan stok tersedia (TC-FA-TAG-373, TC-FA-TAG-374)

25. Tutup Popup Detail, isi stok Global dengan Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` Available, dan atur 'Excavator 20 Ton - 22' berstatus In Disposal Process lewat fixture backend hingga tersimpan
26. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
27. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 22'
28. Verifikasi row action `Replace TAG` tetap tampil (visible) namun berstatus Disabled
29. Verifikasi tooltip "This asset is in disposal process or already disposed."
30. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 22'
31. Verifikasi Dialog Replace TAG tidak terbuka
32. Tutup Popup Detail dan atur 'Excavator 20 Ton - 22' berstatus Disposed lewat fixture backend hingga tersimpan
33. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
34. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 22'
35. Verifikasi row action `Replace TAG` tetap tampil (visible) namun berstatus Disabled
36. Verifikasi tooltip "This asset is in disposal process or already disposed."
37. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 22'
38. Verifikasi Dialog Replace TAG tidak terbuka

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-330, 331, 371, 372, 373, 374, 380). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik tooltip Disabled dan Hidden Replace TAG dilanjutkan di spec `TC-FA-TAG-E2E-087-replace-tooltip-disabled-dan-hidden-row-action-dan-bulk-bagian-2` (TC-FA-TAG-381, 382, 384).
- Urutan TC di dalam spec mengikuti keadaan reader dan stok supaya perubahan state seminimal mungkin: TC-331, TC-371, TC-380, TC-372, TC-330, TC-373, TC-374. Setiap perpindahan keadaan adalah langkah penghubung.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 5, 16, 25, dan 32 (mengatur reader, stok, dan Asset Status lewat fixture backend, menutup Popup Detail) serta langkah 12 (centang yang dipakai TC-380) dan awal langkah 16 (hapus centang). Popup Detail dibuka ulang sesudah tiap perubahan state supaya state terbaru terbaca.
- Spec di atas smell 35 langkah (38 langkah). Alasan: seluruh blok satu topik (tooltip Disabled row action dan Bulk Replace TAG pada popup yang sama), satu kelas, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 5, 16, 25, 32) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur tersambung atau tidak tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - TC-FA-TAG-330, 373, dan 374 memakai 'Excavator 20 Ton - 22' dengan Asset Status berbeda dan TC-372 serta TC-330 membutuhkan stok RFID 0; TC tidak menyatakan cara mengubah state di tengah spec (fixture backend).
  - Post Condition TC tanpa langkah observasi tidak diasersi.
