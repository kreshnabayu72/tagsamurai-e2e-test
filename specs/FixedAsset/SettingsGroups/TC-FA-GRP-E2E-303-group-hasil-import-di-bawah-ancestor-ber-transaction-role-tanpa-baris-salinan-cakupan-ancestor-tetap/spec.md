---
id: TC-FA-GRP-E2E-303-group-hasil-import-di-bawah-ancestor-ber-transaction-role-tanpa-baris-salinan-cakupan-ancestor-tetap
title: "Group Hasil Import di Bawah Node yang Ancestor-nya Punya Penugasan Transaction Role: Tanpa Baris Salinan, Cakupan Ancestor Tetap Berlaku"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1302
coverage:
  web: automated
---

# Group Hasil Import di Bawah Node yang Ancestor-nya Punya Penugasan Transaction Role: Tanpa Baris Salinan, Cakupan Ancestor Tetap Berlaku

## Prerequisites

- Mode: FE+BE.
- Akun aktor: user ber-Global Role Import Data (bukan Total Control dan bukan Default User), `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD` (sama dengan spec 287 dan 296). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user yang diamati (hanya dibaca, tidak login): trxAnc Pre-setup No 33 `trxAnc_automated_{namaCompany}@qwertysystem.net` (`Fixture.groupsTrxAnc.email`), pemegang Transaction Role approver Transfer di ancestor, tanpa Group Role dan tanpa Group Manager. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 23, tanpa aset, di-seed lewat sesi API aktor Total Control hanya untuk seeding di hook `before`, dihapus di hook `after`): `Trx Anc Root {runId}-303` (Function None, level 1) > `Trx Anc Mid {runId}-303` (Assignable) > `Trx Anc Leaf {runId}-303` (Assignable). Penugasan Transaction Role approver Transfer trxAnc di-seed lewat API tepat di `Trx Anc Root {runId}-303`. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas dan seluruh node dihapus di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (dihapus di hook `after` lewat API): berkas Import Group `Fixture.groupsImport.trxImpSub` memuat group `Trx Imp Sub {runId}-303` dengan parent `Trx Anc Mid {runId}-303`. Kemampuan import Group untuk importer disediakan tim FE/BE (alur dan berkas tidak ada di TC, PRD, atau LLD, S-13).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Transaction Role per user dan per node di Settings > Role & Permission dengan sidebar Group Tree, dan membaca induk sebuah group lewat fixture BE.

## Test Steps

1. Baca tab Transaction Role user trxAnc pada `Trx Anc Root {runId}-303`, `Trx Anc Mid {runId}-303`, dan `Trx Anc Leaf {runId}-303` lewat kemampuan baca modul Role & Permission
2. Verifikasi `Trx Anc Root {runId}-303` memuat tepat satu baris approver Transfer trxAnc, sedangkan Mid dan Leaf tidak memuat baris trxAnc (precondition terpenuhi)
3. Buka modul Import, unggah berkas Group `Fixture.groupsImport.trxImpSub`
4. Jalankan import
5. Tunggu aksi selesai
6. Buka Fixed Asset > Settings > Groups
7. Ketik Search `Trx Imp Sub {runId}-303`, tekan Enter
8. Verifikasi baris `Trx Imp Sub {runId}-303` tampil pada Groups List (group hasil Import terbentuk)
9. Baca induk group `Trx Imp Sub {runId}-303` lewat fixture BE
10. Verifikasi induk `Trx Imp Sub {runId}-303` adalah `Trx Anc Mid {runId}-303`
11. Klik `(←)` pada kotak Search
12. Baca tab Transaction Role user trxAnc pada `Trx Anc Root {runId}-303` lewat kemampuan baca modul Role & Permission
13. Verifikasi `Trx Anc Root {runId}-303` tetap memuat tepat satu baris approver Transfer trxAnc (anchor untuk asersi tanpa baris di tab yang sama)
14. Baca tab Transaction Role user trxAnc pada `Trx Imp Sub {runId}-303` (pilih node di sidebar Group Tree)
15. Verifikasi tab Transaction Role trxAnc pada `Trx Imp Sub {runId}-303` tidak memuat baris (tabel literal pada node penugasan)
16. Verifikasi Import tidak menyalin penugasan parent untuk user non-TC/RO: tidak ada baris trxAnc di `Trx Imp Sub {runId}-303`, sehingga cakupan penugasan Transaction Role ancestor atas `Trx Imp Sub {runId}-303` tidak diwujudkan sebagai baris tambahan

## Notes

- Spec memiliki 16 langkah. Langkah penghubung (S-03): langkah 1, 9, 12, dan 14 (observasi lewat kemampuan baca), langkah 5 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), langkah 6 dan 7 (membuka Groups dan Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), dan langkah 11 (menutup Search).
- Pembagian TC lintas spec (S-05): TC-1302 muncul di `sourceTc` spec ini dan spec 304 (absence). Spec ini mengasersi Expected a, b, dan c. Asersi tidak adanya entri `Assign` untuk trxAnc dan tidak adanya notifikasi in-app (Expected d) ada di spec 304 dengan baseline sendiri. Hak efektif approver pada node baru tidak diuji di modul ini.
- Temuan untuk QA:
  - TC-1302 langkah 2 dan 3 membaca Settings > Role & Permission, log, dan notifikasi tanpa menyebut aktor; importer (Global Role Import Data) tidak jelas berhak membuka modul Role & Permission (sama dengan temuan TC-1292). Spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-1302 langkah 1 tidak merinci alur modul Import (menu, berkas, parent Trx Anc Mid di berkas); berkas `Fixture.groupsImport.trxImpSub` adalah fixture yang disediakan tim FE/BE (S-13). Akun importer tidak ada di Pre-setup TC.
  - TC-1302 tidak menyebut apa yang tampil di modul Import sesudah import sukses; spec tidak mengasersi pesan modul Import. Langkah 8 sampai 10 adalah anchor penghubung untuk Expected a.
  - Email Pre-setup No 33 (trxAnc) belum punya nilai nyata (TC: perlu data tim FE/QA).
  - TC memakai nama literal `Trx Imp Sub` dan Dinamis No 23 sebagai pre-setup bersama; spec memakai salinan bersuffix `{runId}-303` yang di-seed sendiri (R-06, S-06).
  - Mekanisme seeding penugasan Transaction Role tidak ditegaskan di TC; ditulis sebagai kemampuan tim FE/BE tanpa endpoint karangan.
