---
id: TC-FA-RP-E2E-390-pola-total-control-dan-read-only-menulis-baris-pola-role-transaksi-tanpa-cek-constraint
title: "Assign Total Control dan Read Only ke user ber-Home Group menulis baris pola Role Transaksi di semua group tanpa memeriksa constraint"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1229
  - TC-FA-RP-1230
coverage:
  web: automated
---

# Assign Total Control dan Read Only ke user ber-Home Group menulis baris pola Role Transaksi di semua group tanpa memeriksa constraint

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Spec ini tidak berganti akun.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #17 (Gunawan Halim, Home Group `Data Center`; Hesti Rahma, Home Group `Logistics Warehouse`), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`; `IT Infrastructure` > `Helpdesk`; `Head Office` > `Logistics Warehouse` > `Dock 1`), #19 (baris pola Role Transaksi pada setiap node dan sub-tab: Asset Admin dan Approver untuk Admin Utama, Siti Rahmawati, dan Rina Wulandari; Monitoring & Report untuk Dewi Anggraini dan Maya Anggraeni), #2 (aktor).
- Seeding precondition TC (hook `before`, dipakai sebagai precondition, tidak diasersi): Gunawan Halim dan Hesti Rahma berstatus Standard (tanpa tingkat akses Total Control, Read Only, maupun Group Manager) dan tanpa penugasan Role Transaksi; Home Group keduanya tetap sesuai Pre-setup #17. Kemampuan seed dan pemulihan Pre-setup #17 adalah fixture backend yang disediakan tim FE/BE, tanpa endpoint karangan.
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: langkah 3 menjadikan Gunawan Halim Total Control (menulis baris pola Asset Admin dan Approver di setiap node dan sub-tab) dan langkah 23 menjadikan Hesti Rahma Read Only (menulis baris pola Monitoring & Report). Hook `after` melepas Total Control Gunawan Halim dan Read Only Hesti Rahma beserta baris pola keduanya, lalu memulihkan Pre-setup #17 lewat fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh. Entri Changelog bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1229: Assign Total Control ke user ber-constraint menulis baris pola Asset Admin dan Approver di semua group

1. Klik `[+ Assign]` di Tab Total Control
2. Ketik Search `Gunawan Halim`, tekan Enter
3. Centang Gunawan Halim lalu klik `[Assign]`
4. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
5. Verifikasi tidak ada pesan error constraint
6. Klik Tab `Transaction Role`, klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
7. Verifikasi baris pola Gunawan Halim tampil di section Asset Admin `Helpdesk`
8. Verifikasi baris pola Gunawan Halim tampil di section Approver `Helpdesk`
9. Verifikasi sedikitnya satu baris lain tampil di section Monitoring & Report `Helpdesk`
10. Verifikasi Gunawan Halim tidak ada di section Monitoring & Report dan Staff `Helpdesk`
11. Klik node `Dock 1` di Sidebar Group Tree
12. Verifikasi baris pola Gunawan Halim tampil di section Asset Admin `Dock 1`
13. Verifikasi baris pola Gunawan Halim tampil di section Approver `Dock 1`
14. Verifikasi sedikitnya satu baris lain tampil di section Monitoring & Report `Dock 1`
15. Verifikasi Gunawan Halim tidak ada di section Monitoring & Report dan Staff `Dock 1`
16. Klik node `Data Center` di Sidebar Group Tree
17. Verifikasi baris pola Gunawan Halim tampil di section Asset Admin `Data Center`
18. Verifikasi baris pola Gunawan Halim tampil di section Approver `Data Center`
19. Verifikasi sedikitnya satu baris lain tampil di section Monitoring & Report `Data Center`
20. Verifikasi Gunawan Halim tidak ada di section Monitoring & Report dan Staff `Data Center`

### TC-FA-RP-1230: Assign Read Only ke user ber-constraint menulis baris pola Monitoring & Report di semua group

21. Klik Tab `Read Only`, lalu klik `[+ Assign]` di Tab Read Only
22. Ketik Search `Hesti Rahma`, tekan Enter
23. Centang Hesti Rahma lalu klik `[Assign]`
24. Verifikasi muncul toast sukses: `Success, Read Only has been assigned.`
25. Verifikasi tidak ada pesan error constraint
26. Klik Tab `Transaction Role`, klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
27. Verifikasi baris pola Hesti Rahma tampil di section Monitoring & Report `Data Center`
28. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin dan di section Approver `Data Center`
29. Verifikasi Hesti Rahma tidak ada di section Asset Admin dan Approver `Data Center`
30. Klik node `Dock 1` di Sidebar Group Tree
31. Verifikasi baris pola Hesti Rahma tampil di section Monitoring & Report `Dock 1`
32. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin dan di section Approver `Dock 1`
33. Verifikasi Hesti Rahma tidak ada di section Asset Admin dan Approver `Dock 1`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 33 langkah, di bawah batas sekitar 35.
- Langkah penghubung (S-03): langkah 6, 11, 16, 21, 26, dan 30 (navigasi Tab, node, dan sub-tab; sub-tab `Disposal` diasumsikan tetap terpilih saat berpindah node, mengikuti TC yang hanya menyebut "klik node"). Langkah 2 dan 22 adalah Search nama kandidat di Table User Picker (R-16, R-22): Search menemukan target pada picker yang dapat memuat lebih dari satu halaman; popup ditutup oleh `[Assign]` sehingga Search tidak perlu dibersihkan.
- Anchor positif absence (bagian 8b butir 2): toast sukses langkah 4 mendahului absence pesan error constraint langkah 5, dan toast langkah 24 mendahului langkah 25. Langkah 9, 14, dan 19 (baris pola Read Only lain tampil di Monitoring & Report) mendahului absence langkah 10, 15, dan 20; langkah 28 dan 32 (baris pola Total Control tampil di Asset Admin dan Approver) mendahului absence langkah 29 dan 33. Presence pada langkah 7, 8, 12, 13, 17, 18, 27, dan 31 membuktikan penulisan baris pola pada node yang sama.
- Tanpa Search pada tabel Role Transaksi: precondition TC hanya memuat Pre-setup #17, #18, dan #19 sehingga tiap section pada `Helpdesk`, `Dock 1`, dan `Data Center` memuat paling banyak lima baris dalam satu halaman.
- Hook `after` melepas penugasan dan baris pola; tidak ada asersi pelepasan di spec ini.
- Temuan untuk QA:
  - NC-20 / Open Item #9 (arah gate constraint Role Transaksi; baris pola dikecualikan dari gate) menunggu PM; bila PM menetapkan lain, Expected TC-FA-RP-1229 dan TC-FA-RP-1230 usang.
  - Email akun login Gunawan Halim dan Hesti Rahma tidak tertulis di Pre-setup #17. Spec ini tidak login sebagai keduanya (aktor Total Control), sehingga `FA_GUNAWAN_PASSWORD` dan `FA_HESTI_PASSWORD` tidak dipakai.
  - Pre-setup #17 tidak menyebut tingkat akses Gunawan Halim dan Hesti Rahma; precondition d kedua TC menyebut Standard tanpa penugasan Role Transaksi, dan spec memakai seeding sesuai precondition itu.
  - TC-FA-RP-1229 Expected a dan TC-FA-RP-1230 Expected a menyebut "tanpa error constraint" tanpa teks error; spec mengasersi tidak ada pesan error constraint di samping toast sukses dan tidak mengutip teks error.
  - Section Staff pada `Helpdesk`, `Dock 1`, dan `Data Center` tidak memuat baris manual maupun pola (Pre-setup #19), sehingga bisa kosong; anchor absence Staff (langkah 10, 15, 20) adalah section Monitoring & Report yang berbaris pada node yang sama, bukan baris di section Staff.
  - TC-FA-RP-1230 tidak menyebut section Staff dalam Expected; spec tidak mengasersinya.
  - Post Condition kedua TC kosong ("-").
