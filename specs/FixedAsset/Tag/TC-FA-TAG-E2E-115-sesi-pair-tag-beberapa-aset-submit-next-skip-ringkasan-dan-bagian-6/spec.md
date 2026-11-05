---
id: TC-FA-TAG-E2E-115-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-6
title: "Sesi Pair TAG Beberapa Aset: Tag Combined Dipindai Ulang dan Semua Aset Skipped (Bagian 6)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1445
  - TC-FA-TAG-1446
  - TC-FA-TAG-1487
coverage:
  web: automated
---

# Sesi Pair TAG Beberapa Aset: Tag Combined Dipindai Ulang dan Semua Aset Skipped (Bagian 6)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Tag combined, dan stok Available; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset NFC dan QR | 'Laptop Pro 14 - 9' (AST-0109) dan 'Laptop Pro 14 - 10' (AST-0110); Not Paired Yet, Group Plant A, TAG Type Asset Name NFC dan QR | `aset109`, `aset110` |
| Tag combined | Tag combined NFC+QR `NF-00810` / `QR-00810` Available (satu unit) | `combined810` |
| Aset sesi RFID | 'Excavator 20 Ton - 51' (AST-0051), 'Excavator 20 Ton - 52' (AST-0052), 'Excavator 20 Ton - 54' (AST-0054); Not Paired Yet, Group Plant A, TAG Type Asset Name RFID | `aset51`, `aset52`, `aset54` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokRfid` |

- State yang diubah dan pemulihannya: Tag combined `NF-00810` / `QR-00810` dipasangkan pada 'Laptop Pro 14 - 9' pada TC-FA-TAG-1445; hook `after` memulihkan aset ke Not Paired Yet dan Tag combined ke Available lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 26); entri TAG Log Global (langkah 26).

## Test Steps

### Tag combined dari aset yang di-Skip ditolak (TC-FA-TAG-1446)

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Centang baris 'Laptop Pro 14 - 9' dan 'Laptop Pro 14 - 10'
4. Klik Bulk `Pair TAG`
5. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00810`
6. Klik [Skip]
7. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` aset 2 lalu pindai Tag `NF-00810`
8. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada aset 2
9. Verifikasi slot `NFC TAG` dan `QR TAG` aset 2 tetap `Not scanned` dan tidak terverifikasi

### Semua aset Skipped (TC-FA-TAG-1487)

10. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
11. Klik `Show` di samping `Not Paired Yet`
12. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
13. Klik Bulk `Pair TAG`
14. Klik [Skip]
15. Klik [Skip]
16. Klik [Skip]
17. Verifikasi ringkasan akhir memuat 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54' berlabel `Skipped` beserta tombol `[Retry skipped (3)]` dan `[Close]`
18. Klik [Close]
19. Verifikasi ringkasan menutup
20. Verifikasi toast T-20 ("Success, assets have been paired.") dan toast T-19 ("Success, asset has been paired.") tidak tampil

### Tag combined dari aset yang sudah Done ditolak (TC-FA-TAG-1445)

21. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
22. Klik `Show` di samping `Not Paired Yet`
23. Centang baris 'Laptop Pro 14 - 9' dan 'Laptop Pro 14 - 10'
24. Klik Bulk `Pair TAG`
25. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00810`
26. Klik [Submit & next]
27. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` aset 2 lalu pindai Tag `NF-00810`
28. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada aset 2
29. Verifikasi slot `NFC TAG` dan `QR TAG` aset 2 tetap `Not scanned` dan tidak terverifikasi

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1445, 1446, 1487). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Pair beberapa aset ada juga di spec 110 s.d. 114 (TC-FA-TAG-459 s.d. 466, 469 s.d. 472, 1383).
- Urutan TC di dalam spec: TC-1446 (aset 1 di-Skip), TC-1487 (aset RFID lain, semua Skipped, tanpa perubahan data), lalu TC-1445 yang menyimpan perubahan; sehingga tidak ada pemulihan data di antaranya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10 dan 21 (memuat ulang halaman, yang juga mengakhiri sesi sebelumnya, dan membuka popup dari keadaan bersih).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 26); entri TAG Log Global (langkah 26).
- Temuan untuk QA:
  - TC-FA-TAG-1487 butir c (toast T-20 dan T-19 tidak tampil) diasersi setelah ringkasan menutup (langkah 19) sebagai anchor positif bahwa respons sudah diproses; TC tidak memberi anchor lain.
  - TC-FA-TAG-1445 dan TC-FA-TAG-1446 tidak memberi cara menutup sesi di akhir; spec mengandalkan F5.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-1445, 1446, dan 1487 (aset Done/Skipped, "tidak ada entri Changelog Pair TAG") tanpa langkah observasi di TC tidak diasersi.
