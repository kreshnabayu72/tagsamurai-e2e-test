---
id: TC-FA-RP-E2E-106-approval-scope-sub-tab-transfer-1
title: "Approval Scope sub-tab Transfer (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-356
  - TC-FA-RP-357
  - TC-FA-RP-359
coverage:
  web: automated
---

# Approval Scope sub-tab Transfer (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18 (pohon group), #20 (sub-tab `Transfer` pada `IT Infrastructure`: Require Approval ON dengan Approver Pandu Wijaya, aturan OR, Approval Scope `Both`; `Data Center` Require Approval OFF, Approval Scope `Both`).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: Approval Scope `IT Infrastructure` sub-tab `Transfer` diubah lalu dikembalikan ke `Both` oleh langkah spec; hook `after` memulihkan Pre-setup #20 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`

### TC-FA-RP-356: Approval Scope sub-tab Transfer, default Both, ubah ke Origin only dan Destination only

2. Klik node `IT Infrastructure` pada Sidebar Group Tree
3. Klik sub-tab `Transfer`
4. Verifikasi RadioGroup `Approval scope` tampil dengan tiga opsi `Origin only`, `Destination only`, `Both`
5. Verifikasi `Both` terpilih
6. Pilih `Origin only`
7. Verifikasi toast sukses `Success, approval rule has been updated.`
8. Tutup toast yang tampil
9. Muat ulang halaman
10. Klik Tab `Transaction Role`
11. Klik node `IT Infrastructure` pada Sidebar Group Tree
12. Klik sub-tab `Transfer`
13. Verifikasi `Origin only` tetap terpilih
14. Pilih `Destination only`
15. Verifikasi toast sukses `Success, approval rule has been updated.`
16. Tutup toast yang tampil
17. Pilih `Both`
18. Verifikasi toast sukses `Success, approval rule has been updated.`
19. Verifikasi `Both` terpilih kembali

### TC-FA-RP-357: Approval Scope nilai yang sama, toast netral

20. Tutup toast yang tampil
21. Klik node `IT Infrastructure` pada Sidebar Group Tree
22. Klik sub-tab `Transfer`
23. Pilih opsi `Both` yang sudah terpilih
24. Verifikasi toast netral (Info) `No changes to save.`

### TC-FA-RP-359: Label RadioGroup Approval Scope hanya pada sub-tab Transfer

25. Klik node `IT Infrastructure` pada Sidebar Group Tree
26. Klik sub-tab `Transfer`
27. Verifikasi label RadioGroup `Approval scope` dengan tiga opsi tampil
28. Klik sub-tab `Borrowing & Assignment`
29. Verifikasi sub-tab `Borrowing & Assignment` tidak memuat field Approval scope
30. Klik node `Data Center` pada Sidebar Group Tree (Require Approval Transfer OFF)
31. Klik sub-tab `Transfer`
32. Verifikasi label RadioGroup `Approval scope` dengan tiga opsi tetap tampil walau toggle OFF

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8, 16, dan 20 (menutup toast agar toast identik berikutnya tidak tertukar), langkah 10 sampai 12 (membuka kembali Tab, node, dan sub-tab sesudah muat ulang), langkah 21 sampai 22 dan 25 sampai 26 (navigasi diulang agar keadaan deterministik).
- Pembagian TC lintas spec: klausa "tidak ada entri log baru" pada TC-FA-RP-357 diasersi di spec absence log (spec 291); spec ini mengasersi toast netralnya. Id TC tetap di `sourceTc` spec ini.
- Teks bertanda `copy usulan, PRD 12 #1` (label `Approval scope`, opsi, toast `Success, approval rule has been updated.`) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - TC-FA-RP-356 tidak menyebut Tab, node, dan sub-tab yang dibuka setelah muat ulang; spec menambah langkah 10 sampai 12.
  - TC-FA-RP-359 butir c menyebut node `Data Center` dengan "Require Approval Transfer OFF" tanpa memuat langkah untuk memastikannya; spec memakai nilai Pre-setup #20 dan tidak mengasersi toggle itu.
