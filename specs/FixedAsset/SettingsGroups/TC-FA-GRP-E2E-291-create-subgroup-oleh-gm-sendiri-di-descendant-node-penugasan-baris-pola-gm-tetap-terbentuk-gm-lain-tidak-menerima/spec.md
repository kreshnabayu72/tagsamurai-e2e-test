---
id: TC-FA-GRP-E2E-291-create-subgroup-oleh-gm-sendiri-di-descendant-node-penugasan-baris-pola-gm-tetap-terbentuk-gm-lain-tidak-menerima
title: "Create Subgroup oleh GM Sendiri di Descendant Node Penugasan: Baris Pola GM Tetap Terbentuk, GM Lain yang Tidak Mencakup Parent Tidak Menerima"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1294
coverage:
  web: automated
---

# Create Subgroup oleh GM Sendiri di Descendant Node Penugasan: Baris Pola GM Tetap Terbentuk, GM Lain yang Tidak Mencakup Parent Tidak Menerima

## Prerequisites

- Mode: FE+BE.
- Akun aktor: gmPattern Pre-setup No 28 `gmPattern_automated_{namaCompany}@qwertysystem.net` (tier Group Manager di `GM Pattern Parent {runId}-291`), password `Spectra.env.FA_GRP_GMPATTERN_PASSWORD` (nama env baru yang diusulkan, mengikuti pola `FA_GRP_*`; didaftarkan pemilik repo e2e di `executionConfig.environmentVariables` dan `.env.example`, lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): gmPatternOther Pre-setup No 30 `gmPatternOther_automated_{namaCompany}@qwertysystem.net` (tier Group Manager di `GM Pattern Other {runId}-291` saja). Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan No 21, di-seed lewat sesi API aktor Total Control Pre-setup No 1 (`Spectra.env.FA_TC_PASSWORD`) hanya untuk seeding di hook `before`, dihapus di hook `after`): `GM Pattern Parent {runId}-291` (Function None, level 1) dengan descendant `GM Pattern Child {runId}-291` (Assignable) dan `GM Pattern Other {runId}-291` (Assignable, level 1). Penugasan Group Manager dan baris pola GM yang sudah terbentuk (`FARP-LOGIC-04i`) di-seed lewat API: gmPattern di Parent dan baris pola di Parent dan Child; gmPatternOther di `GM Pattern Other {runId}-291` saja. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan GM dilepas di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec: `GM Sub B {runId}-291` di bawah `GM Pattern Child {runId}-291` (dihapus di hook `after` lewat API).
- State client: Addon Audit tidak berlisensi (dipastikan fixture BE yang disediakan tim FE/BE, tidak diubah oleh spec ini).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role, tab Transaction Role, dan tab Group Manager (Settings > Role & Permission) per node dan per user, serta log Role & Permission (Action dan Modified By per entri). Node memakai nama bersuffix unik sehingga baseline entri log untuk penanda nama node adalah nol (S-12).

## Test Steps

1. Klik (⋯) pada node `GM Pattern Child {runId}-291` di sidebar
2. Klik `Add Subgroup`
3. Isi Group Name `GM Sub B {runId}-291`
4. Klik [Submit]
5. Verifikasi toast sukses `Success, group has been created.`
6. Baca tab Group Role dan tab Transaction Role user gmPattern pada `GM Sub B {runId}-291` lewat kemampuan baca modul Role & Permission
7. Verifikasi pada `GM Sub B {runId}-291`, user gmPattern memiliki baris pola Group Manager untuk seluruh Group Role katalog kecuali `Manage user & role` dengan CRUD penuh sesuai kolom yang berlaku
8. Verifikasi pada `GM Sub B {runId}-291`, user gmPattern memiliki baris `Asset Admin` dan `Approver` pada setiap Jenis Transaksi (sembilan, termasuk Addon yang lisensinya belum aktif)
9. Baca tab Group Manager user gmPattern lewat kemampuan baca modul Role & Permission
10. Verifikasi penugasan Group Manager gmPattern hanya pada `GM Pattern Parent {runId}-291` (ancestor), bukan pada `GM Pattern Child {runId}-291`, sehingga baris pola pada `GM Sub B {runId}-291` berasal dari penugasan pada ancestor yang mencakup parent
11. Verifikasi baris pola GM pada `GM Sub B {runId}-291` terbentuk untuk gmPattern sendiri sebagai pembuat Subgroup (aktor sesi ini adalah gmPattern)
12. Baca log Role & Permission untuk `GM Sub B {runId}-291`
13. Verifikasi Modified By entri `Assign` pada `GM Sub B {runId}-291` adalah gmPattern (format `[First Name] [Last Initial]`)
14. Verifikasi log memuat satu entri `Assign` biasa per baris pola GM gmPattern yang dibaca pada langkah 6
15. Baca tab Group Role dan tab Transaction Role user gmPatternOther pada `GM Sub B {runId}-291` lewat kemampuan baca modul Role & Permission
16. Verifikasi user gmPatternOther tidak memiliki baris Group Role pada `GM Sub B {runId}-291` (anchor: baris pola gmPattern pada node yang sama tampil, langkah 7)
17. Verifikasi user gmPatternOther tidak memiliki baris Transaction Role pada `GM Sub B {runId}-291`

## Notes

- Spec memiliki 17 langkah. Aktor GM (bukan Total Control) membuat Subgroup agar jalur "baris pola tidak bergantung pada aktor" (`FARP-LOGIC-09`) teramati.
- Langkah penghubung (S-03): langkah 6, 9, 12, dan 15 (observasi lewat kemampuan baca).
- Pembagian TC lintas spec: TC-1294 muncul di `sourceTc` spec ini dan spec 292 (absence, S-05). Spec ini mengasersi presence (toast, baris pola gmPattern, Modified By, entri `Assign`, dan gmPatternOther tanpa baris Group Role/Transaction Role). Asersi tidak adanya notifikasi in-app ke gmPattern (Expected c) dan tidak adanya entri log untuk gmPatternOther (Expected e) ada di spec 292 dengan baseline sendiri.
- Temuan untuk QA:
  - Email Pre-setup No 28 dan No 30 belum punya nilai nyata (TC: perlu data tim FE/QA). Usulan env baru `FA_GRP_GMPATTERN_PASSWORD` untuk login gmPattern perlu didaftarkan pemilik repo e2e (di luar suite); akun gmPatternOther hanya dibaca.
  - TC-1294 langkah 3 dan 4 membaca Role & Permission, log, dan notifikasi oleh aktor Group Manager yang tidak jelas berhak membuka modul itu (sama dengan temuan spec 020 dan 285); spec memakai kemampuan baca yang disediakan tim FE/BE.
  - Mekanisme seeding penugasan GM dan baris pola yang sudah terbentuk tidak ditegaskan di TC; ditulis sebagai kemampuan tim FE/BE tanpa endpoint karangan.
  - TC-1294 Expected b menyebut Jenis Transaksi Addon yang lisensinya belum aktif; tampilan UI tab Transaction Role untuk Addon tak berlisensi belum terverifikasi, spec membaca daftar sembilan Jenis lewat kemampuan baca.
