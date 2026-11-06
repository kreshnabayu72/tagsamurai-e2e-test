---
id: TC-FA-RP-E2E-356-assign-staff-ke-gm-turun-tangga-dialog-d05-varian-role-transaksi
title: "Assign Staff (turun tangga) ke target Group Manager pada node di subtree GM-nya: satu dialog auto-revert D-05 varian Role Transaksi, D-13 tidak tampil, Staff dipertahankan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1191
coverage:
  web: automated
---

# Assign Staff (turun tangga) ke target Group Manager pada node di subtree GM-nya: satu dialog auto-revert D-05 varian Role Transaksi, D-13 tidak tampil, Staff dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager hanya di `Data Center`; memegang baris pola Asset Admin dan Approver pada sub-tab `Disposal` di `Data Center` dan `Rack A1`), #18 (pohon Group), #19 (seed Role Transaksi sub-tab `Disposal`; hitungan baris berlaku tanpa seed GM, sehingga baris Kevin Susanto menambah satu baris Asset Admin dan satu baris Approver per node), #24 (`Company Changelog`; dipakai sebagai latar log, tidak diasersi).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri Changelog Transaction Role sub-tab `Disposal` dan jumlah entri ber-Action `Remove (via Group Manager)` di dalamnya sebagai baseline (langkah 1 dan 2).
- State yang diubah dan pemulihannya: penugasan Group Manager Kevin Susanto di `Data Center` dilepas oleh langkah 25 (baris pola GM dipertahankan sebagai penugasan biasa, kecuali baris Asset Admin `Data Center` yang digantikan Staff oleh aksi pemicu), dan Kevin Susanto ditetapkan Staff `Disposal` di `Data Center`. Hook `before` memastikan state Pre-setup #13 dan hook `after` memulihkannya (Group Manager `Data Center` beserta baris pola termasuk Asset Admin `Data Center`, tanpa penugasan Staff) lewat fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh (TC: "dipulihkan ke state Pre-setup #13 oleh automation baseline"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1191: Assign Staff ke target Group Manager pada node di subtree GM-nya, satu dialog auto-revert D-05 varian Role Transaksi

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Transaction Role sub-tab `Disposal`
2. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri ber-Action `Remove (via Group Manager)` pada Changelog Transaction Role sub-tab `Disposal`
3. Klik Tab `Transaction Role`
4. Klik node `Data Center` pada Sidebar Group Tree
5. Klik sub-tab `Disposal`
6. Klik `[+ Assign]` pada section Staff
7. Ketik Search `Kevin Susanto`, tekan Enter
8. Centang Kevin Susanto
9. Klik `[Assign]`
10. Verifikasi dialog severity danger: Title `Remove Group Manager`, Body `• Kevin S` lalu `This change will remove Group Manager status for this group.` lalu `Their other role assignments will remain as they are.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]` (copy usulan, PRD 12 #7)
11. Verifikasi dialog tidak memuat bullet `(currently ...)` dan tidak memuat kalimat `This will change their role for ...` (D-13 tidak tampil)
12. Klik `[Cancel]`
13. Verifikasi tidak ada toast
14. Verifikasi Kevin Susanto tetap tampil di section Asset Admin dan Approver pada `Data Center` sub-tab `Disposal`
15. Verifikasi Kevin Susanto tidak tampil di section Staff (tidak ada penugasan tersimpan)
16. Klik Tab `Group Manager`
17. Verifikasi Kevin Susanto tetap tampil di Tab `Group Manager`
18. Klik Tab `Transaction Role`
19. Klik node `Data Center` pada Sidebar Group Tree
20. Klik sub-tab `Disposal`
21. Klik `[+ Assign]` pada section Staff
22. Ketik Search `Kevin Susanto`, tekan Enter
23. Centang Kevin Susanto
24. Klik `[Assign]`
25. Klik `[Remove]` pada dialog
26. Verifikasi toast sukses `Success, Staff has been assigned. Kevin Susanto is no longer Group Manager for Data Center.` (copy usulan, PRD 12 #7)
27. Verifikasi Kevin Susanto tampil di section Staff pada `Data Center` sub-tab `Disposal` (penugasan hasil Assign pemicu non-pola dipertahankan)
28. Verifikasi sedikitnya satu baris lain tampil di section Asset Admin pada `Data Center`
29. Verifikasi Kevin Susanto tidak lagi tampil di section Asset Admin pada `Data Center` (digantikan Staff oleh aksi pemicu, `FARP-LOGIC-18d`)
30. Verifikasi baris Approver Kevin Susanto tetap tampil di section Approver pada `Data Center` (baris pola dipertahankan)
31. Klik ikon Changelog sub-tab `Disposal`
32. Verifikasi jumlah entri Changelog bertambah dari baseline langkah 1
33. Verifikasi entri `Assign` Field `Staff — Data Center` dengan New Value `Kevin Susanto` tampil pada entri teratas sebanyak selisih
34. Verifikasi jumlah entri ber-Action `Remove (via Group Manager)` sama dengan baseline langkah 2
35. Tutup modal Changelog
36. Klik node `Rack A1` pada Sidebar Group Tree
37. Verifikasi Kevin Susanto tetap tampil di section Asset Admin pada `Rack A1` (baris pola dipertahankan)
38. Verifikasi Kevin Susanto tetap tampil di section Approver pada `Rack A1` (baris pola dipertahankan)
39. Klik Tab `Group Manager`
40. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
41. Verifikasi Kevin Susanto tidak ada di Tab `Group Manager`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 41 langkah.
- Alasan di atas sekitar 35 langkah (41 langkah): satu TC, satu alur Assign Staff dengan dua jalur (Cancel lalu Confirm) pada state Group Manager yang sama, kelas fungsional yang sama; Cancel yang membocorkan penugasan membuat jalur Confirm kehilangan makna, sehingga jalur tidak dipisah. Dua langkah baseline dan pembacaan dua node menyumbang tambahan.
- Langkah penghubung (S-03): langkah 1 dan 2 (baseline Changelog, S-12), langkah 3 sampai 6, 16, 18 sampai 21, 31, 36, dan 39 (navigasi Tab, node, sub-tab, dan pembukaan popup), langkah 7, 22 (Search kandidat `Kevin Susanto` pada popup Assign, R-16 dan R-23), langkah 35 (menutup modal Changelog). Tanpa Search pada section role di halaman Transaction Role: tiap section memuat paling banyak sepuluh baris, dalam satu halaman. Langkah 28 dan 40 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 29 dan 41 (bagian 8b butir 2). Anchor positif atas asersi D-13 tidak tampil (langkah 11) adalah langkah 10 (dialog D-05 tampil); anchor atas langkah 15 adalah langkah 14; langkah 32 dan 33 adalah anchor positif atas asersi langkah 34.
- Pembacaan Changelog langkah 32 sampai 34 memakai selisih jumlah entri terhadap baseline langkah 1 dan 2 (S-12); entri baru dibaca pada baris teratas urutan default Date terbaru sebanyak selisih tanpa mengasersi urutan di antaranya (S-14). Tidak ada asersi total entri. Langkah 34 bukan asersi kelas g (S-05, P-1): state auto-revert dibangun spec ini sendiri pada langkah 24 dan 25.
- Pembagian TC lintas spec: TC-FA-RP-1193 (submit campuran tiga dialog) ada di spec 366.
- Fix pass 4 (keputusan: auto-revert GM mempertahankan baris): hanya baris Asset Admin Kevin Susanto di `Data Center` yang digantikan Staff oleh aksi pemicu; baris Approver `Data Center` dan baris Asset Admin dan Approver `Rack A1` dipertahankan, tanpa entri `Remove (via Group Manager)`.
- Temuan untuk QA:
  - TC-FA-RP-1191 menandai copy dialog D-05 dan toast sebagai `copy usulan, PRD 12 #7`; spec menulis teks TC apa adanya.
  - Action entri penggantian baris Asset Admin oleh aksi pemicu tidak ditetapkan PRD (Gap Spec butir 6). TC menyatakan tidak ada entri `Remove (via Group Manager)` untuk baris pola mana pun; bila implementasi mencatat penggantian itu dengan Action tersebut, langkah 34 gagal dan perlu diselaraskan oleh PM.
  - Expected d menyebut "seluruh baris pola GM lain di `Data Center` dan `Rack A1`" tanpa merinci sub-tab Jenis Transaksi lain dan Group Role; spec menelusuri Asset Admin dan Approver sub-tab `Disposal` pada kedua node serta Tab `Group Manager`.
  - Seed Kevin Susanto tidak konsisten antar sumber: Pre-setup #13 dan #43 hanya `Data Center`, Pre-setup #38 dan beberapa TC lain `Data Center` dan `Helpdesk`. Spec mengikuti #13.
  - Post Condition "Kevin Susanto dipulihkan ke state Pre-setup #13" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
