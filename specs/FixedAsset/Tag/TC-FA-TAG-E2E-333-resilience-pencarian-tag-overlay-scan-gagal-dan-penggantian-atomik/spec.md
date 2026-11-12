---
id: TC-FA-TAG-E2E-333-resilience-pencarian-tag-overlay-scan-gagal-dan-penggantian-atomik
title: "Resilience: Pencarian Tag di Overlay Scan Gagal (5xx dan Timeout) dan Penggantian Atomik saat Pemasangan Tag Baru Gagal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-259
  - TC-FA-TAG-260
  - TC-FA-TAG-1350
coverage:
  web: automated
---

# Resilience: Pencarian Tag di Overlay Scan Gagal (5xx dan Timeout) dan Penggantian Atomik saat Pemasangan Tag Baru Gagal

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di overlay scan dan ButtonScan; (2) `Spectra.intercept` parsial: respons 5xx hanya pada pindaian pertama pencarian Tag, tidak ada respons sampai timeout pada pencarian Tag, dan kegagalan 5xx pada pemasangan Tag baru di layanan Global setelah validasi lolos; hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Global; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00330` Paired | `aset220` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: intercept dipasang di langkah 1, 10, dan 21 dan dilepas di langkah 16 dan 24; hook `after` melepas semua intercept dan memastikan `RF-00330` Paired pada AST-0220 dan `RF-00412` Available.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 22 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.

## Test Steps

### TC-FA-TAG-259: Pencarian Tag 5xx di overlay, lalu pindai ulang

1. Pasang intercept 5xx pada pencarian Tag untuk pindaian pertama saja (normal sesudahnya)
2. Klik tombol scan `Replace TAG` di toolbar tab Paired
3. Pindai Tag `RF-00330`
4. Verifikasi pesan inline "Error, failed to read TAG. Please try again."
5. Verifikasi overlay tetap terbuka
6. Pindai ulang Tag `RF-00330`
7. Verifikasi overlay menutup
8. Verifikasi Dialog Replace TAG terbuka untuk 'Excavator 20 Ton - 220'
9. Klik [Cancel] pada Dialog Replace TAG

### TC-FA-TAG-260: Pencarian Tag timeout di overlay

10. Pasang intercept yang membuat pencarian Tag tidak merespons sampai timeout
11. Klik tombol scan `Replace TAG` di toolbar tab Paired
12. Pindai Tag `RF-00330`
13. Verifikasi pesan inline "Error, failed to read TAG. Please try again."
14. Verifikasi overlay tetap terbuka
15. Verifikasi tidak ada dialog yang tampil
16. Lepas intercept, lalu tutup overlay scan

### TC-FA-TAG-1350: Penggantian atomik saat pemasangan Tag baru gagal

17. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
18. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
19. Klik ButtonScan `Scan RFID` pada baris `RF-00330` lalu pindai Tag `RF-00330`
20. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
21. Pasang intercept 5xx pada pemasangan Tag baru di layanan Global
22. Klik [Submit]
23. Verifikasi toast "Error, failed to replace TAG."
24. Lepas intercept
25. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-259, 260, 1350). Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 (menutup Dialog Replace TAG dengan [Cancel]), 16 (melepas intercept dan menutup overlay scan), 24 (melepas intercept), 25 (muat ulang halaman untuk menutup dialog dirty; dialog `beforeunload` ditangani sesuai Prerequisites).
- Langkah 15 (tidak ada dialog) didahului `Verifikasi` pesan inline dan overlay pada surface yang sama sebagai anchor positif.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 22 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.
- Temuan untuk QA:
  - TC-FA-TAG-1350 menulis langkah 3 "Klik ButtonScan `Scan RFID` pada baris `RF-00330` lalu pindai Tag `RF-00330`" dan Expected hanya toast; Post Condition (Tag `RF-00330` tetap Paired, aset tidak tanpa Tag, tidak ada entri Changelog dan TAG Log) tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-260 tidak menyebut cara menutup overlay scan; langkah 16 menutupnya sebagai langkah penghubung (mekanisme tutup overlay tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE).
  - Post Condition TC-FA-TAG-259 dan TC-FA-TAG-260 tidak memuat langkah observasi dan tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
