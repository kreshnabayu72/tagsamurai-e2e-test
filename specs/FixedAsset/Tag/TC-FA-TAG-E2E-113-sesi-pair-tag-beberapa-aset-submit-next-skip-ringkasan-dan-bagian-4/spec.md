---
id: TC-FA-TAG-E2E-113-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-4
title: "Sesi Pair TAG Beberapa Aset: Retry skipped, Konflik D-03, dan Ikon Close Tanpa Kode (Bagian 4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-466
  - TC-FA-TAG-469
  - TC-FA-TAG-470
coverage:
  web: automated
---

# Sesi Pair TAG Beberapa Aset: Retry skipped, Konflik D-03, dan Ikon Close Tanpa Kode (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Sesi API aktor: pelaku kedua pada TC-FA-TAG-469 (pengguna lain yang memasangkan Tag `RF-00415` ke aset lain) memakai login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya; akun pelaku disediakan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan stok Available; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset sesi 1 sampai 3 | 'Excavator 20 Ton - 51' (AST-0051), 'Excavator 20 Ton - 52' (AST-0052), 'Excavator 20 Ton - 54' (AST-0054); Not Paired Yet, Group Plant A, TAG Type Asset Name RFID | `aset51`, `aset52`, `aset54` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokRfid` |
| Aset tujuan perebutan (TC-469) | satu aset Not Paired Yet dengan TAG Type Asset Name RFID yang menerima `RF-00415` dari pelaku kedua | `asetTujuanRebut` |

- State yang diubah dan pemulihannya: Tag `RF-00412` dipasangkan pada 'Excavator 20 Ton - 51' di tiap blok dan `RF-00415` dipasangkan ke aset lain oleh pelaku kedua (TC-469); fixture backend memulihkan aset ke Not Paired Yet dan stok Available antar blok dan di hook `after`.

## Test Steps

### Retry skipped (TC-FA-TAG-466)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
4. Klik Bulk `Pair TAG`
5. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
6. Klik [Submit & next]
7. Klik [Skip]
8. Klik [Skip]
9. Klik `[Retry skipped (2)]`
10. Verifikasi dialog sesi terbuka untuk 'Excavator 20 Ton - 52'
11. Klik [Skip]
12. Verifikasi dialog sesi berganti ke 'Excavator 20 Ton - 54'
13. Verifikasi aset 'Excavator 20 Ton - 51' yang `Done` tidak dibuka lagi

### Konflik D-03 (TC-FA-TAG-469)

14. Pulihkan ketiga aset ke Not Paired Yet dan isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416` lewat fixture backend hingga tersimpan, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
15. Klik `Show` di samping `Not Paired Yet`
16. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
17. Klik Bulk `Pair TAG`
18. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
19. Klik [Submit & next]
20. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
21. Pelaku kedua lewat sesi API memasangkan Tag `RF-00415` ke aset lain hingga tersimpan
22. Klik [Submit & next]
23. Verifikasi dialog judul "Cannot Pair TAG", body "RF-00415 is no longer available. Scan another TAG.", tombol [OK]
24. Klik [OK] pada dialog
25. Verifikasi dialog kembali ke slot `RFID TAG` aset ke-2 dalam keadaan `Not scanned`

### Ikon close pada aset terbuka tanpa kode (TC-FA-TAG-470)

26. Pulihkan ketiga aset ke Not Paired Yet, kembalikan `RF-00415` ke Available, dan isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416` lewat fixture backend hingga tersimpan, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
27. Klik `Show` di samping `Not Paired Yet`
28. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
29. Klik Bulk `Pair TAG`
30. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
31. Klik [Submit & next]
32. Klik ikon close pada dialog aset ke-2 tanpa mengisi apa pun
33. Verifikasi dialog konfirmasi D-11 tidak tampil
34. Verifikasi ringkasan akhir tampil memuat 'Excavator 20 Ton - 51 (AST-0051)' berlabel `Done`
35. Verifikasi aset ke-3 yang belum dibuka tidak masuk ringkasan

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-466, 469, 470). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Pair beberapa aset ada juga di spec 110, 111, 112, 114, dan 115 (TC-FA-TAG-459 s.d. 465, 471, 472, 1383, 1445, 1446, 1487).
- Pelaku kedua memakai sesi API (keputusan 2026-10-21/30): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 21).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14 dan 26 (memulihkan data lewat fixture backend hingga tersimpan, memuat ulang halaman, dan membuka popup dari keadaan bersih; F5 juga mengakhiri sesi sebelumnya).
- Temuan untuk QA:
  - TC-FA-TAG-469 tidak menyebut aset tujuan pemasangan `RF-00415` dan pelaku pengguna lain; spec memakai aset Not Paired Yet milik seed dan pelaku sesi API yang disediakan tim FE.
  - TC-FA-TAG-466 dan TC-FA-TAG-469 tidak memberi cara menutup sesi di akhir; spec mengandalkan F5 pada langkah berikutnya.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-469 ("Aset 1 tetap Paired") dan TC-470 ("Aset ke-3 tetap Not Paired Yet") tanpa langkah observasi di TC tidak diasersi.
