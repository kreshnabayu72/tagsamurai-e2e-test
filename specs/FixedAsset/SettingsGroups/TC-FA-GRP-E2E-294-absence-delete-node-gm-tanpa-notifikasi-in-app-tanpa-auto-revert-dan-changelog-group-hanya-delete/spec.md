---
id: TC-FA-GRP-E2E-294-absence-delete-node-gm-tanpa-notifikasi-in-app-tanpa-auto-revert-dan-changelog-group-hanya-delete
title: "Absence Delete Node GM: Tanpa Notifikasi In-App ke User GM, Tanpa Action Remove (via Group Manager), Tanpa Auto-Revert, dan Changelog Group Hanya Baris Delete"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1297
  - TC-FA-GRP-1298
coverage:
  web: automated
---

# Absence Delete Node GM: Tanpa Notifikasi In-App ke User GM, Tanpa Action Remove (via Group Manager), Tanpa Auto-Revert, dan Changelog Group Hanya Baris Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user yang diamati (hanya dibaca, tidak login): gmDelete Pre-setup No 31, gmPatternAnc dan delGmUser Pre-setup No 32, masing-masing `<nama>_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (salinan kedua pohon Delete GM, terpisah dari spec 293 dan 300 karena node spec itu sudah terhapus; Pre-setup tambahan No 22 tanpa aset, di-seed lewat sesi API aktor di hook `before`, sisa dihapus di hook `after`): `Del GM Parent {runId}-294` > `Del GM Child {runId}-294`; `Del GM Anc {runId}-294` > `Del GM Anc Child {runId}-294` > `Del GM Anc Leaf {runId}-294`, dan `Del GM Anc {runId}-294` > `Del GM Anc Sibling {runId}-294`. Penugasan Group Manager dan baris pola GM yang sudah terbentuk di-seed lewat API: gmDelete di `Del GM Parent {runId}-294` dengan baris pola di Parent dan Child; gmPatternAnc di `Del GM Anc {runId}-294` dengan baris pola di keempat node; delGmUser memegang Group Role `Manage purchase` di `Del GM Anc Child {runId}-294`. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca log Role & Permission (Action dan jumlah entri per user dan per penanda nama node), membaca Changelog: Group per node termasuk node terhapus, membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), dan langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11).

## Test Steps

### TC-FA-GRP-1297: Delete node penugasan GM tanpa notifikasi dan dengan Changelog Group hanya Delete

1. Catat baseline sebelum pemicu: jumlah notifikasi in-app gmDelete dan jumlah entri Action `Remove (via Group Manager)` pada log Role & Permission gmDelete
2. Ketik Search `Del GM Parent {runId}-294`, tekan Enter
3. Buka elipsis `Del GM Parent {runId}-294`, pilih Delete
4. Verifikasi dialog varian warning dengan bullet `Del GM Parent {runId}-294` (anchor: Delete diproses)
5. Klik [Delete]
6. Verifikasi toast sukses `Success, group has been deleted.`
7. Baca log Role & Permission user gmDelete
8. Verifikasi log memuat entri `Remove (Group Deleted)` untuk baris pola GM gmDelete pada kedua node (anchor: Delete diproses dan log tercatat)
9. Verifikasi jumlah entri Action `Remove (via Group Manager)` gmDelete sama dengan baseline langkah 1
10. Tunggu 5 detik tanpa memuat ulang halaman
11. Verifikasi jumlah notifikasi in-app gmDelete sama dengan baseline langkah 1
12. Baca Changelog: Group untuk `Del GM Parent {runId}-294` dan `Del GM Child {runId}-294`
13. Verifikasi Changelog: Group memuat baris `Delete` untuk kedua node (anchor)
14. Verifikasi Changelog: Group tidak memuat baris selain `Delete` untuk kedua node
15. Klik `(←)` pada kotak Search

### TC-FA-GRP-1298: Delete descendant node tercakup GM tanpa Auto-Revert dan tanpa notifikasi

16. Catat baseline sebelum pemicu: jumlah notifikasi in-app gmPatternAnc dan jumlah entri `Auto-Revert` pada log Role & Permission gmPatternAnc
17. Ketik Search `Del GM Anc Child {runId}-294`, tekan Enter
18. Buka elipsis `Del GM Anc Child {runId}-294`, pilih Delete
19. Verifikasi dialog varian warning dengan bullet `Del GM Anc Child {runId}-294` dan `Del GM Anc Leaf {runId}-294` (anchor: Delete diproses)
20. Klik [Delete]
21. Verifikasi toast sukses `Success, group has been deleted.`
22. Baca log Role & Permission user gmPatternAnc
23. Verifikasi log memuat entri `Remove (Group Deleted)` untuk baris pola GM gmPatternAnc pada kedua node terhapus (anchor: Delete diproses dan log tercatat)
24. Verifikasi jumlah entri `Auto-Revert` gmPatternAnc sama dengan baseline langkah 16
25. Tunggu 5 detik tanpa memuat ulang halaman
26. Verifikasi jumlah notifikasi in-app gmPatternAnc (termasuk notifikasi `Auto-Revert`) sama dengan baseline langkah 16
27. Klik `(←)` pada kotak Search

## Notes

- Spec memiliki 27 langkah. Langkah penghubung (S-03): langkah 7, 12, dan 22 (observasi lewat kemampuan baca), langkah 2 dan 17 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 10 dan 25 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11), dan langkah 15 dan 27 (menutup Search).
- Pembagian TC lintas spec (S-05): TC-1297 (spec asal 293) dan TC-1298 (spec asal 300) muncul di `sourceTc` spec ini dan satu spec asal masing-masing. Spec ini memuat aksi nyata (Delete pada salinan node bersuffix `-294`, karena node spec 293 dan 300 sudah terhapus; tidak dilipat ke spec asal agar asersi absence tidak bercampur dengan asersi presence) dengan baseline sendiri untuk: tidak ada notifikasi in-app ke gmDelete, Action bukan `Remove (via Group Manager)`, dan Changelog: Group hanya baris `Delete` (TC-1297 Expected d bagian "bukan `Remove (via Group Manager)`" dan Expected e); tidak ada entri maupun notifikasi `Auto-Revert` (TC-1298 Expected d). Presence diasersi di spec 293 dan 300.
- Temuan untuk QA:
  - Email Pre-setup No 31 dan No 32 belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan GM dan baris pola yang sudah terbentuk tidak ditegaskan di TC.
  - TC tidak menyediakan Pre-setup terpisah untuk spec absence Delete; salinan node `-294` dibuat dinamis dari Pre-setup tambahan No 22. Perlu konfirmasi bila absence Delete lebih baik dilipat ke spec 293 dan 300 (menyimpang dari S-05).
  - NC-12 (Menunggu konfirmasi, PRD FAGRP-LOGIC-03k): dialog varian warning pada langkah 4 dan 19 mengikuti TC-1297 dan TC-1298; asersinya hanya anchor Delete diproses.
  - TC-1297 Expected e menyebut "Changelog: Group hanya baris `Delete`" tanpa menyebut node selain Del GM Parent dan Del GM Child; spec membatasinya pada kedua node itu.
