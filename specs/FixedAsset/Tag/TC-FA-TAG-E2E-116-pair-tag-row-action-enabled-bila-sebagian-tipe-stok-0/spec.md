---
id: TC-FA-TAG-E2E-116-pair-tag-row-action-enabled-bila-sebagian-tipe-stok-0
title: "Pair TAG: Row Action Tetap Enabled bila Hanya Sebagian Tipe Stok 0"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-453
coverage:
  web: automated
---

# Pair TAG: Row Action Tetap Enabled bila Hanya Sebagian Tipe Stok 0

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
| Stok Available | Tag RFID `RF-00412` dan Tag QR `QR-00701` Available; tidak ada Tag NFC Available | `stokTanpaNfc` |

- State yang diubah dan pemulihannya: stok Tag NFC Available dikosongkan lewat fixture backend; hook `after` memulihkan stok Available seperti awal.

## Test Steps

1. Kosongkan stok Tag NFC Available dan pastikan Tag RFID `RF-00412` serta Tag QR `QR-00701` Available lewat fixture backend hingga tersimpan, lalu muat ulang halaman TAG (F5)
2. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
3. Klik tombol teks `Show` di samping field `Not Paired Yet`
4. Arahkan kursor ke row action `Pair TAG` pada baris 'Server Rack 42U - 101'
5. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
6. Verifikasi row action `Pair TAG` Enabled
7. Verifikasi Dialog Pair TAG terbuka dengan tiga slot
8. Klik [Cancel]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-453). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik tooltip Disabled Pair TAG ada di spec 106 (TC-FA-TAG-449 s.d. 452), spec 107 (TC-FA-TAG-454 s.d. 458), spec 108, dan spec 109.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (mengatur stok lewat fixture backend dan memuat ulang halaman), langkah 8 ([Cancel] pada dialog tanpa isian, tanpa konfirmasi D-11).
- Temuan untuk QA:
  - TC-FA-TAG-453 mengarahkan kursor ke row action lalu mengklik tanpa Expected tooltip; spec mengasersi hanya butir Expected (Enabled dan dialog tiga slot).
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme mengatur reader tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
