---
id: TC-FA-TAG-E2E-103-pair-tag-combined-slot-dan-penolakan-bagian-2
title: "Pair TAG: Tag Combined Sebagian, Konflik dengan Tag Tunggal, Pindai Ulang, dan Komponen Gagal (Bagian 2)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-440
  - TC-FA-TAG-441
  - TC-FA-TAG-442
  - TC-FA-TAG-443
coverage:
  web: automated
---

# Pair TAG: Tag Combined Sebagian, Konflik dengan Tag Tunggal, Pindai Ulang, dan Komponen Gagal (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Tag combined, dan komponen Tag berstatus Reserved; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Aset NFC dan QR | 'Laptop Pro 14 - 9' (AST-0109, Group Plant A, TAG Type Asset Name NFC dan QR), Not Paired Yet | `aset109` |
| Combined RFID+QR | `RF-00811` / `QR-00811` Available (satu unit) | `combined811` |
| Combined NFC+QR | `NF-00810` / `QR-00810` Available (satu unit) | `combined810` |
| Combined komponen Reserved | Combined NFC+QR `NF-00819` dengan komponen QR `QR-00819` berstatus Reserved | `combined819` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: spec tidak menyimpan perubahan (semua dialog dibuang dengan [Discard] atau penolakan); hook `after` memastikan Tag di atas tetap Available lewat fixture backend.

## Test Steps

### Combined sebagian mengisi slot yang cocok (TC-FA-TAG-440)

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00811`
5. Verifikasi slot `RFID TAG` dan `QR TAG` terisi
6. Verifikasi slot `NFC TAG` tetap `Not scanned`
7. Klik [Submit]
8. Verifikasi teks error inline "Please verify the TAG to pair"
9. Klik ikon close dialog Pair TAG
10. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
11. Klik [Discard]

### Combined mencakup tipe slot yang sudah terisi Tag tunggal (TC-FA-TAG-441)

12. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
14. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `RF-00811`
15. Verifikasi error inline "This combined TAG doesn't match the open slots."
16. Verifikasi slot `RFID TAG` tetap menampilkan `RF-00412` `Verified`
17. Klik ikon close dialog Pair TAG
18. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
19. Klik [Discard]

### Komponen combined yang gagal validasi dan pindai ulang slot hasil combined (TC-FA-TAG-443, TC-FA-TAG-442)

20. Tutup Popup Detail
21. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
22. Klik tombol teks `Show` di samping field `Not Paired Yet`
23. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
24. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00819`
25. Verifikasi error inline "QR-00819 is not available (Reserved)."
26. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned`
27. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00810`
28. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
29. Verifikasi slot `QR TAG` kembali `Not scanned`
30. Verifikasi slot `NFC TAG` menampilkan `NF-00500` dengan badge `Verified`
31. Klik ikon close dialog Pair TAG
32. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
33. Klik [Discard]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-440 s.d. 443). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Tag combined pada Pair TAG ada juga di spec 102 (TC-FA-TAG-435 s.d. 439).
- Urutan TC di dalam spec: TC-443 mendahului TC-442 pada dialog 'Laptop Pro 14 - 9' yang sama (pindaian yang ditolak tidak mengisi slot sehingga TC-442 mulai dari slot kosong). TC-440 dan TC-441 memakai dialog 'Server Rack 42U - 101' secara berurutan dan dibuang dengan [Discard] di antaranya (S-08).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9, 11, 17, 19, 31, dan 33 (menutup dialog yang berisi pindaian dengan ikon close dan [Discard]), langkah 12 (membuka ulang dialog pada popup yang masih terbuka), serta langkah 20 (menutup Popup Detail sebelum membuka popup grup lain).
- Temuan untuk QA:
  - TC-FA-TAG-441 menempatkan combined `RF-00811` (RFID+QR) di slot `QR TAG` sementara RFID sudah terisi; TC tidak menyebut apakah slot `QR TAG` tetap `Not scanned` sesudah penolakan, sehingga hal itu tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-440 ("Aset tetap Not Paired Yet") tanpa langkah observasi di TC tidak diasersi.
