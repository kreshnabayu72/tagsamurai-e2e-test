---
id: TC-FA-TAG-E2E-088-replace-entry-row-action-bulk-satu-aset-aksi-grup-dan-tab-tbr
title: "Replace TAG: Pintu Masuk Row Action, Bulk Satu Aset, Aksi Grup, Tab To Be Returned, dan Overlay Scan NFC"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-377
  - TC-FA-TAG-378
  - TC-FA-TAG-379
  - TC-FA-TAG-385
  - TC-FA-TAG-386
  - TC-FA-TAG-387
coverage:
  web: automated
---

# Replace TAG: Pintu Masuk Row Action, Bulk Satu Aset, Aksi Grup, Tab To Be Returned, dan Overlay Scan NFC

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan dan overlay scan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Asset Status, Tag per status registri, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 1 | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID), Tag RFID `RF-00130` Paired | `aset220` |
| Aset Non-standard 1 | 'Excavator 20 Ton - 42' (AST-0042, Group Plant A, TAG Type Asset Name RFID), Tag QR `QR-00230` Paired (Non-standard) | `aset42` |
| Aset Non-standard 2 | 'Excavator 20 Ton - 243' (AST-0243, Group Plant A), Tag QR `QR-00231` Paired (Non-standard) | `aset243` |
| Aset In Disposal Process | 'Excavator 20 Ton - 46' (AST-0046, Group Plant A, Asset Status In Disposal Process), Tag QR `QR-00234` Paired (Non-standard) | `aset46` |
| Aset NFC dan QR | 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type Asset Name NFC dan QR), Tag NFC `NF-00092` dan Tag QR `QR-00300` Paired | `aset108` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500` | `stokAvailable` |

- State yang diubah dan pemulihannya: Tag `RF-00130` diganti `RF-00412` (TC-379); stok Available disetel ulang antar blok lewat fixture; hook `after` memulihkan Tag Paired aset dan stok Available seperti awal.

## Test Steps

### Row action Replace TAG tanpa overlay scan (TC-FA-TAG-377)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Verifikasi Dialog Replace TAG terbuka langsung dengan judul aset 'Excavator 20 Ton - 220'
4. Verifikasi tidak ada overlay scan dan tidak ada langkah Identify
5. Verifikasi baris `RF-00130` otomatis terpilih
6. Verifikasi baris `RF-00130` berbadge `Not scanned`
7. Klik [Cancel] pada Dialog Replace TAG

### Bulk Batch Replace TAG dengan satu aset (TC-FA-TAG-378, TC-FA-TAG-379)

8. Centang baris 'Excavator 20 Ton - 220' pada Popup Detail
9. Klik Bulk `Batch Replace TAG` pada Bulk Action Bar
10. Verifikasi Dialog Replace TAG terbuka langsung (bukan sesi batch) dengan header `Replace TAG`
11. Verifikasi footer memuat [Cancel] dan [Submit]
12. Verifikasi footer tidak memuat [Skip] dan [Submit & next]
13. Verifikasi tidak ada ringkasan akhir sesi
14. Klik [Cancel] pada Dialog Replace TAG
15. Klik Bulk `Batch Replace TAG` pada Bulk Action Bar
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
17. Klik [Submit]
18. Verifikasi toast "Success, TAG has been replaced."
19. Verifikasi dialog menutup

### Aksi grup Replace non-standard TAGs (TC-FA-TAG-385)

20. Tutup Popup Detail, lalu isi ulang stok Global dengan Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` Available lewat fixture backend hingga tersimpan
21. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
22. Klik aksi `Replace non-standard TAGs`
23. Verifikasi sesi Batch Replace TAG terbuka dengan header `Replace TAG · Asset 1 of 2`
24. Verifikasi aset pertama sesi adalah 'Excavator 20 Ton - 42'
25. Verifikasi Tag Non-standard `QR-00230` tercentang awal
26. Klik [Skip]
27. Verifikasi aset kedua sesi adalah 'Excavator 20 Ton - 243' dan 'Excavator 20 Ton - 46' tidak dimasukkan ke sesi
28. Klik ikon close dialog lalu klik [Close] pada ringkasan akhir

### Tab To Be Returned dan overlay scan NFC (TC-FA-TAG-386, TC-FA-TAG-387)

29. Klik tab To Be Returned
30. Verifikasi toolbar memuat `Event Log` dan tombol scan `Receive TAG`
31. Verifikasi tombol `Replace TAG` dan `Print QR` Hidden
32. Klik tab Paired
33. Klik tombol scan `Replace TAG` di toolbar tab Paired
34. Pindai Tag `NF-00092`
35. Verifikasi Dialog Replace TAG terbuka untuk 'Laptop Pro 14 - 8'
36. Verifikasi baris `NF-00092` tercentang dan berbadge `Scanned`
37. Verifikasi baris `QR-00300` tidak tercentang
38. Klik [Cancel] pada Dialog Replace TAG

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-377, 378, 379, 385, 386, 387). Tidak ada TC hanya-BE.
- Urutan TC di dalam spec: TC-377, TC-378, TC-379, TC-385, TC-386, TC-387. TC-379 mengganti Tag aset 220 sehingga ditaruh sesudah TC-377 dan TC-378 yang membaca keadaan awalnya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 dan 14 (menutup dialog tanpa menyimpan), 20 (menutup popup dan menyetel ulang stok), 26 (Skip untuk mengamati aset kedua sebagai bagian asersi TC-385 butir b), 28 (menutup sesi dan ringkasan), 32, dan 38.
- Spec di atas smell 35 langkah (38 langkah). Alasan: seluruh blok satu topik (pintu masuk dialog Replace TAG dari row action, Bulk satu aset, aksi grup, dan overlay scan) pada halaman TAG yang sama dengan reader yang sama, satu kelas, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-TAG-385 butir b ("Excavator 20 Ton - 46 tidak dimasukkan") dan butir a ("Asset 1 of 2") hanya teramati lewat pergeseran ke aset kedua; spec menambah satu langkah [Skip] sebagai langkah penghubung untuk mengamatinya.
  - TC-FA-TAG-385 tidak menyatakan cara menutup sesi di akhir; spec memakai ikon close lalu [Close] (perilaku ikon close tanpa isian: TC-FA-TAG-398).
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan dan overlay scan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-379 ("Tag `RF-00412` Paired pada AST-0220") tanpa langkah observasi tidak diasersi.
