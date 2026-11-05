---
id: TC-FA-GRP-E2E-305-delete-node-di-bawah-ancestor-ber-transaction-role-dialog-normal-penugasan-ancestor-tetap-subtree-terhapus
title: "Delete Node di Bawah Ancestor Ber-Transaction Role: Dialog Normal (Bukan D-15), Penugasan Ancestor Tetap, Seluruh Subtree Terhapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1303
coverage:
  web: automated
---

# Delete Node di Bawah Ancestor Ber-Transaction Role: Dialog Normal (Bukan D-15), Penugasan Ancestor Tetap, Seluruh Subtree Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): trxAnc Pre-setup No 33 `trxAnc_automated_{namaCompany}@qwertysystem.net` (`Fixture.groupsTrxAnc.email`), pemegang Transaction Role approver Transfer di ancestor, tanpa Group Role dan tanpa Group Manager. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 23, tanpa aset aktif, di-seed lewat sesi API aktor di hook `before`, sisa dihapus di hook `after`): `Trx Anc Root {runId}-305` (Function None, level 1) > `Trx Anc Mid {runId}-305` (Assignable) > `Trx Anc Leaf {runId}-305` (Assignable), serta `Trx Sub A {runId}-305` dan `Trx Imp Sub {runId}-305` (Assignable) di bawah `Trx Anc Mid {runId}-305`. Penugasan Transaction Role approver Transfer trxAnc di-seed lewat API tepat di `Trx Anc Root {runId}-305`; trxAnc tidak punya penugasan apa pun di Mid, Leaf, Trx Sub A, maupun Trx Imp Sub. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas dan sisa node (Trx Anc Root) dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Transaction Role per user dan per node di Settings > Role & Permission dengan sidebar Group Tree, dan membaca Changelog: Group per node termasuk node terhapus.

## Test Steps

1. Baca tab Transaction Role user trxAnc pada `Trx Anc Root {runId}-305` lewat kemampuan baca modul Role & Permission
2. Verifikasi `Trx Anc Root {runId}-305` memuat tepat satu baris approver Transfer trxAnc (precondition terpenuhi)
3. Ketik Search `Trx Anc Mid {runId}-305`, tekan Enter
4. Buka elipsis `Trx Anc Mid {runId}-305`, pilih Delete
5. Verifikasi dialog dengan title "Delete Group", bullet `Trx Anc Mid {runId}-305`, isi "Are you sure you want to delete it? This action cannot be undone." (bukan varian warning D-15; Transaction Role trxAnc di ancestor tidak dihitung kondisi 5)
6. Klik [Delete]
7. Verifikasi toast sukses `Success, group has been deleted.`
8. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Trx Anc Mid {runId}-305`
9. Ganti isi kotak search dengan `Trx Anc Leaf {runId}-305`, tekan Enter
10. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Trx Anc Leaf {runId}-305`
11. Ganti isi kotak search dengan `Trx Sub A {runId}-305`, tekan Enter
12. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Trx Sub A {runId}-305`
13. Ganti isi kotak search dengan `Trx Imp Sub {runId}-305`, tekan Enter
14. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Trx Imp Sub {runId}-305`
15. Ganti isi kotak search dengan `Trx Anc Root {runId}-305`, tekan Enter
16. Verifikasi Groups List memuat baris `Trx Anc Root {runId}-305` (Trx Anc Root tetap ada)
17. Klik `(←)` pada kotak Search
18. Baca tab Transaction Role user trxAnc pada `Trx Anc Root {runId}-305` lewat kemampuan baca modul Role & Permission
19. Verifikasi `Trx Anc Root {runId}-305` tetap memuat tepat satu baris approver Transfer trxAnc, nilai tidak berubah dibanding langkah 2 (penugasan Transaction Role di ancestor node yang dihapus tidak terpengaruh)
20. Baca Changelog: Group untuk `Trx Anc Mid {runId}-305`, `Trx Anc Leaf {runId}-305`, `Trx Sub A {runId}-305`, dan `Trx Imp Sub {runId}-305`
21. Verifikasi Changelog: Group memuat baris `Delete` untuk masing-masing dari keempat node terhapus

## Notes

- Spec memiliki 21 langkah. Langkah penghubung (S-03): langkah 1, 18, dan 20 (observasi lewat kemampuan baca), langkah 3, 9, 11, 13, dan 15 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), dan langkah 17 (menutup Search). Aksi hapus diletakkan sesudah pembacaan precondition (S-10).
- Pembagian TC lintas spec (S-05): TC-1303 muncul di `sourceTc` spec ini dan spec 306 (absence). Spec ini mengasersi Expected a, b, c, dan bagian presence Expected d ("Changelog: Group memuat baris `Delete` per node terhapus"). Bagian absence Expected d (tidak ada `Remove` atau `Remove (Group Deleted)` untuk trxAnc di log Role & Permission dan Changelog: User, tidak ada notifikasi in-app) ada di spec 306 dengan baseline sendiri.
- Temuan untuk QA:
  - TC-1303 langkah 4 dan 5 membaca Settings > Role & Permission, log, Changelog: User, dan notifikasi tanpa menyebut aktor; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-1303 precondition memakai `Trx Sub A` dan `Trx Imp Sub` hasil TC-1301 dan TC-1302, sedangkan spec harus mandiri (S-06). Spec membuat keduanya lewat seeding API dengan nama bersuffix `{runId}-305`; Expected b menyebut nama literal tanpa suffix (R-06). Perlu konfirmasi bahwa seeding sah dan bahwa `Trx Imp Sub` seeding setara hasil Import.
  - TC-1303 Expected d mencampur presence (`Delete` di Changelog: Group) dan absence (tanpa `Remove`, tanpa notifikasi); spec membaginya ke spec 305 dan 306.
  - TC-1303 Expected a hanya menyebut bullet `Trx Anc Mid`; spec mengasersi bullet itu sesuai TC dan tidak menebak apakah bullet descendant (Leaf, Trx Sub A, Trx Imp Sub) ikut tampil.
  - Email Pre-setup No 33 (trxAnc) belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan Transaction Role tidak ditegaskan di TC.
