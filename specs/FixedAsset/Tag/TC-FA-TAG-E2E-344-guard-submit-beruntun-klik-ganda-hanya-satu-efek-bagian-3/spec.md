---
id: TC-FA-TAG-E2E-344-guard-submit-beruntun-klik-ganda-hanya-satu-efek-bagian-3
title: "Guard Klik Ganda: Submit Pair dan Submit & next Sesi Batch Replace Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 3)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1348
  - TC-FA-TAG-1349
coverage:
  web: automated
---

# Guard Klik Ganda: Submit Pair dan Submit & next Sesi Batch Replace Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 3)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) `Spectra.intercept` parsial yang menahan respons Submit Pair dan Submit & next beberapa detik dan menghitung request yang terkirim, lalu melepas tahanan respons; hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset dan Tag; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Not Paired Yet | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja, belum punya Tag Paired) | `aset51` |
| Dua aset Paired | 'Excavator 20 Ton - 220' (`RF-00130`) dan 'Excavator 20 Ton - 221' (`RF-00140`), Group Plant A, masing-masing satu Tag RFID Paired | `asetBatch` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: langkah 7 memasangkan `RF-00412` ke AST-0051 dan dipulihkan lewat fixture backend di langkah 12; langkah 19 mengganti Tag 'Excavator 20 Ton - 220' dari `RF-00130` menjadi `RF-00412`. Hook `after` memulihkan AST-0051 ke Not Paired Yet, AST-0220 ke `RF-00130`, `RF-00412` ke Available, dan melepas intercept walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-1348: Klik ganda cepat pada Submit Pair

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
2. Klik `Show` di samping `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Pasang intercept yang menahan respons Submit Pair beberapa detik dan menghitung request
6. Tunggu toast lama hilang otomatis
7. Klik [Submit] dua kali beruntun cepat
8. Verifikasi tombol [Submit] tetap tampil dan Disabled dengan state loading selama proses
9. Lepas tahanan respons dan intercept
10. Verifikasi hanya satu request terkirim
11. Verifikasi hanya satu Toast "Success, TAG has been paired."
12. Pulihkan AST-0051 ke Not Paired Yet dan `RF-00412` ke Available lewat fixture BE hingga tersimpan
13. Muat ulang halaman (F5)

### TC-FA-TAG-1349: Klik ganda cepat pada Submit & next sesi Batch

14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
15. Centang kedua aset 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
16. Klik Bulk `Batch Replace TAG`
17. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
18. Pasang intercept yang menahan respons Submit & next beberapa detik dan menghitung request
19. Klik [Submit & next] dua kali beruntun cepat
20. Verifikasi hanya satu request terkirim
21. Verifikasi tombol [Submit & next] tetap tampil dan Disabled dengan state loading selama proses
22. Lepas tahanan respons dan intercept
23. Verifikasi dialog berganti ke header `Replace TAG · Asset 2 of 2` tepat sekali
24. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1348 dan 1349). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: klik ganda pada pindaian, Start Print, dan Receive (TC-FA-TAG-257, 494, 566) ada di spec 342; Submit Decline Report dan Submit Replace (TC-FA-TAG-646, 1344) ada di spec 343; Submit Report TAG dan Cancel Report (TC-FA-TAG-619, 669) ada di spec 351; Submit Receive Manually (TC-FA-TAG-587) ada di spec 383.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 5 dan 18 (memasang intercept penahan respons), 6 (menunggu toast lama hilang otomatis sebelum hitungan toast), 9 dan 22 (melepas tahanan respons dan intercept), 12 (memulihkan AST-0051 dan `RF-00412`, karena TC-FA-TAG-1349 memakai `RF-00412` yang sama), 13 dan 24 (muat ulang halaman untuk menutup dialog dan membersihkan seleksi).
- Langkah 20 (hanya satu request) dan langkah 21 (Disabled dengan state loading) diasersi sebelum header sesi diverifikasi di langkah 23, mengikuti urutan state (bagian 8b butir 5): header berganti hanya sesudah respons dilepas.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-1348 ("Hanya satu entri Changelog Pair TAG dan satu TAG Log Paired untuk `RF-00412`") dan TC-FA-TAG-1349 ("Hanya satu entri Changelog Replace untuk 'Excavator 20 Ton - 220'") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-1349 memakai `RF-00412` sebagai Tag pengganti sedangkan TC-FA-TAG-1348 memasangkan `RF-00412` ke AST-0051; spec memulihkan `RF-00412` ke Available di antara keduanya.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
