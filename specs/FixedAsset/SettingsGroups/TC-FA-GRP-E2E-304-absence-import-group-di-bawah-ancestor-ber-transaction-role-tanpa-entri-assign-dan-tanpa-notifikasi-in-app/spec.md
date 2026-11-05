---
id: TC-FA-GRP-E2E-304-absence-import-group-di-bawah-ancestor-ber-transaction-role-tanpa-entri-assign-dan-tanpa-notifikasi-in-app
title: "Absence Import Group di Bawah Node Ber-Transaction Role Ancestor: Tanpa Entri Assign untuk trxAnc dan Tanpa Notifikasi In-App"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1302
coverage:
  web: automated
---

# Absence Import Group di Bawah Node Ber-Transaction Role Ancestor: Tanpa Entri Assign untuk trxAnc dan Tanpa Notifikasi In-App

## Prerequisites

- Mode: FE+BE.
- Akun aktor: user ber-Global Role Import Data (bukan Total Control dan bukan Default User), `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD` (sama dengan spec 287, 289, dan 303). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Penerima yang diamati (hanya dibaca, tidak login): trxAnc Pre-setup No 33 `trxAnc_automated_{namaCompany}@qwertysystem.net` (`Fixture.groupsTrxAnc.email`), pemegang Transaction Role approver Transfer di ancestor, tanpa Group Role dan tanpa Group Manager. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 23, tanpa aset, di-seed lewat sesi API aktor Total Control hanya untuk seeding di hook `before`, dihapus di hook `after`): `Trx Anc Root {runId}-304` (Function None, level 1) > `Trx Anc Mid {runId}-304` (Assignable) > `Trx Anc Leaf {runId}-304` (Assignable). Penugasan Transaction Role approver Transfer trxAnc di-seed lewat API tepat di `Trx Anc Root {runId}-304`. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas dan seluruh node dihapus di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (dihapus di hook `after` lewat API): berkas Import Group `Fixture.groupsImport.trxImpAbsen` memuat group `Trx Imp Abs {runId}-304` dengan parent `Trx Anc Mid {runId}-304`. Kemampuan import Group untuk importer disediakan tim FE/BE (alur dan berkas tidak ada di TC, PRD, atau LLD, S-13).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca log Role & Permission (Action dan jumlah entri per user dan per node), membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11).

## Test Steps

1. Catat baseline sebelum pemicu: jumlah entri `Assign` untuk trxAnc pada log Role & Permission dan jumlah notifikasi in-app trxAnc
2. Buka modul Import, unggah berkas Group `Fixture.groupsImport.trxImpAbsen`
3. Jalankan import
4. Tunggu aksi selesai
5. Baca log Role & Permission untuk `Trx Imp Abs {runId}-304`
6. Verifikasi log memuat entri `Assign` untuk baris pola Total Control/Read Only pada `Trx Imp Abs {runId}-304` (anchor: Import diproses dan log tercatat)
7. Verifikasi jumlah entri `Assign` untuk trxAnc sama dengan baseline langkah 1 (log tidak memuat entri `Assign` untuk trxAnc dari Import ini)
8. Tunggu 5 detik tanpa memuat ulang halaman
9. Verifikasi jumlah notifikasi in-app trxAnc sama dengan baseline langkah 1

## Notes

- Spec memiliki 9 langkah. Langkah penghubung (S-03): langkah 4 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), langkah 5 (observasi lewat kemampuan baca), dan langkah 8 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11).
- Pembagian TC lintas spec (S-05): TC-1302 muncul di `sourceTc` spec ini dan spec 303 (spec asal). Spec ini memuat aksi nyata (Import `Trx Imp Abs`) dengan baseline sendiri untuk TC-1302 Expected d: tidak ada entri `Assign` untuk trxAnc dan tidak ada notifikasi in-app ke trxAnc. Presence (group terbentuk di bawah Trx Anc Mid, tidak ada baris salinan, baris tetap di Trx Anc Root) diasersi di spec 303.
- Temuan untuk QA:
  - TC-1302 langkah 3 membuka log Role & Permission dan notifikasi in-app trxAnc oleh importer (Global Role Import Data) tanpa menyebut aktor atau cara membukanya; importer tidak jelas berhak membuka modul itu. Spec memakai kemampuan baca yang disediakan tim FE/BE.
  - Alur modul Import tidak dirinci di TC; berkas `Fixture.groupsImport.trxImpAbsen` adalah fixture yang disediakan tim FE/BE. Akun importer tidak ada di Pre-setup TC.
  - Anchor langkah 6 (entri `Assign` untuk baris pola Total Control/Read Only pada group hasil Import) diturunkan dari TC-1292; TC-1302 tidak memberi Expected positif untuk log.
  - Email Pre-setup No 33 (trxAnc) belum punya nilai nyata (TC: perlu data tim FE/QA).
  - TC memakai nama literal dan Dinamis No 23 sebagai pre-setup bersama; spec memakai salinan bersuffix `{runId}-304` yang di-seed sendiri (R-06, S-06).
  - Mekanisme seeding penugasan Transaction Role tidak ditegaskan di TC; ditulis sebagai kemampuan tim FE/BE tanpa endpoint karangan.
