---
id: TC-FA-TAG-E2E-112-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-3
title: "Sesi Pair TAG Beberapa Aset: Toast T-20 Bentuk Jamak dan Tunggal pada Close (Bagian 3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-464
  - TC-FA-TAG-465
coverage:
  web: automated
---

# Sesi Pair TAG Beberapa Aset: Toast T-20 Bentuk Jamak dan Tunggal pada Close (Bagian 3)

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

- State yang diubah dan pemulihannya: Tag RFID dipasangkan pada aset sesi; fixture backend memulihkan aset ke Not Paired Yet dan stok Available antar blok dan di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 6, 8, 18); entri TAG Log Global (langkah 6, 8, 18).

## Test Steps

### Dua aset Done: toast bentuk jamak (TC-FA-TAG-464)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik `Show` di samping `Not Paired Yet`
3. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
4. Klik Bulk `Pair TAG`
5. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
6. Klik [Submit & next]
7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
8. Klik [Submit & next]
9. Klik [Skip]
10. Klik [Close]
11. Verifikasi toast "Success, assets have been paired."
12. Verifikasi tabel Paired dimuat ulang

### Satu aset Done: toast bentuk tunggal (TC-FA-TAG-465)

13. Pulihkan ketiga aset ke Not Paired Yet dan isi ulang stok Available `RF-00412`, `RF-00415`, `RF-00416` lewat fixture backend hingga tersimpan, lalu muat ulang halaman TAG (F5) dan klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
14. Klik `Show` di samping `Not Paired Yet`
15. Centang baris 'Excavator 20 Ton - 51', 'Excavator 20 Ton - 52', dan 'Excavator 20 Ton - 54'
16. Klik Bulk `Pair TAG`
17. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
18. Klik [Submit & next]
19. Klik [Skip]
20. Klik [Skip]
21. Klik [Close]
22. Verifikasi toast "Success, asset has been paired."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-464, 465). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sesi Pair beberapa aset ada juga di spec 110, 111, 113, 114, dan 115 (TC-FA-TAG-459 s.d. 463, 466, 469 s.d. 472, 1383, 1445, 1446, 1487).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 13 (memulihkan data lewat fixture backend hingga tersimpan, memuat ulang halaman, dan membuka popup dari keadaan bersih).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 6, 8, 18); entri TAG Log Global (langkah 6, 8, 18).
- Temuan untuk QA:
  - TC-FA-TAG-464 butir "Tabel Paired dimuat ulang" tidak memberi cara mengamatinya; spec mengasersinya sebagaimana tertulis dan cara teknis mengamatinya diminta dari tim FE.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-464 ("Dua aset keluar dari Not Paired Yet") dan TC-465 ("Satu aset keluar dari Not Paired Yet") tanpa langkah observasi di TC tidak diasersi.
