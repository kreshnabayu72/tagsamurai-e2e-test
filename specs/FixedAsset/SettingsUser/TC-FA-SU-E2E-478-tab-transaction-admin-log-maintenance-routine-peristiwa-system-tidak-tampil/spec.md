---
id: TC-FA-SU-E2E-478-tab-transaction-admin-log-maintenance-routine-peristiwa-system-tidak-tampil
title: "Tab Transaction Admin Log Sub-tab Maintenance Routine: Peristiwa System Tidak Tampil"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1191
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Maintenance Routine: Peristiwa System Tidak Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Maintenance Routine berisi 2 baris tindakan pengguna sesuai `maintenance-routine.md` §8.3a: `Rescheduled` (`MNT-2026-00031`, `Generator Set - 2`, `Logistics Warehouse`) dan `Approved` (`MNT-2026-00030`, `Air Compressor - 1`, `IT Infrastructure`); task `MNT-2026-00031` juga mengalami peristiwa aktor `System` `Became due` yang tidak tampil. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan seed (disediakan tim FE/BE, tanpa endpoint karangan): seed sub-tab Maintenance Routine Budi Santoso pada Pre-setup #29 TC; baris seed bersifat permanen pada log dan tidak dipulihkan.
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Maintenance Routine
2. Verifikasi baris `MNT-2026-00031` dengan Activity `Rescheduled` menampilkan Name `Generator Set - 2` dan Group `Logistics Warehouse`
3. Verifikasi baris `MNT-2026-00030` dengan Activity `Approved` menampilkan Name `Air Compressor - 1` dan Group `IT Infrastructure`
4. Verifikasi Activity kedua baris berupa teks biasa tanpa badge
5. Verifikasi tidak ada baris dengan Activity `Became due`
6. Klik icon Search, ketik `Became due`, lalu tekan Enter
7. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
8. Kosongkan isi kotak search, lalu tekan Enter
9. Klik icon Filter
10. Klik field Activity pada panel Filter
11. Verifikasi opsi Activity tidak memuat `Became due`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; R-16), pembukaan kotak Search dan pengisian kata kunci, pengosongan Search, serta pembukaan panel Filter dan field Activity.
- Klausa absence (langkah 5, 7, dan 11) didahului `Verifikasi` positif baris `Rescheduled` dan `Approved` pada langkah 2 dan 3 sebagai anchor pada surface yang sama (8b.2).
- Aturan bersumber dari `maintenance-routine.md` §8.3a: hanya tindakan pengguna yang tercatat; peristiwa aktor `System` (mis. `Became due`) tidak muncul di Transaction admin log.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1191 mengandalkan seed Maintenance Routine pada Pre-setup #29 yang baru ditambahkan, termasuk peristiwa `System` `Became due` pada task `MNT-2026-00031`. (2) Opsi dropdown Activity bersifat DISTINCT data tabel; asersi absence opsi mengikuti keluaran TC butir c.
