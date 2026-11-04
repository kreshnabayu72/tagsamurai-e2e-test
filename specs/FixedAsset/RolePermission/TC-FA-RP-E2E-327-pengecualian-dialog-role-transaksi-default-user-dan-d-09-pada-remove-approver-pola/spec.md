---
id: TC-FA-RP-E2E-327-pengecualian-dialog-role-transaksi-default-user-dan-d-09-pada-remove-approver-pola
title: "Pengecualian Dialog Role Transaksi: Default User dan D-09 pada Remove Approver Pola"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1155
  - TC-FA-RP-1160
coverage:
  web: automated
---

# Pengecualian Dialog Role Transaksi: Default User dan D-09 pada Remove Approver Pola

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #1 (Admin Utama, Default User; baris pola Asset Admin dan Approver pada setiap node), #3 (Rina Wulandari, Total Control; baris pola Approver), #18 (pohon group: `IT Infrastructure` dan `Data Center`), #19 (seed Role Transaksi sub-tab `Disposal`), #20 (sub-tab `Transfer` pada `IT Infrastructure` dengan Require Approval ON dan Approver manual Pandu Wijaya; baris Approver pola Admin Utama dan Siti Rahmawati).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: TC-FA-RP-1155 tidak mengubah state; pada TC-FA-RP-1160 (langkah 20) baris Approver pola Rina Wulandari di sub-tab `Transfer` `IT Infrastructure` dihapus dan tingkat akses Total Control Rina lepas, sedangkan Require Approval sub-tab `Transfer` tetap ON. Hook `after` memulihkan Pre-setup #3 dan memastikan Require Approval sub-tab `Transfer` `IT Infrastructure` kembali ke state Pre-setup #20 (ON dengan Approver manual Pandu Wijaya) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`

### TC-FA-RP-1155: Default User memegang baris pola Transaction Role tanpa auto-revert dan tidak dapat diubah

2. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
3. Verifikasi Admin Utama (Default User) tampil di section Asset Admin dan Approver pada node itu
4. Klik node `Data Center` lalu sub-tab `Disposal`
5. Verifikasi Admin Utama (Default User) tampil di section Asset Admin dan Approver pada node lain itu
6. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
7. Klik `[⋯]` pada baris Admin Utama di section Asset Admin
8. Arahkan kursor ke `Remove`
9. Verifikasi aksi `Remove` Disabled dengan tooltip `Default User cannot be modified.`
10. Tutup menu `[⋯]`
11. Klik `[⋯]` pada baris Admin Utama di section Approver
12. Arahkan kursor ke `Remove`
13. Verifikasi aksi `Remove` Disabled dengan tooltip `Default User cannot be modified.`
14. Tutup menu `[⋯]`
15. Verifikasi tidak ada dialog auto-revert untuk Default User (`FARP-LOGIC-04g`)

### TC-FA-RP-1160: Remove Approver pola milik target Total Control tidak memicu D-09 walau Require Approval ON

16. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
17. Klik `[⋯]` pada baris Rina Wulandari di section Approver lalu `Remove`
18. Verifikasi hanya dialog auto-revert `D-04` yang tampil: Title `Remove Total Control`; tombol `[Cancel]` dan `[Remove]`
19. Verifikasi dialog `D-09` (`Remove Last Approver`) tidak tampil
20. Klik `[Remove]` pada dialog
21. Verifikasi toggle Require Approval tetap ON
22. Verifikasi baris Approver pola Admin Utama dan Siti Rahmawati serta Pandu Wijaya tetap ada
23. Verifikasi fallback approver Total Control/Default User (`FARP-LOGIC-12c`) tetap utuh: baris Approver Admin Utama dan Siti Rahmawati tetap tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini memuat 23 langkah.
- Urutan TC sumber diubah menjadi 1155, 1160 sesuai urutan nomor dan agar TC-FA-RP-1160 yang melepas tier Rina (aksi yang mengubah data) berada di akhir; TC-FA-RP-1155 tidak mengubah state.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (buka Tab `Transaction Role`), langkah 4 dan 6 (pindah node untuk Expected a), langkah 10 dan 14 (tutup menu `[⋯]`), langkah 16 (buka sub-tab `Transfer`). Langkah 9 dan 13 memakai hover pada `Remove` sebagai pemicu tooltip dan diasersi segera sebelum menutup menu (bagian 8b butir 5). Langkah 15 (tidak ada dialog auto-revert untuk Default User) memakai langkah 9 dan 13 (aksi Disabled dengan tooltip) sebagai anchor positif. Langkah 19 (D-09 tidak tampil) memakai dialog langkah 18 sebagai anchor positif.
- Post Condition TC-FA-RP-1160 ("Remove Approver manual terakhir tetap memakai D-09, lihat TC-FA-RP-374") dan pemulihan Rina oleh automation baseline tidak punya langkah observasi; tidak diasersi, pemulihan di hook `after`.
- Temuan untuk QA:
  - Copy dialog bertanda "copy usulan, perlu persetujuan PM" di TC sumber; spec memakai teks TC apa adanya. TC-FA-RP-1160 hanya menyebut Title dan tombol dialog D-04; Body tidak diasersi.
  - TC-FA-RP-1155 Expected a menyebut "node itu dan node lain" tanpa menyebut node; spec memakai `Data Center` sub-tab `Disposal` (langkah 4).
  - TC-FA-RP-1155 Expected c ("Tidak ada dialog auto-revert untuk Default User") tidak punya aksi pemicu karena aksi `Remove` Disabled; spec tidak menambah klik pada aksi Disabled dan hanya mengasersi dialog tidak tampil sesudah langkah 7 sampai 14.
  - TC-FA-RP-1155 langkah 3 ("row action baris Admin Utama") tidak menyebut section; spec memeriksa Asset Admin dan Approver sesuai langkah 2 TC.
  - TC-FA-RP-1160 Expected c ("fallback approver tetap utuh") tidak punya observasi tersendiri selain baris Approver pola Admin Utama dan Siti Rahmawati yang sudah dikutip Expected b; langkah 22 dan 23 memverifikasi baris yang sama dari dua klausa.
  - TC-FA-RP-1160 tidak menyebut toast sesudah `[Remove]`; tidak diasersi.
