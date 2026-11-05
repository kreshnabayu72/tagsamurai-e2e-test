---
id: TC-FA-GRP-E2E-300-delete-descendant-node-tercakup-gm-baris-pola-di-node-terhapus-saja-ancestor-gm-tidak-terpengaruh
title: "Delete Descendant Node Tercakup GM: Hanya Baris Pola GM di Node Terhapus dan Descendant-nya yang Dihapus, Penugasan GM di Ancestor dan Baris di Node Lain Tetap"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1298
coverage:
  web: automated
---

# Delete Descendant Node Tercakup GM: Hanya Baris Pola GM di Node Terhapus dan Descendant-nya yang Dihapus, Penugasan GM di Ancestor dan Baris di Node Lain Tetap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): gmPatternAnc Pre-setup No 32 `gmPatternAnc_automated_{namaCompany}@qwertysystem.net` dan delGmUser Pre-setup No 32 `delGmUser_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 22, tanpa aset, di-seed lewat sesi API aktor di hook `before`, sisa dihapus di hook `after`): `Del GM Anc {runId}-300` > `Del GM Anc Child {runId}-300` > `Del GM Anc Leaf {runId}-300`, dan `Del GM Anc {runId}-300` > `Del GM Anc Sibling {runId}-300`. Penugasan Group Manager dan baris pola GM yang sudah terbentuk di-seed lewat API: gmPatternAnc ber-tier Group Manager di `Del GM Anc {runId}-300` dengan baris pola di keempat node; delGmUser memegang Group Role `Manage purchase` di `Del GM Anc Child {runId}-300`. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Manager, tab Group Role, dan tab Transaction Role (Settings > Role & Permission) per node dan per user termasuk node yang sudah dihapus, serta log Role & Permission (Action, Modified By, penanda nama node). Baseline jumlah entri log dibaca lewat kemampuan yang sama (8b butir 10).

## Test Steps

1. Baca tab Group Role dan tab Transaction Role user gmPatternAnc pada keempat node, lalu catat jumlah baris pola GM pada `Del GM Anc Child {runId}-300` dan `Del GM Anc Leaf {runId}-300` sebagai R dan jumlah baris pada `Del GM Anc {runId}-300` dan `Del GM Anc Sibling {runId}-300` sebagai baseline pola
2. Verifikasi keempat node memuat baris pola GM gmPatternAnc (R lebih dari nol)
3. Baca log Role & Permission user gmPatternAnc untuk entri `Remove (Group Deleted)` yang memuat nama `Del GM Anc Child {runId}-300` atau `Del GM Anc Leaf {runId}-300`, lalu catat jumlahnya sebagai baseline
4. Ketik Search `Del GM Anc Child {runId}-300`, tekan Enter
5. Buka elipsis `Del GM Anc Child {runId}-300`, pilih Delete
6. Verifikasi dialog varian warning (karena delGmUser ter-scope di node) dengan title "Delete Group", bullet `Del GM Anc Child {runId}-300` dan `Del GM Anc Leaf {runId}-300`, isi "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?"
7. Klik [Delete]
8. Verifikasi toast sukses `Success, group has been deleted.`
9. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Del GM Anc Child {runId}-300`
10. Ganti isi kotak search dengan `Del GM Anc Leaf {runId}-300`, tekan Enter
11. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Del GM Anc Leaf {runId}-300`
12. Ganti isi kotak search dengan `Del GM Anc {runId}-300`, tekan Enter
13. Verifikasi Groups List memuat baris `Del GM Anc {runId}-300`
14. Ganti isi kotak search dengan `Del GM Anc Sibling {runId}-300`, tekan Enter
15. Verifikasi Groups List memuat baris `Del GM Anc Sibling {runId}-300`
16. Baca tab Group Role dan tab Transaction Role user gmPatternAnc pada keempat node
17. Verifikasi baris pola GM gmPatternAnc pada `Del GM Anc Child {runId}-300` dan `Del GM Anc Leaf {runId}-300` terhapus
18. Verifikasi baris pola GM gmPatternAnc pada `Del GM Anc {runId}-300` dan `Del GM Anc Sibling {runId}-300` tidak berubah (jumlah dan nilai sama dengan baseline pola langkah 1)
19. Baca tab Group Manager user gmPatternAnc lewat kemampuan baca modul Role & Permission
20. Verifikasi penugasan Group Manager gmPatternAnc di `Del GM Anc {runId}-300` tetap dan tier tetap Group Manager
21. Baca log Role & Permission user gmPatternAnc untuk entri `Remove (Group Deleted)`
22. Verifikasi log bertambah tepat R entri `Remove (Group Deleted)` dibanding baseline langkah 3, satu per baris pola GM yang terhapus, hanya pada kedua node terhapus
23. Verifikasi pelaku entri adalah admin penghapus, yaitu aktor Total Control (format `[First Name] [Last Initial]`)
24. Klik angka Total User `Del GM Anc Sibling {runId}-300`
25. Verifikasi Tab Users `Del GM Anc Sibling {runId}-300` memuat gmPatternAnc
26. Tutup Popup Detail Group
27. Klik `(←)` pada kotak Search

## Notes

- Spec memiliki 27 langkah. TC-1297 (Delete node penugasan GM) ada di spec 293 karena memakai pohon node dan akun yang berbeda.
- Langkah penghubung (S-03): langkah 1, 3, 16, 19, dan 21 (pembacaan precondition, baseline, dan observasi lewat kemampuan baca), langkah 4, 10, 12, dan 14 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 26 (menutup Popup Detail Group), dan langkah 27 (menutup Search). Aksi hapus diletakkan sesudah pembacaan precondition dan baseline (S-10).
- Pembagian TC lintas spec: TC-1298 muncul di `sourceTc` spec ini dan spec 294 (absence, S-05). Spec ini mengasersi presence: dialog warning, toast, node terhapus dan node yang tetap, baris pola yang terhapus dan yang tidak berubah, penugasan GM tetap, entri `Remove (Group Deleted)` per baris beserta pelaku, dan Total User Sibling (TC-1298 Expected a sampai f). Tidak adanya entri atau notifikasi `Auto-Revert` (Expected d bagian absence) ada di spec 294 dengan baseline sendiri.
- Temuan untuk QA:
  - Email Pre-setup No 32 (gmPatternAnc dan delGmUser) belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan GM dan baris pola yang sudah terbentuk tidak ditegaskan di TC.
  - NC-12 (Menunggu konfirmasi, PRD FAGRP-LOGIC-03k): delGmUser dipakai sebagai pemicu dialog warning agar tidak bergantung pada pembacaan baris pola GM untuk kondisi 5 guard Delete (TC-1298 Expected a menyebut "karena delGmUser ter-scope di node").
  - TC-1298 Expected f menyebut Total User `Del GM Anc Sibling` tetap memuat gmPatternAnc tanpa menyebut nilai angkanya; spec mengasersi keberadaan gmPatternAnc di Tab Users, bukan angka (NC-12).
  - TC-1298 langkah 3 sampai 5 membaca Role & Permission untuk node yang sudah terhapus; spec memakai kemampuan baca yang disediakan tim FE/BE karena UI tidak lagi menampilkan node itu.
