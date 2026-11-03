---
id: TC-FA-TAG-E2E-108-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-3
title: "Pair TAG: Urutan Prioritas Tooltip Disabled Reader, Status Aset, dan Stok (Bagian 3)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1455
  - TC-FA-TAG-1491
  - TC-FA-TAG-1492
  - TC-FA-TAG-1493
coverage:
  web: automated
---

# Pair TAG: Urutan Prioritas Tooltip Disabled Reader, Status Aset, dan Stok (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB yang dapat diatur tersambung atau tidak tersambung (driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Asset Status aset, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Aset target | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet; normal atau In Disposal Process sesuai bagian | `aset51` |
| Aset In Disposal Process | 'Excavator 20 Ton - 53' (AST-0053, Group Plant A, TAG Type RFID, Asset Status In Disposal Process), Not Paired Yet | `aset53` |
| Stok Available | tidak ada Tag RFID, NFC, maupun QR Available pada bagian TC-1455; tidak ada Tag RFID Available pada bagian lain | `stokKosong` |

- State yang diubah dan pemulihannya: status reader, Asset Status aset 51, dan stok Available diatur per bagian lewat fixture; hook `after` memulihkan reader tersambung, Asset Status normal, dan stok seperti awal.

## Test Steps

### Stok seluruh tipe 0 menyebut tiga tipe (TC-FA-TAG-1455)

1. Sambungkan reader (driver terpasang, aktif, sudah disinkronkan), hapus semua Tag RFID, NFC, dan QR Available dari stok Global, dan pastikan 'Server Rack 42U - 101' Not Paired Yet lewat fixture backend hingga tersimpan
2. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
3. Klik tombol teks `Show` di samping field `Not Paired Yet`
4. Arahkan kursor ke row action `Pair TAG` pada baris 'Server Rack 42U - 101'
5. Verifikasi row action `Pair TAG` tetap tampil (visible) namun berstatus Disabled
6. Verifikasi tooltip "No available RFID, NFC and QR TAG in stock."
7. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
8. Verifikasi Dialog Pair TAG tidak terbuka

### Status aset didahulukan atas stok bila reader terhubung (TC-FA-TAG-1492)

9. Tutup Popup Detail, atur 'Excavator 20 Ton - 51' berstatus In Disposal Process Not Paired Yet, dan hapus semua Tag RFID Available dari stok Global lewat fixture backend hingga tersimpan (reader tetap tersambung)
10. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
11. Klik tombol teks `Show` di samping field `Not Paired Yet`
12. Arahkan kursor ke row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
13. Verifikasi row action `Pair TAG` tetap tampil (visible) namun berstatus Disabled
14. Verifikasi tooltip "This asset can't be paired while it is in disposal."
15. Verifikasi tooltip bukan "No available RFID TAG in stock."
16. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
17. Verifikasi Dialog Pair TAG tidak terbuka

### Reader tidak terhubung didahulukan atas status aset dan stok (TC-FA-TAG-1491)

18. Tutup Popup Detail dan putuskan reader dari komputer lewat simulator reader (aset 51 tetap In Disposal Process dan stok RFID tetap 0)
19. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
20. Klik tombol teks `Show` di samping field `Not Paired Yet`
21. Arahkan kursor ke row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
22. Verifikasi row action `Pair TAG` tetap tampil (visible) namun berstatus Disabled
23. Verifikasi tooltip "Connect a TAG reader to pair."
24. Verifikasi tooltip bukan "This asset can't be paired while it is in disposal." maupun "No available RFID TAG in stock."
25. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
26. Verifikasi Dialog Pair TAG tidak terbuka

### Bulk Pair TAG: reader tidak terhubung didahulukan (TC-FA-TAG-1493)

27. Tutup Popup Detail dan atur 'Excavator 20 Ton - 51' berstatus normal Not Paired Yet, pastikan 'Excavator 20 Ton - 53' In Disposal Process Not Paired Yet, serta stok RFID tetap 0 dan reader tetap terputus lewat fixture backend hingga tersimpan
28. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
29. Klik `Show` di samping `Not Paired Yet`
30. Centang baris 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 53'
31. Arahkan kursor ke Bulk `Pair TAG`
32. Verifikasi Bulk `Pair TAG` tetap tampil namun Disabled
33. Verifikasi tooltip "Connect a TAG reader to pair."
34. Verifikasi tooltip bukan "This asset can't be paired while it is in disposal." maupun "No available RFID TAG in stock."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1455, 1491, 1492, 1493). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik tooltip Disabled Pair TAG ada di spec 106 (TC-FA-TAG-449 s.d. 452), spec 107 (TC-FA-TAG-454 s.d. 458), spec 109 (TC-FA-TAG-1494), dan spec 116 (TC-FA-TAG-453).
- Urutan TC di dalam spec mengikuti keadaan reader dan Asset Status: reader tersambung (TC-1455, TC-1492), lalu reader terputus (TC-1491, TC-1493).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 9, 18, dan 27 (mengatur reader, Asset Status, dan stok lewat fixture backend serta menutup Popup Detail).
- Temuan untuk QA:
  - TC-FA-TAG-1492 butir c ("tooltip bukan ...") adalah asersi negatif tanpa anchor tambahan; tooltip yang benar sudah diasersi pada butir b di elemen yang sama.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur reader tersambung atau tidak tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
