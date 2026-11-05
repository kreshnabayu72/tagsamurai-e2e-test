---
id: TC-FA-TAG-E2E-091-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-3
title: "Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-395
  - TC-FA-TAG-396
  - TC-FA-TAG-397
coverage:
  web: automated
---

# Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 3)

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

- State yang diubah dan pemulihannya: Tag aset 'Excavator 20 Ton - 220' diganti oleh Submit & next pada TC-FA-TAG-396; hook `after` memulihkan Tag `RF-00330` Paired dan stok Available seperti awal lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 16); entri TAG Log Global (langkah 16).

## Test Steps

### Semua aset Skipped (TC-FA-TAG-397, TC-FA-TAG-395)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
3. Klik Bulk `Batch Replace TAG`
4. Klik [Skip]
5. Klik [Skip]
6. Klik [Skip]
7. Verifikasi ringkasan memuat tombol `[Retry skipped and failed (3)]`
8. Klik [Close]
9. Verifikasi ringkasan menutup
10. Verifikasi tabel Paired dimuat ulang
11. Verifikasi toast "Success, asset has been replaced." (T-02) tidak tampil

### Retry skipped and failed (TC-FA-TAG-396)

12. Muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
14. Klik Bulk `Batch Replace TAG`
15. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
16. Klik [Submit & next]
17. Klik [Skip]
18. Klik [Skip]
19. Klik `[Retry skipped and failed (2)]`
20. Verifikasi dialog sesi terbuka untuk 'Excavator 20 Ton - 221'
21. Klik [Skip]
22. Verifikasi dialog sesi berganti ke 'Excavator 20 Ton - 23'
23. Verifikasi aset 'Excavator 20 Ton - 220' yang `Done` tidak dibuka lagi
24. Klik ikon close dialog tanpa mengisi apa pun
25. Klik [Close] pada ringkasan akhir

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-395, 396, 397). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Batch Replace dilanjutkan di spec 089 (TC-FA-TAG-388 s.d. 391), spec 090 (TC-FA-TAG-392 s.d. 394), dan spec 092 (TC-FA-TAG-398, 399, 1473).
- Urutan TC di dalam spec: TC-397 dan TC-395 berbagi satu sesi (langkah 1 sampai 11) karena langkah TC-395 adalah tiga kali [Skip] diikuti [Close] dan TC-397 berhenti sebelum [Close]; urutan Expected mengikuti urutan keadaan layar (butir tombol Retry sebelum [Close]). TC-396 menyimpan perubahan sehingga ditaruh terakhir.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 12 (memuat ulang halaman supaya tabel dan popup dibuka dari keadaan bersih), 21 (Skip untuk mengamati aset berikutnya yang dibuka Retry), 24 dan 25 (menutup sesi).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 16); entri TAG Log Global (langkah 16).
- Temuan untuk QA:
  - TC-FA-TAG-396 butir b ("aset yang `Done` tidak dibuka lagi") tidak memberi cara teramati selain urutan dialog; spec mengasersinya sebagai tertulis.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-395 ("Tidak ada Tag yang berubah") dan TC-396 ("Tidak ada perubahan tambahan") tanpa langkah observasi tidak diasersi.
