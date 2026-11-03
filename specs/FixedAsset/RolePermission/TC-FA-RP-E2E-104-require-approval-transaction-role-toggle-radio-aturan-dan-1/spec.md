---
id: TC-FA-RP-E2E-104-require-approval-transaction-role-toggle-radio-aturan-dan-1
title: "Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-337
  - TC-FA-RP-343
  - TC-FA-RP-344
  - TC-FA-RP-346
coverage:
  web: automated
---

# Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (hanya identitas, dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18 (pohon group Company Alpha), #19 (seed Role Transaksi `IT Infrastructure` sub-tab `Disposal`; Require Approval OFF di semua node; Approver Pandu Wijaya hanya pada `IT Infrastructure`).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: Require Approval dan aturan sub-tab `Disposal` pada `IT Infrastructure`. Hook `after` memulihkan Pre-setup #19 (OFF di semua node, aturan OR) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-337: Sub-label toggle Require Approval Transaction Role

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` pada Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Verifikasi sub-label di bawah toggle `Require Approval for Disposal` tampil `Requests of this transaction type must be approved before they proceed. Requests already submitted are not affected.`

### TC-FA-RP-343: Toggle OFF menyembunyikan radio dan nilai aturan tersimpan dipertahankan saat ON kembali

5. Aktifkan toggle `Require Approval for Disposal`
6. Pilih radio `All approvers (AND)`
7. Matikan toggle `Require Approval for Disposal`
8. Verifikasi toast sukses `Success, permissions have been updated.`
9. Verifikasi radio aturan tidak tampil
10. Aktifkan kembali toggle `Require Approval for Disposal`
11. Verifikasi radio aturan tampil kembali dengan `All approvers (AND)` terpilih

### TC-FA-RP-344: Ubah radio aturan OR ke AND dan kembali ke OR

12. Pilih radio `Any approver (OR)`
13. Tutup toast yang tampil
14. Pilih radio `All approvers (AND)`
15. Verifikasi toast sukses `Success, approval rule has been updated.`
16. Tutup toast yang tampil
17. Muat ulang halaman
18. Klik Tab `Transaction Role`
19. Klik node `IT Infrastructure` pada Sidebar Group Tree
20. Klik sub-tab `Disposal`
21. Verifikasi `All approvers (AND)` tetap terpilih
22. Pilih radio `Any approver (OR)`
23. Verifikasi toast sukses `Success, approval rule has been updated.`

### TC-FA-RP-346: Require Approval per node, nilai induk tidak diwariskan ke anak

24. Klik node `IT Infrastructure` pada Sidebar Group Tree
25. Klik sub-tab `Disposal`
26. Klik node `Data Center` pada Sidebar Group Tree
27. Klik sub-tab `Disposal`
28. Verifikasi toggle `Require Approval for Disposal` node `Data Center` OFF

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 337, 343, 344, 346 karena TC-FA-RP-346 membutuhkan toggle `IT Infrastructure` ON yang dibangun langkah 5 sampai 22. TC-FA-RP-345 dan TC-FA-RP-347 ada di spec 303.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 12 (mengembalikan aturan ke OR sebagai precondition TC-FA-RP-344), langkah 13 dan 16 (menutup toast agar toast identik berikutnya tidak tertukar), langkah 17 sampai 20 (membuka kembali Tab, node, dan sub-tab sesudah muat ulang), langkah 24 sampai 25 dan 27 (navigasi TC-FA-RP-346 yang diulang agar keadaan node dan sub-tab deterministik).
- Langkah TC-FA-RP-337 yang menyebut node dan sub-tab dipakai bersama oleh langkah 1 sampai 3.
- Teks sub-label bertanda `copy usulan, PRD 12 #1` (TC-FA-RP-337) diasersi literal sesuai TC dan bergantung pada persetujuan PM; bila copy berubah, TC dan spec ini diperbarui.
- Temuan untuk QA:
  - TC-FA-RP-344 tidak menyebut halaman kembali ke Tab, node, dan sub-tab mana setelah muat ulang; spec menambah langkah 18 sampai 20.
  - TC-FA-RP-346 tidak menyebut apakah sub-tab aktif dipertahankan saat berpindah node; spec menambah klik sub-tab `Disposal` (langkah 25 dan 27).
  - TC-FA-RP-343 tidak menyebut hasil toast saat toggle diaktifkan (langkah 5 dan 10); tidak diasersi.
