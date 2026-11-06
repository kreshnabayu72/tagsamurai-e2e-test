---
id: TC-FA-RP-E2E-351-home-group-constraint-pada-gm-mencabut-penugasan-dan-baris-pola-per-baris
title: "Home Group constraint pada Group Manager mencabut penugasan dan baris pola per baris, bukan pencabutan silent"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1199
coverage:
  web: automated
---

# Home Group constraint pada Group Manager mencabut penugasan dan baris pola per baris, bukan pencabutan silent

## Prerequisites

- Mode: FE+BE.
- Akun (login akun urutan 1 di hook `before`; akun urutan 2 lewat langkah ganti akun eksplisit):

  | Urutan | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|---|
  | 1 (hook `before`) | Manage global user & role (Update), Hendra Wijaya | #6 | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
  | 2 | Pengguna target, Hesti Rahma | #17 | akun login Hesti Rahma; email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE | `Spectra.env.FA_HESTI_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Seeding state Hesti Rahma memakai sesi API Total Control (Pre-setup #2, `Spectra.env.FA_TC_PASSWORD`); kemampuan disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Hesti Rahma), #18 (pohon Group: `Head Office` > `Logistics Warehouse` > `Dock 1`; `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`), #24 (`Company Changelog`, dipakai sebagai latar log, tidak diasersi).
- Seeding precondition d TC (dipakai sebagai precondition, tidak diasersi): Hesti Rahma tanpa Home Group, Group Manager di `Data Center` (baris pola GM di `Data Center` dan `Rack A1`), memiliki akun login. Pre-setup #17 menaruh Home Group `Logistics Warehouse` pada Hesti Rahma; seeding menimpanya sesuai precondition TC. Spec tidak membuat data Dinamis.
- Kemampuan teknis: membaca baseline dan hasil lewat kemampuan baca (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Detail Role `Manage files`, jumlah entri Changelog Transaction Role `Data Center` sub-tab `Disposal`, jumlah entri System Log dan Activity Log FAMS Hendra Wijaya (audit trail permanen, S-12), dan jumlah notifikasi in-app Hesti Rahma. Jendela asersi notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- Tabel node yang ditelusuri pada langkah 14 sampai 16:

  | Node pola GM Hesti Rahma |
  |---|
  | `Data Center` |
  | `Rack A1` |

- State yang diubah dan pemulihannya: Home Group Hesti Rahma dan penugasan Group Manager beserta baris pola-nya. Hook `after` memulihkan Hesti Rahma ke state seed Pre-setup #17 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state seed oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Entri log dan notifikasi bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`, `FA_HESTI_PASSWORD`, `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1199: Constraint pada Group Manager mencabut penugasan dan baris pola per baris, bukan pencabutan silent

1. Siapkan Hesti Rahma tanpa Home Group, Group Manager di `Data Center` (tanpa penugasan di `Dock 1`), lewat sesi API hingga tersimpan
2. Catat baseline lewat kemampuan baca: jumlah notifikasi in-app Hesti Rahma, jumlah entri Changelog Detail Role `Manage files`, jumlah entri Changelog Transaction Role `Data Center` sub-tab `Disposal`, serta jumlah entri System Log dan Activity Log FAMS Hendra Wijaya
3. Buka Fixed Asset > Settings > User
4. Ketik Search `Hesti Rahma`, tekan Enter
5. Klik Name Hesti Rahma
6. Klik field Home Group, pilih `Logistics Warehouse`, klik `[Select]`
7. Verifikasi dialog D-10 mendaftar `• Group Manager — Data Center` saja (baris pola GM tidak didaftar terpisah)
8. Klik `[Revoke]`
9. Tunggu aksi selesai: dialog tertutup
10. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Group Manager`
11. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
12. Verifikasi baris Hesti Rahma tidak ada di Tab `Group Manager`
13. Buka Tab `System` lalu Detail Role `Manage files`
14. Untuk setiap baris tabel "Node pola GM Hesti Rahma" (langkah 14 sampai 16 diulang untuk node itu): klik node pada Sidebar Group Tree
15. Verifikasi sedikitnya satu baris lain tampil pada node itu
16. Verifikasi baris pola GM Hesti Rahma (Group Role) pada node itu tidak ada
17. Klik ikon Changelog di toolbar Detail Role
18. Verifikasi jumlah entri Changelog bertambah dua terhadap baseline langkah 2 (satu entri per baris pola pada `Data Center` dan `Rack A1`)
19. Verifikasi dua entri baru ber-Action `Remove (via Group Manager)` untuk Hesti Rahma pada `Data Center` dan `Rack A1`
20. Verifikasi Modified By kedua entri baru adalah aktor pengedit `Hendra W`, bukan `System`
21. Tutup modal Changelog
22. Klik Tab `Transaction Role`
23. Klik node `Data Center`
24. Klik sub-tab `Disposal`
25. Verifikasi sedikitnya satu baris tampil pada section Asset Admin
26. Verifikasi baris pola GM Hesti Rahma (Asset Admin dan Approver) tidak tampil pada `Data Center` sub-tab `Disposal`
27. Klik ikon Changelog pada baris sub-tab `Disposal`
28. Verifikasi jumlah entri Changelog Transaction Role bertambah terhadap baseline langkah 2
29. Verifikasi entri baru ber-Action `Remove (via Group Manager)` per baris pola Role Transaksi Hesti Rahma (Asset Admin dan Approver) dengan Modified By `Hendra W`, bukan `System`
30. Tutup modal Changelog
31. Buka Fixed Asset > Settings > User
32. Ketik Search `Hendra Wijaya`, tekan Enter
33. Klik Name Hendra Wijaya
34. Klik Tab `System Log`
35. Verifikasi jumlah entri System Log bertambah terhadap baseline langkah 2 dan entri baru ber-Action `Auto-Revert` Group Manager
36. Verifikasi entri baru System Log tidak memuat `Remove (via Group Manager)` per baris
37. Klik Tab `Activity Log` FAMS
38. Verifikasi jumlah entri Activity Log bertambah terhadap baseline langkah 2 dan entri baru ber-Action `Auto-Revert` Group Manager
39. Verifikasi entri baru Activity Log tidak memuat `Remove (via Group Manager)` per baris
40. Ganti akun: logout dari akun Manage global user & role (Update)
41. Login sebagai Hesti Rahma
42. Buka Overlay Notifikasi
43. Verifikasi notifikasi `You are no longer Group Manager for Data Center` tampil
44. Tunggu 5 detik tanpa memuat ulang halaman
45. Verifikasi jumlah notifikasi Hesti Rahma bertambah tepat satu terhadap baseline langkah 2 (tidak ada notifikasi per baris pola)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 45 langkah nominal (47 langkah setelah ekspansi langkah 14 sampai 16 untuk dua node).
- Alasan melewati sekitar 35 langkah: TC-FA-RP-1199 mengamati satu aksi `[Revoke]` di enam surface (Tab Group Manager, Detail Role, Role Transaksi, dua Changelog, System Log dan Activity Log, notifikasi) yang bergantung pada hasil aksi yang sama dan tidak dapat dipisah tanpa mengulang aksi itu.
- Langkah penghubung (S-03): langkah 1 (menyiapkan state lewat sesi API sesuai Pre-setup #32), langkah 2 (baseline, S-12), langkah 3 sampai 5 dan 31 sampai 33 (membuka daftar User, Search mencari baris target, dan membuka Detail; R-16), langkah 10, 13, 22 sampai 24, 34, 37, 42 (navigasi), langkah 17, 21, 27, 30 (membuka dan menutup modal Changelog), langkah 9 (tunggu aksi selesai, 8b butir 8), langkah 40 dan 41 (ganti akun eksplisit, S-07), langkah 44 (jendela notifikasi, bagian 6). Langkah 11, 15, dan 25 adalah anchor positif atas asersi absence langkah 12, 16, dan 26; langkah 43 menjadi anchor atas langkah 45.
- Tanpa Search pada tabel Detail Role dan tabel Role Transaksi: precondition TC hanya memuat Pre-setup #17, #18, dan #24 sehingga tiap node memuat paling banyak tujuh baris dalam satu halaman.
- Teks bertanda `copy usulan, PRD 12 #7` (dialog D-10, TC-FA-RP-1199 Expected a) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - Pre-setup #17 menaruh Home Group `Logistics Warehouse` pada Hesti Rahma, sedangkan precondition d TC menyebut Hesti Rahma tanpa Home Group; spec memakai seeding precondition TC.
  - Email akun login Hesti Rahma tidak tertulis di Pre-setup #17; akun disediakan tim FE. Nama env `FA_HESTI_PASSWORD` sudah terdaftar di `suite.md`.
  - TC-FA-RP-1199 Expected c menyebut "satu entri per baris pola" tanpa jumlah; spec menyimpulkan dua entri pada Detail Role `Manage files` (`Data Center` dan `Rack A1`) dan hanya mengasersi pertambahan jumlah pada Changelog Transaction Role. Nama Action `Remove (via Group Manager)` mengikuti TC dan menunggu keputusan PM (Open Item #7c).
  - TC-FA-RP-1199 Expected d tidak menyebut jumlah entri `Auto-Revert` pada System Log dan Activity Log; spec hanya mengasersi pertambahan jumlah dan Action entri baru. "Detail aktor" ditafsirkan sebagai Detail Hendra Wijaya (aktor login).
  - TC-FA-RP-1199 Expected e menyebut `You are no longer Group Manager for Data Center`; spec mengasersi teks itu persis.
  - Post Condition TC ("Hesti Rahma dipulihkan ke state seed oleh automation baseline") tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
