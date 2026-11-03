---
id: TC-FA-RP-E2E-107-approval-scope-sub-tab-transfer-2
title: "Approval Scope sub-tab Transfer (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1019
  - TC-FA-RP-1020
  - TC-FA-RP-1021
coverage:
  web: automated
---

# Approval Scope sub-tab Transfer (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18 (pohon group), #20 (sub-tab `Transfer`: `IT Infrastructure` Require Approval ON dengan Approver Pandu Wijaya, aturan OR, Approval Scope `Both`; `Data Center` Require Approval OFF, Approval Scope `Both`).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: Approval Scope `Data Center` (langkah 8 dan 16) dan `IT Infrastructure` (langkah 20 sampai 22) pada sub-tab `Transfer`, serta toggle Require Approval `IT Infrastructure`. Hook `after` memulihkan Pre-setup #20 (toggle ON aturan OR dan Approval Scope `Both` pada `IT Infrastructure`, `Both` pada `Data Center`) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`

### TC-FA-RP-1019: Approval Scope tampil pada node ber-toggle Require Approval OFF

2. Klik node `Data Center` pada Sidebar Group Tree
3. Klik sub-tab `Transfer`
4. Verifikasi toggle `Require Approval for Transfer` OFF
5. Verifikasi radio aturan `Any approver (OR)` dan `All approvers (AND)` tidak tampil
6. Verifikasi RadioGroup berlabel `Approval scope` dengan tiga opsi `Origin only`, `Destination only`, `Both` tampil
7. Verifikasi `Both` terpilih

### TC-FA-RP-1020: Approval Scope pada node ber-toggle OFF disimpan dan dipertahankan setelah muat ulang

8. Pilih `Destination only`
9. Verifikasi toast sukses `Success, approval rule has been updated.`
10. Muat ulang halaman
11. Klik Tab `Transaction Role`
12. Klik node `Data Center` pada Sidebar Group Tree
13. Klik sub-tab `Transfer`
14. Verifikasi toggle `Require Approval for Transfer` tetap OFF
15. Verifikasi `Destination only` tetap terpilih
16. Pilih `Both` (pemulihan Post Condition TC: Approval Scope `Data Center` dikembalikan ke `Both`)
17. Tutup toast yang tampil

### TC-FA-RP-1021: Approval Scope dimiliki per node group

18. Klik node `IT Infrastructure` pada Sidebar Group Tree
19. Klik sub-tab `Transfer`
20. Pilih `Origin only`
21. Verifikasi toast sukses `Success, approval rule has been updated.`
22. Matikan toggle `Require Approval for Transfer`
23. Verifikasi toggle `Require Approval for Transfer` OFF
24. Verifikasi radio aturan tidak tampil
25. Verifikasi RadioGroup `Approval scope` tetap tampil dengan `Origin only` terpilih
26. Klik node `Data Center` pada Sidebar Group Tree
27. Klik sub-tab `Transfer`
28. Verifikasi `Both` terpilih (nilai `IT Infrastructure` tidak diwarisi)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 11 sampai 13 (membuka kembali Tab, node, dan sub-tab sesudah muat ulang), langkah 16 dan 17 (pemulihan Approval Scope `Data Center` ke `Both` sebelum TC berikutnya mengandalkannya, S-09, dan menutup toast).
- Post Condition TC-FA-RP-1021 ("Toggle `IT Infrastructure` dikembalikan ON dan Approval Scope ke `Both`") tidak punya langkah observasi sehingga tidak diasersi; pemulihan dilakukan hook `after`.
- Teks bertanda `copy usulan, PRD 12 #1` (label, opsi, dan toast) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - TC-FA-RP-1020 tidak menyebut Tab, node, dan sub-tab setelah muat ulang; spec menambah langkah 11 sampai 13 (sama dengan perilaku yang dicatat pada spec 106).
  - TC-FA-RP-1021 butir b menulis "radio aturan tidak tampil" dan "RadioGroup tetap tampil" dalam satu butir; spec memecahnya menjadi langkah 24 dan 25.
