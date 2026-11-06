---
id: TC-FA-RP-E2E-365-auto-revert-gm-lewat-remove-baris-approver-pola-descendant
title: "Remove baris Approver pola GM pada node descendant: dialog auto-revert D-05 varian Role Transaksi, Cancel tanpa perubahan, Confirm melepas GM"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1192
coverage:
  web: automated
---

# Remove baris Approver pola GM pada node descendant: dialog auto-revert D-05 varian Role Transaksi, Cancel tanpa perubahan, Confirm melepas GM

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager hanya di `Data Center`; baris pola GM Asset Admin dan Approver pada tiap Jenis Transaksi di `Data Center` dan `Rack A1`), #18 (pohon Group; `Rack A1` adalah descendant `Data Center`), #19 (seed Role Transaksi sub-tab `Disposal`; hitungan baris berlaku tanpa seed GM, sehingga baris Kevin Susanto menambah satu baris Asset Admin dan satu baris Approver), #24 (`Company Changelog`; dipakai sebagai latar log, tidak diasersi).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri Changelog sub-tab `Disposal` dan jumlah entri ber-Action `Remove (via Group Manager)` di dalamnya sebagai baseline (langkah 1 dan 2).
- State yang diubah dan pemulihannya: penugasan Group Manager Kevin Susanto di `Data Center` dilepas dan baris Approver `Rack A1` dihapus oleh langkah 15 (baris pola GM lainnya dipertahankan sebagai penugasan biasa). Hook `before` memastikan state Pre-setup #13 dan hook `after` memulihkannya (Group Manager `Data Center` beserta baris pola) lewat fixture backend yang disediakan tim FE/BE, tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1192: Remove baris Approver pola GM pada node descendant, dialog auto-revert D-05 varian Role Transaksi

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Transaction Role sub-tab `Disposal`
2. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri ber-Action `Remove (via Group Manager)` pada Changelog Transaction Role sub-tab `Disposal`
3. Klik Tab `Transaction Role`
4. Klik node `Rack A1` pada Sidebar Group Tree
5. Klik sub-tab `Disposal`
6. Klik `[⋯]` pada baris Kevin Susanto di section Approver lalu `Remove`
7. Verifikasi dialog severity danger: Title `Remove Group Manager`, Body `• Kevin S` lalu `This change will remove Group Manager status for this group.` lalu `Their other role assignments will remain as they are.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]` (copy usulan, PRD 12 #7)
8. Verifikasi dialog `D-08` (`Remove Approver`) tidak tampil
9. Klik `[Cancel]`
10. Verifikasi dialog tertutup
11. Verifikasi baris Kevin Susanto tetap ada di section Approver
12. Verifikasi tidak ada toast
13. Verifikasi jumlah entri Changelog sub-tab `Disposal` sama dengan baseline langkah 1 (tanpa entri log baru)
14. Klik `[⋯]` pada baris Kevin Susanto di section Approver lalu `Remove`
15. Klik `[Remove]` pada dialog
16. Verifikasi toast sukses `Success, Approver has been removed. Kevin Susanto is no longer Group Manager for Data Center.` (copy usulan, PRD 12 #7)
17. Verifikasi sedikitnya satu baris lain tampil di section Approver pada node `Rack A1`
18. Verifikasi tidak ada baris Kevin Susanto di section Approver pada node `Rack A1` (baris yang di-Remove terhapus oleh aksi pemicu)
19. Verifikasi baris Kevin Susanto tetap tampil di section Asset Admin pada node `Rack A1` (baris pola dipertahankan)
20. Klik node `Data Center` pada Sidebar Group Tree
21. Verifikasi baris Kevin Susanto tetap tampil di section Asset Admin pada node `Data Center` (baris pola dipertahankan)
22. Verifikasi baris Kevin Susanto tetap tampil di section Approver pada node `Data Center` (baris pola dipertahankan)
23. Klik ikon Changelog sub-tab `Disposal`
24. Verifikasi jumlah entri Changelog bertambah dari baseline langkah 1 (aksi pemicu tercatat)
25. Verifikasi jumlah entri ber-Action `Remove (via Group Manager)` sama dengan baseline langkah 2
26. Tutup modal Changelog
27. Klik Tab `Group Manager`
28. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
29. Verifikasi Kevin Susanto tidak ada di Tab `Group Manager`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 29 langkah.
- Langkah penghubung (S-03): langkah 1 dan 2 (baseline Changelog, S-12), langkah 3 sampai 5, 20, 23, 26, dan 27 (navigasi Tab, node, sub-tab, membuka dan menutup modal Changelog). Tanpa Search: section Asset Admin dan Approver pada `Rack A1` dan `Data Center` sub-tab `Disposal` memuat baris pola dan baris Kevin Susanto, dalam satu halaman (R-16). Langkah 17 dan 28 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 18 dan 29 (bagian 8b butir 2); langkah 7 menjadi anchor atas langkah 8, dan langkah 10 sampai 11 atas langkah 12; langkah 24 menjadi anchor positif atas asersi langkah 25.
- Urutan langkah mengikuti keadaan: section pada `Rack A1` dan `Data Center` dibaca selagi sub-tab `Disposal` masih terbuka, lalu Changelog, lalu Tab `Group Manager`.
- Langkah 13 adalah asersi jumlah entri terhadap baseline (bukan kelas g): TC menyebut "tanpa entri log" untuk Cancel tanpa menyebut surface; spec memakai Changelog sub-tab `Disposal`. Langkah 25 juga asersi jumlah entri terhadap baseline (S-12), bukan kelas g (S-05, P-1): state auto-revert dibangun spec ini sendiri pada langkah 14 dan 15.
- Pembagian TC lintas spec: TC-FA-RP-1189 (varian edit CRUD pada Detail Role) ada di spec 354.
- Fix pass 4 (keputusan: auto-revert GM mempertahankan baris): hanya baris Approver yang di-Remove terhapus; baris Asset Admin `Rack A1` serta Asset Admin dan Approver `Data Center` tetap ada, tanpa entri `Remove (via Group Manager)`.
- Temuan untuk QA:
  - TC-FA-RP-1192 menandai copy dialog D-05 dan toast sebagai `copy usulan, PRD 12 #7`; spec menulis teks TC apa adanya.
  - TC-FA-RP-1192 Expected d tidak menyebut apakah aksi pemicu (Remove baris Approver) tercatat di Changelog; langkah 24 mengasumsikan tercatat sebagai anchor positif atas langkah 25. Bila PM menetapkan lain, anchor perlu diganti.
  - Interpretasi "baris Approver yang di-Remove oleh aksi pemicu tetap terhapus" (bukan dikembalikan) menunggu konfirmasi PM.
  - Expected b menyebut "tanpa entri log" tanpa menyebut surface log; spec memakai Changelog sub-tab `Disposal`.
  - Expected d menyebut baris pola GM hanya di `Rack A1` dan `Data Center` untuk Asset Admin dan Approver; sub-tab Jenis Transaksi lain dan baris pola Group Role tidak ditelusuri karena tidak disebut TC.
  - Seed Kevin Susanto tidak konsisten antar sumber: Pre-setup #13 dan #43 hanya `Data Center`, Pre-setup #38 dan beberapa TC lain `Data Center` dan `Helpdesk`. Spec mengikuti #13.
  - Post Condition "Kevin Susanto dipulihkan ke state Pre-setup #13" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
