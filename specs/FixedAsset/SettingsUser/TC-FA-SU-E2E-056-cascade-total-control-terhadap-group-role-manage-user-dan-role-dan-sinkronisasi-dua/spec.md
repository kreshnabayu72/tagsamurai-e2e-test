---
id: TC-FA-SU-E2E-056-cascade-total-control-terhadap-group-role-manage-user-dan-role-dan-sinkronisasi-dua
title: "Cascade Total Control terhadap Group Role Manage user & role dan Sinkronisasi Dua Arah Global Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-189
  - TC-FA-SU-190
  - TC-FA-SU-1055
coverage:
  web: automated
---

# Cascade Total Control terhadap Group Role Manage user & role dan Sinkronisasi Dua Arah Global Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; pohon grup #21; penugasan #23): target Gita Permata (Global Role Import Data ON, Manage accounting ON, Manage asset ID configuration OFF tanpa nilai tersimpan) untuk TC-FA-SU-189 dan 190; target Nanda Pratama (Pre-setup #11: Group Role Manage user & role pada Finance & Accounting; Global Role Manage global user & role OFF) untuk TC-FA-SU-1055. Seed API memulihkan keadaan ini di hook `before`, langkah 12, dan hook `after` (Catatan TC).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca state BE penugasan grup Group Role Nanda (langkah 16); seed API untuk memulihkan Gita dan Nanda.
- State global dan pemulihan: penugasan Global Role Gita (Manage asset ID configuration ON dengan Update tercentang; Manage accounting OFF) dan tier serta penugasan Nanda (Total Control) berubah dan dipulihkan lewat seed API di hook `after`; entri log bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-189: Sinkronisasi dua arah Global Role dari Detail User ke Role & Permission

1. Ketik Search `Gita`, tekan Enter di User List, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
2. Nyalakan switch pada baris Manage asset ID configuration
3. Centang Update pada baris Manage asset ID configuration
4. Buka Settings > Role & Permission > Tab System > Detail Role Manage asset ID configuration
5. Ketik Search `Gita`, tekan Enter di Detail Role
6. Verifikasi baris Gita Permata tampil di Detail Role Manage asset ID configuration
7. Verifikasi perubahan Update (tercentang) tampil pada baris Gita Permata di Detail Role seketika

### TC-FA-SU-190: Sinkronisasi dua arah Global Role dari Role & Permission ke Tab Role

8. Buka Settings > Role & Permission > Tab System > Detail Role Manage accounting
9. Matikan Manage accounting untuk Gita Permata di Detail Role
10. Buka Settings > User > Detail Gita Permata > Tab Role > Sub-tab Global Role
11. Verifikasi switch Manage accounting Gita Permata OFF tanpa muat ulang manual

### TC-FA-SU-1055: Cascade Total Control menghapus penugasan grup Group Role Manage user & role

12. Pulihkan Nanda Pratama (Global Role Manage global user & role OFF; Group Role Manage user & role pada Finance & Accounting) lewat seed API
13. Buka Settings > Role & Permission lalu Assign Total Control kepada Nanda Pratama
14. Buka Settings > User > Detail Nanda Pratama > Tab Role > Sub-tab Group Role
15. Verifikasi baris Group Role lain tampil di Sub-tab Group Role
16. Verifikasi penugasan grup Group Role `Manage user & role` Nanda Pratama tidak ada di state BE
17. Verifikasi baris Group Role `Manage user & role` tidak tampil lagi di Sub-tab Group Role
18. Klik Sub-tab Global Role
19. Verifikasi switch Global Role Manage global user & role Nanda Pratama ON sebagai bagian cascade Total Control
20. Klik Sub-tab Group Role
21. Verifikasi baris Group Role seluruh role × group tampil dengan CRUD penuh (Create, Read, Update, Delete tercentang), kecuali Manage user & role yang tidak dirender

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 5 (Search untuk menemukan baris target, R-16), langkah 4, 8, 10, dan 14 (membuka halaman atau sub-tab), langkah 12 (memulihkan Nanda lewat seed API), langkah 18 dan 20 (membuka sub-tab).
- Asersi tambahan di luar Expected TC: langkah 15 adalah anchor positif bagi asersi absence langkah 17 (bagian 8b butir 2).
- Temuan untuk QA:
  - Langkah Uji TC-FA-SU-190 dan TC-FA-SU-1055 ("Matikan Manage accounting di Role & Permission", "Assign Total Control kepada Nanda") tidak merinci UI Role & Permission; spec menulis satu langkah dan UI-nya diuji di suite Settings Role & Permission.
  - Expected d TC-FA-SU-1055 (cascade menulis baris Group Role seluruh role × group dengan CRUD penuh) tidak menyebut sub-tab atau langkah pengamatannya; spec mengamatinya di Sub-tab Group Role Nanda Pratama sesudah cascade (langkah 20 dan 21).
  - Langkah Uji 3 TC-FA-SU-1055 ("Buka Tab Changelog Nanda Pratama") tidak punya Expected; tidak diasersi dan tidak ditulis sebagai langkah (S-01).
  - Expected c TC-FA-SU-1055 ("switch OFF kembali tidak memulihkan grup") tidak punya langkah OFF di Langkah Uji; pernyataan yang sama diasersi di spec 055 (TC-FA-SU-187), sehingga tidak diasersi lagi.
  - Expected b TC-FA-SU-190 ("tanpa reload manual") dipenuhi dengan membuka halaman Detail Gita sesudah perubahan; TC tidak menyebut sesi Detail User yang sudah terbuka.
  - Post Condition TC-FA-SU-189 dan 190 tidak punya langkah observasi tersendiri dan tidak diasersi di luar Expected (S-01); Post Condition TC-FA-SU-1055 bernilai `-`.
