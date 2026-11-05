---
id: TC-FA-GRP-E2E-301-create-subgroup-di-bawah-ancestor-ber-transaction-role-tanpa-baris-salinan-baris-tetap-di-root-total-user-tidak-menghitung
title: "Create Subgroup di Bawah Node yang Ancestor-nya Punya Penugasan Transaction Role: Tanpa Baris Salinan untuk trxAnc, Baris Tetap di Trx Anc Root, Total User Tidak Menghitung"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1301
coverage:
  web: automated
---

# Create Subgroup di Bawah Node yang Ancestor-nya Punya Penugasan Transaction Role: Tanpa Baris Salinan untuk trxAnc, Baris Tetap di Trx Anc Root, Total User Tidak Menghitung

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): trxAnc Pre-setup No 33 `trxAnc_automated_{namaCompany}@qwertysystem.net` (`Fixture.groupsTrxAnc.email`), pemegang Transaction Role approver Transfer di ancestor, tanpa Group Role dan tanpa Group Manager. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 23, tanpa aset, di-seed lewat sesi API aktor di hook `before`, dihapus di hook `after`): `Trx Anc Root {runId}-301` (Function None, level 1) > `Trx Anc Mid {runId}-301` (Assignable) > `Trx Anc Leaf {runId}-301` (Assignable). Penugasan Transaction Role approver Transfer trxAnc di-seed lewat API tepat di `Trx Anc Root {runId}-301`; trxAnc tidak punya penugasan apa pun di Mid maupun Leaf. Mekanisme seeding penugasan disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas dan seluruh node dihapus di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (dihapus di hook `after` lewat API): `Trx Sub A {runId}-301` di bawah `Trx Anc Mid {runId}-301`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Transaction Role per user dan per node di Settings > Role & Permission dengan sidebar Group Tree. Aktor pembaca tidak disebut TC; spec memakai kemampuan baca yang disediakan tim FE/BE.

## Test Steps

1. Baca tab Transaction Role user trxAnc pada `Trx Anc Root {runId}-301`, `Trx Anc Mid {runId}-301`, dan `Trx Anc Leaf {runId}-301` lewat kemampuan baca modul Role & Permission
2. Verifikasi `Trx Anc Root {runId}-301` memuat tepat satu baris approver Transfer trxAnc, sedangkan Mid dan Leaf tidak memuat baris trxAnc (precondition terpenuhi)
3. Ketik Search `Trx Anc Mid {runId}-301`, tekan Enter
4. Klik (⋯) pada baris `Trx Anc Mid {runId}-301`
5. Klik `Add Subgroup`
6. Isi Group Name `Trx Sub A {runId}-301`
7. Klik [Submit]
8. Verifikasi toast sukses `Success, group has been created.`
9. Baca tab Transaction Role user trxAnc pada `Trx Anc Root {runId}-301` lewat kemampuan baca modul Role & Permission
10. Verifikasi `Trx Anc Root {runId}-301` tetap memuat tepat satu baris approver Transfer trxAnc, jumlah dan nilai sama dengan langkah 2
11. Baca tab Transaction Role user trxAnc pada `Trx Sub A {runId}-301` (pilih node di sidebar Group Tree)
12. Verifikasi tab Transaction Role trxAnc pada `Trx Sub A {runId}-301` tidak memuat baris approver Transfer (tabel menampilkan baris secara literal hanya pada node tempat ditugaskan, tanpa baris warisan ke descendant); anchor: baris trxAnc di `Trx Anc Root {runId}-301` tampil pada tab yang sama (langkah 10)
13. Baca tab Transaction Role user trxAnc pada `Trx Anc Mid {runId}-301`
14. Verifikasi tidak ada baris trxAnc di `Trx Anc Mid {runId}-301` maupun `Trx Sub A {runId}-301`
15. Verifikasi salinan penugasan parent hanya mencakup penugasan yang ada tepat di `Trx Anc Mid {runId}-301` (tidak ada milik trxAnc), sehingga cakupan penugasan Transaction Role ancestor atas `Trx Sub A {runId}-301` tidak diwujudkan sebagai baris salinan
16. Ganti isi kotak search dengan `Trx Sub A {runId}-301`, tekan Enter
17. Verifikasi Groups List memuat baris `Trx Sub A {runId}-301`
18. Klik angka Total User `Trx Sub A {runId}-301`
19. Verifikasi Tab Users memuat user Total Control Pre-setup No 1 (anchor: Tab Users dan Total User tampil)
20. Verifikasi Tab Users `Trx Sub A {runId}-301` tidak memuat trxAnc dan jumlah baris Tab Users sama dengan angka Total User (Transaction Role tidak dihitung; angka tetap exact-match node)
21. Tutup Popup Detail Group
22. Klik `(←)` pada kotak Search

## Notes

- Spec memiliki 22 langkah. Langkah penghubung (S-03): langkah 1, 9, 11, dan 13 (observasi lewat kemampuan baca), langkah 3 dan 16 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 4 dan 5 (membuka menu Add Subgroup), langkah 21 (menutup Popup Detail Group), dan langkah 22 (menutup Search).
- Pembagian TC lintas spec (S-05): TC-1301 muncul di `sourceTc` spec ini dan spec 302 (absence). Spec ini mengasersi Expected a, b, c, d, dan f. Asersi tidak adanya entri `Assign` untuk trxAnc di log Role & Permission dan tidak adanya notifikasi in-app ke trxAnc (Expected e) ada di spec 302 dengan baseline sendiri. Hak efektif approver pada node baru tidak diuji di modul ini (hanya yang teramati: tidak ada baris salinan).
- Temuan untuk QA:
  - TC-1301 langkah 3 dan 4 membaca Settings > Role & Permission, log, dan notifikasi tanpa menyebut aktor; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-1301 Expected d tidak punya langkah baca sendiri dan sebagian tumpang tindih dengan Expected b dan c; spec membaca tab Transaction Role trxAnc pada `Trx Anc Mid {runId}-301` sebagai langkah penghubung (langkah 13) lalu mengasersi d di langkah 15. Bagian "cakupan ancestor tetap berlaku query-time" tidak dapat diamati dari UI modul ini dan tidak diasersi.
  - Email Pre-setup No 33 (trxAnc) belum punya nilai nyata (TC: perlu data tim FE/QA); fixture `Fixture.groupsTrxAnc.*` ditetapkan tim FE.
  - TC memakai nama literal `Trx Sub A`, `Trx Anc Root`, dan seterusnya, serta Dinamis No 23 sebagai pre-setup bersama; spec memakai salinan bersuffix `{runId}-301` yang di-seed sendiri (R-06, S-06). Perlu konfirmasi bahwa seeding sah.
  - Mekanisme seeding penugasan Transaction Role (approver Transfer) tidak ditegaskan di TC; ditulis sebagai kemampuan seeding tim FE/BE tanpa endpoint karangan.
