---
id: TC-FA-RP-E2E-341-auto-revert-role-transaksi-remove-baris-pola-target-read-only
title: "Auto-Revert Role Transaksi: Remove Baris Pola Target Read Only"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1165
coverage:
  web: automated
---

# Auto-Revert Role Transaksi: Remove Baris Pola Target Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #12 (Maya Anggraeni, Read Only; seluruh Global Role hanya Read; baris pola Transaction Role Monitoring & Report pada setiap Jenis Transaksi x Group), #18 (pohon group: `IT Infrastructure` dan `Data Center`), #19 (seed Role Transaksi sub-tab `Disposal`).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: pada langkah 16 baris Monitoring & Report pola Maya Anggraeni di `IT Infrastructure` sub-tab `Disposal` dihapus dan tingkat akses Read Only Maya lepas. Hook `after` memulihkan Pre-setup #12 (tier Read Only dan baris pola) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` lalu sub-tab `Disposal`

### TC-FA-RP-1165: Remove baris pola milik target Read Only, dialog auto-revert D-04 varian Role Transaksi memakai body khusus Role Transaksi

3. Klik `[⋯]` pada baris Maya Anggraeni di section Monitoring & Report lalu `Remove`
4. Verifikasi dialog severity danger: Title `Remove Read Only`; Body `• Maya A` lalu `This change will remove this user's Read Only access level. Their other role assignments will remain as they are.`, ditutup `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
5. Verifikasi teks body varian Remove baris `These users will lose Read Only access:` tidak tampil pada dialog ini
6. Verifikasi dialog `D-08` (`Remove Role Transaksi`) tidak tampil
7. Klik `[Cancel]`
8. Verifikasi dialog tertutup
9. Verifikasi tidak ada toast
10. Verifikasi baris Maya Anggraeni tetap ada di section Monitoring & Report
11. Klik Tab `Read Only`
12. Verifikasi Maya Anggraeni tetap ada di Tab `Read Only`
13. Klik Tab `Transaction Role`
14. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
15. Klik `[⋯]` pada baris Maya Anggraeni di section Monitoring & Report lalu `Remove`
16. Klik `[Remove]` pada dialog
17. Verifikasi sedikitnya satu baris lain tampil di section Monitoring & Report
18. Verifikasi baris Monitoring & Report Maya Anggraeni pada node itu hilang
19. Klik node `Data Center` lalu sub-tab `Transfer`
20. Verifikasi baris pola Maya Anggraeni di section Monitoring & Report pada node dan sub-tab lain itu tetap ada
21. Klik Tab `Read Only`
22. Verifikasi sedikitnya satu baris Read Only lain tampil di Tab `Read Only`
23. Verifikasi Maya Anggraeni tidak ada di Tab `Read Only`
24. Klik Tab `System`
25. Buka Detail Role `Manage accounting`
26. Verifikasi Global Role Maya Anggraeni tidak direset: baris Maya Anggraeni pada `Manage accounting` tetap ada dengan nilai hanya Read

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini memuat 26 langkah.
- Pembagian TC lintas spec: TC-FA-RP-1151 (target Total Control) ada di spec 324; masing-masing TC tepat satu spec.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 13 (buka Tab `Transaction Role`), langkah 11 dan 21 (buka Tab `Read Only`), langkah 19 (pindah ke node dan sub-tab lain untuk Expected d), langkah 24 dan 25 (buka Detail Role). Langkah 17 dan 22 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 18 dan 23 (bagian 8b butir 2). Langkah 9 (tidak ada toast) memakai dialog langkah 4 sebagai anchor positif; langkah 5 dan 6 (teks varian lain dan D-08 tidak tampil) memakai dialog langkah 4 sebagai anchor positif.
- Post Condition TC-FA-RP-1165 (Maya dipulihkan ke Pre-setup #12) dilakukan hook `after`, bukan langkah spec.
- Temuan untuk QA:
  - Copy dialog bertanda "copy usulan, perlu persetujuan PM (PRD 12 #1)" di TC sumber; spec memakai teks TC apa adanya. TC tidak menyebut toast sesudah `[Remove]` (Expected d), sehingga tidak ada `Verifikasi` toast dan langkah 17 memakai baris lain di section yang sama sebagai anchor absence atas langkah 18.
  - TC-FA-RP-1165 Expected d menyebut "node dan sub-tab lain" tanpa menyebut yang mana; spec memakai node `Data Center` sub-tab `Transfer` (langkah 19).
  - TC-FA-RP-1165 Expected d menyebut "Global Role Maya tidak direset" tanpa menyebut Global Role; spec memakai `Manage accounting` dengan nilai hanya Read sesuai Pre-setup #12 (langkah 26).
