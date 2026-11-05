---
id: TC-FA-RP-E2E-369-home-group-constraint-yang-mencakup-node-gm-tidak-mencabut-apa-pun
title: "Home Group constraint yang mencakup node penugasan Group Manager tidak mencabut penugasan maupun baris pola"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1200
coverage:
  web: automated
---

# Home Group constraint yang mencakup node penugasan Group Manager tidak mencabut penugasan maupun baris pola

## Prerequisites

- Mode: FE+BE.
- Akun (login di hook `before`):

  | Urutan | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|---|
  | 1 (hook `before`) | Manage global user & role (Update), Hendra Wijaya | #6 | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Seeding state Hesti Rahma memakai sesi API Total Control (Pre-setup #2, `Spectra.env.FA_TC_PASSWORD`); kemampuan disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Hesti Rahma), #18 (pohon Group: `Head Office` > `Logistics Warehouse` > `Dock 1`; `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`), #24 (`Company Changelog`, dipakai sebagai latar log, tidak diasersi).
- Seeding precondition d TC (dipakai sebagai precondition, tidak diasersi): Hesti Rahma tanpa Home Group, Group Manager di `Dock 1` (baris pola GM di `Dock 1`). Pre-setup #17 menaruh Home Group `Logistics Warehouse` pada Hesti Rahma; seeding menimpanya sesuai precondition TC. Spec tidak membuat data Dinamis.
- Kemampuan teknis: membaca baseline jumlah entri Changelog Detail Role `Manage files` lewat kemampuan baca (disediakan tim FE/BE, tanpa endpoint karangan).
- State yang diubah dan pemulihannya: Home Group Hesti Rahma dan penugasan Group Manager beserta baris pola-nya. Hook `after` memulihkan Hesti Rahma ke state seed Pre-setup #17 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state seed oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`, `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1200: Constraint yang mencakup node penugasan GM tidak mencabut penugasan maupun baris pola

1. Siapkan Hesti Rahma tanpa Home Group, Group Manager di `Dock 1`, lewat sesi API hingga tersimpan
2. Catat jumlah entri Changelog Detail Role `Manage files` sebagai baseline lewat kemampuan baca
3. Buka Fixed Asset > Settings > User
4. Ketik Search `Hesti Rahma`, tekan Enter
5. Klik Name Hesti Rahma
6. Klik field Home Group, pilih `Logistics Warehouse`, klik `[Select]`
7. Verifikasi dialog D-10 tidak tampil
8. Verifikasi Home Group Hesti Rahma tersimpan `Logistics Warehouse`
9. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Group Manager`
10. Verifikasi baris Hesti Rahma di `Dock 1` tetap ada di Tab `Group Manager`
11. Buka Tab `System` lalu Detail Role `Manage files`
12. Klik node `Dock 1` pada Sidebar Group Tree
13. Verifikasi baris pola GM Hesti Rahma (Group Role) tetap ada pada node `Dock 1`
14. Klik ikon Changelog di toolbar Detail Role
15. Verifikasi jumlah entri Changelog sama dengan baseline langkah 2 (tidak ada entri `Remove (via Group Manager)`)
16. Tutup modal Changelog
17. Klik Tab `Transaction Role`
18. Klik node `Dock 1`
19. Klik sub-tab `Disposal`
20. Verifikasi Hesti Rahma tampil di section Asset Admin dan Approver (baris pola GM tetap ada)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 20 langkah, di bawah batas sekitar 35.
- Langkah penghubung (S-03): langkah 1 (menyiapkan state lewat sesi API sesuai Pre-setup #32), langkah 2 (baseline, S-12), langkah 3 sampai 5 (membuka daftar User, Search mencari baris target, dan membuka Detail; R-16), langkah 9, 11, 12, 17 sampai 19 (navigasi), langkah 14 dan 16 (membuka dan menutup modal Changelog). Langkah 8 menjadi anchor atas langkah 7 (8b butir 11).
- Tanpa Search pada tabel Detail Role dan tabel Role Transaksi: precondition TC hanya memuat Pre-setup #17, #18, dan #24 sehingga tiap node memuat paling banyak tujuh baris dalam satu halaman.
- Temuan untuk QA:
  - Pre-setup #17 menaruh Home Group `Logistics Warehouse` pada Hesti Rahma, sedangkan precondition d TC menyebut Hesti Rahma tanpa Home Group; spec memakai seeding precondition TC.
  - TC-FA-RP-1200 Expected b menyebut "tidak ada entri `Auto-Revert` maupun `Remove (via Group Manager)`" tanpa menyebut surface log dan tanpa langkah observasi; spec mengasersi hanya pada Changelog Detail Role `Manage files` (langkah 15, selisih nol terhadap baseline). Entri `Auto-Revert` (System Log dan Activity Log) tidak diasersi di spec ini.
  - Post Condition TC ("Hesti Rahma dipulihkan ke state seed oleh automation baseline") tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
