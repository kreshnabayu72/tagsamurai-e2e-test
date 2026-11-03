---
id: TC-FA-TAG-E2E-089-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-1
title: "Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-388
  - TC-FA-TAG-389
  - TC-FA-TAG-390
  - TC-FA-TAG-391
coverage:
  web: automated
---

# Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 1)

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
| Laporan terbuka | satu laporan terbuka pada Tag `RF-00130` (TC-FA-TAG-391) | `laporan130` |

- State yang diubah dan pemulihannya: Tag Paired aset sesi 1 sampai 3 dan stok Available berubah oleh Submit & next; fixture backend memulihkannya antar blok dan hook `after` memulihkan keadaan awal (Tag `RF-00130`, `RF-00140`, `RF-00141` Paired; stok Available seperti awal; laporan `RF-00130` dikembalikan).

## Test Steps

### Header, footer, dan Skip (TC-FA-TAG-388, TC-FA-TAG-390)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
3. Klik Bulk `Batch Replace TAG`
4. Verifikasi header dialog `Replace TAG · Asset 1 of 3`
5. Verifikasi isi dialog sama dengan Dialog Replace TAG: blok info, `TAG to replace`, `Replacement TAG`
6. Verifikasi footer memuat tombol [Skip] dan [Submit & next]
7. Klik [Skip]
8. Verifikasi dialog berganti ke header `Replace TAG · Asset 2 of 3`
9. Verifikasi tidak ada konfirmasi dan tidak ada Toast
10. Klik ikon close dialog aset ke-2 tanpa mengisi apa pun
11. Klik [Close] pada ringkasan akhir

### Submit & next (TC-FA-TAG-389)

12. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
14. Klik Bulk `Batch Replace TAG`
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
16. Klik [Submit & next]
17. Verifikasi dialog berganti ke header `Replace TAG · Asset 2 of 3` untuk 'Excavator 20 Ton - 221'
18. Verifikasi isian aset 1 tidak terbawa ke aset 2 (slot `RFID TAG` `Not scanned`)
19. Klik ikon close dialog aset ke-2 tanpa mengisi apa pun
20. Klik [Close] pada ringkasan akhir

### Ringkasan akhir Done, Skipped, dan laporan ditutup (TC-FA-TAG-391)

21. Pulihkan Tag `RF-00130` Paired pada 'Excavator 20 Ton - 220' dengan laporan terbuka, isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416`, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
22. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
23. Klik Bulk `Batch Replace TAG`
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
25. Klik [Submit & next]
26. Klik [Skip]
27. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
28. Klik [Submit & next]
29. Verifikasi dialog ringkasan berjudul `Batch Replace TAG` tampil
30. Verifikasi aset 1 dan aset 3 berlabel `Done` dan aset 2 berlabel `Skipped`
31. Verifikasi tiap aset ditulis `[Asset Name] - [Increment] ([Asset ID])`, contoh `Excavator 20 Ton - 220 (AST-0220)`
32. Verifikasi baris "1 report closed as Replaced."
33. Verifikasi tombol `[Retry skipped and failed (1)]` dan [Close] tampil
34. Klik [Close]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-388, 389, 390, 391). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Batch Replace dilanjutkan di spec 090 (TC-FA-TAG-392 s.d. 394), spec 091 (TC-FA-TAG-395 s.d. 397), dan spec 092 (TC-FA-TAG-398, 399, 1473).
- Urutan TC di dalam spec: TC-388 dan TC-390 berbagi satu sesi (langkah 1 sampai 11) karena TC-390 hanya melewati aset tanpa mengubah apa pun; sesudahnya TC-389 yang menyimpan, lalu TC-391 yang membutuhkan keadaan awal dipulihkan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10 dan 11 (mengakhiri sesi tanpa mengubah data), 12 dan 21 (memuat ulang halaman supaya tabel dan popup dibuka dari keadaan bersih), 19, 20, dan 34 (menutup sesi dan ringkasan). Langkah 21 juga memulihkan data lewat fixture backend hingga tersimpan.
- Temuan untuk QA:
  - TC-FA-TAG-390 tidak menyebut cara mengakhiri sesi; spec mengakhirinya dengan ikon close (perilaku di TC-FA-TAG-398).
  - TC-FA-TAG-389 dan TC-FA-TAG-391: sesi tidak diselesaikan sampai ringkasan di TC-389; spec menutup sesinya dengan ikon close dan [Close] sebagai langkah penghubung.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-389, 390, dan 391 tanpa langkah observasi di TC (Tag Paired, tidak ada entri Changelog baru) tidak diasersi.
