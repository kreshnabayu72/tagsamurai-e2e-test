---
id: TC-FA-TAG-E2E-111-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-2
title: "Sesi Pair TAG Beberapa Aset: Ringkasan Akhir Done, Skipped, dan Tombol Retry (Bagian 2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-462
  - TC-FA-TAG-463
coverage:
  web: automated
---

# Sesi Pair TAG Beberapa Aset: Ringkasan Akhir Done, Skipped, dan Tombol Retry (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan stok Available; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset sesi 1 sampai 3 | 'Excavator 20 Ton - 51' (AST-0051), 'Excavator 20 Ton - 52' (AST-0052), 'Excavator 20 Ton - 54' (AST-0054); Not Paired Yet, Group Plant A, TAG Type Asset Name RFID | `aset51`, `aset52`, `aset54` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokRfid` |

- State yang diubah dan pemulihannya: Tag RFID dipasangkan pada aset sesi (TC-FA-TAG-462 dan 463); fixture backend memulihkan aset ke Not Paired Yet dan stok Available antar blok dan di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 6, 9, 20, 22, 24); entri TAG Log Global (langkah 6, 9, 20, 22, 24).

## Test Steps

### Ringkasan Done dan Skipped tanpa Failed (TC-FA-TAG-462)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
4. Klik Bulk `Pair TAG`
5. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
6. Klik [Submit & next]
7. Klik [Skip]
8. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
9. Klik [Submit & next]
10. Verifikasi dialog ringkasan berjudul `Pair TAG`
11. Verifikasi 'Excavator 20 Ton - 51 (AST-0051)' dan 'Excavator 20 Ton - 54 (AST-0054)' berlabel `Done` dan 'Excavator 20 Ton - 52 (AST-0052)' berlabel `Skipped`
12. Verifikasi label `Failed` tidak tampil
13. Verifikasi tombol `[Retry skipped (1)]` dan [Close] tampil
14. Klik [Close]

### Semua aset Done tanpa tombol Retry (TC-FA-TAG-463)

15. Pulihkan ketiga aset ke Not Paired Yet dan isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416` lewat fixture backend hingga tersimpan, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
16. Klik `Show` di samping `Not Paired Yet`
17. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
18. Klik Bulk `Pair TAG`
19. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
20. Klik [Submit & next]
21. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
22. Klik [Submit & next]
23. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00416`
24. Klik [Submit & next]
25. Verifikasi ketiga aset berlabel `Done`
26. Verifikasi tombol berlabel `Retry skipped` (beserta jumlah dalam kurung) tidak tampil dan hanya [Close] tersedia
27. Klik [Close]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-462, 463). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Pair beberapa aset ada juga di spec 110 (TC-FA-TAG-459 s.d. 461), spec 112 (TC-FA-TAG-464, 465), spec 113 (TC-FA-TAG-466, 469, 470), spec 114 (TC-FA-TAG-471, 472, 1383), dan spec 115 (TC-FA-TAG-1445, 1446, 1487).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14 dan 27 (menutup ringkasan), langkah 15 (memulihkan data lewat fixture backend hingga tersimpan, memuat ulang halaman, dan membuka popup dari keadaan bersih).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 6, 9, 20, 22, 24); entri TAG Log Global (langkah 6, 9, 20, 22, 24).
- Temuan untuk QA:
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-462 ("Aset 1 dan 3 Paired; aset 2 tetap Not Paired Yet") dan TC-463 ("Ketiga aset Paired") tanpa langkah observasi di TC tidak diasersi.
