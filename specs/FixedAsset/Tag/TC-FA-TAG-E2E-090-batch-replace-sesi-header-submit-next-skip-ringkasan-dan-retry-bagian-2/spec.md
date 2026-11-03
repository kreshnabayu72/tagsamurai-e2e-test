---
id: TC-FA-TAG-E2E-090-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-2
title: "Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-392
  - TC-FA-TAG-393
  - TC-FA-TAG-394
coverage:
  web: automated
---

# Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, stok Available, dan laporan Tag terbuka; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset sesi 1 | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A), Tag RFID `RF-00130` Paired | `aset220` |
| Aset sesi 2 | 'Excavator 20 Ton - 221' (AST-0221, Group Plant A), Tag RFID `RF-00140` Paired | `aset221` |
| Aset sesi 3 | 'Excavator 20 Ton - 23' (AST-0023, Group Plant A), Tag RFID `RF-00141` Paired | `aset23` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokRfid` |
| Laporan terbuka | tanpa laporan terbuka (TC-FA-TAG-392 dan TC-FA-TAG-394); laporan terbuka pada Tag `RF-00130` dan `RF-00140` (TC-FA-TAG-393) | `laporan130`, `laporan140` |

- State yang diubah dan pemulihannya: Tag Paired aset sesi, stok Available, dan laporan Tag berubah oleh Submit & next; fixture backend memulihkannya antar blok dan hook `after` memulihkan keadaan awal.

## Test Steps

### Semua aset Done tanpa laporan ditutup (TC-FA-TAG-392)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
3. Klik Bulk `Batch Replace TAG`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit & next]
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
7. Klik [Submit & next]
8. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00416`
9. Klik [Submit & next]
10. Verifikasi ketiga aset berlabel `Done`
11. Verifikasi baris laporan yang ditutup tidak tampil
12. Verifikasi tombol `[Retry skipped and failed ([N])]` tidak tampil dan hanya [Close] tersedia
13. Klik [Close]

### Dua laporan ditutup (TC-FA-TAG-393)

14. Pulihkan Tag `RF-00130`, `RF-00140`, `RF-00141` Paired pada ketiga aset dengan laporan terbuka pada `RF-00130` dan `RF-00140`, isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416`, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
15. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
16. Klik Bulk `Batch Replace TAG`
17. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
18. Klik [Submit & next]
19. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
20. Klik [Submit & next]
21. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00416`
22. Klik [Submit & next]
23. Verifikasi baris "2 reports closed as Replaced."
24. Klik [Close]

### Close pada ringkasan (TC-FA-TAG-394)

25. Pulihkan Tag `RF-00130`, `RF-00140`, `RF-00141` Paired tanpa laporan terbuka dan isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416`, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
26. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
27. Klik Bulk `Batch Replace TAG`
28. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
29. Klik [Submit & next]
30. Klik [Skip]
31. Klik [Skip]
32. Klik [Close]
33. Verifikasi toast "Success, asset has been replaced."
34. Verifikasi ringkasan menutup
35. Verifikasi tabel Paired dimuat ulang

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-392, 393, 394). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Batch Replace dilanjutkan di spec 089 (TC-FA-TAG-388 s.d. 391), spec 091 (TC-FA-TAG-395 s.d. 397), dan spec 092 (TC-FA-TAG-398, 399, 1473).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 13 dan 24 (menutup ringkasan), 14 dan 25 (memulihkan data lewat fixture backend hingga tersimpan, memuat ulang halaman, dan membuka popup dari keadaan bersih).
- Temuan untuk QA:
  - TC-FA-TAG-394 butir "tabel Paired dimuat ulang" tidak memberi cara mengamatinya; spec mengasersinya sebagaimana tertulis dan cara teknis mengamatinya diminta dari tim FE.
  - TC-FA-TAG-392 menulis tombol `[Retry skipped and failed ([N])]` dengan placeholder [N]; spec memakai teks itu sebagaimana tertulis.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-392, 393, dan 394 ("Tiga aset diganti", "Dua laporan ditutup `Replaced`", "Tag `RF-00412` Paired pada 'Excavator 20 Ton - 220'") tanpa langkah observasi di TC tidak diasersi.
