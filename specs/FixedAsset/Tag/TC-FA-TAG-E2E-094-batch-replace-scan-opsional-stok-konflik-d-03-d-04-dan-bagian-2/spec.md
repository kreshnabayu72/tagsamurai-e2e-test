---
id: TC-FA-TAG-E2E-094-batch-replace-scan-opsional-stok-konflik-d-03-d-04-dan-bagian-2
title: "Batch Replace TAG: Stok Habis di Tengah Sesi dan Konflik D-03 serta D-04 (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-404
  - TC-FA-TAG-408
  - TC-FA-TAG-409
coverage:
  web: automated
---

# Batch Replace TAG: Stok Habis di Tengah Sesi dan Konflik D-03 serta D-04 (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Sesi API aktor: pelaku kedua memakai login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`). Pelaku kedua di TC-FA-TAG-408 memasangkan Tag `RF-00415` ke aset lain; pelaku kedua di TC-FA-TAG-409 (pengguna Dedi K., tidak ada di Tabel Pre-setup TC: disediakan tim FE) mengganti Tag `RF-00140` pada 'Excavator 20 Ton - 221'. Keduanya tanpa asersi di sesinya.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri (Available, Reserved, Paired), dan stok Available; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset sesi 1 sampai 3 | 'Excavator 20 Ton - 220' (AST-0220, `RF-00130`), 'Excavator 20 Ton - 221' (AST-0221, `RF-00140`), 'Excavator 20 Ton - 23' (AST-0023, `RF-00141`), masing-masing satu Tag RFID Paired, Group Plant A | `aset220`, `aset221`, `aset23` |
| Stok TC-404 | hanya Tag RFID `RF-00412` Available; Tag RFID `RF-00601` Reserved | `stokRfid412`, `tagReserved601` |
| Stok TC-408 dan TC-409 | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` Available | `stokRfid` |
| Aset tujuan perebutan (TC-408) | satu aset Not Paired Yet dengan TAG Type Asset Name RFID yang menerima `RF-00415` dari pelaku kedua | `asetTujuanRebut` |

- State yang diubah dan pemulihannya: Tag `RF-00130` diganti (TC-404, TC-408, TC-409), `RF-00415` dipasangkan ke aset lain (TC-408), dan `RF-00140` diganti (TC-409); fixture backend memulihkan keadaan awal antar blok dan di hook `after`.

## Test Steps

### Stok habis di tengah sesi (TC-FA-TAG-404)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
3. Klik Bulk `Batch Replace TAG`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit & next]
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00601`
7. Verifikasi slot aset 2 menampilkan error inline "RF-00601 is not available (Reserved)."
8. Verifikasi slot aset 2 tetap `Not scanned`
9. Klik [Skip]
10. Verifikasi dialog berganti ke header `Replace TAG · Asset 3 of 3`

### Konflik D-03 (TC-FA-TAG-408)

11. Pulihkan Tag `RF-00130` Paired pada 'Excavator 20 Ton - 220', isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416`, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
12. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
13. Klik Bulk `Batch Replace TAG`
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
15. Klik [Submit & next]
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
17. Pelaku kedua lewat sesi API memasangkan Tag `RF-00415` ke aset lain hingga tersimpan
18. Klik [Submit & next]
19. Verifikasi dialog judul "Cannot Pair TAG", body "RF-00415 is no longer available. Scan another TAG.", tombol [OK]
20. Klik [OK] pada dialog
21. Verifikasi dialog kembali ke bagian Scan the Replacement TAG aset ke-2
22. Verifikasi slot aset ke-2 `Not scanned`
23. Klik ikon close dialog aset ke-2
24. Verifikasi ringkasan akhir memuat aset 1 berlabel `Done`

### Konflik D-04 (TC-FA-TAG-409)

25. Pulihkan Tag `RF-00130` dan `RF-00140` Paired, isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416`, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
26. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
27. Klik Bulk `Batch Replace TAG`
28. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
29. Klik [Submit & next]
30. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
31. Pelaku kedua (Dedi K.) lewat sesi API mengganti Tag `RF-00140` pada 'Excavator 20 Ton - 221' hingga tersimpan
32. Klik [Submit & next]
33. Verifikasi dialog judul "Asset TAG Has Changed", body "AST-0221 TAG has changed since this page was opened.", tombol [Update Data]
34. Klik [Update Data]
35. Verifikasi hanya aset ke-2 dimuat ulang dengan daftar lepas dihitung ulang
36. Klik ikon close dialog aset ke-2
37. Verifikasi ringkasan akhir memuat aset 1 berlabel `Done`

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-404, 408, 409). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik scan opsional, stok, dan konflik Batch ada di spec 093 (TC-FA-TAG-400 s.d. 403) dan spec 095 (TC-FA-TAG-410, 1382). Kegagalan di dalam sesi Batch (TC-FA-TAG-405 s.d. 407) ada di spec kelas fault injection tersendiri.
- Pelaku kedua memakai sesi API (keputusan 2026-10-21/30): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 17 dan 31).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 11 dan 25 (memulihkan data lewat fixture backend hingga tersimpan, memuat ulang halaman, dan membuka popup dari keadaan bersih; F5 juga mengakhiri sesi sebelumnya), 23 dan 36 (menutup aset ke-2 tanpa isian agar ringkasan akhir tampil sehingga status aset 1 `Done` teramati sebagai asersi butir c TC-408 dan TC-409).
- Spec di atas smell 35 langkah (37 langkah). Alasan: seluruh blok satu topik (sesi Batch Replace dengan kondisi yang berubah di tengah sesi) pada halaman dan reader yang sama, satu kelas (tanpa kelas c karena pelaku kedua memakai sesi API), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-TAG-408 tidak menyebut aset tujuan pemasangan `RF-00415` dan pelaku pengguna lain; spec memakai aset Not Paired Yet milik seed dan pelaku sesi API yang disediakan tim FE.
  - TC-FA-TAG-409 menyebut pelaku Dedi K. yang tidak ada di Tabel Pre-setup TC; akun disediakan tim FE.
  - TC-FA-TAG-408 dan TC-FA-TAG-409 butir "Status aset 1 (`Done`) dipertahankan" hanya teramati pada ringkasan akhir; spec menambah langkah menutup aset ke-2 untuk menampilkan ringkasan sebagai langkah penghubung.
  - TC-FA-TAG-404 tidak menyebut cara menutup sesi di akhir; spec memakai F5 pada langkah 11.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-404, 408, dan 409 tanpa langkah observasi di TC (mis. "Tag `RF-00130` pada aset 2 tetap Paired", "Penggantian Dedi K. tidak tertimpa") tidak diasersi.
