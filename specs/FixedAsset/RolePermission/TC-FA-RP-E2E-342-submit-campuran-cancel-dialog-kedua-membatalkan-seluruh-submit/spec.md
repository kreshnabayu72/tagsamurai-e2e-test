---
id: TC-FA-RP-E2E-342-submit-campuran-cancel-dialog-kedua-membatalkan-seluruh-submit
title: "Auto-Revert Role Transaksi: Cancel Dialog Kedua Membatalkan Seluruh Submit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1168
coverage:
  web: automated
---

# Auto-Revert Role Transaksi: Cancel Dialog Kedua Membatalkan Seluruh Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, Total Control; baris pola Asset Admin dan Approver), #18 (pohon group: `IT Infrastructure`), #19 (seed Role Transaksi sub-tab `Disposal`: Nadia Putri di Asset Admin; Nadia Putri dan Rina Wulandari belum ada di Monitoring & Report).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca jumlah entri Changelog sub-tab `Disposal` (langkah 4 dan 27) dan jumlah notifikasi in-app Rina Wulandari lewat sesi API Total Control kedua (Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`; langkah 7 dan 30), disediakan tim FE/BE tanpa endpoint karangan. Jendela absence notifikasi in-app: "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 29), pilihan spec (bukan nilai TC atau PRD).
- State yang diubah dan pemulihannya: spec ini tidak mengubah state (seluruh Submit dibatalkan). Hook `after` memastikan Pre-setup #3 dan #19 tetap pada state awal lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
3. Klik ikon Changelog pada Table Tools
4. Catat jumlah entri Changelog sub-tab `Disposal` sebagai baseline
5. Tutup modal Changelog
6. Catat jumlah pada header section Monitoring & Report sebagai baseline
7. Catat jumlah notifikasi in-app Rina Wulandari sebagai baseline

### TC-FA-RP-1168: Submit campuran, Cancel pada dialog kedua (D-04) membatalkan seluruh Submit termasuk target Standard yang sudah dikonfirmasi pada dialog pertama (D-13)

8. Klik `[+ Assign]` pada section Monitoring & Report
9. Centang Nadia Putri
10. Centang Rina Wulandari
11. Klik `[Assign]`
12. Verifikasi dialog pertama `D-13`: Title `Change Transaction Role`; bullet `• Nadia P (currently Asset Admin)`, `This will change their role for Disposal to Monitoring & Report in IT Infrastructure.`, lalu `Are you sure you want to change it?`; tombol `[Cancel]` dan `[Change]`
13. Verifikasi dialog pertama hanya untuk Nadia Putri (Rina tidak didaftar)
14. Klik `[Change]` pada dialog pertama
15. Verifikasi dialog kedua `D-04` varian Role Transaksi: Title `Remove Total Control`; Body `• Rina W` lalu `This change will remove this user's Total Control access level. Their other role assignments will remain as they are.`, ditutup `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
16. Verifikasi dialog kedua hanya untuk Rina Wulandari (Nadia Putri tidak didaftar)
17. Verifikasi dialog kedua tampil terpisah dan bukan satu dialog gabungan dengan dialog pertama
18. Klik `[Cancel]` pada dialog kedua
19. Verifikasi kedua dialog tertutup
20. Verifikasi tidak ada toast
21. Verifikasi jumlah pada header section Monitoring & Report sama dengan baseline langkah 6 (tidak ada penugasan tersimpan sama sekali)
22. Verifikasi Nadia Putri tetap ada di section Asset Admin
23. Verifikasi sedikitnya satu baris lain tampil di section Monitoring & Report
24. Verifikasi Nadia Putri tidak tampil di section Monitoring & Report
25. Verifikasi baris pola Rina Wulandari di section Asset Admin dan Approver tetap ada
26. Klik ikon Changelog pada Table Tools
27. Verifikasi jumlah entri Changelog sama dengan baseline langkah 4 (tidak ada entri `Remove`, `Assign`, atau `Auto-Revert`)
28. Tutup modal Changelog
29. Tunggu 5 detik tanpa memuat ulang halaman
30. Verifikasi jumlah notifikasi in-app Rina Wulandari sama dengan baseline langkah 7 (tidak ada notifikasi)
31. Klik Tab `Total Control`
32. Verifikasi Rina Wulandari tetap ada di Tab `Total Control`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini memuat 32 langkah.
- Pembagian TC lintas spec: TC-FA-RP-1154 (Cancel pada dialog pertama dan Confirm) ada di spec 326; masing-masing TC tepat satu spec. Spec 326 destruktif (melepas tier Rina) sedangkan spec ini tidak mengubah state.
- Urutan langkah mengikuti state: klausa Expected c (Rina tetap di Tab `Total Control`, langkah 32) ditulis sesudah klausa d (Changelog dan notifikasi, langkah 26 sampai 30) agar Changelog dan baris Role Transaksi dibaca tanpa kembali ke Tab `Transaction Role`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (buka Tab `Transaction Role`), langkah 3, 4, 5, 6, 7, 26, dan 28 (baseline dan penutupan Changelog, baseline header dan notifikasi), langkah 29 (jendela absence notifikasi), langkah 31 (buka Tab `Total Control`). Langkah 23 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 24 (bagian 8b butir 2). Langkah 20 (tidak ada toast) dan langkah 21 memakai dialog kedua langkah 15 sebagai anchor positif.
- S-05 dan P-1: klausa Expected d ("tidak ada entri `Remove`, `Assign`, `Auto-Revert` pada Changelog dan tidak ada notifikasi ke Rina") ditulis sebagai `Verifikasi` selisih terhadap baseline (langkah 27 dan 30), bukan spec absence, karena state dialog berurutan dibangun langkah sebelumnya di spec ini.
- Post Condition TC-FA-RP-1168 (log per penugasan dan `Auto-Revert`, satu notifikasi ke Rina) berlawanan dengan Expected d dan tidak punya langkah observasi sendiri; tidak diasersi.
- Temuan untuk QA:
  - Copy dialog bertanda "copy usulan, perlu persetujuan PM (PRD 12 #1)" di TC sumber; spec memakai teks TC apa adanya. TC-FA-RP-1168 hanya menyebut Title dan tombol dialog pertama; Body dialog pertama pada langkah 12 disalin dari TC-FA-RP-1154 (dialog yang sama).
  - Post Condition TC-FA-RP-1168 ("Log `Remove`/`Assign` per penugasan dan `Auto-Revert` untuk Rina Wulandari; satu notifikasi ke Rina Wulandari") bertentangan dengan Expected d ("tidak ada entri ... dan tidak ada notifikasi"); spec mengikuti Expected d.
  - Asersi absence notifikasi (langkah 30) tidak punya anchor positif pengiriman notifikasi pada alur batal (bagian 6); pembuktian pengiriman notifikasi ada di TC-FA-RP-1164 (spec 336). Asersi dapat lulus semu bila notifikasi tertunda lebih dari jendela 5 detik.
  - TC-FA-RP-1168 Expected d tidak menyebut cara membaca notifikasi Rina; spec memakai kemampuan baca lewat sesi API yang disediakan tim FE/BE.
