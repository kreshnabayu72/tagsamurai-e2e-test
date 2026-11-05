---
id: TC-FA-GRP-E2E-298-create-group-level-1-tanpa-baris-pola-gm-dan-total-user-hanya-tc-du-ro
title: "Create Group Level 1: Tanpa Baris Pola GM untuk User Group Manager, Total User Hanya Total Control, Default User, dan Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1296
coverage:
  web: automated
---

# Create Group Level 1: Tanpa Baris Pola GM untuk User Group Manager, Total User Hanya Total Control, Default User, dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user GM yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): gmPattern Pre-setup No 28, gmPatternNested Pre-setup No 29, dan gmPatternOther Pre-setup No 30, masing-masing `<nama>_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 21, di-seed lewat sesi API aktor di hook `before`, dihapus di hook `after`): `GM Pattern Parent {runId}-298` (Function None, level 1) > `GM Pattern Child {runId}-298` (Assignable) dan `GM Pattern Other {runId}-298` (Assignable, level 1). Penugasan Group Manager ketiga user GM di node-node itu (gmPattern dan gmPatternNested di Parent, gmPatternNested juga di Child, gmPatternOther di Other) beserta baris pola GM yang sudah terbentuk di-seed lewat API; mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec: `GM Level One {runId}-298` (level 1, dihapus di hook `after` lewat API).
- N = jumlah user Total Control + Default User + Read Only pada client; diturunkan dari daftar akun client yang di-seed/dibaca di hook `before` (8b butir 10), bukan dari tabel satu halaman.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role dan tab Transaction Role (Settings > Role & Permission) per node dan per user, serta log Role & Permission (Action dan Modified By per entri). Node memakai nama bersuffix unik sehingga baseline entri log untuk penanda nama node adalah nol (S-12).

## Test Steps

1. Klik [+] Group
2. Isi Group Name `GM Level One {runId}-298`
3. Klik [Submit]
4. Verifikasi toast sukses `Success, group has been created.`
5. Baca tab Group Role dan tab Transaction Role user gmPattern, gmPatternNested, dan gmPatternOther pada `GM Level One {runId}-298` lewat kemampuan baca modul Role & Permission
6. Verifikasi pada `GM Level One {runId}-298`, baris pola Group Role user Total Control tampil (anchor: Create diproses dan baris pola TC/RO terbentuk)
7. Verifikasi ketiga user GM tidak memiliki baris Group Role pada `GM Level One {runId}-298`
8. Verifikasi ketiga user GM tidak memiliki baris Transaction Role pada `GM Level One {runId}-298`
9. Ketik Search `GM Level One {runId}-298`, tekan Enter
10. Verifikasi Groups List memuat baris `GM Level One {runId}-298`
11. Verifikasi Total User `GM Level One {runId}-298` sama dengan N (jumlah user Total Control + Default User + Read Only client)
12. Klik angka Total User `GM Level One {runId}-298`
13. Verifikasi Tab Users memuat user Total Control, Default User, dan Read Only (anchor: tabel terisi)
14. Verifikasi Tab Users tidak memuat user gmPattern, gmPatternNested, dan gmPatternOther
15. Tutup Popup Detail Group
16. Klik `(←)` pada kotak Search
17. Baca log Role & Permission untuk `GM Level One {runId}-298`
18. Verifikasi log memuat entri `Assign` untuk baris pola Total Control/Read Only pada `GM Level One {runId}-298`

## Notes

- Spec memiliki 18 langkah. Langkah penghubung (S-03): langkah 5 dan 17 (observasi lewat kemampuan baca), langkah 9 (Search untuk menemukan baris target, R-16), langkah 15 (menutup Popup Detail Group), dan langkah 16 (menutup Search).
- Pembagian TC lintas spec: TC-1296 muncul di `sourceTc` spec ini dan spec 292 (absence, S-05). Spec ini mengasersi presence dan keadaan tabel (toast, ketiga user GM tanpa baris Group Role/Transaction Role, Total User = N, Tab Users tanpa user GM, entri `Assign` untuk baris pola Total Control/Read Only). Asersi tidak adanya entri log untuk user GM (TC-1296 Expected d bagian "tidak ada entri untuk user GM") ada di spec 292 dengan anchor sendiri.
- Temuan untuk QA:
  - Email Pre-setup No 28 sampai 30 belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan GM dan baris pola yang sudah terbentuk tidak ditegaskan di TC.
  - TC-1296 Expected c menyebut "jumlah user Total Control + Default User + Read Only client" sebagai Total User, tetapi client Tabel A dapat memuat user lain di group level 1 baru yang diwarisi; N diturunkan dari daftar akun client yang di-seed. Pengaruh baris pola GM pada Total User masih NC-12 (Menunggu konfirmasi).
  - TC-1296 Expected d merujuk "lihat TC-FA-GRP-1289" untuk entri `Assign` baris pola TC/RO; spec hanya mengasersi keberadaan entri `Assign` untuk baris pola Total Control/Read Only, bukan jumlah per baris (diasersi spec 285).
