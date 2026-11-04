---
id: TC-FA-RP-E2E-322-auto-revert-group-role-pola-lewat-edit-crud-dan-remove-baris
title: "Auto-revert tier lewat edit CRUD dan Remove baris pola Group Role: dialog D-04, tier lepas, role lain utuh"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1171
  - TC-FA-RP-1172
coverage:
  web: automated
---

# Auto-revert tier lewat edit CRUD dan Remove baris pola Group Role: dialog D-04, tier lepas, role lain utuh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup: #3 (Rina Wulandari, Total Control kedua; seluruh Global Role CRUD penuh, baris pola Group Role CRUD penuh pada setiap role × group, baris pola Transaction Role Asset Admin dan Approver), #12 (Maya Anggraeni, Read Only; seluruh Global Role hanya Read, baris pola Group Role Read saja, baris pola Transaction Role Monitoring & Report), #18 (pohon Group; node `Data Center` dan `Helpdesk`), #39 (Detail Role Group Role `Manage files` terisi; tiap node memuat lima baris pola ditambah baris non-pola node itu, `Data Center` tujuh baris dan `Helpdesk` enam baris). Pre-setup #39 belum tercantum di pernyataan Pre-setup bersama `suite.md` (lihat Temuan untuk QA).
- Precondition TC: Rina Wulandari dan Maya Anggraeni memegang tier dan baris pola sesuai Pre-setup di atas pada awal tiap blok TC (seeding API di hook `before`, kemampuan disediakan tim FE/BE, tanpa endpoint karangan); TC dependensi TC-FA-RP-384 dan TC-FA-RP-389 dipenuhi lewat state Pre-setup itu, bukan lewat penyalinan langkah (S-04).
- Pemulihan: langkah 16 dan 32 menetapkan ulang Rina Wulandari dan Maya Anggraeni ke state Pre-setup #3 dan #12 (baris pola Group Role dan tingkat akses); hook `after` mengulang pemulihan itu sebagai cadangan (Post Condition TC: dipulihkan oleh automation baseline). Pemulihan dijamin fixture backend yang disediakan tim FE/BE.
- Identitas Pre-setup mengacu ke fixture `Fixture.fixedAssetRolePermission` (belum ada di repo, tanpa password; ditandai untuk tim FE).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1171: Confirm auto-revert Total Control lewat edit CRUD baris Group Role: tier lepas, baris Global Role, Group Role lain, dan Role Transaksi utuh

1. Buka Detail Role Group Role `Manage files` dan pilih node `Data Center`
2. Hapus centang Delete pada baris Rina Wulandari
3. Verifikasi dialog yang tampil adalah `D-04` (bukan `D-03` dan bukan edit biasa)
4. Klik `[Remove]` pada dialog
5. Verifikasi muncul toast sukses: `Success, permissions have been updated. Rina Wulandari is no longer Total Control.`
6. Verifikasi checkbox Delete `Manage files` di `Data Center` pada baris Rina Wulandari tidak tercentang sesuai editan
7. Verifikasi checkbox Read `Manage files` di `Data Center` pada baris Rina Wulandari tetap aktif
8. Klik Tab `Total Control`
9. Verifikasi Rina Wulandari tidak lagi ada di Tab Total Control
10. Buka Detail Role Group Role `Manage files` dan klik node `Helpdesk`
11. Verifikasi baris Rina Wulandari di `Helpdesk` tetap ada dengan CRUD tidak berubah
12. Buka Detail Role Global Role `Manage accounting`
13. Verifikasi baris Rina Wulandari pada Global Role `Manage accounting` tidak direset
14. Klik Tab `Transaction Role`, klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
15. Verifikasi baris pola Transaction Role Rina Wulandari (Asset Admin dan Approver) tidak direset
16. Tetapkan ulang Rina Wulandari ke state Pre-setup #3 (Total Control dengan baris pola Group Role CRUD penuh) lewat seeding API

### TC-FA-RP-1172: Confirm Remove baris Group Role target Read Only: dialog D-04 varian Remove baris, baris dihapus, tier lepas, role lain utuh

17. Buka Detail Role Group Role `Manage files` dan pilih node `Data Center`
18. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`
19. Verifikasi dialog severity danger: Title `Remove Read Only`; Body `These users will lose Read Only access:` lalu `• Maya A` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`
20. Verifikasi dialog `Remove User` (D-03) tidak tampil
21. Klik `[Remove]`
22. Verifikasi muncul toast sukses: `Success, permissions have been updated. Maya Anggraeni is no longer Read Only.`
23. Verifikasi baris Maya Anggraeni di `Data Center` hilang
24. Klik Tab `Read Only`
25. Verifikasi Maya Anggraeni tidak ada di Tab Read Only
26. Buka Detail Role Group Role `Manage files` dan klik node `Helpdesk`
27. Verifikasi baris Maya Anggraeni di `Helpdesk` tetap ada dengan Read aktif
28. Buka Detail Role Global Role `Manage accounting`
29. Verifikasi baris Maya Anggraeni pada Global Role `Manage accounting` tidak direset
30. Klik Tab `Transaction Role`, klik node `IT Infrastructure`, lalu klik sub-tab `Disposal`
31. Verifikasi baris pola Transaction Role Maya Anggraeni (Monitoring & Report) tidak direset
32. Tetapkan ulang Maya Anggraeni ke state Pre-setup #12 (Read Only dengan baris pola Group Role Read) lewat seeding API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 32 langkah.
- Langkah penghubung (S-03): membuka Detail Role, tab, node, dan sub-tab (langkah 1, 8, 10, 12, 14, 17, 24, 26, 28, 30). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan (S-04, S-09): langkah 16 dan 32; tidak ada `Verifikasi`.
- Detail Role Group Role pada node `Data Center` dan `Helpdesk` memuat tujuh dan enam baris (Pre-setup #39), tidak melebihi satu halaman, sehingga baris target dibuka tanpa Search (R-23).
- Asersi absence baris/tier (langkah 9, 23, 25) memakai toast sukses langkah 5 dan 22 sebagai anchor bahwa respons server sudah diproses (butir 8b.2); absence dialog D-03 (langkah 20) memakai dialog D-04 pada langkah 19 sebagai anchor positif. Anchor ini tidak menambah asersi di luar TC.
- Langkah 2 sampai 4 TC-FA-RP-1171: dialog `D-04` muncul sesudah centang Delete dihapus dan diasersi sebelum `[Remove]` (state sementara, butir 8b.5).
- Temuan untuk QA:
  - TC-FA-RP-1171 dan 1172 Post Condition (log `Auto-Revert` dan `Remove` dengan Modified By admin pengedit; notifikasi in-app ke Rina Wulandari dan Maya Anggraeni dengan Title `Your Total Control access was removed` dan `Your Read Only access was removed`) tidak punya langkah observasi di TC dan tidak diasersi; pencatatan dan notifikasi diasersi TC-FA-RP-1163 dan 1164 (spec 335 dan 336).
  - Rina Wulandari adalah target TC-FA-RP-1171 (toast "Rina Wulandari is no longer Total Control"), sehingga tidak dapat menjadi aktornya; precondition TC hanya menyebut "Total Control" tanpa akun, dan spec memakai Total Control Siti Rahmawati (Pre-setup #2) sebagai aktor di kedua blok. Precondition TC tidak menyebut Pre-setup #2 secara eksplisit.
  - TC-FA-RP-1171 Expected a menyebut dialog `D-04` tanpa teks (judul, isi, tombol); spec hanya mengasersi identitasnya (bukan `D-03`, bukan edit biasa). TC-FA-RP-1171 langkah 6 menyebut Tab Transaction Role tanpa node dan sub-tab; spec memakai `IT Infrastructure` sub-tab `Disposal` (asumsi).
  - Global Role `Manage accounting` disebut hanya di TC-FA-RP-1171 (langkah 6); TC-FA-RP-1172 menyebut "Global Role" tanpa nama. Spec memakai `Manage accounting` juga untuk TC-FA-RP-1172 (asumsi).
  - TC-FA-RP-1171 dan 1172 Expected "role lain utuh" tidak memuat nilai konkret; spec mengasersi baris tetap ada dengan nilai sesuai Pre-setup #3 dan #12 (CRUD penuh dan Read saja).
  - Precondition kedua TC tidak merujuk Pre-setup #39 padahal baris `Manage files` per node berasal dari #39; #39 belum ada di pernyataan Pre-setup bersama `suite.md` (dicatat di Prerequisites, suite.md tidak diubah).
  - TC dependensi TC-FA-RP-384 dan TC-FA-RP-389 tidak disalin; state yang dibangunnya sama dengan Pre-setup #3 dan #12 sehingga dibentuk lewat seeding.
