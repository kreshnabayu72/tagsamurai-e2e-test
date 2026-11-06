---
id: TC-FA-GRP-E2E-306-absence-delete-node-di-bawah-ancestor-ber-transaction-role-tanpa-entri-remove-dan-tanpa-notifikasi-in-app
title: "Absence Delete Node di Bawah Ancestor Ber-Transaction Role: Tanpa Entri Remove untuk trxAnc dan Tanpa Notifikasi In-App"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1303
coverage:
  web: automated
---

# Absence Delete Node di Bawah Ancestor Ber-Transaction Role: Tanpa Entri Remove untuk trxAnc dan Tanpa Notifikasi In-App

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Penerima yang diamati (hanya dibaca, tidak login): trxAnc Pre-setup No 33 `trxAnc_automated_{namaCompany}@qwertysystem.net` (`Fixture.groupsTrxAnc.email`), pemegang Transaction Role approver Transfer di ancestor, tanpa Group Role dan tanpa Group Manager. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (salinan kedua pohon Trx, terpisah dari spec 305 karena node spec itu sudah terhapus; Pre-setup tambahan No 23, tanpa aset aktif, di-seed lewat sesi API aktor di hook `before`, sisa dihapus di hook `after`): `Trx Anc Root {runId}-306` (Function None, level 1) > `Trx Anc Mid {runId}-306` (Assignable) > `Trx Anc Leaf {runId}-306` (Assignable), serta `Trx Sub A {runId}-306` dan `Trx Imp Sub {runId}-306` (Assignable) di bawah `Trx Anc Mid {runId}-306`. Penugasan Transaction Role approver Transfer trxAnc di-seed lewat API tepat di `Trx Anc Root {runId}-306`. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas dan sisa node (Trx Anc Root) dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca log Role & Permission dan Changelog: User (Action dan jumlah entri per user), membaca Changelog: Group per node termasuk node terhapus, membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11). Baseline jumlah entri log dan Changelog: User dibaca lewat kemampuan yang sama (audit trail tidak diturunkan dari seeding, 8b butir 10).

## Test Steps

1. Catat baseline sebelum pemicu: jumlah entri `Remove` dan `Remove (Group Deleted)` untuk trxAnc pada log Role & Permission, jumlah entri yang sama pada Changelog: User trxAnc, dan jumlah notifikasi in-app trxAnc
2. Ketik Search `Trx Anc Mid {runId}-306`, tekan Enter
3. Buka elipsis `Trx Anc Mid {runId}-306`, pilih Delete
4. Verifikasi dialog dengan title "Delete Group" dan bullet `Trx Anc Mid {runId}-306` (anchor: Delete diproses)
5. Klik [Delete]
6. Verifikasi toast sukses `Success, group has been deleted.`
7. Baca Changelog: Group untuk `Trx Anc Mid {runId}-306`, `Trx Anc Leaf {runId}-306`, `Trx Sub A {runId}-306`, dan `Trx Imp Sub {runId}-306`
8. Verifikasi Changelog: Group memuat baris `Delete` untuk masing-masing dari keempat node (anchor: Delete diproses dan tercatat)
9. Baca log Role & Permission dan Changelog: User untuk trxAnc
10. Verifikasi jumlah entri `Remove` dan `Remove (Group Deleted)` untuk trxAnc pada log Role & Permission sama dengan baseline langkah 1 (tidak ada baris trxAnc pada node yang terhapus)
11. Verifikasi jumlah entri `Remove` dan `Remove (Group Deleted)` pada Changelog: User trxAnc sama dengan baseline langkah 1
12. Tunggu 5 detik tanpa memuat ulang halaman
13. Verifikasi jumlah notifikasi in-app trxAnc sama dengan baseline langkah 1
14. Klik `(←)` pada kotak Search

## Notes

- Spec memiliki 14 langkah. Langkah penghubung (S-03): langkah 2 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 7 dan 9 (observasi lewat kemampuan baca), langkah 12 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11), dan langkah 14 (menutup Search).
- Pembagian TC lintas spec (S-05): TC-1303 muncul di `sourceTc` spec ini dan spec 305 (spec asal). Spec ini memuat aksi nyata (Delete pada salinan node bersuffix `-306`, karena node spec 305 sudah terhapus; tidak dilipat ke spec asal agar asersi absence tidak bercampur dengan asersi presence) dengan baseline sendiri untuk bagian absence TC-1303 Expected d: tidak ada entri `Remove` atau `Remove (Group Deleted)` untuk trxAnc di log Role & Permission dan Changelog: User, serta tidak ada notifikasi in-app. Dialog normal, toast, penugasan ancestor tetap, dan seluruh subtree terhapus diasersi di spec 305.
- Temuan untuk QA:
  - TC-1303 langkah 5 membuka log Role & Permission, Changelog: User, dan notifikasi in-app trxAnc tanpa menyebut aktor atau cara membukanya; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-1303 tidak memberi Expected positif untuk log trxAnc (tidak ada entri yang diharapkan); anchor langkah 8 memakai baris `Delete` pada Changelog: Group sebagai bukti Delete diproses dan tercatat, bukan anchor di surface log yang sama.
  - TC tidak menyediakan Pre-setup terpisah untuk spec absence Delete; salinan node `-306` dibuat dinamis dari Dinamis No 23. Perlu konfirmasi bila absence Delete lebih baik dilipat ke spec 305 (menyimpang dari S-05).
  - TC-1303 precondition memakai `Trx Sub A` dan `Trx Imp Sub` hasil TC-1301 dan TC-1302; spec membuatnya lewat seeding API dengan nama bersuffix `{runId}-306` (S-06, R-06).
  - Email Pre-setup No 33 (trxAnc) belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan Transaction Role tidak ditegaskan di TC.
