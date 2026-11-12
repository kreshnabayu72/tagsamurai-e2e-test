---
id: TC-FA-TAG-E2E-114-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-5
title: "Sesi Pair TAG Beberapa Aset: Ikon Close Terisi dan Kode yang Sudah Dipakai Ditolak (Bagian 5)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-471
  - TC-FA-TAG-472
  - TC-FA-TAG-1383
coverage:
  web: automated
---

# Sesi Pair TAG Beberapa Aset: Ikon Close Terisi dan Kode yang Sudah Dipakai Ditolak (Bagian 5)

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

- State yang diubah dan pemulihannya: Tag `RF-00412` dipasangkan pada 'Excavator 20 Ton - 51' pada TC-FA-TAG-472; hook `after` memulihkan aset ke Not Paired Yet dan `RF-00412` ke Available lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 23); entri TAG Log Global (langkah 23).

## Test Steps

### Kode dari aset yang di-Skip ditolak (TC-FA-TAG-1383)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
4. Klik Bulk `Pair TAG`
5. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
6. Klik [Skip]
7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
8. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada slot `RFID TAG` aset 2
9. Verifikasi Tag `RF-00412` tidak terisi dan tidak terverifikasi di slot aset 2

### Ikon close pada aset terbuka yang sudah berisi kode (TC-FA-TAG-471)

10. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
11. Klik `Show` di samping `Not Paired Yet`
12. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
13. Klik Bulk `Pair TAG`
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
15. Klik ikon close dialog
16. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
17. Klik [Discard]

### Kode dari aset yang sudah Done ditolak (TC-FA-TAG-472)

18. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
19. Klik `Show` di samping `Not Paired Yet`
20. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
21. Klik Bulk `Pair TAG`
22. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
23. Klik [Submit & next]
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
25. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada slot `RFID TAG` aset 2
26. Verifikasi Tag `RF-00412` tidak terisi dan tidak terverifikasi di slot aset 2

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-471, 472, 1383). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Pair beberapa aset ada juga di spec 110, 111, 112, 113, dan 115 (TC-FA-TAG-459 s.d. 470, 1445, 1446, 1487).
- Urutan TC di dalam spec: TC-1383 (aset 1 di-Skip), TC-471 (dialog dibuang dengan [Discard]), lalu TC-472 yang menyimpan perubahan; sehingga tidak ada pemulihan data di antaranya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10 dan 18 (memuat ulang halaman, yang juga mengakhiri sesi sebelumnya, dan membuka popup dari keadaan bersih), dan langkah 17 ([Discard] dari konfirmasi D-11 yang diasersi pada langkah 16).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 23); entri TAG Log Global (langkah 23).
- Temuan untuk QA:
  - TC-FA-TAG-471 tidak menyebut hasil [Discard] pada sesi Pair (ringkasan atau penutupan sesi); spec tidak mengasersinya.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-472 ("Aset 1 Done dengan Tag `RF-00412` Paired; aset 2 tetap Not Paired Yet") dan TC-1383 tanpa langkah observasi di TC tidak diasersi.
