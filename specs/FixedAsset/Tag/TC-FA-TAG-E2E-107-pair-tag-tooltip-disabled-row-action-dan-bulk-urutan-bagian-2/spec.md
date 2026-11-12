---
id: TC-FA-TAG-E2E-107-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-2
title: "Pair TAG: Bulk Pair TAG Disabled, Hidden, dan Satu Aset (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-454
  - TC-FA-TAG-455
  - TC-FA-TAG-456
  - TC-FA-TAG-457
  - TC-FA-TAG-458
coverage:
  web: automated
---

# Pair TAG: Bulk Pair TAG Disabled, Hidden, dan Satu Aset (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB yang dapat diatur tersambung atau tidak tersambung (driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Asset Status aset, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset target 1 | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset target 2 | 'Excavator 20 Ton - 52' (AST-0052, Group Plant A, TAG Type RFID), Not Paired Yet | `aset52` |
| Aset In Disposal Process | 'Excavator 20 Ton - 53' (AST-0053, Group Plant A, TAG Type RFID, Asset Status In Disposal Process), Not Paired Yet | `aset53` |
| Aset sudah ber-Tag | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID), Tag RFID `RF-00330` Paired | `aset220` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701`; stok RFID 0 pada bagian TC-456 | `stokAvailable` |

- State yang diubah dan pemulihannya: status reader dan stok Available RFID diatur per bagian lewat fixture; hook `after` memulihkan reader tersambung dan stok seperti awal.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 8, 15, 28) yang menyiapkan atau memulihkan state.

## Test Steps

### Reader tidak tersambung (TC-FA-TAG-454)

1. Putuskan reader dari komputer lewat simulator reader, isi stok Global dengan Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` Available, dan pastikan 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 52' Not Paired Yet lewat fixture backend hingga tersimpan
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
3. Klik `Show` di samping `Not Paired Yet`
4. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 52'
5. Arahkan kursor ke Bulk `Pair TAG`
6. Verifikasi Bulk `Pair TAG` tetap tampil namun Disabled
7. Verifikasi tooltip "Connect a TAG reader to pair."

### Seleksi memuat aset In Disposal Process (TC-FA-TAG-455)

8. Tutup Popup Detail, sambungkan reader (driver terpasang, aktif, sudah disinkronkan), dan pastikan 'Excavator 20 Ton - 53' berstatus In Disposal Process Not Paired Yet lewat fixture backend hingga tersimpan
9. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
10. Klik `Show` di samping `Not Paired Yet`
11. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 53'
12. Arahkan kursor ke Bulk `Pair TAG`
13. Verifikasi Bulk `Pair TAG` tetap tampil namun Disabled
14. Verifikasi tooltip "This asset can't be paired while it is in disposal."

### Seleksi memuat aset yang bukan Not Paired Yet (TC-FA-TAG-457)

15. Tutup Popup Detail dan pastikan 'Excavator 20 Ton - 220' punya Tag RFID `RF-00330` Paired lewat fixture backend hingga tersimpan
16. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
17. Centang baris 'Excavator 20 Ton - 51' (Not Paired Yet) dan baris 'Excavator 20 Ton - 220' (sudah ber-Tag)
18. Verifikasi Bulk Action Bar tampil dengan jumlah terpilih 2
19. Verifikasi Bulk Action Bar tidak memuat `Pair TAG` (Hidden)

### Bulk Pair TAG satu aset (TC-FA-TAG-458)

20. Hapus centang baris 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 51'
21. Klik `Show` di samping `Not Paired Yet`
22. Centang baris 'Excavator 20 Ton - 51'
23. Klik Bulk `Pair TAG`
24. Verifikasi Dialog Pair TAG berjudul `Pair TAG` terbuka langsung
25. Verifikasi footer memuat [Cancel] dan [Submit]
26. Verifikasi footer tidak memuat [Skip] dan [Submit & next]
27. Klik [Cancel]

### Stok seluruh tipe 0 (TC-FA-TAG-456)

28. Tutup Popup Detail dan hapus semua Tag RFID Available dari stok Global lewat fixture backend hingga tersimpan
29. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
30. Klik `Show` di samping `Not Paired Yet`
31. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 52'
32. Arahkan kursor ke Bulk `Pair TAG`
33. Verifikasi Bulk `Pair TAG` tetap tampil namun Disabled
34. Verifikasi tooltip "No available RFID TAG in stock."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-454 s.d. 458). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik tooltip Disabled Pair TAG ada di spec 106 (TC-FA-TAG-449 s.d. 452), spec 108 (TC-FA-TAG-1455, 1491 s.d. 1493), spec 109 (TC-FA-TAG-1494), dan spec 116 (TC-FA-TAG-453).
- Urutan TC di dalam spec mengikuti keadaan reader dan stok agar perubahan state seminimal mungkin: reader tidak tersambung (TC-454), reader tersambung dengan stok tersedia (TC-455, TC-457, TC-458), lalu stok RFID 0 (TC-456).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 8, 15, dan 28 (mengatur reader, aset, dan stok lewat fixture backend serta menutup Popup Detail), langkah 20 (menghapus centang sisa TC-457), dan langkah 27 ([Cancel] pada dialog tanpa isian, tanpa konfirmasi D-11).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 8, 15, 28) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-457 tidak mengklik `Show` di samping `Not Paired Yet` sebelum mencentang aset yang Not Paired Yet; spec mengikuti langkah TC dan menganggap baris 'Excavator 20 Ton - 51' tampil pada tabel Popup Detail.
  - TC-FA-TAG-457 dan TC-FA-TAG-458 tidak menyebut apakah Show Not Paired Yet masih aktif sesudah pindah TC; spec memberi langkah `Show` eksplisit pada TC-458 (langkah 21).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur reader tersambung atau tidak tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
