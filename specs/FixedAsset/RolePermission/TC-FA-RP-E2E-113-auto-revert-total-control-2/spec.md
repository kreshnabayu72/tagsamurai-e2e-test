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
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, seluruh Global Role CRUD penuh; baris pola Group Role Total Control pada `Manage files` di `Data Center`), #12, #15 (kolam pengguna Standard: Ahmad Fauzi), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca nilai tersimpan baris Group Role (disediakan tim FE/BE tanpa endpoint karangan) untuk langkah 9.
- State yang diubah dan pemulihannya: TC-FA-RP-384 tidak mengubah state (kedua dialog di-Cancel); Ahmad Fauzi diberi CRUD penuh pada `Manage accounting` dan `Manage Open API` lalu dijadikan Total Control lewat sesi API lalu dilepas oleh langkah 35; Rina Wulandari kehilangan Total Control dan baris `Manage Open API` pada TC-FA-RP-383. Hook `after` memulihkan Pre-setup #3 dan #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage files`

### TC-FA-RP-384: Edit CRUD dan Remove baris Group Role target Total Control memicu auto-revert D-04 (bukan edit biasa dan bukan D-03), Cancel tanpa perubahan

3. Klik node `Data Center` pada Sidebar Group Tree
4. Hapus centang Delete pada baris Rina Wulandari
5. Verifikasi dialog severity danger: Title `Remove Total Control`; Body `• Rina W` lalu `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
6. Verifikasi tidak ada toast sukses
7. Klik `[Cancel]`
8. Verifikasi checkbox Delete baris Rina Wulandari kembali tercentang
9. Verifikasi tidak ada perubahan tersimpan pada baris Rina Wulandari lewat kemampuan baca
10. Klik `[⋯]` baris Rina Wulandari lalu `Remove`
11. Verifikasi dialog severity danger: Title `Remove Total Control`; Body `These users will lose Total Control access:` lalu `• Rina W` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
12. Verifikasi dialog `Remove User` (D-03) tidak tampil
13. Klik `[Cancel]`
14. Verifikasi baris Rina Wulandari tetap ada di Detail Role `Manage files` pada `Data Center`
15. Klik Tab `Total Control`
16. Verifikasi Rina Wulandari tetap ada di Tab `Total Control`

### TC-FA-RP-390: Penugasan Standard yang disusun manual menyerupai pola Total Control tidak dipromosikan

17. Klik Tab `System`
18. Buka Detail Role `Manage accounting`
19. Centang Create, Update, dan Delete pada baris Ahmad Fauzi satu per satu
20. Verifikasi toast sukses `Success, permissions have been updated.` tampil setelah tiap centang
21. Verifikasi dialog auto-revert tidak tampil
22. Kembali ke Tab `System`
23. Buka Detail Role `Manage Open API`
24. Centang Create, Update, dan Delete pada baris Ahmad Fauzi satu per satu
25. Verifikasi toast sukses `Success, permissions have been updated.` tampil setelah tiap centang
26. Verifikasi dialog auto-revert tidak tampil
27. Klik Tab `Total Control`
28. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
29. Verifikasi Ahmad Fauzi tidak muncul di Tab `Total Control`

### TC-FA-RP-394: Status target berubah antara render dan submit, Total Control mengikuti status saat submit

30. Klik Tab `System`
31. Buka Detail Role `Manage accounting`
32. Tetapkan Ahmad Fauzi sebagai Total Control lewat sesi API hingga tersimpan
33. Hapus centang Delete pada baris Ahmad Fauzi
34. Verifikasi dialog D-04 muncul karena status saat submit adalah Total Control
35. Klik `[Remove]` pada dialog
36. Verifikasi toast sukses `Success, permissions have been updated. Ahmad Fauzi is no longer Total Control.`

### TC-FA-RP-383: Confirm Remove baris Global Role target Total Control, baris dihapus dan tingkat akses lepas dalam satu transaksi

37. Kembali ke Tab `System`
38. Buka Detail Role `Manage Open API`
39. Klik `[⋯]` baris Rina Wulandari lalu `Remove`
40. Klik `[Remove]` pada dialog
41. Verifikasi toast sukses `Success, permissions have been updated. Rina Wulandari is no longer Total Control.`
42. Verifikasi baris Rina Wulandari pada `Manage Open API` hilang
43. Klik Tab `Total Control`
44. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
45. Verifikasi Rina Wulandari tidak ada di Tab `Total Control`
46. Klik Tab `System`
47. Buka Detail Role `Manage accounting`
48. Verifikasi penugasan Global Role lain tidak direset: baris Rina Wulandari pada `Manage accounting` tetap ada dengan nilai CRUD penuh

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 384, 390, 394, 383: TC-FA-RP-383 melepas Total Control Rina Wulandari sehingga diletakkan di akhir (aksi yang menghapus data), dan TC-FA-RP-384 membutuhkan Rina Wulandari masih Total Control.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 22 dan 37 (kembali ke Tab `System`). Langkah 28 dan 44 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 29 dan 45 (bagian 8b butir 2). Langkah 6 (tidak ada toast sukses) memakai dialog langkah 5 sebagai anchor positif; langkah 12 (D-03 tidak tampil) memakai dialog langkah 11 sebagai anchor positif.
- Pada TC-FA-RP-394 Sesi 2 hanya memicu state dan memakai sesi API (langkah 32, "hingga tersimpan"); langkah TC "Sesi 1 membuka Detail Role dan melihat baris Ahmad Fauzi" terpenuhi oleh langkah 31 dan tidak diasersi.
- Post Condition TC-FA-RP-383 (notifikasi in-app ke target) tidak punya langkah observasi di TC ini; tidak diasersi.
- Alasan di atas sekitar 35 langkah (48 langkah): empat TC satu topik (Auto-Revert Total Control) yang berbagi Detail Role, kolam pengguna, dan target Rina Wulandari dengan urutan yang menentukan keadaan; langkah TC-FA-RP-390 diulang pada dua Global Role. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-390 menyebut "seluruh Global Role Ahmad Fauzi" tanpa daftar; spec memakai `Manage accounting` dan `Manage Open API` (Global Role yang pasti memuat baris Ahmad Fauzi menurut Pre-setup #39). Daftar lengkap perlu klarifikasi.
  - TC-FA-RP-394 membutuhkan Delete pada baris Ahmad Fauzi sudah tercentang; keadaan itu berasal dari langkah 19 (TC-FA-RP-390) dan tidak dinyatakan di precondition TC-FA-RP-394.
  - TC tidak menyebut cara kembali dari Detail Role ke daftar Tab `System`; spec memakai langkah "Kembali ke Tab `System`".
  - TC-FA-RP-384 Expected a ("tidak ada perubahan tersimpan") tidak memberi cara observasi; langkah 9 memakai kemampuan baca state yang disediakan tim FE/BE.
