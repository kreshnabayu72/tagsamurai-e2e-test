---
id: TC-FA-TAG-E2E-348-state-tenant-entitas-suspended-atau-expired-baca-boleh-tulis-bagian-1
title: "State Tenant: Entitas Suspended Menolak Submit Replace, Submit Pair, dan Submit & next Sesi Batch dengan Pesan V-22 (Bagian 1)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1285
  - TC-FA-TAG-1287
  - TC-FA-TAG-1288
coverage:
  web: automated
---

# State Tenant: Entitas Suspended Menolak Submit Replace, Submit Pair, dan Submit & next Sesi Batch dengan Pesan V-22 (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah status entitas Client.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) perubahan status entitas Client menjadi Suspended lewat fixture backend; hook `before` menyetelnya dan hook `after` memulihkan status Active; akun Admin untuk perubahan status disediakan tim FE; (3) pembacaan state data lewat fixture backend (Tag Paired atau Not Paired Yet, jumlah entri Changelog sebagai baseline, audit trail permanen sehingga asersi memakai selisih terhadap baseline); (4) seed dan pemulihan idempotent lewat fixture backend untuk aset dan stok Tag; (5) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID, Tag RFID `RF-00330` Paired) dan 'Excavator 20 Ton - 221' (AST-0221, Group Plant A, `RF-00140` Paired) | `asetPaired` |
| Aset Not Paired Yet | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja) | `aset51` |
| Stok Global Available | Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: entitas Client berstatus Suspended sepanjang spec (diatur hook `before`); semua Submit ditolak sehingga tidak ada data aset yang berubah. Hook `after` memulihkan status entitas Client ke Active walau spec gagal di tengah.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5, 17, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Jumlah entri Changelog dibaca sebagai baseline pada langkah 1; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.

## Test Steps

### TC-FA-TAG-1285: Submit Replace ditolak

1. Catat jumlah entri Changelog Paired TAG sebagai baseline lewat fixture BE
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit]
6. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
7. Verifikasi (lewat fixture BE) Tag `RF-00330` tetap Paired
8. Muat ulang halaman (F5)
9. Klik tombol `Changelog`
10. Verifikasi Modal Changelog Paired TAG terbuka
11. Verifikasi jumlah entri Changelog sama dengan baseline (tidak ada entri baru)
12. Tutup Modal Changelog

### TC-FA-TAG-1287: Submit Pair ditolak

13. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
14. Klik `Show` di samping `Not Paired Yet`
15. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
17. Klik [Submit]
18. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
19. Verifikasi (lewat fixture BE) 'Excavator 20 Ton - 51' tetap Not Paired Yet
20. Muat ulang halaman (F5)

### TC-FA-TAG-1288: Submit & next sesi Batch ditolak

21. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
22. Centang baris 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
23. Klik Bulk `Batch Replace TAG`
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
25. Klik [Submit & next]
26. Verifikasi pesan "Changes can't be saved while this workspace is suspended or expired." tampil
27. Verifikasi (lewat fixture BE) aset 'Excavator 20 Ton - 220' tidak tersimpan dan tetap ber-Tag `RF-00330`
28. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1285, 1287, 1288). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Submit Replace saat entitas Expired (TC-FA-TAG-1286) ada di spec 385; Start Print, Receive TAG, dan Receive Manually saat Suspended atau Expired (TC-FA-TAG-1289, 1296 s.d. 1298) ada di spec 349; Report TAG dan Cancel Report (TC-FA-TAG-1299, 1300, 1302) ada di spec 350; Decline Report dan halaman baca-saja (TC-FA-TAG-1301, 1317) ada di spec 385.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (baseline Changelog, S-12), 8, 20, dan 28 (muat ulang halaman untuk menutup dialog yang berisi isian; dialog `beforeunload` ditangani sesuai Prerequisites), 12 (menutup Modal Changelog).
- Pesan pada langkah 6, 18, dan 26 diasersi sebagai teks tampil tanpa menentukan jenis elemen (toast atau pesan inline) karena TC hanya menyebut "Pesan".
- Asersi tidak ada entri log baru (langkah 11, TC-FA-TAG-1285 butir c) memakai pengecualian kelas h (S-05, prinsip 13g): objek uji TC state tenant ini adalah penolakan aksi tulis, sehingga asersi berada di spec ini sendiri dengan `Verifikasi` selisih jumlah entri Changelog Paired TAG terhadap baseline langkah 1 (S-12, satu surface log).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 5, 17, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.
- Temuan untuk QA:
  - Expected TC-FA-TAG-1285 butir b ("Tag `RF-00330` tetap Paired"), TC-FA-TAG-1287 butir b, dan TC-FA-TAG-1288 ("aset tidak tersimpan") tidak punya langkah observasi di UI pada TC; spec mengasersinya lewat pembacaan state data fixture BE (S-11).
  - Changelog tidak memuat entri baru (TC-FA-TAG-1285 butir c): Changelog adalah audit trail permanen sehingga spec memakai baseline jumlah entri (S-12).
  - Post Condition TC-FA-TAG-1285 ("Tidak ada perubahan data dan tidak ada log"), TC-FA-TAG-1287, dan TC-FA-TAG-1288 tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
