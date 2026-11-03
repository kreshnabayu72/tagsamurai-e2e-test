---
id: TC-FA-RP-E2E-115-auto-revert-read-only-1
title: "Auto-Revert Read Only (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-385
  - TC-FA-RP-386
  - TC-FA-RP-387
coverage:
  web: automated
---

# Auto-Revert Read Only (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Rina Wulandari, dirujuk precondition TC, tidak dipakai langkah), #12 (Maya Anggraeni, Read Only; seluruh Global Role hanya Read).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca tingkat akses dan nilai tersimpan baris Detail Role (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: pada TC-FA-RP-386 tingkat akses Read Only Maya Anggraeni lepas dan Create pada `Manage accounting` tercentang. Hook `after` memulihkan Pre-setup #12 (Read Only, seluruh Global Role hanya Read) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage accounting`

### TC-FA-RP-385: Edit CRUD yang menyimpangkan target Read Only, dialog D-04 dan Cancel mengembalikan cell

3. Centang Create pada baris Maya Anggraeni
4. Verifikasi dialog severity danger dengan Title `Remove Read Only`, Body `• Maya A` lalu `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
5. Klik `[Cancel]`
6. Verifikasi tidak ada toast
7. Verifikasi checkbox Create baris Maya Anggraeni kembali ke nilai semula (tidak tercentang)
8. Verifikasi tidak ada perubahan tersimpan pada Create baris Maya Anggraeni lewat kemampuan baca

### TC-FA-RP-387: Remove baris Global Role target Read Only, dialog D-04 varian Remove baris

9. Kembali ke Tab `System`
10. Buka Detail Role `Manage Open API`
11. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`
12. Verifikasi dialog severity danger dengan Title `Remove Read Only`, Body `These users will lose Read Only access:` lalu `• Maya A` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
13. Verifikasi dialog Remove biasa `Remove User` tidak tampil
14. Klik `[Cancel]`
15. Verifikasi baris Maya Anggraeni tetap ada
16. Verifikasi tingkat akses Maya Anggraeni tidak berubah (tetap Read Only) lewat kemampuan baca

### TC-FA-RP-386: Confirm auto-revert Read Only lewat edit CRUD, tingkat akses lepas tanpa reset penugasan lain

17. Kembali ke Tab `System`
18. Buka Detail Role `Manage accounting`
19. Centang Create pada baris Maya Anggraeni
20. Klik `[Remove]` pada dialog
21. Verifikasi toast sukses `Success, permissions have been updated. Maya Anggraeni is no longer Read Only.`
22. Verifikasi checkbox Create pada `Manage accounting` tercentang sesuai editan
23. Verifikasi checkbox Read pada baris Maya Anggraeni tetap aktif
24. Klik Tab `Read Only`
25. Verifikasi sedikitnya satu baris Read Only lain tampil di Tab `Read Only`
26. Verifikasi Maya Anggraeni tidak lagi ada di Tab `Read Only`
27. Klik Tab `System`
28. Buka Detail Role `Manage Open API`
29. Verifikasi penugasan Global Role lain tidak direset: baris Maya Anggraeni pada `Manage Open API` tetap hanya Read seperti sebelum edit

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 385, 387, 386: TC-FA-RP-386 melepas tingkat akses Read Only Maya Anggraeni, sedangkan TC-FA-RP-387 membutuhkan Maya Anggraeni masih Read Only.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9 dan 17 (kembali ke Tab `System`). Langkah 25 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 26 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-386 butir d menulis "nilai pada `Manage Open API` tetap seperti sebelum edit" tanpa menyebut nilainya; spec memakai hanya Read sesuai Pre-setup #12 (langkah 29).
  - Post Condition TC-FA-RP-386 (log `Auto-Revert` dan notifikasi in-app ke target) tidak punya langkah observasi di TC ini; tidak diasersi.
  - TC-FA-RP-385 butir b dan TC-FA-RP-387 butir c ("tidak ada perubahan tersimpan", "tingkat akses tidak berubah") tidak punya indikator UI; spec memakai kemampuan baca (langkah 8 dan 16).
  - TC tidak menyebut cara kembali dari Detail Role ke daftar Tab `System`; spec memakai langkah "Kembali ke Tab `System`".
