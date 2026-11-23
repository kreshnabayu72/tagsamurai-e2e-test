---
id: TC-FA-SU-E2E-449-tab-transaction-admin-log-assignment-filter-activity
title: "Tab Transaction Admin Log Sub-tab Assignment: Filter Kolom Activity"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1154
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Filter Kolom Activity

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan Activity `Handed over`, `Approved`, `Requested`, dan `Rejected` sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter sisi klien.

## Test Steps

### TC-FA-SU-1154: Filter kelas enum, kolom Activity

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Klik icon Filter
3. Buka dropdown `Activity`
4. Verifikasi opsi dropdown = DISTINCT nilai kolom Activity pada tabel: `Approved`, `Handed over`, `Rejected`, `Requested`
5. Centang `Rejected`
6. Klik `[Apply]`
7. Verifikasi tabel menyisakan `ASG-20260715-0068` (1 baris)
8. Verifikasi chip `Rejected` tampil di dalam field `Activity`
9. Verifikasi panel Filter tetap terbuka setelah `[Apply]` (tidak menutup otomatis)
10. Klik icon Filter untuk menutup panel
11. Verifikasi panel Filter tertutup
12. Klik icon Filter, klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
13. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan langkah 12 dan 13 (melepas filter dan menutup panel supaya spec tidak meninggalkan state, S-09). Langkah 10 mengikuti Expected b TC (panel tertutup setelah icon Filter diklik).
- Pembagian TC lintas spec: screening panel Filter, Filter kolom Group dan Name ada di spec 458.
- Temuan untuk QA (S-15): TC-FA-SU-1154 menyebut seed Assignment Budi Santoso dari Pre-setup #29 tanpa menyatakan mekanisme seed; spec membaca seed itu apa adanya dan tidak mengarang endpoint. Post Condition tidak ada.
