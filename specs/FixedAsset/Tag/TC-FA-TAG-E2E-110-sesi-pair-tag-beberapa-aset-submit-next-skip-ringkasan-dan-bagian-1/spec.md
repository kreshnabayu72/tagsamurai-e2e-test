---
id: TC-FA-TAG-E2E-110-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-1
title: "Sesi Pair TAG Beberapa Aset: Header, Footer, Submit & next, dan Skip (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-459
  - TC-FA-TAG-460
  - TC-FA-TAG-461
coverage:
  web: automated
---

# Sesi Pair TAG Beberapa Aset: Header, Footer, Submit & next, dan Skip (Bagian 1)

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

- State yang diubah dan pemulihannya: Tag `RF-00412` dipasangkan pada 'Excavator 20 Ton - 51' (TC-FA-TAG-460); hook `after` memulihkan aset ke Not Paired Yet dan `RF-00412` ke Available lewat fixture backend.

## Test Steps

### Header, footer, isi dialog, dan Skip (TC-FA-TAG-459, TC-FA-TAG-461)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
4. Klik Bulk `Pair TAG`
5. Verifikasi header dialog `Pair TAG · Asset 1 of 3`
6. Verifikasi footer memuat tombol [Skip] dan [Submit & next]
7. Verifikasi isi dialog sama dengan Dialog Pair TAG: bagian `TAG to pair` dengan slot `RFID TAG`
8. Klik [Skip]
9. Verifikasi dialog berganti ke header `Pair TAG · Asset 2 of 3`
10. Klik ikon close dialog aset ke-2 tanpa mengisi apa pun
11. Klik [Close] pada ringkasan akhir

### Submit & next (TC-FA-TAG-460)

12. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Klik `Show` di samping `Not Paired Yet`
14. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
15. Klik Bulk `Pair TAG`
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
17. Klik [Submit & next]
18. Verifikasi dialog berganti ke header `Pair TAG · Asset 2 of 3`
19. Verifikasi slot `RFID TAG` `Not scanned`
20. Klik ikon close dialog aset ke-2 tanpa mengisi apa pun
21. Klik [Close] pada ringkasan akhir

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-459, 460, 461). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Pair beberapa aset dilanjutkan di spec 111 (TC-FA-TAG-462, 463), spec 112 (TC-FA-TAG-464, 465), spec 113 (TC-FA-TAG-466, 469, 470), spec 114 (TC-FA-TAG-471, 472, 1383), dan spec 115 (TC-FA-TAG-1445, 1446, 1487).
- Urutan TC di dalam spec: TC-459 dan TC-461 berbagi satu sesi (langkah 1 sampai 11) karena TC-461 hanya melewati aset tanpa mengubah apa pun; TC-460 menyimpan perubahan sehingga ditaruh terakhir.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10 dan 11, 20 dan 21 (mengakhiri sesi tanpa mengubah data lain), serta 12 (memuat ulang halaman dan membuka popup dari keadaan bersih).
- Temuan untuk QA:
  - TC-FA-TAG-459, 460, 461 tidak menyebut cara menutup sesi di akhir; spec memakai ikon close pada aset tanpa isian lalu [Close] (perilaku ikon close tanpa isian: TC-FA-TAG-470).
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-460 ("Tag `RF-00412` Paired pada 'Excavator 20 Ton - 51'", "Dua aset lain tetap Not Paired Yet") dan TC-461 ("Aset 'Excavator 20 Ton - 51' tetap Not Paired Yet") tanpa langkah observasi di TC tidak diasersi.
