---
id: TC-FA-TAG-E2E-098-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-1
title: "Pair TAG: Penolakan Scan Menurut Status Tag V-07 (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-419
  - TC-FA-TAG-420
  - TC-FA-TAG-421
  - TC-FA-TAG-422
  - TC-FA-TAG-423
coverage:
  web: automated
---

# Pair TAG: Penolakan Scan Menurut Status Tag V-07 (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan Tag per status registri; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset target | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Tag Paired | Tag RFID `RF-00101` berstatus Paired | `tagPaired101` |
| Tag Reserved | Tag RFID `RF-00601` berstatus Reserved | `tagReserved601` |
| Tag Retired | Tag RFID `RF-00602` berstatus Retired | `tagRetired602` |
| Tag Damaged/Missing | Tag RFID `RF-00603` berstatus Damaged/Missing | `tagDamaged603` |
| Tag Waiting for Approval | Tag RFID `RF-00604` berstatus Waiting for Approval | `tagWaiting604` |

- State yang diubah dan pemulihannya: spec tidak mengubah data (semua pindaian ditolak dan dialog dibatalkan tanpa isian).

## Test Steps

### Pindai Tag dengan status tidak tersedia

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'

#### Paired (TC-FA-TAG-419)

4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00101`
5. Verifikasi error inline "RF-00101 is not available (Paired)."
6. Verifikasi slot `RFID TAG` tetap `Not scanned`

#### Reserved (TC-FA-TAG-420)

7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00601`
8. Verifikasi error inline "RF-00601 is not available (Reserved)."
9. Verifikasi slot `RFID TAG` tetap `Not scanned`

#### Retired (TC-FA-TAG-421)

10. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00602`
11. Verifikasi error inline "RF-00602 is not available (Retired)."
12. Verifikasi slot `RFID TAG` tetap `Not scanned`

#### Damaged/Missing (TC-FA-TAG-422)

13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00603`
14. Verifikasi error inline "RF-00603 is not available (Damaged/Missing)."
15. Verifikasi slot `RFID TAG` tetap `Not scanned`

#### Waiting for Approval (TC-FA-TAG-423)

16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00604`
17. Verifikasi error inline "RF-00604 is not available (Waiting for Approval)."
18. Verifikasi slot `RFID TAG` tetap `Not scanned`
19. Klik [Cancel]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-419 s.d. 423). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik penolakan scan Pair TAG dilanjutkan di spec 099 (TC-FA-TAG-424, 426 s.d. 429), spec 100 (TC-FA-TAG-430 s.d. 434), dan spec 101 (TC-FA-TAG-1453, 1454, 1462). TC-FA-TAG-425 ada di spec kelas defense-in-depth tersendiri.
- Kelima TC memakai dialog Pair TAG yang sama (precondition dan langkah pembuka identik) dan tidak menyimpan perubahan; dialog dibuka satu kali dan error tiap pindaian berbeda teks sehingga tidak ada langkah pembersih di antaranya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 19 (menutup dialog tanpa isian dengan [Cancel], yang menutup langsung tanpa konfirmasi D-11).
- Temuan untuk QA:
  - TC-FA-TAG-419 sampai 423 tidak menyebut apakah pesan error pindaian sebelumnya hilang ketika pindaian berikutnya dilakukan; spec mengasersi pesan yang sesuai pada tiap pindaian.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-419 sampai 423 ("Aset tetap Not Paired Yet") tanpa langkah observasi di TC tidak diasersi.
