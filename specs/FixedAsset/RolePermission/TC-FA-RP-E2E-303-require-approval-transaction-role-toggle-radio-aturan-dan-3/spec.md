---
id: TC-FA-RP-E2E-303-require-approval-transaction-role-toggle-radio-aturan-dan-3
title: "Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (3/3)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-345
  - TC-FA-RP-347
coverage:
  web: automated
---

# Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Pelaku kedua (penugasan Approver) memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18 (pohon group), #19 (Require Approval OFF di semua node; `IT Infrastructure` OFF dan tidak diubah spec ini), Approver Pandu Wijaya (Pre-setup #19).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: penugasan Approver Pandu Wijaya dan Require Approval sub-tab `Disposal` pada `Rack A1` dan `Data Center`. Hook `after` memulihkan Pre-setup #19 (tanpa penugasan pada `Rack A1` dan `Data Center`, OFF di semua node) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`

### TC-FA-RP-345: Node yang belum pernah dikonfigurasi dibaca OFF dengan aturan OR

2. Tugaskan Approver Pandu Wijaya pada node `Rack A1` sub-tab `Disposal` lewat sesi API hingga tersimpan
3. Klik node `Rack A1` pada Sidebar Group Tree
4. Klik sub-tab `Disposal`
5. Verifikasi toggle `Require Approval for Disposal` OFF dan radio aturan tidak tampil
6. Aktifkan toggle `Require Approval for Disposal`
7. Verifikasi toggle ON dengan `Any approver (OR)` terpilih sebagai default

### TC-FA-RP-347: Require Approval per node, nilai anak tidak diwariskan ke induk

8. Tugaskan Approver Pandu Wijaya pada node `Data Center` sub-tab `Disposal` lewat sesi API hingga tersimpan
9. Klik node `Data Center` pada Sidebar Group Tree
10. Klik sub-tab `Disposal`
11. Aktifkan toggle `Require Approval for Disposal`
12. Klik node `IT Infrastructure` pada Sidebar Group Tree
13. Verifikasi toggle node `IT Infrastructure` tetap pada nilai tersimpannya sendiri, yaitu OFF sesuai Pre-setup #19

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 dan 12 mengulang klik sub-tab dan node agar keadaan tampilan deterministik; TC-FA-RP-345 dan TC-FA-RP-347 menyebut "setelah menugaskan Approver Pandu Wijaya pada node itu" sehingga penugasan dijalankan lewat sesi API (langkah 2 dan 8) dan dipakai sebagai precondition TC, tidak diasersi.
- Pembagian TC lintas spec: TC-FA-RP-337, 343, 344, 346 ada di spec 104; TC-FA-RP-348, 349, 355, 360 ada di spec 105; TC-FA-RP-350 ada di spec 296; TC-FA-RP-354 ada di spec 304.
- Temuan untuk QA:
  - TC-FA-RP-345 dan TC-FA-RP-347 tidak menyebut toast hasil aktivasi toggle (langkah 6 dan 11); tidak diasersi.
  - TC-FA-RP-345 menyebut node `Rack A1` tanpa menyebut bahwa node itu berada beberapa level di bawah root pada Sidebar Group Tree; spec memakai klik node langsung sesuai TC.
