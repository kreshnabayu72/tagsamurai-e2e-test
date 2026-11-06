---
id: TC-FA-RP-E2E-132-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-2
title: Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (2/3)
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-456
  - TC-FA-RP-457
  - TC-FA-RP-458
  - TC-FA-RP-459
  - TC-FA-RP-460
coverage:
  web: automated
---

# Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (2/3)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control pada client `Company Isolated` (Pre-setup #35; akun disediakan tim FE, email tidak tertulis di Pre-setup TC), `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup: #18 (struktur Group), #35 (tanpa Group Manager; Approver Pandu Wijaya pada `Disposal` di `IT Infrastructure`, mencakup descendant pada `Disposal`; sub-tab `Damaged` tanpa Approver manual; Require Approval OFF di semua node), #15 (Budi Setiawan dan Ahmad Fauzi), #43 (Kevin Susanto Group Manager di `Data Center`, diseed ulang per blok).
- Tiap blok TC menyiapkan state sendiri lewat seeding API (langkah "Siapkan state") sesuai precondition d TC. Blok TC 459 dan TC 460 menambah satu Group Manager pembanding (Ahmad Fauzi di `Helpdesk`, tidak diasersi selain tampil) supaya asersi absence baris Kevin Susanto punya baris pembanding di surface yang sama; `Helpdesk` bukan ancestor atau descendant `Data Center`, sehingga tidak menjadi fallback bagi `Data Center`.
- Hook `after` memulihkan state `Company Isolated` ke Pre-setup #35 lewat fixture backend yang disediakan tim FE/BE.
- Kemampuan teknis: seeding API Pre-setup per blok; pemulihan fixture.

## Test Steps

### Remove Group Manager saat ada Group Manager lain (TC 456)

1. Siapkan state: Kevin Susanto Group Manager di `Data Center`; toggle `Require Approval for Damaged` ON di `Data Center`; Dimas Pranata juga Group Manager di `Data Center`, hingga tersimpan.
2. Buka Tab Group Manager, lalu klik node `Data Center`.
3. Klik `[⋯]` pada baris Kevin Susanto, lalu pilih `Remove`.
4. Verifikasi dialog D-02 `Remove Group Manager` tampil.
5. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil karena Group Manager lain menjadi fallback.
6. Klik `[Cancel]`.

### Remove Group Manager saat ada Approver manual (TC 457)

7. Siapkan state: Kevin Susanto Group Manager di `Data Center`; toggle ON di `Data Center`; Pandu Wijaya Approver pada `Data Center` sub-tab `Disposal`, hingga tersimpan.
8. Muat ulang halaman (F5), buka Tab Group Manager, lalu klik node `Data Center`.
9. Klik `[⋯]` pada baris Kevin Susanto, lalu pilih `Remove`.
10. Verifikasi dialog D-02 `Remove Group Manager` tampil.
11. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil karena Approver manual menjadi fallback.
12. Klik `[Cancel]`.

### Remove Group Manager saat ada pemegang Update registrasi (TC 458)

13. Siapkan state: Kevin Susanto Group Manager di `Data Center`; toggle `Require Approval for Damaged` ON di `Data Center`; Budi Setiawan memegang Manage asset & TAG Update di `Data Center` dan toggle registrasi ON, hingga tersimpan.
14. Muat ulang halaman (F5), buka Tab Group Manager, lalu klik node `Data Center`.
15. Klik `[⋯]` pada baris Kevin Susanto, lalu pilih `Remove`.
16. Verifikasi dialog D-02 `Remove Group Manager` tampil.
17. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil karena pemegang Update menjadi fallback.
18. Klik `[Cancel]`.

### Pelepasan Group Manager otomatis lewat Assign Total Control (TC 459)

19. Siapkan state: Kevin Susanto Group Manager di `Data Center` sebagai satu-satunya fallback non-Total Control dengan toggle `Require Approval for Damaged` ON (tanpa Approver manual yang mencakup); Ahmad Fauzi Group Manager di `Helpdesk` sebagai pembanding, hingga tersimpan.
20. Muat ulang halaman (F5), buka Tab Total Control, lalu klik `[+ Assign]`.
21. Centang Kevin Susanto, lalu klik `[Assign]`.
22. Verifikasi toast sukses `Success, Total Control has been assigned.`
23. Verifikasi tidak ada dialog D-09 `Remove Last Approver`.
24. Buka Tab Group Manager, lalu klik `All Groups`.
25. Verifikasi baris Ahmad Fauzi di `Helpdesk` tampil di Tab Group Manager.
26. Verifikasi penugasan Group Manager Kevin Susanto di `Data Center` lepas (baris Kevin Susanto di `Data Center` tidak tampil).
27. Buka Tab Transaction Role, klik node `Data Center`, lalu sub-tab `Damaged`.
28. Verifikasi toggle `Require Approval for Damaged` di `Data Center` tetap ON.

### Auto-revert Group Manager tidak memicu D-09 tambahan (TC 460)

29. Siapkan state: Kevin Susanto Group Manager di `Data Center` dengan baris `Manage group` CRUD penuh; toggle `Require Approval for Damaged` ON (tanpa Approver manual yang mencakup); tanpa fallback lain; Ahmad Fauzi Group Manager di `Helpdesk` sebagai pembanding, hingga tersimpan.
30. Muat ulang halaman (F5), buka Tab System, buka Detail Role `Manage group`, lalu klik node `Data Center`.
31. Hapus centang Delete pada baris Kevin Susanto.
32. Verifikasi dialog D-05 tampil.
33. Klik `[Remove]` pada dialog D-05.
34. Tunggu aksi selesai (Detail Role `Manage group` tampil kembali tanpa dialog).
35. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil sesudah dialog D-05.
36. Buka Tab Group Manager, lalu klik `All Groups`.
37. Verifikasi baris Ahmad Fauzi di `Helpdesk` tampil di Tab Group Manager.
38. Verifikasi penugasan Group Manager Kevin Susanto di `Data Center` lepas (baris Kevin Susanto di `Data Center` tidak tampil).

## Notes

- Alasan di atas 35 langkah: kelima blok berkelas fungsional sama, berdiri sendiri dengan seeding state masing-masing, pada tenant dan akun yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): 1 sampai 3, 6 sampai 9, 12 sampai 15, 18 sampai 21, 24, 27, 29 sampai 31, 33, 34, 36. Muat ulang (F5) sesudah seeding API memastikan UI membaca state terbaru. Langkah 6, 12, dan 18 menutup dialog supaya blok berikutnya tidak mewarisi dialog terbuka (S-09). Langkah 24 sampai 28 dan 36 sampai 38 membuka surface yang diperlukan Expected b TC 459 dan TC 460, karena kedua TC hanya memberi langkah Assign dan hapus centang tanpa langkah observasi penugasan dan toggle.
- Langkah 5, 11, 17, 23, dan 35 adalah asersi absence dialog D-09; pembanding positifnya dialog D-02 atau toast sukses yang tampil sebelumnya (langkah 4, 10, 16, 22, dan 32). Langkah 26 dan 38 adalah asersi absence baris dengan pembanding langkah 25 dan 37.
- Temuan untuk QA:
  - Seluruh TC di spec ini mensyaratkan login pada `Company Isolated` (Pre-setup #35); akun Total Control tenant itu tidak tertulis di Pre-setup #1 sampai #11 dan disediakan tim FE.
  - TC 459 dan TC 460 tidak memberi langkah observasi untuk "penugasan Group Manager lepas" dan "toggle tetap ON"; spec menambah langkah navigasi sebagai langkah penghubung. Pembanding Ahmad Fauzi di `Helpdesk` adalah seeding tambahan spec, bukan Pre-setup TC.
  - TC 459 tidak menyebut jumlah baris yang dicentang selain Kevin Susanto, dan tidak menyebut apakah toggle diobservasi pada sub-tab `Disposal`; spec memakai sub-tab `Damaged` sesuai precondition TC 459 dan TC 460. Blok TC 456 dan TC 458 (precondition tanpa sub-tab) memakai `Damaged` supaya Approver Pandu Wijaya `Disposal` yang mencakup `Data Center` tidak menjadi fallback; blok TC 457 tetap `Disposal` (Pandu Approver di `Data Center`).
