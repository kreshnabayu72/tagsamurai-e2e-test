---
id: TC-FA-GRP-E2E-296-group-hasil-import-di-bawah-node-tercakup-gm-baris-pola-gm-atomik-dan-group-level-1-tanpa-baris-pola
title: "Group Hasil Import di Bawah Node Tercakup GM: Baris Pola GM Ditulis Atomik, Group Level 1 Hasil Import Tanpa Baris Pola GM"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1300
coverage:
  web: automated
---

# Group Hasil Import di Bawah Node Tercakup GM: Baris Pola GM Ditulis Atomik, Group Level 1 Hasil Import Tanpa Baris Pola GM

## Prerequisites

- Mode: FE+BE.
- Akun aktor: user ber-Global Role Import Data (bukan Total Control dan bukan Default User), `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD` (sama dengan spec 287). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user GM yang diamati (hanya dibaca, tidak login): gmPattern Pre-setup No 28, gmPatternNested Pre-setup No 29, dan gmPatternOther Pre-setup No 30, masing-masing `<nama>_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 21, di-seed lewat sesi API aktor Total Control hanya untuk seeding di hook `before`, dihapus di hook `after`): `GM Pattern Parent {runId}-296` (Function None, level 1) > `GM Pattern Child {runId}-296` (Assignable) dan `GM Pattern Other {runId}-296` (Assignable, level 1). Penugasan Group Manager di-seed lewat API: gmPattern di Parent; gmPatternNested di Parent dan Child; gmPatternOther di Other; baris pola GM yang sudah terbentuk di node-node itu. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (dihapus di hook `after`): berkas Import Group `Fixture.groupsGmPattern.importSub` memuat group `GM Imp Sub {runId}-296` dengan parent `GM Pattern Child {runId}-296`, dan berkas `Fixture.groupsGmPattern.importRoot` memuat group `GM Imp Root {runId}-296` (level 1). Kemampuan import Group untuk importer disediakan tim FE/BE (alur dan berkas tidak ada di TC, PRD, atau LLD, S-13).
- State client: Addon Audit tidak berlisensi (dipastikan fixture BE yang disediakan tim FE/BE, tidak diubah oleh spec ini).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role, tab Transaction Role, dan tab Group Manager (Settings > Role & Permission) per node dan per user, serta log Role & Permission (Action dan Modified By per entri). Node memakai nama bersuffix unik sehingga baseline entri log untuk penanda nama node adalah nol (S-12).

## Test Steps

1. Baca tab Group Manager user gmPattern, gmPatternNested, dan gmPatternOther lewat kemampuan baca modul Role & Permission, lalu catat penugasan Group Manager masing-masing sebagai baseline
2. Buka modul Import, unggah berkas Group `Fixture.groupsGmPattern.importSub`
3. Jalankan import
4. Tunggu aksi selesai
5. Buka modul Import, unggah berkas Group `Fixture.groupsGmPattern.importRoot`
6. Jalankan import
7. Tunggu aksi selesai
8. Baca tab Group Role dan tab Transaction Role user gmPattern, gmPatternNested, dan gmPatternOther pada `GM Imp Sub {runId}-296` lewat kemampuan baca modul Role & Permission
9. Verifikasi pada `GM Imp Sub {runId}-296`, user gmPattern memiliki baris pola Group Manager untuk seluruh Group Role katalog kecuali `Manage user & role` dengan CRUD penuh sesuai kolom yang berlaku
10. Verifikasi pada `GM Imp Sub {runId}-296`, user gmPattern memiliki baris `Asset Admin` dan `Approver` pada setiap Jenis Transaksi (tujuh, termasuk Addon yang lisensinya belum aktif)
11. Verifikasi pada `GM Imp Sub {runId}-296`, user gmPatternNested memiliki satu set baris pola GM (setiap Group Role katalog dan setiap pasangan Jenis Transaksi dengan `Asset Admin`/`Approver` tepat satu baris, tidak ganda) sama seperti Subgroup manual
12. Verifikasi user gmPatternOther tidak memiliki baris Group Role maupun Transaction Role pada `GM Imp Sub {runId}-296` (anchor: baris pola gmPattern pada node yang sama tampil, langkah 9)
13. Baca tab Group Role dan tab Transaction Role ketiga user GM pada `GM Imp Root {runId}-296`
14. Verifikasi pada `GM Imp Root {runId}-296`, baris pola Total Control tampil (anchor: Import diproses dan baris pola TC/RO terbentuk)
15. Verifikasi ketiga user GM tidak memiliki baris Group Role maupun Transaction Role pada `GM Imp Root {runId}-296`
16. Baca log Role & Permission untuk `GM Imp Sub {runId}-296`
17. Verifikasi log memuat satu entri `Assign` biasa per baris pola GM gmPattern dan gmPatternNested yang dibaca pada langkah 8 (bukan `Assign (via Group Manager)`)
18. Verifikasi Modified By entri `Assign` adalah pelaku Import, yaitu importer (format `[First Name] [Last Initial]`)
19. Baca tab Group Manager user gmPattern, gmPatternNested, dan gmPatternOther lewat kemampuan baca modul Role & Permission
20. Verifikasi penugasan Group Manager ketiga user sama dengan baseline langkah 1 (tidak berubah)

## Notes

- Spec memiliki 20 langkah. Langkah penghubung (S-03): langkah 4 dan 7 (tunggu aksi selesai sebelum membuka surface lain, 8b butir 8) dan langkah 1, 8, 13, 16, dan 19 (observasi lewat kemampuan baca).
- Pembagian TC lintas spec: TC-1300 muncul di `sourceTc` spec ini dan spec 297 (absence, S-05). Spec ini mengasersi presence (baris pola GM, set tunggal, gmPatternOther dan Group level 1 tanpa baris, entri `Assign`, Modified By, penugasan GM tidak berubah). Tidak adanya notifikasi in-app ke user GM, tidak adanya entri `Auto-Revert` (Expected c dan d bagian absence), dan kegagalan penulisan baris pola me-rollback group (Expected e) ada di spec 297 dengan baseline sendiri.
- Temuan untuk QA:
  - Email Pre-setup No 28 sampai 30 dan akun importer belum punya nilai nyata di TC; berkas Import `importSub` dan `importRoot` adalah fixture yang disediakan tim FE/BE.
  - TC-1300 langkah 3 dan 4 membaca Role & Permission, log, dan notifikasi oleh importer (Global Role Import Data) yang tidak jelas berhak membuka modul itu; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-1300 tidak menyebut apa yang tampil di modul Import sesudah import sukses; spec tidak mengasersi pesan modul Import.
  - TC-1300 Expected b mengasumsikan Group level 1 hasil Import tetap memuat baris pola Total Control (TC-1292); spec memakainya sebagai anchor, bukan sebagai asersi utama.
