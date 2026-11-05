---
id: TC-FA-GRP-E2E-302-absence-create-subgroup-di-bawah-ancestor-ber-transaction-role-tanpa-entri-assign-dan-tanpa-notifikasi-in-app
title: "Absence Create Subgroup di Bawah Node Ber-Transaction Role Ancestor: Tanpa Entri Assign untuk trxAnc dan Tanpa Notifikasi In-App"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1301
coverage:
  web: automated
---

# Absence Create Subgroup di Bawah Node Ber-Transaction Role Ancestor: Tanpa Entri Assign untuk trxAnc dan Tanpa Notifikasi In-App

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Penerima yang diamati (hanya dibaca, tidak login): trxAnc Pre-setup No 33 `trxAnc_automated_{namaCompany}@qwertysystem.net` (`Fixture.groupsTrxAnc.email`), pemegang Transaction Role approver Transfer di ancestor, tanpa Group Role dan tanpa Group Manager. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 23, tanpa aset, di-seed lewat sesi API aktor di hook `before`, dihapus di hook `after`): `Trx Anc Root {runId}-302` (Function None, level 1) > `Trx Anc Mid {runId}-302` (Assignable) > `Trx Anc Leaf {runId}-302` (Assignable). Penugasan Transaction Role approver Transfer trxAnc di-seed lewat API tepat di `Trx Anc Root {runId}-302`. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas dan seluruh node dihapus di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (dihapus di hook `after` lewat API): `Trx Abs Sub {runId}-302` di bawah `Trx Anc Mid {runId}-302`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca log Role & Permission (Action dan jumlah entri per user dan per node), membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11).

## Test Steps

1. Catat baseline sebelum pemicu: jumlah entri `Assign` untuk trxAnc pada log Role & Permission dan jumlah notifikasi in-app trxAnc
2. Ketik Search `Trx Anc Mid {runId}-302`, tekan Enter
3. Klik (⋯) pada baris `Trx Anc Mid {runId}-302`
4. Klik `Add Subgroup`
5. Isi Group Name `Trx Abs Sub {runId}-302`
6. Klik [Submit]
7. Verifikasi toast sukses `Success, group has been created.`
8. Baca log Role & Permission untuk `Trx Abs Sub {runId}-302`
9. Verifikasi log memuat entri `Assign` untuk baris pola Total Control/Read Only pada `Trx Abs Sub {runId}-302` (anchor: Create diproses dan log tercatat)
10. Verifikasi jumlah entri `Assign` untuk trxAnc sama dengan baseline langkah 1 (log tidak memuat entri `Assign` untuk trxAnc dari Create ini)
11. Tunggu 5 detik tanpa memuat ulang halaman
12. Verifikasi jumlah notifikasi in-app trxAnc sama dengan baseline langkah 1
13. Klik `(←)` pada kotak Search

## Notes

- Spec memiliki 13 langkah. Langkah penghubung (S-03): langkah 2 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 3 dan 4 (membuka menu Add Subgroup), langkah 8 (observasi lewat kemampuan baca), langkah 11 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11), dan langkah 13 (menutup Search).
- Pembagian TC lintas spec (S-05): TC-1301 muncul di `sourceTc` spec ini dan spec 301 (spec asal). Spec ini memuat aksi nyata (Create Subgroup `Trx Abs Sub`) dengan baseline sendiri untuk TC-1301 Expected e: tidak ada entri `Assign` untuk trxAnc dan tidak ada notifikasi in-app ke trxAnc. Presence (toast, tidak ada baris salinan di tab Transaction Role, baris tetap di Trx Anc Root, Total User) diasersi di spec 301.
- Temuan untuk QA:
  - TC-1301 langkah 4 membuka log Role & Permission dan notifikasi in-app trxAnc tanpa menyebut aktor atau cara membukanya; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - Anchor langkah 9 (entri `Assign` untuk baris pola Total Control/Read Only pada node baru) diturunkan dari TC-1289; TC-1301 tidak memberi Expected positif untuk log.
  - Email Pre-setup No 33 (trxAnc) belum punya nilai nyata (TC: perlu data tim FE/QA).
  - TC memakai nama literal dan Dinamis No 23 sebagai pre-setup bersama; spec memakai salinan bersuffix `{runId}-302` yang di-seed sendiri (R-06, S-06).
  - Mekanisme seeding penugasan Transaction Role tidak ditegaskan di TC; ditulis sebagai kemampuan tim FE/BE tanpa endpoint karangan.
