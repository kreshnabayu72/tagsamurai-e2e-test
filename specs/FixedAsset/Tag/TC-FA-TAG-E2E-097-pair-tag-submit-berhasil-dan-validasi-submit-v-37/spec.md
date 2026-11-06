---
id: TC-FA-TAG-E2E-097-pair-tag-submit-berhasil-dan-validasi-submit-v-37
title: "Pair TAG: Validasi Submit V-37 dan Submit Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-415
  - TC-FA-TAG-416
  - TC-FA-TAG-417
  - TC-FA-TAG-418
coverage:
  web: automated
---

# Pair TAG: Validasi Submit V-37 dan Submit Berhasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, status Tag, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Aset satu tipe | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: Tag `RF-00412`, `NF-00500`, `QR-00701` dipasangkan pada 'Server Rack 42U - 101' dan `RF-00412` pada 'Excavator 20 Ton - 51'; hook `after` memulihkan kedua aset ke Not Paired Yet dan stok Available seperti awal lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 13, 22); entri TAG Log Global (langkah 13, 22). Aksi tulis pada langkah 4, 8 ditolak dan tidak menambah entri.

## Test Steps

### Submit tanpa slot terisi dan dengan sebagian slot terisi (TC-FA-TAG-417, TC-FA-TAG-418)

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Klik [Submit]
5. Verifikasi teks error inline "Please verify the TAG to pair" tampil di atas footer
6. Verifikasi dialog tetap terbuka
7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
8. Klik [Submit]
9. Verifikasi teks error inline "Please verify the TAG to pair"
10. Verifikasi dialog tetap terbuka dengan slot RFID tetap `Verified`

### Pair satu aset tiga slot dalam satu transaksi (TC-FA-TAG-416)

11. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
12. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
13. Klik [Submit]
14. Verifikasi toast "Success, TAG has been paired."
15. Verifikasi dialog menutup

### Pair satu aset satu slot RFID (TC-FA-TAG-415)

16. Isi ulang stok Available Tag RFID `RF-00412` dan `RF-00415` lewat fixture backend hingga tersimpan, lalu muat ulang halaman TAG (F5)
17. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
18. Klik tombol teks `Show` di samping field `Not Paired Yet`
19. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
20. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
21. Verifikasi slot `RFID TAG` menampilkan `RF-00412` dengan badge `Verified` sebelum Submit
22. Klik [Submit]
23. Verifikasi toast "Success, TAG has been paired."
24. Verifikasi dialog menutup
25. Verifikasi tabel Paired dimuat ulang
26. Verifikasi baris 'Excavator 20 Ton - 51' tidak lagi muncul saat filter `Show` Not Paired Yet aktif

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-415, 416, 417, 418). Tidak ada TC hanya-BE.
- Urutan TC di dalam spec mengikuti prinsip validasi diblokir sebelum aksi sukses: TC-417, TC-418, lalu TC-416, lalu TC-415 (aset lain). TC-416 melanjutkan dialog TC-418 pada aset yang sama: slot `RFID TAG` sudah berisi `RF-00412` dari TC-418 sehingga langkah memindai RFID TC-416 tidak diulang (langkah 7); slot NFC dan QR dipindai pada langkah 11 dan 12.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 16 (mengisi ulang stok dan memuat ulang halaman karena `RF-00412` terpakai pada TC-416).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Pair TAG` per Tag (langkah 13, 22); entri TAG Log Global (langkah 13, 22). Aksi tulis pada langkah 4, 8 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - TC-FA-TAG-415 butir d ("baris tidak lagi muncul saat filter `Show` Not Paired Yet aktif") tidak menyebut baris pembanding; toast sukses yang sudah diasersi (langkah 23) menjadi anchor (bagian 8b butir 2).
  - TC-FA-TAG-417 dan 418 tidak menyebut cara menutup dialog; sesudah TC-416 dialog menutup sendiri sehingga tidak ada form dirty di akhir blok.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-415 sampai TC-418 ("Tag Paired pada aset", "Aset tetap Not Paired Yet", "Tag `RF-00412` tetap Available") tanpa langkah observasi di TC tidak diasersi.
