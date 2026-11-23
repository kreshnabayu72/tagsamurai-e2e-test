---
id: TC-FA-SU-E2E-477-tab-transaction-admin-log-audit-baris-tingkat-task-dan-activity-nama-node
title: "Tab Transaction Admin Log Sub-tab Audit: Baris Tingkat Task dan Activity Nama Node"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1190
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Audit: Baris Tingkat Task dan Activity Nama Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Audit berisi 3 baris sesuai `audit.md` §8.2: `Audit finished` (`AUD-2026-0042`, Name `—`, Group `—`) dan dua baris `Verified` dari satu sesi mobile `AUD-2026-0041` (`Laptop Dell Latitude - 11` dan `Monitor LG 24 - 7`, Group `IT Infrastructure`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan seed (disediakan tim FE/BE, tanpa endpoint karangan): seed sub-tab Audit Budi Santoso pada Pre-setup #29 TC; baris seed bersifat permanen pada log dan tidak dipulihkan.
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Audit
2. Verifikasi baris `AUD-2026-0042` dengan Activity `Audit finished` menampilkan Name `—`
3. Verifikasi baris `AUD-2026-0042` menampilkan Group `—`
4. Verifikasi sesi mobile `AUD-2026-0041` menampilkan baris `Verified` dengan Name `Laptop Dell Latitude - 11`
5. Verifikasi baris `Verified` `Laptop Dell Latitude - 11` menampilkan Group `IT Infrastructure`
6. Verifikasi sesi mobile `AUD-2026-0041` menampilkan baris `Verified` dengan Name `Monitor LG 24 - 7`
7. Verifikasi baris `Verified` `Monitor LG 24 - 7` menampilkan Group `IT Infrastructure`
8. Verifikasi `AUD-2026-0041` tidak memiliki baris per sesi (tepat dua baris, keduanya `Verified`)
9. Verifikasi Activity seluruh baris berupa nama node `Audit finished` dan `Verified`
10. Verifikasi Activity seluruh baris berupa teks biasa tanpa badge
11. Verifikasi Activity seluruh baris tanpa akhiran pelaku

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16).
- Nilai Activity bersumber dari katalog `audit.md` §8.2 (nama node §8.1); baris tingkat task memakai Name dan Group `—`.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1190 mengandalkan seed Audit pada Pre-setup #29 yang baru ditambahkan; spec lain (E2E-442) hanya mengasersi struktur dan jumlah baris sedikitnya dua. (2) Seed disediakan tim FE/BE tanpa endpoint karangan.
