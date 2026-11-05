---
id: TC-FA-GRP-E2E-293-delete-node-penugasan-gm-penugasan-terlepas-baris-pola-terhapus-dan-log-remove-group-deleted-per-baris
title: "Delete Node Penugasan GM: Penugasan GM Terlepas, Baris Pola GM pada Node dan Descendant Terhapus, dan Log Remove (Group Deleted) per Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1297
coverage:
  web: automated
---

# Delete Node Penugasan GM: Penugasan GM Terlepas, Baris Pola GM pada Node dan Descendant Terhapus, dan Log Remove (Group Deleted) per Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): gmDelete Pre-setup No 31 `gmDelete_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 22, tanpa aset, di-seed lewat sesi API aktor di hook `before`, sisa dihapus di hook `after`): `Del GM Parent {runId}-293` > `Del GM Child {runId}-293`. Penugasan Group Manager dan baris pola GM yang sudah terbentuk di-seed lewat API: gmDelete ber-tier Group Manager di `Del GM Parent {runId}-293` dengan baris pola di Parent dan Child. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Manager, tab Group Role, dan tab Transaction Role (Settings > Role & Permission) per node dan per user termasuk node yang sudah dihapus; membaca log Role & Permission dan Changelog: User (Action, Modified By, penanda nama node); membaca Changelog: Group per node termasuk node terhapus. Baseline jumlah entri log dibaca lewat kemampuan yang sama (audit trail tidak diturunkan dari seeding, 8b butir 10).

## Test Steps

1. Baca tab Group Role dan tab Transaction Role user gmDelete pada `Del GM Parent {runId}-293` dan `Del GM Child {runId}-293`, lalu catat jumlah baris pola GM pada kedua node sebagai R
2. Verifikasi kedua node memuat baris pola GM gmDelete (R lebih dari nol)
3. Baca tab Group Manager user gmDelete lewat kemampuan baca modul Role & Permission
4. Verifikasi penugasan Group Manager gmDelete tercatat pada `Del GM Parent {runId}-293`
5. Baca log Role & Permission user gmDelete untuk entri `Remove (Group Deleted)` yang memuat nama kedua node, lalu catat jumlahnya sebagai baseline
6. Ketik Search `Del GM Parent {runId}-293`, tekan Enter
7. Buka elipsis `Del GM Parent {runId}-293`, pilih Delete
8. Verifikasi dialog varian warning dengan title "Delete Group", bullet `Del GM Parent {runId}-293`, isi "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?", tombol [Cancel] dan [Delete]
9. Klik [Delete]
10. Verifikasi toast sukses `Success, group has been deleted.`
11. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Del GM Parent {runId}-293`
12. Ganti isi kotak search dengan `Del GM Child {runId}-293`, tekan Enter
13. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Del GM Child {runId}-293`
14. Klik `(←)` pada kotak Search
15. Baca tab Group Manager user gmDelete lewat kemampuan baca modul Role & Permission
16. Verifikasi penugasan Group Manager gmDelete di `Del GM Parent {runId}-293` terlepas
17. Baca tab Group Role dan tab Transaction Role user gmDelete pada kedua node terhapus
18. Verifikasi tidak ada sisa baris pola GM (Group Role maupun Transaction Role) gmDelete pada kedua node
19. Baca log Role & Permission user gmDelete dan Changelog: User gmDelete
20. Verifikasi log Role & Permission bertambah tepat R entri `Remove (Group Deleted)` dibanding baseline langkah 5, satu entri per baris pola GM pada setiap node (bukan entri ringkas)
21. Verifikasi Changelog: User gmDelete memuat entri `Remove (Group Deleted)` yang sama, satu per baris pola GM pada setiap node
22. Verifikasi log memuat entri pelepasan penugasan Group Manager gmDelete di `Del GM Parent {runId}-293` (teks Action tidak ditegaskan, lihat Temuan untuk QA)
23. Verifikasi pelaku entri adalah admin penghapus, yaitu aktor Total Control (format `[First Name] [Last Initial]`)
24. Baca Changelog: Group untuk `Del GM Parent {runId}-293` dan `Del GM Child {runId}-293`
25. Verifikasi Changelog: Group memuat baris `Delete` untuk `Del GM Parent {runId}-293` dan `Del GM Child {runId}-293`

## Notes

- Spec memiliki 25 langkah. TC-1298 (Delete descendant tercakup GM) dipisah ke spec 300 karena memakai pohon node dan akun yang berbeda.
- Langkah penghubung (S-03): langkah 1, 3, 5, 15, 17, 19, dan 24 (pembacaan precondition, baseline, dan observasi lewat kemampuan baca), langkah 6 dan 12 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), dan langkah 14 (menutup Search). Aksi hapus diletakkan sesudah pembacaan precondition dan baseline (S-10).
- Pembagian TC lintas spec: TC-1297 muncul di `sourceTc` spec ini dan spec 294 (absence, S-05). Spec ini mengasersi presence: dialog warning, toast, kedua node terhapus, penugasan GM terlepas, tidak ada sisa baris pola, entri `Remove (Group Deleted)` per baris beserta pelaku, dan baris `Delete` pada Changelog: Group (TC-1297 Expected a sampai d dan bagian presence e). Tidak adanya notifikasi in-app ke gmDelete, Action `Remove (via Group Manager)`, dan Changelog: Group yang hanya memuat baris `Delete` ada di spec 294 dengan baseline sendiri.
- Temuan untuk QA:
  - Email Pre-setup No 31 belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan GM dan baris pola yang sudah terbentuk tidak ditegaskan di TC.
  - TC-1297 Expected d menyebut "entri pelepasan penugasan Group Manager sesuai kebijakan pemilik (`settings-role-permission` §8)" tanpa teks Action; spec hanya mengasersi keberadaan entri pelepasan (langkah 22) tanpa teks Action.
  - NC-12 (Menunggu konfirmasi, PRD FAGRP-LOGIC-03k): apakah baris pola GM ikut menghitung kondisi 5 guard Delete belum final. TC-1297 mengharapkan dialog varian warning (`D-15`) karena gmDelete ter-scope; bila pembacaan literal NC-12 menang, ekspektasi dialog perlu ditinjau. Spec mengasersi dialog sesuai TC.
  - TC-1297 Expected d menyebut log Role & Permission dan Changelog: User tanpa membedakan surface; spec mengasersi entri `Remove (Group Deleted)` di keduanya sebagai dua Verifikasi (langkah 20 dan 21).
  - TC-1297 langkah 3 dan 4 membaca Role & Permission untuk node yang sudah terhapus; spec memakai kemampuan baca yang disediakan tim FE/BE karena UI tidak lagi menampilkan node itu.
