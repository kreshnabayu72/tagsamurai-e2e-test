---
id: TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1
title: Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (1/3)
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-450
  - TC-FA-RP-451
  - TC-FA-RP-452
  - TC-FA-RP-453
  - TC-FA-RP-454
  - TC-FA-RP-455
coverage:
  web: automated
---

# Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (1/3)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control pada client `Company Isolated` (Pre-setup #35; akun disediakan tim FE, email tidak tertulis di Pre-setup TC), `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup: #18 (struktur Group `Company Isolated` sama dengan Company Alpha), #35 (Approver Pandu Wijaya pada sub-tab `Disposal` di `IT Infrastructure`; tanpa Group Manager; Require Approval OFF di semua node), #15 (Ahmad Fauzi untuk TC 453).
- Tiap blok TC menyiapkan state sendiri lewat seeding API (langkah "Siapkan state"): toggle `Require Approval for Disposal`, Approver, Group Manager (Kevin Susanto di `Data Center`), sesuai precondition d TC. Hook `after` memulihkan state `Company Isolated` ke Pre-setup #35 lewat fixture backend yang disediakan tim FE/BE.
- Kemampuan teknis: seeding API Pre-setup per blok; pemulihan fixture.

## Test Steps

### Remove Approver terakhir saat Require Approval ON tanpa Group Manager (TC 450)

1. Siapkan state: toggle `Require Approval for Disposal` ON di `IT Infrastructure` dengan Pandu Wijaya sebagai satu-satunya Approver, tanpa Group Manager, hingga tersimpan.
2. Buka Tab Transaction Role, klik node `IT Infrastructure`, lalu sub-tab `Disposal`.
3. Klik `[⋯]` pada baris Pandu Wijaya, lalu pilih `Remove`.
4. Verifikasi dialog severity danger: Title `Remove Last Approver`; Body `• Pandu W` lalu `IT Infrastructure will have no approver other than Total Control while approval is required.` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`.
5. Verifikasi dialog `Remove Approver` biasa tidak tampil.
6. Klik `[Cancel]`.
7. Verifikasi dialog tertutup.
8. Verifikasi baris Pandu Wijaya tetap ada.
9. Verifikasi toggle `Require Approval for Disposal` tetap ON.

### Confirm Remove Approver terakhir (TC 451)

10. Klik `[⋯]` pada baris Pandu Wijaya, lalu pilih `Remove`.
11. Klik `[Remove]` pada dialog `Remove Last Approver`.
12. Verifikasi toast sukses `Success, Approver has been removed.`
13. Verifikasi section Approver kosong dengan empty state `No approvers assigned`.
14. Verifikasi toggle `Require Approval for Disposal` tetap ON.

### Remove Approver terakhir saat Group Manager aktif (TC 452)

15. Siapkan state: Kevin Susanto Group Manager di `IT Infrastructure`; toggle ON dengan Pandu Wijaya sebagai satu-satunya Approver, hingga tersimpan.
16. Muat ulang halaman (F5), buka Tab Transaction Role, klik node `IT Infrastructure`, lalu sub-tab `Disposal`.
17. Klik `[⋯]` pada baris Pandu Wijaya, lalu pilih `Remove`.
18. Verifikasi dialog `Remove Approver` biasa tampil dengan Body `This user will no longer be assigned to this role for IT Infrastructure.`
19. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil.
20. Klik `[Cancel]`.

### Remove salah satu dari dua Approver (TC 453)

21. Siapkan state: toggle ON di `IT Infrastructure` dengan Pandu Wijaya dan Ahmad Fauzi sebagai Approver, tanpa Group Manager, hingga tersimpan.
22. Muat ulang halaman (F5), buka Tab Transaction Role, klik node `IT Infrastructure`, lalu sub-tab `Disposal`.
23. Klik `[⋯]` pada baris Ahmad Fauzi, lalu pilih `Remove`.
24. Verifikasi dialog `Remove Approver` biasa tampil.
25. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil.
26. Klik `[Cancel]`.

### Remove Approver terakhir saat toggle OFF (TC 454)

27. Siapkan state: toggle OFF di `IT Infrastructure` dengan Pandu Wijaya sebagai satu-satunya Approver, hingga tersimpan.
28. Muat ulang halaman (F5), buka Tab Transaction Role, klik node `IT Infrastructure`, lalu sub-tab `Disposal`.
29. Klik `[⋯]` pada baris Pandu Wijaya, lalu pilih `Remove`.
30. Verifikasi dialog `Remove Approver` biasa tampil.
31. Verifikasi dialog D-09 `Remove Last Approver` tidak tampil karena toggle OFF.
32. Klik `[Cancel]`.

### Remove Group Manager fallback non-Total Control terakhir (TC 455)

33. Siapkan state: Kevin Susanto Group Manager di `Data Center`; toggle `Require Approval for Disposal` ON di `Data Center`; tanpa Approver manual, tanpa pemegang Update, tanpa Group Manager lain, hingga tersimpan.
34. Muat ulang halaman (F5), buka Tab Group Manager, lalu klik node `Data Center`.
35. Klik `[⋯]` pada baris Kevin Susanto, lalu pilih `Remove`.
36. Verifikasi dialog severity danger: Title `Remove Last Approver`; Body `• Kevin S` lalu `Data Center will have no approver other than Total Control while approval is required.`, lalu `Their role assignments in Data Center will also be removed permanently.` dan `Are you sure you want to remove it?`; tombol `[Cancel]` dan `[Remove]`.
37. Verifikasi dialog D-02 `Remove Group Manager` tidak tampil.
38. Klik `[Remove]`.
39. Verifikasi toast sukses `Success, Group Manager has been removed.`
40. Buka Tab Transaction Role, klik node `Data Center`, lalu sub-tab `Disposal`.
41. Verifikasi toggle `Require Approval for Disposal` di `Data Center` tetap ON.

## Notes

- Alasan di atas 35 langkah: keenam blok berkelas fungsional sama, berdiri sendiri dengan seeding state masing-masing, dan memakai tenant serta akun yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah tambahan di atas perkiraan hanya seeding state, muat ulang, dan penutupan dialog.
- Langkah penghubung (S-03): 1, 2, 3, 6, 10, 11, 15, 16, 17, 20 sampai 23, 26 sampai 29, 32 sampai 35, 38, 40. Muat ulang (F5) sesudah seeding API memastikan UI membaca state terbaru. Langkah 20, 26, dan 32 menutup dialog supaya blok berikutnya tidak mewarisi dialog terbuka (S-09). Langkah 40 membuka Tab Transaction Role karena TC 455 tidak memberi langkah observasi toggle.
- Langkah 5, 19, 25, 31, dan 37 adalah asersi absence dialog; pembanding positifnya adalah dialog lain yang tampil pada langkah sebelumnya (langkah 4, 18, 24, 30, 36) dan langkah 4 untuk 5.
- Copy bertanda `copy usulan, PRD 12 #1` (TC 455: Body dialog D-09 untuk Group Manager) di-assert literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - Tenant: seluruh TC di spec ini mensyaratkan login pada `Company Isolated` (Pre-setup #35); akun Total Control tenant itu tidak tertulis di Pre-setup #1 sampai #11 dan disediakan tim FE.
  - TC 450 sampai 454 tidak menulis Post Condition dan tidak menyebut apakah state diakhiri dengan Remove; TC 451 mengeksekusi Remove sehingga state Approver dipulihkan lewat seeding di blok berikutnya.
