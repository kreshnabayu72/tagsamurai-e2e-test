---
id: TC-FA-TAG-E2E-093-batch-replace-scan-opsional-stok-konflik-d-03-d-04-dan-bagian-1
title: "Batch Replace TAG: Pilihan Tag Awal, Scan Current TAG Opsional, dan Stok Kurang (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-400
  - TC-FA-TAG-401
  - TC-FA-TAG-402
  - TC-FA-TAG-403
coverage:
  web: automated
---

# Batch Replace TAG: Pilihan Tag Awal, Scan Current TAG Opsional, dan Stok Kurang (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset NFC dan QR | 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type Asset Name NFC dan QR), Tag NFC `NF-00292` dan Tag QR `QR-00300` Paired | `aset108` |
| Aset NFC | 'Laptop Pro 14 - 12' (AST-0112, Group Plant A, TAG Type NFC), Tag NFC `NF-00097` Paired | `aset112` |
| Stok NFC (TC-400) | Tag NFC `NF-00500`, `NF-00501` Available | `stokNfc` |
| Aset RFID dan QR | 'Excavator 20 Ton - 244' (AST-0244, Group Plant A, TAG Type Asset Name RFID), Tag RFID `RF-00332` Paired (sesuai tipe) dan Tag QR `QR-00432` Paired (Non-standard) | `aset244` |
| Aset sesi 1 sampai 3 | 'Excavator 20 Ton - 220' (AST-0220, `RF-00330`), 'Excavator 20 Ton - 221' (AST-0221, `RF-00140`), 'Excavator 20 Ton - 23' (AST-0023, `RF-00141`), masing-masing satu Tag RFID Paired | `aset220`, `aset221`, `aset23` |
| Stok RFID (TC-402 dan TC-403) | hanya Tag RFID `RF-00412` Available (kurang dari kebutuhan tiga aset) | `stokRfid412` |

- State yang diubah dan pemulihannya: stok Available RFID disetel hanya `RF-00412`; Tag `RF-00330` diganti dan menjadi Damaged/Missing pada TC-402; hook `after` memulihkan Tag `RF-00330` Paired, status registri Tag, dan stok Available seperti awal lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 31); entri TAG Log Global (langkah 31).

## Test Steps

### Tag pada aset beberapa Tag tidak tercentang awal (TC-FA-TAG-400)

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Laptop Pro 14 - 8' dan 'Laptop Pro 14 - 12'
3. Klik Bulk `Batch Replace TAG`
4. Verifikasi header `Replace TAG · Asset 1 of 2`
5. Verifikasi checkbox `NF-00292` dan `QR-00300` aktif pada aset 'Laptop Pro 14 - 8'
6. Verifikasi tidak ada Tag yang tercentang awal pada aset 'Laptop Pro 14 - 8'
7. Verifikasi tidak ada baris berbadge `Scanned`
8. Centang baris `NF-00292`
9. Verifikasi hanya baris `NF-00292` yang tercentang
10. Klik ikon close (✕) pada dialog sesi Batch Replace TAG
11. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
12. Klik [Discard]
13. Klik [Close] pada ringkasan akhir
14. Muat ulang halaman TAG (F5)

### Aksi grup Replace non-standard TAGs: Tag Non-standard tercentang awal (TC-FA-TAG-401)

15. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
16. Klik aksi `Replace non-standard TAGs`
17. Verifikasi baris `QR-00432` tercentang awal
18. Verifikasi baris `RF-00332` tidak tercentang
19. Hapus centang baris `QR-00432` lalu centang baris `RF-00332`
20. Verifikasi pembatalan centang `QR-00432` diizinkan
21. Klik ikon close (✕) pada dialog sesi Replace non-standard TAGs
22. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
23. Klik [Discard]
24. Klik [Close] pada ringkasan akhir

### Stok kurang dari kebutuhan dan Scan Current TAG opsional (TC-FA-TAG-403, TC-FA-TAG-402)

25. Atur stok Global sehingga hanya Tag RFID `RF-00412` yang Available lewat fixture backend hingga tersimpan, muat ulang halaman TAG (F5), lalu klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
26. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
27. Klik Bulk `Batch Replace TAG`
28. Verifikasi sesi dimulai pada header `Replace TAG · Asset 1 of 3`
29. Verifikasi tidak ada Alert peringatan stok sebelum sesi maupun di dialog
30. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412` tanpa memindai Tag lama `RF-00330`
31. Klik [Submit & next]
32. Verifikasi aset 1 tersimpan tanpa error pemindaian wajib
33. Klik [Skip]
34. Klik [Skip]
35. Klik [Close] pada ringkasan akhir

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-400, 401, 402, 403). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik scan opsional, stok, dan konflik Batch dilanjutkan di spec 094 (TC-FA-TAG-404, 408, 409) dan spec 095 (TC-FA-TAG-410, 1382).
- Urutan TC di dalam spec: TC-403 dan TC-402 berbagi satu sesi (langkah 26 sampai 35) karena keduanya membutuhkan stok hanya `RF-00412` dan langkah awal sesi yang sama (tiga aset RFID Plant A); TC-403 hanya mengamati awal sesi sehingga ditaruh sebelum TC-402 yang menyimpan perubahan. TC-402 memakai stok `RF-00412` saja (TC-402 menyebut `RF-00412`, `RF-00415`, `RF-00416` Available).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10, 12, 13, dan 14 (mengakhiri sesi TC-400 yang berisi pilihan centang lewat ikon close, [Discard] pada konfirmasi D-09, [Close] pada ringkasan akhir, lalu memuat ulang halaman), langkah 21, 23, dan 24 (mengakhiri sesi TC-401 dengan cara yang sama), 25 (mengatur stok lewat fixture backend, memuat ulang halaman, dan membuka popup), serta langkah 33 dan 34 (Skip untuk menuntaskan sesi sampai ringkasan) dan 35 (menutup ringkasan).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 31); entri TAG Log Global (langkah 31).
- Temuan untuk QA:
  - TC-FA-TAG-401 tidak menyebut aset Non-standard lain pada grup Excavator 20 Ton Plant A (mis. AST-0042, AST-0243 di data TC lain); jika ada, sesi dimulai pada aset lain dan header `Asset 1 of N` berbeda. Spec memakai data TC apa adanya.
  - TC-FA-TAG-402 tidak memberi langkah observasi untuk "Tag `RF-00330` berstatus Damaged/Missing di registri Global" (Post Condition) sehingga tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
