---
id: TC-FA-GRP-E2E-287-group-hasil-import-baris-pola-group-role-dan-transaction-role-tc-ro-user-non-tc-ro-tidak-diturunkan
title: "Group Hasil Import: Baris Pola Group Role dan Transaction Role Total Control/Read Only Terbentuk dengan Log Assign per Baris, User Non-TC/RO Tidak Diturunkan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1292
coverage:
  web: automated
---

# Group Hasil Import: Baris Pola Group Role dan Transaction Role Total Control/Read Only Terbentuk dengan Log Assign per Baris, User Non-TC/RO Tidak Diturunkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: user ber-Global Role Import Data (bukan Total Control dan bukan Default User), `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): user Total Control No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Default User No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net`, dan Read Only No 3 `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`.
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix `{runId}-287`): group induk `Induk Pola {runId}-287` dengan penugasan Group Role dan Transaction Role untuk user Standard `Fixture.groupsPola.standard.email` (precondition TC-FA-GRP-1292, dibaca sebagai anchor di langkah 14). Berkas Import Group `Fixture.groupsImport.branchPola` memuat satu group baru `Branch Pola {runId}-287` dengan induk `Induk Pola {runId}-287`. Kemampuan import Group untuk importer disediakan tim FE/BE (alur dan berkas tidak ada di TC, PRD, atau LLD, S-13). Group hasil Import dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role dan tab Transaction Role (Settings > Role & Permission) per node dan per user, serta log Role & Permission (Action dan Modified By per entri). `Branch Pola {runId}-287` bernama bersuffix unik sehingga baseline entri log untuk penanda namanya adalah nol (S-12).

## Test Steps

1. Buka modul Import, unggah berkas Group `Fixture.groupsImport.branchPola`
2. Jalankan import
3. Tunggu aksi selesai
4. Buka Fixed Asset > Settings > Groups
5. Ketik Search `Branch Pola {runId}-287`, tekan Enter
6. Verifikasi baris `Branch Pola {runId}-287` tampil pada Groups List (group hasil Import terbentuk)
7. Baca tab Group Role pada `Branch Pola {runId}-287` lewat kemampuan baca modul Role & Permission
8. Verifikasi `Branch Pola {runId}-287` memuat baris pola Group Role untuk seluruh user Total Control (termasuk Default User) dengan seluruh baris Group Role CRUD penuh, sama seperti Group level 1 biasa
9. Verifikasi `Branch Pola {runId}-287` memuat baris pola Group Role untuk seluruh user Read Only dengan seluruh baris Group Role Read saja
10. Baca tab Transaction Role pada `Branch Pola {runId}-287` lewat kemampuan baca modul Role & Permission
11. Verifikasi `Branch Pola {runId}-287` memuat baris pola Transaction Role Asset Admin dan Approver untuk seluruh user Total Control (termasuk Default User) pada setiap Jenis Transaksi
12. Verifikasi `Branch Pola {runId}-287` memuat baris pola Transaction Role Monitoring & Report saja untuk seluruh user Read Only pada setiap Jenis Transaksi
13. Baca penugasan Group Role dan Transaction Role user Standard pada `Induk Pola {runId}-287`
14. Verifikasi `Induk Pola {runId}-287` memuat penugasan Group Role dan Transaction Role untuk user Standard (anchor: parent punya penugasan yang bisa diturunkan)
15. Baca penugasan Group Role dan Transaction Role user Standard pada `Branch Pola {runId}-287`
16. Verifikasi user Standard tidak mendapat baris Group Role tersimpan di `Branch Pola {runId}-287` (tidak ada pewarisan salinan)
17. Verifikasi user Standard tidak mendapat baris Transaction Role tersimpan di `Branch Pola {runId}-287` (tidak ada pewarisan salinan)
18. Baca log Role & Permission untuk `Branch Pola {runId}-287`
19. Verifikasi log memuat satu entri `Assign` biasa per baris pola Group Role dan Transaction Role yang dibaca pada langkah 7 dan 10
20. Verifikasi Modified By setiap entri `Assign` adalah pelaku Import (format `[First Name] [Last Initial]`)
21. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 3 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), langkah 4 dan 5 (membuka Groups dan Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 7, 10, 13, 15, dan 18 (observasi lewat kemampuan baca), dan langkah 21 (menutup Search).
- Pembagian TC lintas spec: TC-1292 muncul di `sourceTc` spec ini dan spec 289 (absence, S-05). Spec ini mengasersi Expected a, b, dan bagian log `Assign` serta Modified By dari Expected c. Asersi tidak adanya notifikasi in-app (Expected c) dan Expected d (kegagalan penulisan baris pola) ada di spec 289 dengan baseline dan pemicu sendiri. Klausa Expected b tentang cakupan penugasan Transaction Role ancestor atas group hasil Import (query-time, tanpa baris tambahan) tidak diasersi di spec ini karena precondition TC-1292 tidak menyiapkan ancestor ber-Transaction Role dan klausanya bersyarat "bila ada"; cakupan itu dimiliki TC-1302 di spec 303.
- Temuan untuk QA:
  - TC-1292 membutuhkan akun importer yang tidak ada di Pre-setup TC. Alur modul Import (menu, berkas, jalan import) tidak dirinci di TC; spec mengikuti teks TC dan menandai berkas Import sebagai fixture yang disediakan tim FE/BE.
  - TC-1292 langkah 2 membaca Settings > Role & Permission dan log oleh aktor importer yang tidak jelas berhak membuka modul itu; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-1292 tidak menyebut induk Branch Pola; spec memakai induk `Induk Pola {runId}-287` agar precondition c (parent punya penugasan untuk user Standard) teramati.
  - Langkah 6 (baris group hasil Import tampil) adalah anchor penghubung; TC tidak memberi Expected untuk hasil Import itu sendiri.
