---
id: TC-FA-GRP-E2E-295-total-user-node-descendant-memuat-user-gm-yang-penugasannya-mencakup-node-dihitung-distinct
title: "Total User Node Descendant Memuat User GM yang Penugasannya Mencakup Node, Dihitung Distinct, dan Tidak Memuat Node Ancestor atau Node Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1299
coverage:
  web: automated
---

# Total User Node Descendant Memuat User GM yang Penugasannya Mencakup Node, Dihitung Distinct, dan Tidak Memuat Node Ancestor atau Node Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user GM yang diamati (hanya dibaca, tidak login): gmPattern Pre-setup No 28, gmPatternNested Pre-setup No 29, dan gmPatternOther Pre-setup No 30, masing-masing `<nama>_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 21, di-seed lewat sesi API aktor di hook `before`, dihapus di hook `after`): `GM Pattern Parent {runId}-295` (Function None, level 1) > `GM Pattern Child {runId}-295` (Assignable) dan `GM Pattern Other {runId}-295` (Assignable, level 1). Penugasan Group Manager dan baris pola GM yang sudah terbentuk di-seed lewat API: gmPattern dan gmPatternNested di Parent; gmPatternNested juga di Child; gmPatternOther di Other. Tidak ada user lain yang di-assign pada node-node ini. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- N = jumlah user Total Control + Default User + Read Only pada client; diturunkan dari daftar akun client yang dibaca di hook `before` (8b butir 10), bukan dari tabel satu halaman. Head Office adalah node Pre-setup Tabel A (hanya dibaca).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca daftar akun client per tier Total Control, Default User, dan Read Only untuk menurunkan N.

## Test Steps

1. Ketik Search `{runId}-295`, tekan Enter
2. Verifikasi Groups List memuat baris `GM Pattern Parent {runId}-295`, `GM Pattern Child {runId}-295`, dan `GM Pattern Other {runId}-295`
3. Verifikasi Total User `GM Pattern Parent {runId}-295` sama dengan N + 2 (gmPattern dan gmPatternNested)
4. Verifikasi Total User `GM Pattern Child {runId}-295` sama dengan N + 2 (gmPattern tercakup lewat baris pola GM dari penugasan di ancestor; gmPatternNested dihitung satu kali walau tercakup dua penugasan)
5. Verifikasi Total User `GM Pattern Other {runId}-295` sama dengan N + 1 (gmPatternOther)
6. Ganti isi kotak search dengan `Head Office`, tekan Enter
7. Verifikasi Total User `Head Office` sama dengan N dan tidak memuat ketiga user GM
8. Ganti isi kotak search dengan `GM Pattern Child {runId}-295`, tekan Enter
9. Klik angka Total User `GM Pattern Child {runId}-295`
10. Verifikasi Tab Users memuat user gmPattern dan gmPatternNested
11. Verifikasi jumlah baris Tab Users sama dengan angka Total User `GM Pattern Child {runId}-295`
12. Verifikasi user gmPatternNested muncul tepat satu baris di Tab Users (dihitung distinct)
13. Verifikasi penambahan Total User `GM Pattern Child {runId}-295` hanya berasal dari baris pola GM sebagai Group Role biasa pada node itu, yaitu hitungan tetap N + 2 dan Transaction Role approver tidak menambah hitungan
14. Tutup Popup Detail Group
15. Klik `(←)` pada kotak Search

## Notes

- Spec memiliki 15 langkah. Langkah penghubung (S-03): langkah 1, 6, dan 8 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 14 (menutup Popup Detail Group), dan langkah 15 (menutup Search).
- Temuan untuk QA:
  - NC-12 (Menunggu konfirmasi, PRD FAGRP-LOGIC-03k): efek baris pola GM pada Total User belum final. Spec mengikuti TC-1299 (Total User = N + jumlah user GM). Nilai sel Group Role kedua user di Tab Users pada node ini (`Group Manager` vs `[N] roles`) tidak ditegaskan TC dan tidak diasersi spec ini.
  - Email Pre-setup No 28 sampai 30 belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan GM dan baris pola yang sudah terbentuk tidak ditegaskan di TC.
  - TC-1299 Expected e ("Transaction Role approver tetap tidak dihitung") tidak dapat diamati terpisah dari UI karena user yang hanya memegang Transaction Role tidak ada pada data uji; spec mengasersinya lewat hitungan N + 2 yang tidak berubah (langkah 13).
  - TC-1299 Expected c menyebut Total User Head Office = N tanpa mempertimbangkan user lain yang mungkin ter-assign di Head Office pada client Tabel A; N diturunkan dari daftar akun client.
