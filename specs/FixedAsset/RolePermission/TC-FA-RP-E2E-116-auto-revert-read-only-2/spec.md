---
id: TC-FA-RP-E2E-116-auto-revert-read-only-2
title: "Auto-Revert Read Only (2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-388
  - TC-FA-RP-389
coverage:
  web: automated
---

# Auto-Revert Read Only (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (dirujuk precondition TC), #12 (Maya Anggraeni, Read Only; seluruh Global Role hanya Read; baris Group Role eksplisit `Manage files` Read di `Data Center`), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: pada TC-FA-RP-389 baris Group Role Maya Anggraeni pada `Manage files` `Data Center` dihapus; pada TC-FA-RP-388 baris `Manage Open API` dihapus dan tingkat akses Read Only lepas. Hook `after` memulihkan Pre-setup #12 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage files`

### TC-FA-RP-389: Baris Group Role target Read Only tidak memicu auto-revert, edit dan Remove memakai alur biasa

3. Klik node `Data Center` pada Sidebar Group Tree
4. Centang Delete pada baris Maya Anggraeni
5. Verifikasi toast sukses `Success, permissions have been updated.`
6. Verifikasi dialog auto-revert tidak tampil
7. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`
8. Verifikasi dialog `Remove User` (D-03) tampil dengan `The role assignment, including its permissions, will be removed permanently.`
9. Klik `[Remove]`
10. Verifikasi toast sukses `Success, user has been removed.`
11. Klik Tab `Read Only`
12. Verifikasi Maya Anggraeni tetap ada di Tab `Read Only`

### TC-FA-RP-388: Confirm Remove baris Global Role target Read Only, baris dihapus dan tingkat akses lepas dalam satu transaksi

13. Klik Tab `System`
14. Buka Detail Role `Manage Open API`
15. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`
16. Klik `[Remove]` pada dialog
17. Verifikasi toast sukses `Success, permissions have been updated. Maya Anggraeni is no longer Read Only.`
18. Verifikasi baris Maya Anggraeni pada `Manage Open API` hilang
19. Klik Tab `Read Only`
20. Verifikasi sedikitnya satu baris Read Only lain tampil di Tab `Read Only`
21. Verifikasi Maya Anggraeni tidak ada di Tab `Read Only`
22. Klik Tab `System`
23. Buka Detail Role `Manage accounting`
24. Verifikasi penugasan Global Role lain tidak direset: baris Maya Anggraeni pada `Manage accounting` tetap ada dengan nilai hanya Read

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 389, 388: TC-FA-RP-388 melepas tingkat akses Read Only Maya Anggraeni sehingga diletakkan di akhir (aksi yang menghapus data), sedangkan TC-FA-RP-389 mengasersi Maya Anggraeni masih ada di Tab `Read Only`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): tidak ada. Langkah 20 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 21 (bagian 8b butir 2).
- Post Condition TC-FA-RP-388 (notifikasi in-app ke target) tidak punya langkah observasi di TC ini; tidak diasersi.
- Temuan untuk QA:
  - TC-FA-RP-388 butir c ("Penugasan Global Role lain tidak direset") tidak menyebut Global Role dan nilainya; spec memakai `Manage accounting` dengan nilai hanya Read sesuai Pre-setup #12 (langkah 24).
