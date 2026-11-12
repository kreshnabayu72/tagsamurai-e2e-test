---
id: TC-FA-TAG-E2E-105-pair-tag-cancel-ikon-close-backdrop-dan-esc-bagian-2
title: "Pair TAG: Ikon Close, Klik Backdrop, dan Esc pada Konfirmasi D-11 (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-448
  - TC-FA-TAG-1439
  - TC-FA-TAG-1442
coverage:
  web: automated
---

# Pair TAG: Ikon Close, Klik Backdrop, dan Esc pada Konfirmasi D-11 (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: spec tidak menyimpan perubahan (dialog dibuang dengan [Discard]).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### Klik backdrop dan ikon close pada dialog yang terisi (TC-FA-TAG-1439, TC-FA-TAG-448)

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik area backdrop di luar Dialog Pair TAG
6. Verifikasi Dialog Pair TAG tetap terbuka
7. Verifikasi slot `RFID TAG` tetap menampilkan `RF-00412` dengan badge `Verified`
8. Klik ikon close dialog
9. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]

### Esc pada konfirmasi D-11 (TC-FA-TAG-1442)

10. Klik [Cancel] pada dialog `Discard Pairing`
11. Klik [Cancel] pada dialog Pair TAG
12. Tekan Esc pada dialog `Discard Pairing`
13. Verifikasi dialog konfirmasi menutup
14. Verifikasi slot `RFID TAG` tetap menampilkan `RF-00412` dengan badge `Verified`
15. Klik [Cancel] pada dialog Pair TAG
16. Verifikasi dialog `Discard Pairing` dengan body "Discard this pairing? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
17. Klik [Discard]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-448, 1439, 1442). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik penutupan Dialog Pair TAG ada juga di spec 104 (TC-FA-TAG-444 s.d. 447).
- Urutan TC di dalam spec: TC-1439 mendahului TC-448 pada dialog yang sama (klik backdrop tidak menutup dan tidak mengubah isian), lalu TC-1442 memakai dialog yang sama sesudah konfirmasi D-11 TC-448 ditutup dengan [Cancel].
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10 (menutup konfirmasi D-11 TC-448 dengan [Cancel]), 15 dan 17 (membuang dialog yang berisi pindaian dengan [Cancel] dan [Discard], S-08). Langkah 16 (Verifikasi dialog `Discard Pairing` sebelum [Discard]) adalah asersi tambahan di luar Expected TC (S-03).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
