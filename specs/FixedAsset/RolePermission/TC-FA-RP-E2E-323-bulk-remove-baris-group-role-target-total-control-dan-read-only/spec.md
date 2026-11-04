---
id: TC-FA-RP-E2E-323-bulk-remove-baris-group-role-target-total-control-dan-read-only
title: "Bulk Remove baris Group Role target Total Control dan Read Only: dialog D-07 dengan anotasi tier, Confirm melepas kedua tier"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1173
coverage:
  web: automated
---

# Bulk Remove baris Group Role target Total Control dan Read Only: dialog D-07 dengan anotasi tier, Confirm melepas kedua tier

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup: #15 (Ahmad Fauzi, Standard), #18 (pohon Group; node `Data Center`), #3 (Rina Wulandari, Total Control kedua), #12 (Maya Anggraeni, Read Only), #39 (Detail Role Group Role `Manage files` terisi; node `Data Center` memuat lima baris pola ditambah Ahmad Fauzi dan Dimas Pranata, tujuh baris). Pre-setup #39 belum tercantum di pernyataan Pre-setup bersama `suite.md` (lihat Temuan untuk QA).
- Precondition TC: Rina Wulandari (Total Control) dan Maya Anggraeni (Read Only) memegang baris pola Group Role pada `Manage files` di `Data Center`; Ahmad Fauzi (Standard) memegang `Manage files` di `Data Center`; dibentuk lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Spec ini destruktif (melepas tier Total Control Rina Wulandari dan tier Read Only Maya Anggraeni serta menghapus baris Group Role Ahmad Fauzi) dan dijalankan terakhir di suite. Pemulihan: langkah 19 menetapkan ulang Rina Wulandari, Maya Anggraeni, dan Ahmad Fauzi ke state Pre-setup #3, #12, dan #39; hook `after` mengulang pemulihan itu sebagai cadangan (Post Condition TC: dipulihkan oleh automation baseline), dijamin fixture backend yang disediakan tim FE/BE (suite.md, Pre-setup bersama).
- Identitas Pre-setup mengacu ke fixture `Fixture.fixedAssetRolePermission` (belum ada di repo, tanpa password; ditandai untuk tim FE).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1173: Bulk Remove memuat baris Group Role target Total Control dan Read Only: dialog D-07 dengan anotasi tier, Confirm melepas kedua tier

1. Buka Detail Role Group Role `Manage files` dan pilih node `Data Center`
2. Centang baris Rina Wulandari, Maya Anggraeni, dan Ahmad Fauzi
3. Klik `Bulk Action` > `Remove`
4. Verifikasi dialog Bulk Remove `D-07` memuat bullet `Rina W (Total Control)`, `Maya A (Read Only)`, dan `Ahmad F`
5. Verifikasi kalimat `The users marked above will lose their access level as a result.` tampil sebelum `Are you sure you want to remove them?`
6. Verifikasi dialog `D-06` tidak tampil
7. Klik `[Remove]`
8. Verifikasi sedikitnya satu baris lain tampil di node `Data Center`
9. Verifikasi ketiga baris (Rina Wulandari, Maya Anggraeni, dan Ahmad Fauzi) dihapus dari node `Data Center`
10. Klik Tab `Total Control`
11. Verifikasi sedikitnya satu baris lain tampil di Tab Total Control
12. Verifikasi Rina Wulandari tidak ada di Tab Total Control (lepas tingkat akses, auto-revert)
13. Klik Tab `Read Only`
14. Verifikasi sedikitnya satu baris lain tampil di Tab Read Only
15. Verifikasi Maya Anggraeni tidak ada di Tab Read Only (lepas tingkat akses, auto-revert)
16. Buka Detail Role Global Role `Manage accounting`
17. Verifikasi baris Rina Wulandari pada Global Role `Manage accounting` tidak direset
18. Verifikasi baris Maya Anggraeni pada Global Role `Manage accounting` tidak direset
19. Tetapkan ulang Rina Wulandari, Maya Anggraeni, dan Ahmad Fauzi ke state Pre-setup #3, #12, dan #39 lewat seeding API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 19 langkah.
- Langkah penghubung (S-03): membuka Detail Role, tab (langkah 1, 10, 13, 16). Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah pemulihan lewat seeding API (S-04, S-09): langkah 19; tidak ada `Verifikasi`.
- Detail Role `Manage files` node `Data Center` memuat tujuh baris (Pre-setup #39), Tab Total Control sembilan baris (#36), dan Tab Read Only empat baris (#37); semuanya tidak melebihi satu halaman sehingga baris target dibuka tanpa Search (R-23).
- Asersi tambahan di luar TC (S-03): langkah 8, 11, dan 14 adalah anchor positif untuk asersi absence baris pada langkah 9, 12, dan 15 (butir 8b.2); TC tidak memuat toast sukses sehingga tidak ada anchor toast. Klausa Expected c "lepas tingkat aksesnya (auto-revert)" diasersi lewat langkah 12 dan 15 (Expected d).
- Langkah 17 dan 18: Expected d "Global Role keduanya tidak direset" tidak menyebut Global Role tertentu; spec memakai `Manage accounting` (asumsi) dan mengasersi baris tetap ada sesuai Pre-setup #3 (CRUD penuh) dan #12 (Read saja).
- Temuan untuk QA:
  - Format anotasi bullet `[User Name] ([Access Level])` dan kalimat `The users marked above will lose their access level as a result.` ditandai "copy usulan" di TC (PRD §12 #1); teks diikuti persis dari TC dan perlu dikonfirmasi final.
  - Pre-setup #39 (41 baris `All Groups` dan lima baris pola `Manage files` per node) dirujuk TC tetapi belum tercantum di pernyataan Pre-setup bersama `suite.md`; pemulihan #39 dijamin tim FE/BE dan dicatat di Prerequisites (suite.md tidak diubah). Pre-setup #24 tidak dipakai TC ini.
  - Post Condition TC (entri `Auto-Revert` dengan Modified By admin pengedit) tidak punya langkah observasi di TC dan tidak diasersi; pencatatan diasersi TC-FA-RP-1163 (spec 335).
  - TC tidak menyebut toast sukses untuk Bulk Remove ini; Expected c hanya "ketiga baris dihapus".
  - Pre-setup #15 menggambarkan Ahmad Fauzi tanpa Group Role, sedangkan precondition d TC dan Pre-setup #39 menyatakan Ahmad Fauzi memegang `Manage files` di `Data Center`; spec mengikuti #39 dan precondition d.
