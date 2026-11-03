---
id: TC-FA-RP-E2E-113-auto-revert-total-control-2
title: "Auto-Revert Total Control (2/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-383
  - TC-FA-RP-384
  - TC-FA-RP-390
  - TC-FA-RP-394
coverage:
  web: automated
---

# Auto-Revert Total Control (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Pelaku kedua pada TC-FA-RP-394 hanya memicu perubahan state dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, seluruh Global Role CRUD penuh; baris Group Role eksplisit `Manage files` Read di `Data Center`), #12, #15 (kolam pengguna Standard: Ahmad Fauzi), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: baris Group Role Rina Wulandari pada `Manage files` `Data Center` dihapus (TC-FA-RP-384); Ahmad Fauzi diberi CRUD penuh pada `Manage accounting` dan `Manage Open API` lalu dijadikan Total Control lewat sesi API lalu dilepas oleh langkah 31; Rina Wulandari kehilangan Total Control dan baris `Manage Open API` pada TC-FA-RP-383. Hook `after` memulihkan Pre-setup #3 dan #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage files`

### TC-FA-RP-384: Baris Group Role target Total Control tidak memicu auto-revert, edit dan Remove memakai alur biasa

3. Klik node `Data Center` pada Sidebar Group Tree
4. Centang Delete pada baris Rina Wulandari
5. Verifikasi toast sukses `Success, permissions have been updated.`
6. Verifikasi dialog auto-revert tidak tampil
7. Klik `[⋯]` baris Rina Wulandari lalu `Remove`
8. Verifikasi dialog `Remove User` (D-03) tampil dengan `The role assignment, including its permissions, will be removed permanently.`
9. Klik `[Remove]`
10. Verifikasi toast sukses `Success, user has been removed.`
11. Klik Tab `Total Control`
12. Verifikasi Rina Wulandari tetap ada di Tab `Total Control`

### TC-FA-RP-390: Penugasan Standard yang disusun manual menyerupai pola Total Control tidak dipromosikan

13. Klik Tab `System`
14. Buka Detail Role `Manage accounting`
15. Centang Create, Update, dan Delete pada baris Ahmad Fauzi satu per satu
16. Verifikasi toast sukses `Success, permissions have been updated.` tampil setelah tiap centang
17. Verifikasi dialog auto-revert tidak tampil
18. Kembali ke Tab `System`
19. Buka Detail Role `Manage Open API`
20. Centang Create, Update, dan Delete pada baris Ahmad Fauzi satu per satu
21. Verifikasi toast sukses `Success, permissions have been updated.` tampil setelah tiap centang
22. Verifikasi dialog auto-revert tidak tampil
23. Klik Tab `Total Control`
24. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
25. Verifikasi Ahmad Fauzi tidak muncul di Tab `Total Control`

### TC-FA-RP-394: Status target berubah antara render dan submit, Total Control mengikuti status saat submit

26. Klik Tab `System`
27. Buka Detail Role `Manage accounting`
28. Tetapkan Ahmad Fauzi sebagai Total Control lewat sesi API hingga tersimpan
29. Hapus centang Delete pada baris Ahmad Fauzi
30. Verifikasi dialog D-04 muncul karena status saat submit adalah Total Control
31. Klik `[Remove]` pada dialog
32. Verifikasi toast sukses `Success, permissions have been updated. Ahmad Fauzi is no longer Total Control.`

### TC-FA-RP-383: Confirm Remove baris Global Role target Total Control, baris dihapus dan tingkat akses lepas dalam satu transaksi

33. Kembali ke Tab `System`
34. Buka Detail Role `Manage Open API`
35. Klik `[⋯]` baris Rina Wulandari lalu `Remove`
36. Klik `[Remove]` pada dialog
37. Verifikasi toast sukses `Success, permissions have been updated. Rina Wulandari is no longer Total Control.`
38. Verifikasi baris Rina Wulandari pada `Manage Open API` hilang
39. Klik Tab `Total Control`
40. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
41. Verifikasi Rina Wulandari tidak ada di Tab `Total Control`
42. Klik Tab `System`
43. Buka Detail Role `Manage accounting`
44. Verifikasi penugasan Global Role lain tidak direset: baris Rina Wulandari pada `Manage accounting` tetap ada dengan nilai CRUD penuh

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 384, 390, 394, 383: TC-FA-RP-383 melepas Total Control Rina Wulandari sehingga diletakkan di akhir (aksi yang menghapus data), dan TC-FA-RP-384 membutuhkan Rina Wulandari masih Total Control.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 18 dan 33 (kembali ke Tab `System`). Langkah 24 dan 40 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 25 dan 41 (bagian 8b butir 2).
- Pada TC-FA-RP-394 Sesi 2 hanya memicu state dan memakai sesi API (langkah 28, "hingga tersimpan"); langkah TC "Sesi 1 membuka Detail Role dan melihat baris Ahmad Fauzi" terpenuhi oleh langkah 27 dan tidak diasersi.
- Post Condition TC-FA-RP-383 (notifikasi in-app ke target) tidak punya langkah observasi di TC ini; tidak diasersi.
- Alasan di atas sekitar 35 langkah (44 langkah): empat TC satu topik (Auto-Revert Total Control) yang berbagi Detail Role, kolam pengguna, dan target Rina Wulandari dengan urutan yang menentukan keadaan; langkah TC-FA-RP-390 diulang pada dua Global Role. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-390 menyebut "seluruh Global Role Ahmad Fauzi" tanpa daftar; spec memakai `Manage accounting` dan `Manage Open API` (Global Role yang pasti memuat baris Ahmad Fauzi menurut Pre-setup #39). Daftar lengkap perlu klarifikasi.
  - TC-FA-RP-394 membutuhkan Delete pada baris Ahmad Fauzi sudah tercentang; keadaan itu berasal dari langkah 15 (TC-FA-RP-390) dan tidak dinyatakan di precondition TC-FA-RP-394.
  - TC tidak menyebut cara kembali dari Detail Role ke daftar Tab `System`; spec memakai langkah "Kembali ke Tab `System`".
