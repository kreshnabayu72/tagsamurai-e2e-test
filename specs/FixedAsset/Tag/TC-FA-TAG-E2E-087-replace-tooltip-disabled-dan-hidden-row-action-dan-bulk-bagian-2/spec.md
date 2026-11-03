---
id: TC-FA-TAG-E2E-087-replace-tooltip-disabled-dan-hidden-row-action-dan-bulk-bagian-2
title: "Replace TAG: Tooltip Disabled dan Hidden Bulk serta Aksi Grup (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-381
  - TC-FA-TAG-382
  - TC-FA-TAG-384
coverage:
  web: automated
---

# Replace TAG: Tooltip Disabled dan Hidden Bulk serta Aksi Grup (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB yang dapat diatur tersambung atau tidak tersambung (driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader); (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Asset Status aset, Tag per status registri, dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 1 | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID), satu Tag RFID `RF-00130` Paired | `aset220` |
| Aset 2 | 'Excavator 20 Ton - 22' (AST-0022, Group Plant A), Tag RFID `RF-00142` Paired, Asset Status In Disposal Process | `aset22` |
| Aset 3 | 'Excavator 20 Ton - 42' (AST-0042, Group Plant A, TAG Type Asset Name RFID), satu Tag QR `QR-00230` Paired (Non-standard) | `aset42` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500` (bagian TC-382 dan TC-384 tidak memerlukannya sebagai asersi) | `stokAvailable` |

- State yang diubah dan pemulihannya: status reader, stok Available RFID, dan Asset Status 'Excavator 20 Ton - 22' diatur per bagian lewat fixture; hook `after` memulihkan reader tersambung, stok seperti awal, dan Asset Status aset.

## Test Steps

### Stok tipe yang dibutuhkan 0 (TC-FA-TAG-381)

1. Sambungkan reader (driver terpasang, aktif, sudah disinkronkan), hapus semua Tag RFID Available dari stok Global, dan pastikan 'Excavator 20 Ton - 220' punya satu Tag RFID `RF-00130` Paired lewat fixture backend hingga tersimpan
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Centang baris 'Excavator 20 Ton - 220'
4. Verifikasi Bulk Action Bar tidak memuat `Batch Replace TAG` (Hidden)

### Aset terpilih In Disposal Process (TC-FA-TAG-382)

5. Hapus centang baris 'Excavator 20 Ton - 220', tutup Popup Detail, isi stok Global dengan Tag RFID `RF-00412` dan `RF-00415` serta Tag NFC `NF-00500` Available, dan atur 'Excavator 20 Ton - 22' berstatus In Disposal Process dengan Tag RFID `RF-00142` Paired lewat fixture backend hingga tersimpan
6. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
7. Centang baris 'Excavator 20 Ton - 220' dan baris 'Excavator 20 Ton - 22'
8. Verifikasi Bulk Action Bar tidak memuat `Batch Replace TAG` (Hidden)

### Aksi grup Replace non-standard TAGs saat reader tidak terhubung (TC-FA-TAG-384)

9. Hapus centang kedua baris, tutup Popup Detail, dan putuskan reader dari komputer lewat simulator reader (Tag QR `QR-00230` Paired pada 'Excavator 20 Ton - 42')
10. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
11. Arahkan kursor ke aksi `Replace non-standard TAGs`
12. Verifikasi aksi `Replace non-standard TAGs` tetap tampil namun Disabled
13. Verifikasi tooltip "Connect a TAG reader to replace."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-381, 382, 384). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-330, 331, 371 s.d. 374, dan 380 (topik yang sama) ada di spec `TC-FA-TAG-E2E-086-replace-tooltip-disabled-dan-hidden-row-action-dan-bulk-bagian-1`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 5, dan 9 (mengatur reader, stok, dan Asset Status lewat fixture backend, menghapus centang, menutup Popup Detail). Popup Detail dibuka ulang sesudah tiap perubahan state supaya state terbaru terbaca.
- Temuan untuk QA:
  - TC-FA-TAG-382 tidak menyebut stok Tag; spec mengisi stok Available agar Hidden hanya bisa berasal dari aset In Disposal Process (bukan stok 0 seperti TC-381).
  - TC-FA-TAG-381 dan 382 mengharapkan Bulk `Batch Replace TAG` Hidden tanpa anchor positif di TC; spec tidak menambah asersi anchor.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur tersambung atau tidak tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC tanpa langkah observasi tidak diasersi.
