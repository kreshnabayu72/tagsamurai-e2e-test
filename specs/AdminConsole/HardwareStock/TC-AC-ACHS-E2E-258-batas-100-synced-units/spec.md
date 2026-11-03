---
id: TC-AC-ACHS-E2E-258-batas-100-synced-units
title: "Batas 100 Synced Units pada Add Stock Sync"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-130
coverage:
  web: automated
---

# Batas 100 Synced Units pada Add Stock Sync

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Kelas harness: d (simulator reader USB, Pre-setup #25) dan e (volume 100 baris Synced Units) sekaligus karena satu TC tunggal; lihat Notes dan Temuan untuk QA.
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |

- Data Pre-setup: SKU `{skuLong}` (Long Range; Pre-setup #16); service driver mock Handheld Reader (Pre-setup #25); Pre-setup #26: System Limits `register_asset_bulk_limit` default 1.000, nilai minimum 100 dipakai TC batas.
- Data Dinamis: 100 perangkat simulasi dengan Serial Number `SN-ZEBRA-RFD40-{NNN}-{runId}-258` untuk NNN `001` sampai `100`; tidak pernah disimpan (form ditutup tanpa Submit).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader USB Pre-setup #25 yang dapat diatur untuk 100 perangkat berurutan; mengubah System Limit `register_asset_bulk_limit` (aktor dan mekanisme tidak disebut TC, PRD, atau LLD, S-13).
- State global: System Limit `register_asset_bulk_limit` diatur ke 100 pada langkah 1 dan dikembalikan ke nilai awal pada langkah 18 dan hook `after` walau spec gagal di tengah. Suite berjalan serial.

## Test Steps

1. Atur System Limits > Register Asset Bulk Limit = 100 (Pre-setup #26)
2. Ketik Search `{skuLong}`, tekan Enter
3. Klik `(⋯)` pada baris SKU `{skuLong}`
4. Klik opsi `Add Stock`
5. Untuk setiap nomor NNN dari `001` sampai `099` (langkah 5 sampai 6): atur simulator dengan perangkat `SN-ZEBRA-RFD40-{NNN}-{runId}-258`
6. Klik `[Sync]` (diulang bersama langkah 5 untuk setiap NNN dari `001` sampai `099`)
7. Verifikasi counter "99 units synced"
8. Atur simulator dengan perangkat `SN-ZEBRA-RFD40-100-{runId}-258`
9. Klik `[Sync]`
10. Verifikasi baris ke-100 diterima: counter "100 units synced"
11. Verifikasi `[Sync]` Disabled
12. Verifikasi pesan inline "You've reached the maximum of 100 assets per submission. Submit this batch first, then continue with a new one."
13. Klik `[Sync]` yang Disabled
14. Verifikasi baris ke-101 tidak dapat ditambahkan: tabel Synced Units tetap berisi 100 baris dan counter tetap "100 units synced"
15. Klik `[Cancel]`
16. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
17. Klik `[Leave]`
18. Kembalikan Register Asset Bulk Limit ke nilai awal

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-130). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah bila diekspansi (langkah 5 sampai 6 diulang 99 kali, sekitar 210 langkah ekspansi); langkah 5 sampai 6 memakai idiom "untuk setiap nomor ... (langkah 5 dan 6)" dengan parameter di Prerequisites. Alasan: TC tunggal dan batas 100 baris hanya dapat dicapai dengan 100 Sync berurutan; tidak ada blok lain yang kehilangan makna.
- Spec memuat dua kelas harness (d dan e) karena satu TC yang inheren membutuhkan simulator USB dan volume 100 baris; bagian 3 konvensi tidak memiliki pengecualian bernomor untuk kombinasi ini (P-7 hanya d bersama c atau h). Hal ini dicatat di Temuan untuk QA.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search (langkah 2), pengaturan simulator (langkah 5, 8), pemulihan limit (langkah 18), serta `[Cancel]` dan `[Leave]` (langkah 15 dan 17). Langkah 13 (klik `[Sync]` yang Disabled) adalah aksi untuk Expected butir c.
- Temuan untuk QA:
  - TC-130 butir b menyebut pesan inline V-18 dengan angka 100 yang sama dengan nilai limit uji; TC tidak menyebut apakah angka pada pesan mengikuti limit terkini atau tetap.
  - Mengatur System Limit dan aktor pengubahnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
  - TC-130 Post Condition ("Limit dikembalikan ke nilai awal") dijalankan sebagai aksi (langkah 18), bukan asersi.
