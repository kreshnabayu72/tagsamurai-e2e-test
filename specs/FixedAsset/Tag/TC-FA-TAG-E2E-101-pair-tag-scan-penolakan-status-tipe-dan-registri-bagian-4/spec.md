---
id: TC-FA-TAG-E2E-101-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-4
title: "Pair TAG: Penolakan Pindai Ulang V-09 dan Tag Milik Supply Asset (Bagian 4)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1453
  - TC-FA-TAG-1454
  - TC-FA-TAG-1462
coverage:
  web: automated
---

# Pair TAG: Penolakan Pindai Ulang V-09 dan Tag Milik Supply Asset (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, stok Available per tipe, Tag combined, dan Tag milik produk Supply Asset; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |
| Tag combined | Tag combined NFC+QR `NF-00810` / `QR-00810` Available (satu unit) | `combined810` |
| Tag Supply Asset | Tag `SA-00020` terdaftar di produk Supply Asset (stok dan SKU) | `tagSupplyAsset20` |

- State yang diubah dan pemulihannya: spec tidak mengubah data (semua pindaian ditolak atau dibuang dengan [Discard]).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*/SA-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### Tag milik produk Supply Asset (TC-FA-TAG-1462)

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai kode `SA-00020`
5. Verifikasi pesan inline "This TAG is used by Supply Asset." tampil pada slot `RFID TAG`
6. Verifikasi pesan V-07 "[TAG Code] is not available ([Status])." tidak tampil
7. Verifikasi slot `RFID TAG` tetap `Not scanned` dan tidak terverifikasi

### Tag tunggal dipindai ulang ke slot bertipe lain (TC-FA-TAG-1453)

8. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
9. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai ulang Tag `RF-00412`
10. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada slot `NFC TAG`
11. Verifikasi pesan V-08 "This slot needs a NFC TAG." tidak tampil
12. Verifikasi slot `RFID TAG` tetap menampilkan `RF-00412` dengan badge `Verified`
13. Verifikasi slot `NFC TAG` tetap `Not scanned` dan tidak terverifikasi
14. Klik ikon close dialog Pair TAG
15. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
16. Klik [Discard]

### Tag combined dipindai ulang ke slot lain (TC-FA-TAG-1454)

17. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
18. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag combined `NF-00810`
19. Verifikasi slot `NFC TAG` dan `QR TAG` terisi `NF-00810` / `QR-00810` dengan badge `Verified`
20. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai ulang Tag combined `NF-00810`
21. Verifikasi error inline V-09 "This TAG has already been scanned." tampil pada slot `RFID TAG`
22. Verifikasi pesan V-26 "This combined TAG doesn't match the open slots." dan V-08 "This slot needs a RFID TAG." tidak tampil
23. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Verified` dan slot `RFID TAG` tetap `Not scanned` dan tidak terverifikasi
24. Klik ikon close dialog Pair TAG
25. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
26. Klik [Discard]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1453, 1454, 1462). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik penolakan scan Pair TAG ada di spec 098 (TC-FA-TAG-419 s.d. 423), spec 099 (TC-FA-TAG-424, 426 s.d. 429), dan spec 100 (TC-FA-TAG-430 s.d. 434).
- Urutan TC di dalam spec: TC-1462 (tanpa isian tersimpan) dahulu, lalu TC-1453, lalu TC-1454; dialog TC-1453 yang berisi `RF-00412` ditutup dengan `✕`, verifikasi dialog `Unsaved Changes` setara `Discard Pairing`, dan [Discard] sebelum TC-1454 dimulai dari slot kosong (S-08).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14, 16, 24, dan 26 (menutup dialog yang berisi pindaian) serta 17 (membuka ulang dialog Pair TAG pada popup yang masih terbuka).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*/SA-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1462 butir b tidak memberi anchor selain butir a; pesan V-07 tidak tampil diasersi sesudah pesan Supply Asset tampil pada slot yang sama.
  - TC-FA-TAG-1453 dan TC-FA-TAG-1454 menulis "Tag `RF-00412` dipindai di slot lalu dipindai ulang"; spec memakai kode persis.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-1453, 1454, dan 1462 ("Tidak ada Tag yang dipasangkan; aset tetap Not Paired Yet") tanpa langkah observasi di TC tidak diasersi.
