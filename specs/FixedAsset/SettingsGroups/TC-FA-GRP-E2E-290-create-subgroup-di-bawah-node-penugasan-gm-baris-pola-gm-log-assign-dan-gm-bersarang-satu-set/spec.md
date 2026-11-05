---
id: TC-FA-GRP-E2E-290-create-subgroup-di-bawah-node-penugasan-gm-baris-pola-gm-log-assign-dan-gm-bersarang-satu-set
title: "Create Subgroup di Bawah Node Penugasan Group Manager: Baris Pola GM Terbentuk, Log Assign Biasa, dan GM Bersarang Memegang Satu Set Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1293
  - TC-FA-GRP-1295
coverage:
  web: automated
---

# Create Subgroup di Bawah Node Penugasan Group Manager: Baris Pola GM Terbentuk, Log Assign Biasa, dan GM Bersarang Memegang Satu Set Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user GM yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): gmPattern Pre-setup No 28 `gmPattern_automated_{namaCompany}@qwertysystem.net` (TC-FA-GRP-1293) dan gmPatternNested Pre-setup No 29 `gmPatternNested_automated_{namaCompany}@qwertysystem.net` (TC-FA-GRP-1295). Nilai email nyata kedua akun belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 21, di-seed lewat sesi API aktor di hook `before` dan dihapus di hook `after`): `GM Pattern Parent {runId}-290` (Function None, level 1) dengan descendant `GM Pattern Child {runId}-290` (Assignable). Penugasan Group Manager dan baris pola GM yang sudah terbentuk (`FARP-LOGIC-04i`) di-seed lewat API di hook `before`: gmPattern ber-tier Group Manager di `GM Pattern Parent {runId}-290` dengan baris pola GM di Parent dan Child; gmPatternNested ber-tier Group Manager di Parent dan di Child. Mekanisme seeding penugasan GM dan baris pola disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan GM dilepas di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (dihapus di hook `after` lewat API):

| TC | Nama dibuat | Induk |
|---|---|---|
| TC-FA-GRP-1293 | `GM Sub A {runId}-290` | `GM Pattern Parent {runId}-290` |
| TC-FA-GRP-1295 | `GM Sub C {runId}-290` | `GM Pattern Child {runId}-290` |

- State client: Addon Audit tidak berlisensi (precondition TC-FA-GRP-1293; dipastikan fixture BE yang disediakan tim FE/BE, tidak diubah oleh spec ini).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role, tab Transaction Role, dan tab Group Manager (Settings > Role & Permission) per node dan per user termasuk daftar Jenis Transaksi untuk tipe Addon yang belum berlisensi; membaca log Role & Permission (Action dan Modified By per entri); dan membaca Changelog: Group. Node memakai nama bersuffix unik sehingga baseline entri log untuk penanda nama node adalah nol (S-12).

## Test Steps

### TC-FA-GRP-1293: Create Subgroup di bawah node penugasan Group Manager

1. Klik (⋯) pada node `GM Pattern Parent {runId}-290` di sidebar
2. Klik `Add Subgroup`
3. Isi Group Name `GM Sub A {runId}-290`
4. Klik [Submit]
5. Verifikasi toast sukses `Success, group has been created.`
6. Baca tab Group Role dan tab Transaction Role user gmPattern pada `GM Sub A {runId}-290` lewat kemampuan baca modul Role & Permission
7. Verifikasi pada `GM Sub A {runId}-290`, user gmPattern memiliki baris pola Group Manager untuk seluruh Group Role katalog kecuali `Manage user & role` dengan CRUD penuh sesuai kolom yang berlaku
8. Verifikasi pada `GM Sub A {runId}-290`, user gmPattern memiliki baris `Asset Admin` dan `Approver` pada setiap Jenis Transaksi (sembilan, termasuk Addon yang lisensinya belum aktif)
9. Verifikasi tidak ada baris `Manage user & role` untuk user gmPattern pada `GM Sub A {runId}-290`
10. Verifikasi baris pola GM sudah terbentuk pada pembacaan pertama sesudah toast sukses Create (tidak ada kondisi `GM Sub A {runId}-290` tanpa baris pola GM)
11. Baca tab Group Manager user gmPattern lewat kemampuan baca modul Role & Permission
12. Verifikasi penugasan Group Manager gmPattern tetap pada `GM Pattern Parent {runId}-290` dan tidak ada penugasan Group Manager baru pada `GM Sub A {runId}-290`
13. Verifikasi tier Group Manager gmPattern tetap terpasang (tidak terlepas)
14. Baca log Role & Permission untuk `GM Sub A {runId}-290`
15. Verifikasi log memuat satu entri `Assign` biasa per baris pola GM yang dibaca pada langkah 6 (bukan `Assign (via Group Manager)`)
16. Verifikasi Modified By entri `Assign` adalah pembuat Subgroup, yaitu aktor Total Control (format `[First Name] [Last Initial]`)
17. Buka Changelog: Group untuk `GM Sub A {runId}-290`
18. Verifikasi Changelog: Group memuat baris `Create` `GM Sub A {runId}-290`

### TC-FA-GRP-1295: Create Subgroup untuk user dengan dua penugasan GM yang mencakup parent

19. Klik (⋯) pada node `GM Pattern Child {runId}-290` di sidebar
20. Klik `Add Subgroup`
21. Isi Group Name `GM Sub C {runId}-290`
22. Klik [Submit]
23. Verifikasi toast sukses `Success, group has been created.`
24. Baca tab Group Role dan tab Transaction Role user gmPatternNested pada `GM Sub C {runId}-290` lewat kemampuan baca modul Role & Permission
25. Verifikasi pada `GM Sub C {runId}-290`, setiap Group Role katalog (kecuali `Manage user & role`) untuk gmPatternNested tepat satu baris
26. Verifikasi pada `GM Sub C {runId}-290`, setiap pasangan (Jenis Transaksi, `Asset Admin`/`Approver`) untuk gmPatternNested tepat satu baris, tidak ada baris ganda per penugasan GM
27. Baca log Role & Permission untuk `GM Sub C {runId}-290`
28. Verifikasi log memuat satu entri `Assign` biasa per baris pola yang dibaca pada langkah 24 (tidak digandakan per penugasan GM)
29. Verifikasi Modified By entri `Assign` adalah pembuat Subgroup, yaitu aktor Total Control

## Notes

- Spec memiliki 29 langkah, di bawah batas 35 langkah. Dua TC satu topik (Create Subgroup di bawah node penugasan GM) dengan akun GM yang berbeda; tiap TC berdiri sendiri dengan node bersuffix sendiri.
- Langkah penghubung (S-03): langkah 6, 11, 14, 24, dan 27 (observasi lewat kemampuan baca) dan langkah 17 (membuka Changelog: Group).
- Pembagian TC lintas spec: TC-1293 muncul di `sourceTc` spec ini dan spec 292 (absence, S-05); TC-1295 hanya di spec ini. Spec ini mengasersi presence: toast, baris pola GM, penugasan GM tetap, entri `Assign` biasa beserta Modified By, dan baris `Create` pada Changelog: Group (TC-1293); satu set baris tanpa ganda (TC-1295). Asersi tidak adanya notifikasi in-app ke gmPattern, tidak adanya entri `Auto-Revert`, dan Changelog: Group yang hanya memuat baris `Create` (TC-1293 Expected c, d, f) ada di spec 292 dengan baseline sendiri. TC-1296 (Create Group level 1) ada di spec 298 dan spec 292.
- Temuan untuk QA:
  - Email Pre-setup No 28 sampai 32 belum punya nilai nyata (TC: perlu data tim FE/QA); spec memakai pola email Pre-setup dan fixture `Fixture.groupsGmPattern.*` yang ditetapkan tim FE.
  - Pembentukan baris pola GM yang sudah ada (precondition TC-1293 dan TC-1295) tidak punya mekanisme seeding yang ditegaskan di TC; spec menuliskannya sebagai kemampuan seeding tim FE/BE tanpa endpoint karangan.
  - TC-1293 Expected b menyebut Jenis Transaksi Addon yang lisensinya belum aktif (sembilan jenis); belum diverifikasi apakah tab Transaction Role di UI menampilkan Jenis Transaksi Addon tak berlisensi. Spec membaca daftar sembilan Jenis lewat kemampuan baca dan tidak mengasersi tampilan UI-nya.
  - TC-1293 Expected e ("transaksi yang sama dengan Create") tidak teramati langsung dari UI; spec mengasersi hasil yang teramati (baris pola ada pada pembacaan pertama).
  - TC-1293 langkah 5 membuka notifikasi in-app gmPattern tanpa menyebut cara membukanya; asersinya ada di spec 292 lewat kemampuan baca.
  - NC-12 (Menunggu konfirmasi, PRD FAGRP-LOGIC-03k): efek baris pola GM pada guard Delete kondisi 5 dan Total User belum final; spec ini tidak mengasersi keduanya.
  - Frasa "CRUD penuh sesuai kolom yang berlaku" (Expected b) tidak merinci kolom per Group Role; spec mengasersi CRUD penuh sesuai kolom yang tampil di tab Group Role.
