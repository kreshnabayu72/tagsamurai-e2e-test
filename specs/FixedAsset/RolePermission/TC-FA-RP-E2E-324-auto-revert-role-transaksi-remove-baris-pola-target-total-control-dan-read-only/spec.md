---
id: TC-FA-RP-E2E-324-auto-revert-role-transaksi-remove-baris-pola-target-total-control-dan-read-only
title: "Auto-Revert Role Transaksi: Remove Baris Pola Target Total Control"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1151
coverage:
  web: automated
---

# Auto-Revert Role Transaksi: Remove Baris Pola Target Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, Total Control; baris pola Transaction Role Asset Admin dan Approver pada setiap Jenis Transaksi x Group; seluruh Global Role CRUD penuh), #18 (pohon group: `IT Infrastructure` dan `Data Center`), #19 (seed Role Transaksi sub-tab `Disposal`).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca jumlah entri Changelog sub-tab `Disposal` (disediakan tim FE/BE bila total tidak tampil di modal, tanpa endpoint karangan) untuk langkah 4 dan 14.
- State yang diubah dan pemulihannya: pada langkah 21 baris Approver pola Rina Wulandari di `IT Infrastructure` sub-tab `Disposal` dihapus dan tingkat akses Total Control Rina lepas; Changelog bertambah entri `Remove` dan `Auto-Revert` (audit trail permanen, tidak dipulihkan). Hook `after` memulihkan Pre-setup #3 (tier Total Control dan baris pola) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
3. Klik ikon Changelog pada Table Tools
4. Catat jumlah entri Changelog sub-tab `Disposal` sebagai baseline
5. Tutup modal Changelog

### TC-FA-RP-1151: Remove baris pola milik target Total Control oleh Total Control, satu dialog auto-revert D-04 varian Role Transaksi, Cancel tanpa perubahan, Confirm melepas tier tanpa reset penugasan lain

6. Klik `[⋯]` pada baris Rina Wulandari di section Approver lalu `Remove`
7. Verifikasi dialog severity danger: Title `Remove Total Control`; Body `• Rina W` lalu `This change will remove this user's Total Control access level. Their other role assignments will remain as they are.`, ditutup `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
8. Verifikasi dialog `D-08` tidak tampil
9. Klik `[Cancel]`
10. Verifikasi dialog tertutup
11. Verifikasi tidak ada toast
12. Verifikasi baris Approver Rina Wulandari tetap ada
13. Klik ikon Changelog pada Table Tools
14. Verifikasi jumlah entri Changelog sama dengan baseline langkah 4 (tanpa entri log)
15. Tutup modal Changelog
16. Klik Tab `Total Control`
17. Verifikasi Rina Wulandari tetap ada di Tab `Total Control`
18. Klik Tab `Transaction Role`
19. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
20. Klik `[⋯]` pada baris Rina Wulandari di section Approver lalu `Remove`
21. Klik `[Remove]` pada dialog
22. Verifikasi toast sukses `Success, Approver has been removed. Rina Wulandari is no longer Total Control.`
23. Verifikasi baris Approver Rina Wulandari pada node itu hilang
24. Verifikasi baris Asset Admin Rina Wulandari pada node itu tetap ada
25. Klik node `Data Center` lalu sub-tab `Disposal`
26. Verifikasi seluruh baris Rina Wulandari pada node `Data Center` (section Asset Admin dan Approver) tetap ada
27. Klik Tab `Total Control`
28. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
29. Verifikasi Rina Wulandari tidak ada di Tab `Total Control`
30. Klik Tab `System`
31. Buka Detail Role `Manage accounting`
32. Verifikasi Global Role Rina Wulandari tidak direset: baris Rina Wulandari pada `Manage accounting` tetap ada dengan nilai CRUD penuh

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini memuat 32 langkah.
- Pembagian TC lintas spec: TC-FA-RP-1165 (Remove baris pola target Read Only) ada di spec 341; masing-masing TC tepat satu spec.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 18 (buka Tab `Transaction Role`), langkah 3, 4, 5, 13, dan 15 (baseline dan penutupan Changelog), langkah 16 dan 27 (buka Tab `Total Control`), langkah 30 dan 31 (buka Detail Role). Langkah 28 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 29 (bagian 8b butir 2). Langkah 11 (tidak ada toast) memakai dialog langkah 7 sebagai anchor positif; langkah 8 (D-08 tidak tampil) memakai dialog langkah 7 sebagai anchor positif.
- S-05 dan P-1: klausa Expected "tanpa entri log" setelah `[Cancel]` ditulis sebagai `Verifikasi` selisih jumlah entri Changelog terhadap baseline (langkah 14), bukan spec absence terpisah, karena state (dialog auto-revert dan tier Total Control Rina) dibangun langkah sebelumnya di spec ini.
- Post Condition TC-FA-RP-1151 (log `Remove` dan `Auto-Revert` bermodifier admin pengedit, notifikasi in-app ke Rina Wulandari) tidak punya langkah observasi di TC ini; tidak diasersi (dirujuk TC sumber ke TC-FA-RP-1163 dan TC-FA-RP-1164).
- Temuan untuk QA:
  - Copy dialog dan toast bertanda "copy usulan, perlu persetujuan PM (PRD 12 #1)" di TC sumber; spec memakai teks TC apa adanya dan perlu diperbarui bila PM mengubah copy.
  - TC-FA-RP-1151 Expected d menyebut "seluruh baris pada node `Data Center`" tanpa sub-tab; spec memakai sub-tab `Disposal` (langkah 25).
  - TC-FA-RP-1151 Expected d menyebut "Global Role Rina tidak direset" tanpa menyebut Global Role dan nilainya; spec memakai `Manage accounting` dengan CRUD penuh sesuai Pre-setup #3 (langkah 32).
  - TC-FA-RP-1151 Expected b ("tanpa entri log") tidak menyebut cara membaca log; spec memakai baseline jumlah entri Changelog dan mengandalkan kemampuan baca bila total tidak tampil di modal.
  - Slug id spec memuat "read-only", tetapi isi spec ini hanya target Total Control; TC target Read Only ada di spec 341.
