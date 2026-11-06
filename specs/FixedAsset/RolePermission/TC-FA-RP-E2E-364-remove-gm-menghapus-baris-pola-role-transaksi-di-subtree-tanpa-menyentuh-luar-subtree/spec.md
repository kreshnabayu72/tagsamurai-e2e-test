---
id: TC-FA-RP-E2E-364-remove-gm-menghapus-baris-pola-role-transaksi-di-subtree-tanpa-menyentuh-luar-subtree
title: "Remove Group Manager menghapus baris pola Role Transaksi pada node penugasan dan descendant tanpa menyentuh penugasan Role Transaksi di luar subtree"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1187
coverage:
  web: automated
---

# Remove Group Manager menghapus baris pola Role Transaksi pada node penugasan dan descendant tanpa menyentuh penugasan Role Transaksi di luar subtree

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager hanya di `Data Center` dengan baris pola GM di `Data Center` dan `Rack A1`), #18 (pohon Group), #19 (seed Role Transaksi), #24 (`Company Changelog`, dipakai sebagai latar log, tidak diasersi).
- Seeding precondition d TC (dipakai sebagai precondition, tidak diasersi): Kevin Susanto juga memegang Monitoring & Report pada `Helpdesk` sub-tab `Disposal` (baris non-pola di luar subtree `Data Center`), dibentuk lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan). Spec tidak membuat data Dinamis.
- Kemampuan teknis: membaca (a) jumlah entri Changelog Transaction Role `Data Center` sub-tab `Disposal` dan (b) jumlah entri `Changelog: User > Transaction Role` Detail Kevin Susanto sebagai baseline (audit trail permanen, S-12; disediakan tim FE/BE).
- Tabel node yang ditelusuri pada langkah 8 sampai 14:

  | Node yang diperiksa |
  |---|
  | `Data Center` |
  | `Rack A1` |

- State yang diubah dan pemulihannya: Remove penugasan `Data Center` menghapus baris pola GM Kevin Susanto pada `Data Center` dan `Rack A1`. Hook `after` memulihkan Kevin Susanto ke state Pre-setup #13 (penugasan Group Manager di `Data Center` beserta baris pola dan baris non-pola Pre-setup #13) dan menghapus baris Monitoring & Report `Helpdesk` yang di-seed, lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #13 oleh automation baseline"). Entri Changelog bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1187: Remove Group Manager menghapus baris pola Role Transaksi pada node penugasan dan descendant

1. Catat baseline lewat kemampuan baca: jumlah entri Changelog Transaction Role `Data Center` sub-tab `Disposal` dan jumlah entri `Changelog: User > Transaction Role` Detail Kevin Susanto
2. Klik Tab `Group Manager`
3. Ketik Search `Kevin Susanto`, tekan Enter
4. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`
5. Klik `[Remove]` pada dialog konfirmasi
6. Tunggu aksi selesai: dialog tertutup
7. Klik Tab `Transaction Role`
8. Untuk setiap baris tabel "Node yang diperiksa" (langkah 8 sampai 14 diulang untuk node itu): klik node pada Sidebar Group Tree
9. Klik sub-tab `Disposal`
10. Verifikasi sedikitnya satu baris tampil pada section Asset Admin
11. Verifikasi Kevin Susanto tidak tampil di section mana pun pada sub-tab `Disposal`
12. Klik sub-tab `Transfer`
13. Verifikasi sedikitnya satu baris tampil pada section Asset Admin
14. Verifikasi Kevin Susanto tidak tampil di section mana pun pada sub-tab `Transfer`
15. Klik node `Helpdesk`
16. Klik sub-tab `Disposal`
17. Verifikasi Kevin Susanto tetap tampil di section Monitoring & Report pada `Helpdesk` (di luar subtree, non-pola)
18. Klik node `Data Center`
19. Klik sub-tab `Disposal`
20. Klik ikon Changelog pada baris sub-tab `Disposal`
21. Verifikasi jumlah entri Changelog bertambah terhadap baseline langkah 1
22. Verifikasi entri baru ber-Action `Remove (via Group Manager)` Field `Asset Admin — Data Center` dan `Approver — Data Center` dengan Old Value `Kevin Susanto`, New Value `—`, dan Modified By `Siti R`
23. Verifikasi entri yang sama (Field `Asset Admin — Rack A1` dan `Approver — Rack A1`) tampil untuk `Rack A1`
24. Verifikasi tidak ada entri baru untuk `Helpdesk`
25. Tutup modal Changelog
26. Buka Fixed Asset > Settings > User
27. Ketik Search `Kevin Susanto`, tekan Enter
28. Klik Name Kevin Susanto
29. Buka `Changelog: User > Transaction Role` pada Detail Kevin Susanto
30. Verifikasi jumlah entri bertambah terhadap baseline langkah 1
31. Verifikasi entri yang sama dengan langkah 22 dan 23 tampil di `Changelog: User > Transaction Role`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah nominal (38 langkah setelah ekspansi langkah 8 sampai 14 untuk dua node).
- Alasan melewati sekitar 35 langkah setelah ekspansi: satu TC dengan satu aksi Remove (langkah 4 dan 5) yang hasilnya diamati di tiga surface (tabel Role Transaksi, Changelog Transaction Role, Changelog User). Seluruh pengamatan bergantung pada hasil Remove yang sama dan tidak dapat dipisah tanpa mengulang aksi destruktif itu.
- Langkah penghubung (S-03): langkah 1 (baseline, S-12), langkah 2 sampai 5 (membuka Tab, Search mencari baris target, dan aksi Remove; R-16), langkah 6 (tunggu aksi selesai, 8b butir 8), langkah 7, 9, 12, 15, 16, 18, 19, 26 sampai 29 (navigasi), langkah 20 dan 25 (membuka dan menutup modal Changelog). Langkah 10 dan 13 adalah anchor positif atas asersi absence langkah 11 dan 14; langkah 22 sampai 23 menjadi anchor atas langkah 24 (8b butir 2). Langkah 28 didahului Search langkah 27 (R-23).
- Tanpa Search pada tabel Role Transaksi: tiap section node memuat paling banyak sepuluh baris (baris pola Total Control dan Read Only ditambah seed Pre-setup #19 dan baris pola GM Kevin Susanto), dalam satu halaman.
- Temuan untuk QA:
  - Seed Kevin Susanto belum direkonsiliasi: TC-FA-RP-1187 dan Pre-setup #13 menyatakan Group Manager hanya di `Data Center`, sedangkan Pre-setup #38 (dan TC lain) menaruh Kevin Susanto juga sebagai Group Manager di `Helpdesk`. Spec mengikuti TC-FA-RP-1187: tidak ada penugasan Group Manager di `Helpdesk`; baris Monitoring & Report `Helpdesk` adalah penugasan Role Transaksi biasa.
  - Expected c TC-FA-RP-1187 menulis Field `Asset Admin — Data Center` dan `Approver — Data Center` tanpa menyebut jenis transaksi (sub-tab) tempat entri dihitung dan tanpa jumlah entri; spec hanya mengasersi pertambahan jumlah dan isi entri yang disebut TC. Nama Action `Remove (via Group Manager)` mengikuti TC dan menunggu keputusan PM (Open Item #7c).
  - Langkah 2 TC memeriksa `Rack A1` pada sub-tab `Disposal` dan `Transfer`; Expected c menyebut "entri yang sama untuk `Rack A1`" sehingga Field pada langkah 23 memakai pola nama yang sama dengan `Data Center`. TC tidak menulis teks Field `Rack A1` secara eksplisit.
  - Expected b mengasersi Kevin Susanto di Monitoring & Report `Helpdesk` "di luar subtree, non-pola"; TC tidak menyebut cara membedakan baris pola dan non-pola di UI sehingga spec hanya mengasersi kehadiran baris.
  - Post Condition "Kevin Susanto dipulihkan ke state Pre-setup #13 oleh automation baseline" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
