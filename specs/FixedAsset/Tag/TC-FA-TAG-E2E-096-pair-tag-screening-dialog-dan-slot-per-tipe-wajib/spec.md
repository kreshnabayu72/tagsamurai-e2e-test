---
id: TC-FA-TAG-E2E-096-pair-tag-screening-dialog-dan-slot-per-tipe-wajib
title: "Pair TAG: Screening Dialog dan Slot per Tipe Wajib"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-411
  - TC-FA-TAG-412
  - TC-FA-TAG-413
  - TC-FA-TAG-414
coverage:
  web: automated
---

# Pair TAG: Screening Dialog dan Slot per Tipe Wajib

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Aset satu tipe | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset dua tipe | 'Laptop Pro 14 - 9' (AST-0109, Group Plant A, TAG Type Asset Name NFC dan QR), Not Paired Yet | `aset109` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: spec tidak mengubah data (dialog hanya dibuka dan dibatalkan tanpa isian).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### Screening header, blok info, dan footer (TC-FA-TAG-411)

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Verifikasi Dialog (Size MD) berjudul `Pair TAG` terbuka di atas tab Paired
5. Verifikasi dialog tanpa Breadcrumb
6. Verifikasi blok info aset sama dengan Dialog Replace TAG: judul `Server Rack 42U - 101`, Asset ID `AST-0101`, tanpa ikon tipe Tag, grid `Brand`, `Model/Type`, `Group`, `Asset Status`
7. Verifikasi footer memuat tombol [Cancel] dan [Submit]
8. Verifikasi teks error V-37 belum tampil

### Slot per tipe wajib Asset Name (TC-FA-TAG-412)

9. Verifikasi bagian `TAG to pair` memuat tiga slot berurutan: `RFID TAG`, `NFC TAG`, `QR TAG`
10. Verifikasi tiap slot memuat badge tipe, label `[Type] TAG`, ButtonScan `Scan RFID`, `Scan NFC`, `Scan QR`, dan status `Not scanned`
11. Verifikasi slot `QR TAG` memuat tombol `Print QR` (Button Outline, ikon PrinterLine) di sebelah kiri `Scan QR`
12. Verifikasi slot RFID dan NFC tidak memuat tombol `Print QR`
13. Klik [Cancel]

### Aset dengan satu tipe wajib (TC-FA-TAG-413)

14. Tutup Popup Detail
15. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
16. Klik tombol teks `Show` di samping field `Not Paired Yet`
17. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
18. Verifikasi bagian `TAG to pair` hanya memuat satu slot `RFID TAG`
19. Klik [Cancel]

### Aset dengan dua tipe wajib (TC-FA-TAG-414)

20. Tutup Popup Detail
21. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
22. Klik tombol teks `Show` di samping field `Not Paired Yet`
23. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
24. Verifikasi bagian `TAG to pair` memuat slot `NFC TAG` lalu `QR TAG`
25. Klik [Cancel]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-411, 412, 413, 414). Tidak ada TC hanya-BE.
- Urutan TC di dalam spec: TC-412 memakai dialog yang sama dengan TC-411 (langkah 3) karena precondition dan langkah pembukanya identik; TC-413 dan TC-414 memakai aset lain sehingga popup grup dibuka ulang.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 13, 19, dan 25 (menutup dialog tanpa isian dengan [Cancel], yang menutup langsung tanpa konfirmasi D-11), serta langkah 14 dan 20 (menutup Popup Detail sebelum membuka popup grup lain).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-411 butir b menulis blok info "sama dengan Dialog Replace TAG" dengan rincian di klausa yang sama; spec mengasersinya sebagai satu butir daftar elemen.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur reader tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
