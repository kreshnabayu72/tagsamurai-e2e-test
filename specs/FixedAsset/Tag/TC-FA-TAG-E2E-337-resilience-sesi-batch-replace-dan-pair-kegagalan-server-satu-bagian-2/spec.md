---
id: TC-FA-TAG-E2E-337-resilience-sesi-batch-replace-dan-pair-kegagalan-server-satu-bagian-2
title: "Resilience: Kegagalan Server pada Satu Aset dalam Sesi Batch Pair (Toast, Dialog Tetap Terbuka, Skip) (Bagian 2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-467
  - TC-FA-TAG-468
coverage:
  web: automated
---

# Resilience: Kegagalan Server pada Satu Aset dalam Sesi Batch Pair (Toast, Dialog Tetap Terbuka, Skip) (Bagian 2)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) `Spectra.intercept` parsial per aset atas penyimpanan sesi Batch Pair: respons 5xx pada aset tertentu; hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan Tag Available; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tiga aset Not Paired Yet | 'Excavator 20 Ton - 51' (AST-0051), 'Excavator 20 Ton - 52' (AST-0052), 'Excavator 20 Ton - 54' (AST-0054), semuanya Group Plant A dengan TAG Type Asset Name RFID | `asetPair` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokAvailable` |

- State yang diubah dan pemulihannya: intercept dipasang di langkah 5 dan dilepas di langkah 14; spec tidak menyimpan pairing (aset 1 gagal di server). Hook `after` memastikan ketiga aset Not Paired Yet dan ketiga Tag Available serta melepas semua intercept.

## Test Steps

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
4. Klik Bulk `Pair TAG`
5. Pasang intercept 5xx pada penyimpanan aset 'Excavator 20 Ton - 51'
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
7. Klik [Submit & next]
8. Verifikasi toast "Error, failed to pair TAG."
9. Verifikasi dialog aset 1 tetap terbuka pada header `Pair TAG · Asset 1 of 3`
10. Verifikasi slot `RFID TAG` tetap berisi `RF-00412`
11. Verifikasi sesi tidak lanjut ke aset berikutnya
12. Klik [Skip]
13. Verifikasi dialog berganti ke header `Pair TAG · Asset 2 of 3`
14. Lepas intercept
15. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-467, 468). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-405 s.d. 407 (kegagalan server pada sesi Batch Replace) ada di spec 336.
- TC-468 memakai sesi yang sama dengan TC-467: langkah 1 s.d. 7 TC-468 identik dengan langkah 1 s.d. 7 TC-467 (dataset, intercept, dan pindaian sama), sehingga langkah 12 melanjutkan dari dialog TC-467 tanpa membangun sesi ulang.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14 (melepas intercept), 15 (muat ulang halaman untuk menutup dialog dirty; dialog `beforeunload` ditangani sesuai Prerequisites).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-467 dan TC-FA-TAG-468 (aset 'Excavator 20 Ton - 51' tetap Not Paired Yet, Tag `RF-00412` tetap Available) tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
