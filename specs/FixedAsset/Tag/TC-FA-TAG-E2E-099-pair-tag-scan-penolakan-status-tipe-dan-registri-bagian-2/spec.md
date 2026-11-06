---
id: TC-FA-TAG-E2E-099-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-2
title: "Pair TAG: Penolakan Scan Menurut Tipe dan Registri serta Kode QR Hasil Cetak (Bagian 2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-424
  - TC-FA-TAG-426
  - TC-FA-TAG-427
  - TC-FA-TAG-428
  - TC-FA-TAG-429
coverage:
  web: automated
---

# Pair TAG: Penolakan Scan Menurut Tipe dan Registri serta Kode QR Hasil Cetak (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Tag per status registri, User TAG, dan kode QR hasil Start Print; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Aset satu tipe | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset QR | 'Label Printer - 71' (AST-0171, Group Plant A, TAG Type Asset Name QR saja), Not Paired Yet | `aset171` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |
| Kode QR hasil cetak | `QR-00700` berstatus Available (dibuat backend saat Start Print sebelumnya, belum Paired) | `qrHasilCetak700` |
| Kode tidak dikenal | `RF-09999` dan `QR-09999` tidak ada di registri | `kodeTidakDikenal` |
| User TAG | `UT-00010` terdaftar di Global dan berlaku di client ini | `userTag10` |

- State yang diubah dan pemulihannya: Tag `QR-00700` dipasangkan pada 'Label Printer - 71' pada langkah terakhir; hook `after` memulihkan aset ke Not Paired Yet dan `QR-00700` ke Available lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*/UT-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 25); entri TAG Log Global (langkah 25).

## Test Steps

### Tag bertipe tidak sesuai slot (TC-FA-TAG-424)

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `NF-00500`
5. Verifikasi error inline "This slot needs a RFID TAG."
6. Verifikasi slot `RFID TAG` tetap `Not scanned`
7. Klik [Cancel]

### Tag tidak dikenal dan User TAG (TC-FA-TAG-426, TC-FA-TAG-429)

8. Tutup Popup Detail
9. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
10. Klik tombol teks `Show` di samping field `Not Paired Yet`
11. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
12. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-09999`
13. Verifikasi error inline "Error, can't recognize TAG."
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `UT-00010`
15. Verifikasi error inline "This is a user TAG. Scan an asset TAG."
16. Klik [Cancel]

### Kode QR tidak pernah dicetak lalu kode QR hasil Start Print (TC-FA-TAG-427, TC-FA-TAG-428)

17. Tutup Popup Detail
18. Klik Asset Name 'Label Printer' pada baris grup Plant A untuk membuka Popup Detail
19. Klik tombol teks `Show` di samping field `Not Paired Yet`
20. Klik row action `Pair TAG` pada baris 'Label Printer - 71'
21. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-09999`
22. Verifikasi error inline "Error, can't recognize TAG."
23. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00700`
24. Verifikasi slot `QR TAG` menampilkan `QR-00700` dengan badge `Verified`
25. Klik [Submit]
26. Verifikasi toast "Success, TAG has been paired."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-424, 426, 427, 428, 429). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik penolakan scan Pair TAG ada di spec 098 (TC-FA-TAG-419 s.d. 423), spec 100 (TC-FA-TAG-430 s.d. 434), dan spec 101 (TC-FA-TAG-1453, 1454, 1462). TC-FA-TAG-425 ada di spec kelas defense-in-depth tersendiri.
- Urutan TC di dalam spec: TC-426 dan TC-429 berbagi dialog 'Excavator 20 Ton - 51' (keduanya ditolak tanpa mengubah data); TC-427 dan TC-428 berbagi dialog 'Label Printer - 71' dengan TC-428 terakhir karena menyimpan perubahan. Pindaian yang ditolak tidak mengisi slot sehingga TC-428 tetap mulai dari slot kosong.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7, 16 (menutup dialog tanpa isian dengan [Cancel], tanpa konfirmasi D-11), serta 8 dan 17 (menutup Popup Detail sebelum membuka popup grup lain).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*/UT-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 25); entri TAG Log Global (langkah 25).
- Temuan untuk QA:
  - TC-FA-TAG-428 tidak menyebut hasil di tabel sesudah Submit selain toast; spec hanya mengasersi butir Expected.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-424 sampai TC-429 ("Aset tetap Not Paired Yet", "Tag `QR-00700` Paired pada 'Label Printer - 71'") tanpa langkah observasi di TC tidak diasersi.
