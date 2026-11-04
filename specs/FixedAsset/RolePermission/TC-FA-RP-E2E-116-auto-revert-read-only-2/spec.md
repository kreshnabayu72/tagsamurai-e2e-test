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
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #3 (dirujuk precondition TC), #12 (Maya Anggraeni, Read Only; seluruh Global Role hanya Read; baris pola Group Role Read Only pada `Manage files` di `Data Center`), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca nilai tersimpan baris Group Role (disediakan tim FE/BE tanpa endpoint karangan) untuk langkah 9.
- State yang diubah dan pemulihannya: TC-FA-RP-389 tidak mengubah state (kedua dialog di-Cancel); pada TC-FA-RP-388 baris `Manage Open API` dihapus dan tingkat akses Read Only lepas. Hook `after` memulihkan Pre-setup #12 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage files`

### TC-FA-RP-389: Edit CRUD dan Remove baris Group Role target Read Only memicu auto-revert D-04 (bukan edit biasa dan bukan D-03), Cancel tanpa perubahan

3. Klik node `Data Center` pada Sidebar Group Tree
4. Hapus centang Delete pada baris Maya Anggraeni
5. Verifikasi dialog severity danger: Title `Remove Read Only`; Body `• Maya A` lalu `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
6. Verifikasi tidak ada toast sukses
7. Klik `[Cancel]`
8. Verifikasi checkbox Delete baris Maya Anggraeni kembali ke nilai semula
9. Verifikasi tidak ada perubahan tersimpan pada baris Maya Anggraeni lewat kemampuan baca
10. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`
11. Verifikasi dialog severity danger: Title `Remove Read Only`; Body `These users will lose Read Only access:` lalu `• Maya A` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
12. Verifikasi dialog `Remove User` (D-03) tidak tampil
13. Klik `[Cancel]`
14. Verifikasi baris Maya Anggraeni tetap ada di Detail Role `Manage files` pada `Data Center`
15. Klik Tab `Read Only`
16. Verifikasi Maya Anggraeni tetap ada di Tab `Read Only`

### TC-FA-RP-388: Confirm Remove baris Global Role target Read Only, baris dihapus dan tingkat akses lepas dalam satu transaksi

17. Klik Tab `System`
18. Buka Detail Role `Manage Open API`
19. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`
20. Klik `[Remove]` pada dialog
21. Verifikasi toast sukses `Success, permissions have been updated. Maya Anggraeni is no longer Read Only.`
22. Verifikasi baris Maya Anggraeni pada `Manage Open API` hilang
23. Klik Tab `Read Only`
24. Verifikasi sedikitnya satu baris Read Only lain tampil di Tab `Read Only`
25. Verifikasi Maya Anggraeni tidak ada di Tab `Read Only`
26. Klik Tab `System`
27. Buka Detail Role `Manage accounting`
28. Verifikasi penugasan Global Role lain tidak direset: baris Maya Anggraeni pada `Manage accounting` tetap ada dengan nilai hanya Read

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 389, 388: TC-FA-RP-388 melepas tingkat akses Read Only Maya Anggraeni sehingga diletakkan di akhir (aksi yang menghapus data), sedangkan TC-FA-RP-389 mengasersi Maya Anggraeni masih ada di Tab `Read Only`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): tidak ada. Langkah 24 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 25 (bagian 8b butir 2). Langkah 6 (tidak ada toast sukses) memakai dialog langkah 5 sebagai anchor positif; langkah 12 (D-03 tidak tampil) memakai dialog langkah 11 sebagai anchor positif.
- Post Condition TC-FA-RP-388 (notifikasi in-app ke target) tidak punya langkah observasi di TC ini; tidak diasersi.
- Temuan untuk QA:
  - TC-FA-RP-388 butir c ("Penugasan Global Role lain tidak direset") tidak menyebut Global Role dan nilainya; spec memakai `Manage accounting` dengan nilai hanya Read sesuai Pre-setup #12 (langkah 28).
  - TC-FA-RP-389 Expected a ("tidak ada perubahan tersimpan") tidak memberi cara observasi; langkah 9 memakai kemampuan baca state yang disediakan tim FE/BE.
