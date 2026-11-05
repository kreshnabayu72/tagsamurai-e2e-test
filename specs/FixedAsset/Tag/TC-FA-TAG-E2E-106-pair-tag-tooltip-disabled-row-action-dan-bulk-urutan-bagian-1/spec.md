---
id: TC-FA-TAG-E2E-106-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-1
title: "Pair TAG: Tooltip Disabled Row Action menurut Reader, Status Aset, dan Stok (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-449
  - TC-FA-TAG-450
  - TC-FA-TAG-451
  - TC-FA-TAG-452
coverage:
  web: automated
---

# Pair TAG: Tooltip Disabled Row Action menurut Reader, Status Aset, dan Stok (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB yang dapat diatur tersambung atau tidak tersambung (driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Asset Status aset, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset target | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet; Asset Status normal, In Disposal Process, atau Disposed sesuai bagian | `aset51` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701`; stok RFID 0 pada bagian TC-452 | `stokAvailable` |

- State yang diubah dan pemulihannya: status reader, Asset Status aset 51, dan stok Available RFID diatur per bagian lewat fixture; hook `after` memulihkan reader tersambung, Asset Status normal, dan stok seperti awal.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 9, 17, 25) yang menyiapkan atau memulihkan state.

## Test Steps

### Reader tidak tersambung (TC-FA-TAG-449)

1. Putuskan reader dari komputer lewat simulator reader, isi stok Global dengan Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` Available, dan pastikan 'Excavator 20 Ton - 51' Not Paired Yet berstatus normal lewat fixture backend hingga tersimpan
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Klik tombol teks `Show` di samping field `Not Paired Yet`
4. Arahkan kursor ke row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
5. Verifikasi row action `Pair TAG` tetap tampil (visible) namun berstatus Disabled
6. Verifikasi tooltip "Connect a TAG reader to pair."
7. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
8. Verifikasi Dialog Pair TAG tidak terbuka

### Aset In Disposal Process (TC-FA-TAG-450)

9. Tutup Popup Detail, sambungkan reader (driver terpasang, aktif, sudah disinkronkan), dan atur 'Excavator 20 Ton - 51' berstatus In Disposal Process lewat fixture backend hingga tersimpan
10. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
11. Klik tombol teks `Show` di samping field `Not Paired Yet`
12. Arahkan kursor ke row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
13. Verifikasi row action `Pair TAG` tetap tampil (visible) namun berstatus Disabled
14. Verifikasi tooltip "This asset can't be paired while it is in disposal."
15. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
16. Verifikasi Dialog Pair TAG tidak terbuka

### Aset Disposed (TC-FA-TAG-451)

17. Tutup Popup Detail dan atur 'Excavator 20 Ton - 51' berstatus Disposed lewat fixture backend hingga tersimpan
18. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
19. Klik tombol teks `Show` di samping field `Not Paired Yet`
20. Arahkan kursor ke row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
21. Verifikasi row action `Pair TAG` tetap tampil (visible) namun berstatus Disabled
22. Verifikasi tooltip "This asset can't be paired while it is in disposal."
23. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
24. Verifikasi Dialog Pair TAG tidak terbuka

### Stok seluruh tipe yang dibutuhkan 0 (TC-FA-TAG-452)

25. Tutup Popup Detail, atur 'Excavator 20 Ton - 51' berstatus normal (Not Paired Yet), dan hapus semua Tag RFID Available dari stok Global lewat fixture backend hingga tersimpan
26. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
27. Klik tombol teks `Show` di samping field `Not Paired Yet`
28. Arahkan kursor ke row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
29. Verifikasi row action `Pair TAG` tetap tampil (visible) namun berstatus Disabled
30. Verifikasi tooltip "No available RFID TAG in stock."
31. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
32. Verifikasi Dialog Pair TAG tidak terbuka

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-449 s.d. 452). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik tooltip Disabled Pair TAG dilanjutkan di spec 107 (TC-FA-TAG-454 s.d. 458), spec 108 (TC-FA-TAG-1455, 1491 s.d. 1493), dan spec 109 (TC-FA-TAG-1494). TC-FA-TAG-453 (row action tetap Enabled bila hanya sebagian tipe stok 0) ada di spec 116.
- Urutan TC di dalam spec mengikuti keadaan reader dan Asset Status agar perubahan state seminimal mungkin: reader tidak tersambung (TC-449), lalu reader tersambung dengan Asset Status In Disposal Process (TC-450), Disposed (TC-451), dan stok 0 (TC-452).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 9, 17, dan 25 (mengatur reader, Asset Status, dan stok lewat fixture backend serta menutup Popup Detail). Popup Detail dibuka ulang sesudah tiap perubahan state supaya state terbaru terbaca.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 1, 9, 17, 25) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-452 butir b menulis tooltip "No available RFID TAG in stock." sedangkan TC-FA-TAG-372 untuk Replace menulis "No available RFID TAG in stock. Activate TAG in Global Settings > TAG."; spec mengikuti teks tiap TC.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur reader tersambung atau tidak tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
