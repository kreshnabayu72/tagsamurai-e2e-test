---
id: TC-FA-RP-E2E-112-auto-revert-total-control-1
title: "Auto-Revert Total Control (1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-380
  - TC-FA-RP-381
  - TC-FA-RP-382
coverage:
  web: automated
---

# Auto-Revert Total Control (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (Total Control kedua Rina Wulandari, seluruh Global Role CRUD penuh), #12 (Maya Anggraeni, Read Only; dirujuk precondition TC, tidak dipakai langkah).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca tingkat akses dan nilai tersimpan baris Detail Role (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: pada TC-FA-RP-381 tingkat akses Total Control Rina Wulandari lepas dan Delete pada `Manage accounting` tidak tercentang; hook `after` memulihkan Pre-setup #3 (Total Control dan CRUD penuh) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage accounting`

### TC-FA-RP-380: Edit CRUD yang menyimpangkan target Total Control, dialog D-04 dan Cancel mengembalikan cell

3. Hapus centang Delete pada baris Rina Wulandari
4. Verifikasi dialog severity danger dengan Title `Remove Total Control`, Body `• Rina W` lalu `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
5. Klik `[Cancel]`
6. Verifikasi tidak ada toast
7. Verifikasi checkbox Delete baris Rina Wulandari kembali ke nilai semula (tercentang)
8. Verifikasi tidak ada perubahan tersimpan pada Delete baris Rina Wulandari lewat kemampuan baca

### TC-FA-RP-382: Remove baris Global Role target Total Control, dialog D-04 varian Remove baris

9. Kembali ke Tab `System`
10. Buka Detail Role `Manage Open API`
11. Klik `[⋯]` baris Rina Wulandari lalu `Remove`
12. Verifikasi dialog severity danger dengan Title `Remove Total Control`, Body `These users will lose Total Control access:` lalu `• Rina W` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
13. Verifikasi dialog Remove biasa `Remove User` tidak tampil
14. Klik `[Cancel]`
15. Verifikasi baris Rina Wulandari tetap ada
16. Verifikasi tingkat akses Rina Wulandari tidak berubah (tetap Total Control) lewat kemampuan baca

### TC-FA-RP-381: Confirm auto-revert Total Control lewat edit CRUD, tingkat akses lepas tanpa reset penugasan lain

17. Kembali ke Tab `System`
18. Buka Detail Role `Manage accounting`
19. Hapus centang Delete pada baris Rina Wulandari
20. Klik `[Remove]` pada dialog
21. Verifikasi toast sukses `Success, permissions have been updated. Rina Wulandari is no longer Total Control.`
22. Verifikasi checkbox Delete pada `Manage accounting` tidak tercentang sesuai editan
23. Verifikasi checkbox Read pada baris Rina Wulandari tetap aktif
24. Klik Tab `Total Control`
25. Verifikasi sedikitnya satu baris Total Control lain tampil di Tab `Total Control`
26. Verifikasi Rina Wulandari tidak lagi ada di Tab `Total Control`
27. Klik Tab `System`
28. Buka Detail Role `Manage Open API`
29. Verifikasi penugasan Global Role lain tidak direset: baris Rina Wulandari pada `Manage Open API` tetap CRUD penuh seperti sebelum edit

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 380, 382, 381: TC-FA-RP-381 melepas tingkat akses Total Control Rina Wulandari, sedangkan TC-FA-RP-382 membutuhkan Rina Wulandari masih Total Control.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9 dan 17 (kembali ke Tab `System` sebelum membuka Detail Role lain). Langkah 25 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 26 (bagian 8b butir 2).
- Pola toast PRD pada TC-FA-RP-381 butir e (`Success, permissions have been updated. [User Name] is no longer [Access Level].`) adalah penjelasan pola dari teks toast butir a; teks literal butir a diasersi pada langkah 21.
- Temuan untuk QA:
  - TC-FA-RP-381 butir d menulis "nilai pada `Manage Open API` tetap seperti sebelum edit" tanpa menyebut nilainya; spec memakai CRUD penuh sesuai Pre-setup #3 (langkah 29).
  - Post Condition TC-FA-RP-381 (log `Auto-Revert` dengan Modified By admin pengedit dan notifikasi in-app ke target) tidak punya langkah observasi di TC ini; tidak diasersi.
  - TC-FA-RP-380 butir b menulis "tidak ada perubahan tersimpan" tanpa indikator UI; spec memakai kemampuan baca (langkah 8). TC-FA-RP-382 butir c ("tingkat akses tidak berubah") diperlakukan sama (langkah 16).
  - TC tidak menyebut cara kembali dari Detail Role ke daftar Tab `System`; spec memakai langkah "Kembali ke Tab `System`".
