---
id: TC-FA-RP-E2E-117-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-1
title: "Auto-Revert Group Manager dan pola subset baris eksplisit (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-395
  - TC-FA-RP-396
  - TC-FA-RP-397
  - TC-FA-RP-398
coverage:
  web: automated
---

# Auto-Revert Group Manager dan pola subset baris eksplisit (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager di `Data Center`; Group Role eksplisit seluruh capability CRUD penuh di `Data Center`; Group Role `Manage files` Read dan Delete di `Helpdesk`; Global Role `Manage accounting` hanya Read), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca nilai tersimpan baris Detail Role (disediakan tim FE/BE tanpa endpoint karangan); menetapkan kembali Group Manager dan baris Group Role eksplisit lewat sesi API (langkah 28).
- State yang diubah dan pemulihannya: penugasan Group Manager Kevin Susanto di `Data Center` dilepas oleh langkah 25 dan ditetapkan kembali oleh langkah 31 lalu dilepas lagi oleh langkah 37; nilai Update pada `Manage files` `Helpdesk` dan Create pada `Manage accounting` diubah oleh TC-FA-RP-398. Hook `after` memulihkan Pre-setup #13 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Buka Detail Role `Manage group` dari Tab `System`
2. Klik node `Data Center` pada Sidebar Group Tree

### TC-FA-RP-395: Edit CRUD baris Group Role target Group Manager di node GM-nya, dialog D-05 dan Cancel

3. Hapus centang Delete pada baris Kevin Susanto
4. Verifikasi dialog severity danger dengan Title `Remove Group Manager`, Body `• Kevin S` lalu `This edit will remove Group Manager status for this group. Their role permissions in this group will remain as edited.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
5. Klik `[Cancel]`
6. Verifikasi checkbox Delete baris Kevin Susanto kembali tercentang
7. Verifikasi tidak ada perubahan tersimpan pada Delete baris Kevin Susanto lewat kemampuan baca

### TC-FA-RP-398: Edit baris Group Role di node lain atau Global Role target Group Manager tidak terkunci dan tidak memicu auto-revert

8. Kembali ke Tab `System`
9. Buka Detail Role `Manage files`
10. Klik node `Helpdesk` pada Sidebar Group Tree
11. Centang Update pada baris Kevin Susanto
12. Verifikasi toast sukses `Success, permissions have been updated.`
13. Verifikasi dialog auto-revert tidak tampil
14. Kembali ke Tab `System`
15. Buka Detail Role `Manage accounting`
16. Centang Create pada baris Kevin Susanto
17. Verifikasi toast sukses `Success, permissions have been updated.`
18. Verifikasi dialog auto-revert tidak tampil
19. Klik Tab `Group Manager`
20. Verifikasi baris Kevin Susanto di `Data Center` tetap ada di Tab `Group Manager`

### TC-FA-RP-396: Confirm auto-revert Group Manager lewat edit CRUD, GM di node itu lepas dan editan dipertahankan

21. Kembali ke Tab `System`
22. Buka Detail Role `Manage group`
23. Klik node `Data Center` pada Sidebar Group Tree
24. Hapus centang Delete pada baris Kevin Susanto
25. Klik `[Remove]` pada dialog
26. Verifikasi toast sukses `Success, permissions have been updated. Kevin Susanto is no longer Group Manager for Data Center.`
27. Verifikasi checkbox Delete baris Kevin Susanto di `Manage group` `Data Center` tidak tercentang sesuai editan
28. Klik Tab `Group Manager`
29. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
30. Verifikasi baris Kevin Susanto di `Data Center` hilang dari Tab `Group Manager`

### TC-FA-RP-397: Remove baris Group Role target Group Manager di node GM-nya, dialog D-05 varian Remove baris

31. Tetapkan kembali Kevin Susanto sebagai Group Manager di `Data Center` dengan baris Group Role eksplisit CRUD penuh lewat sesi API hingga tersimpan (pemulihan precondition TC)
32. Klik Tab `System`
33. Buka Detail Role `Manage group`
34. Klik node `Data Center` pada Sidebar Group Tree
35. Klik `[⋯]` baris Kevin Susanto lalu `Remove`
36. Verifikasi dialog severity danger dengan Title `Remove Group Manager`, Body `These users will lose Group Manager access:` lalu `• Kevin S` dan `Are you sure you want to remove it?`
37. Klik `[Remove]`
38. Verifikasi toast sukses `Success, permissions have been updated. Kevin Susanto is no longer Group Manager for Data Center.`
39. Verifikasi baris Kevin Susanto pada `Manage group` `Data Center` dihapus
40. Klik Tab `Group Manager`
41. Verifikasi baris Kevin Susanto di `Data Center` tidak ada di Tab `Group Manager` (GM lepas dalam satu transaksi dengan baris dihapus)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 395, 398, 396, 397: TC-FA-RP-396 dan TC-FA-RP-397 sama-sama melepas Group Manager Kevin Susanto di `Data Center` sehingga diletakkan di akhir, dan TC-FA-RP-395 serta TC-FA-RP-398 membutuhkan Kevin Susanto masih Group Manager.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8, 14, dan 21 (kembali ke Tab `System`), langkah 31 (menetapkan kembali Group Manager dan baris eksplisit lewat sesi API sebagai precondition TC-FA-RP-397). Langkah 29 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 30 (bagian 8b butir 2).
- Pola toast PRD pada TC-FA-RP-396 butir d (`Success, permissions have been updated. [User Name] is no longer Group Manager for [Group Name].`) adalah penjelasan pola dari teks toast butir a; teks literal diasersi pada langkah 26.
- Post Condition TC-FA-RP-396 (log `Auto-Revert` Object `Group Manager` dan notifikasi in-app) tidak punya langkah observasi di TC ini; tidak diasersi.
- Alasan di atas sekitar 35 langkah (41 langkah): empat TC satu topik (Auto-Revert Group Manager Kevin Susanto) yang berbagi Detail Role, node, dan target; urutan menentukan keadaan Kevin Susanto. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-395 butir b dan TC-FA-RP-398 tidak memberi indikator UI untuk "tidak ada perubahan tersimpan"; spec memakai kemampuan baca (langkah 7).
  - TC tidak menyebut cara kembali dari Detail Role ke daftar Tab `System`; spec memakai langkah "Kembali ke Tab `System`".
