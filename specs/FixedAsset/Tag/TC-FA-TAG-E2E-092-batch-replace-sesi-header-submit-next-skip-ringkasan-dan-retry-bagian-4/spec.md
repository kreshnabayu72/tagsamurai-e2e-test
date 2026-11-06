---
id: TC-FA-TAG-E2E-092-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-4
title: "Batch Replace TAG: Ikon Close pada Aset Terbuka dan Discard (Bagian 4)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-398
  - TC-FA-TAG-399
  - TC-FA-TAG-1473
coverage:
  web: automated
---

# Batch Replace TAG: Ikon Close pada Aset Terbuka dan Discard (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Available; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset sesi 1 | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A), Tag RFID `RF-00330` Paired | `aset220` |
| Aset sesi 2 | 'Excavator 20 Ton - 221' (AST-0221, Group Plant A), Tag RFID `RF-00140` Paired | `aset221` |
| Aset sesi 3 | 'Excavator 20 Ton - 23' (AST-0023, Group Plant A), Tag RFID `RF-00141` Paired | `aset23` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokRfid` |

- State yang diubah dan pemulihannya: Tag aset 'Excavator 20 Ton - 220' diganti `RF-00412` pada tiap blok yang memakai [Submit & next]; fixture backend memulihkan Tag `RF-00330` Paired dan stok Available antar blok dan di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 25); entri TAG Log Global (langkah 5, 25). Klik [Discard] pada langkah 18 dan 27 serta penutupan dialog tanpa isian pada langkah 6 dan 33 tidak menyimpan penggantian dan tidak menambah entri.

## Test Steps

### Ikon close pada aset terbuka tanpa isian (TC-FA-TAG-398)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
3. Klik Bulk `Batch Replace TAG`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit & next]
6. Klik ikon close pada dialog aset ke-2 tanpa mengisi apa pun
7. Verifikasi dialog konfirmasi D-09 tidak tampil
8. Verifikasi ringkasan akhir tampil memuat 'Excavator 20 Ton - 220' berlabel `Done`
9. Verifikasi aset ke-2 'Excavator 20 Ton - 221' (AST-0221) berlabel `Skipped`
10. Verifikasi tombol `Retry skipped and failed (1)` tampil
11. Verifikasi aset ke-3 yang belum dibuka tidak masuk ringkasan

### Ikon close pada aset terbuka yang terisi lalu Discard (TC-FA-TAG-399)

12. Pulihkan Tag `RF-00330` Paired pada 'Excavator 20 Ton - 220' dan isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416` lewat fixture backend hingga tersimpan, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
14. Klik Bulk `Batch Replace TAG`
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
16. Klik ikon close dialog
17. Verifikasi dialog judul "Discard Replacement", body "Discard this replacement? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
18. Klik [Discard]
19. Verifikasi ringkasan akhir tampil
20. Verifikasi aset ke-2 dan ke-3 yang belum dibuka tidak masuk ringkasan

### Aset terbuka yang terisi menjadi Skipped dan dapat dijalankan lagi (TC-FA-TAG-1473)

21. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
22. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
23. Klik Bulk `Batch Replace TAG`
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
25. Klik [Submit & next]
26. Pada dialog aset ke-2, klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
27. Klik ikon close lalu klik [Discard] pada dialog konfirmasi D-09
28. Verifikasi ringkasan akhir memuat 'Excavator 20 Ton - 220' berlabel `Done` dan 'Excavator 20 Ton - 221' berlabel `Skipped`
29. Verifikasi aset ke-3 'Excavator 20 Ton - 23' yang belum dibuka tidak masuk ringkasan
30. Verifikasi tombol `Retry skipped and failed (1)` tampil
31. Klik `Retry skipped and failed (1)`
32. Verifikasi Dialog Replace TAG terbuka hanya untuk 'Excavator 20 Ton - 221'
33. Klik ikon close dialog tanpa mengisi apa pun
34. Klik [Close] pada ringkasan akhir

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-398, 399, 1473). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Batch Replace dilanjutkan di spec 089 (TC-FA-TAG-388 s.d. 391), spec 090 (TC-FA-TAG-392 s.d. 394), dan spec 091 (TC-FA-TAG-395 s.d. 397).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 12 dan 21 (memulihkan data lewat fixture backend hingga tersimpan, memuat ulang halaman, dan membuka popup dari keadaan bersih; menutup sesi sebelumnya ikut tercakup F5), serta 33 dan 34 (menutup sesi di akhir spec).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 25); entri TAG Log Global (langkah 5, 25). Klik [Discard] pada langkah 18 dan 27 serta penutupan dialog tanpa isian pada langkah 6 dan 33 tidak menyimpan penggantian dan tidak menambah entri.
- Temuan untuk QA:
  - TC-FA-TAG-398 butir c menulis `Retry skipped and failed (1)` tampil saat aset ke-3 belum dibuka; TC tidak menyatakan apakah aset ke-3 dihitung pada tombol Retry. Spec mengasersi sebagaimana tertulis.
  - TC-FA-TAG-399 tidak menyatakan label aset ke-1 sesudah Discard (Skipped atau tidak masuk ringkasan); spec hanya mengasersi butir Expected.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-398 ("Aset ke-3 tidak berubah", "Tag `RF-00412` Paired pada aset ke-1"), TC-399, dan TC-1473 tanpa langkah observasi di TC tidak diasersi.
