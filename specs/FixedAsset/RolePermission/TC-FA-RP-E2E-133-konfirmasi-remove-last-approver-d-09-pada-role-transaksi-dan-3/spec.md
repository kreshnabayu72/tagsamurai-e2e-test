---
id: TC-FA-RP-E2E-133-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-3
title: Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (3/3)
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1011
  - TC-FA-RP-1012
  - TC-FA-RP-1095
  - TC-FA-RP-1096
  - TC-FA-RP-1138
coverage:
  web: automated
---

# Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (3/3)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control pada client `Company Isolated` (Pre-setup #35; akun disediakan tim FE, email tidak tertulis di Pre-setup TC), `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup: #18 (struktur Group), #35 (`Manage asset & TAG` Read dan Update atas nama Dimas Pranata hanya di `Rack A1`, Budi Setiawan dan Endah Susanti hanya di `Dock 1`; toggle registrasi ON di `Rack A1` dan `Dock 1`; tanpa Group Manager; Approver Pandu Wijaya), #15 (Dimas Pranata, Budi Setiawan, Endah Susanti).
- Tiap blok TC menyiapkan state sendiri lewat seeding API (langkah "Siapkan state") sesuai precondition d TC (termasuk Kevin Susanto Group Manager di `Data Center`, toggle `Require Approval for Disposal` di `Data Center` dan `Rack A1`, dan Dimas Pranata berstatus Total Control untuk TC 1138). Hook `after` memulihkan state `Company Isolated` ke Pre-setup #35 lewat fixture backend yang disediakan tim FE/BE; blok TC 1138 menghapus baris Group Role Dimas Pranata sehingga pemulihannya wajib lewat fixture itu.
- Kemampuan teknis: seeding API Pre-setup per blok; pemulihan fixture.

## Test Steps

### Cancel pada D-09 bentuk jamak Bulk Remove (TC 1011)

1. Siapkan state: node `Dock 1` hanya memiliki dua pemegang Update (Budi Setiawan dan Endah Susanti) tanpa ancestor holder; toggle registrasi ON; tanpa Group Manager, hingga tersimpan.
2. Buka Tab System, lalu buka Detail Role `Manage asset & TAG`.
3. Klik node `Dock 1`.
4. Centang baris Budi Setiawan dan Endah Susanti.
5. Klik `Bulk Action` > `Remove`.
6. Verifikasi dialog D-09 `Remove Last Approver` dengan bullet `• Budi S` dan `• Endah S` dan penutup `Are you sure you want to remove them?`
7. Klik `[Cancel]`.
8. Verifikasi dialog tertutup.
9. Verifikasi tidak ada toast.
10. Verifikasi kedua baris (Budi Setiawan dan Endah Susanti) tetap ada.
11. Verifikasi seleksi kedua baris dipertahankan.
12. Verifikasi toggle registrasi `Dock 1` tetap ON.

### Cancel pada D-09 untuk Remove Group Manager (TC 1012)

13. Siapkan state: Kevin Susanto Group Manager di `Data Center`; toggle `Require Approval for Disposal` ON di `Data Center`; tanpa Approver manual, tanpa pemegang Update, tanpa Group Manager lain, hingga tersimpan.
14. Muat ulang halaman (F5), buka Tab Group Manager, lalu klik node `Data Center`.
15. Klik `[⋯]` pada baris Kevin Susanto, lalu pilih `Remove`.
16. Verifikasi dialog D-09 `Remove Last Approver` menggantikan D-02 dengan Body `• Kevin S` lalu `Data Center will have no approver other than Total Control while approval is required.` dan `Their role assignments in Data Center will also be removed permanently.`
17. Klik `[Cancel]`.
18. Verifikasi dialog tertutup.
19. Verifikasi tidak ada toast.
20. Verifikasi baris Kevin Susanto tetap ada di Tab Group Manager.
21. Buka Tab Transaction Role, klik node `Data Center`, lalu sub-tab `Disposal`.
22. Verifikasi toggle `Require Approval for Disposal` di `Data Center` tetap ON.

### Bulk Remove pemegang Update terakhir pada lebih dari satu group (TC 1095)

23. Siapkan state: toggle registrasi ON di `Rack A1` dan `Dock 1`; Dimas Pranata pemegang Update terakhir di `Rack A1`; Budi Setiawan dan Endah Susanti pemegang Update terakhir di `Dock 1`; tanpa Group Manager, hingga tersimpan.
24. Muat ulang halaman (F5), buka Tab System, lalu buka Detail Role `Manage asset & TAG`.
25. Klik `All Groups` di Sidebar Group Tree.
26. Centang baris Dimas Pranata, Budi Setiawan, dan Endah Susanti.
27. Klik `Bulk Action` > `Remove`.
28. Verifikasi dialog D-09 menggantikan D-06: Title `Remove Last Approver`; bullet `• Dimas P`, `• Budi S`, dan `• Endah S`.
29. Verifikasi kalimat group terdampak memuat kedua nama group `Rack A1` dan `Dock 1` dipisah koma diikuti `will have no approver other than Total Control while approval is required.`
30. Verifikasi penutup dialog `Are you sure you want to remove them?`
31. Klik `[Cancel]`.

### Remove Group Manager fallback terakhir pada node dan descendant (TC 1096)

32. Siapkan state: Kevin Susanto Group Manager di `Data Center`; toggle `Require Approval for Disposal` ON di `Data Center` dan `Rack A1` tanpa Approver, pemegang Update, maupun Group Manager lain, hingga tersimpan.
33. Muat ulang halaman (F5), buka Tab Group Manager, lalu klik `[⋯]` pada baris Kevin Susanto di `Data Center`, lalu pilih `Remove`.
34. Verifikasi dialog D-09 menggantikan D-02: Title `Remove Last Approver`; bullet `• Kevin S`.
35. Verifikasi kalimat group terdampak memuat kedua nama group `Data Center` dan `Rack A1` dipisah koma diikuti `will have no approver other than Total Control while approval is required.`
36. Verifikasi `Their role assignments in Data Center will also be removed permanently.` dan `Are you sure you want to remove it?`
37. Klik `[Cancel]`.

### Remove Total Control tidak memicu D-09 (TC 1138)

38. Siapkan state: Dimas Pranata berstatus Total Control dengan Group Role `Manage asset & TAG` Read dan Update di `Rack A1` sebagai satu-satunya pemegang Update pada scope node dan ancestor, tanpa Group Manager; toggle registrasi `Rack A1` ON, hingga tersimpan.
39. Muat ulang halaman (F5), buka Tab Total Control, lalu klik `[⋯]` pada baris Dimas Pranata, lalu pilih `Remove`.
40. Verifikasi hanya dialog D-01 (Title `Remove Total Control`) yang tampil.
41. Verifikasi tidak ada dialog D-09 dan tidak ada dialog blok D-11.
42. Klik `[Remove]`.
43. Verifikasi toast sukses `Success, Total Control has been removed.`
44. Verifikasi baris Dimas Pranata hilang dari Tab Total Control.
45. Buka Detail Role Group Role `Manage asset & TAG`, klik node `Rack A1`, lalu cari Dimas Pranata (ketik Search `Dimas Pranata`, tekan Enter).
46. Verifikasi baris Dimas Pranata tidak tampil di `Rack A1`.
47. Buka panel Approval Settings Registration pada Detail Role `Manage asset & TAG` di node `Rack A1`.
48. Verifikasi toggle registrasi `Rack A1` tetap ON.

## Notes

- Alasan di atas 35 langkah: kelima blok berkelas fungsional sama, berdiri sendiri dengan seeding state masing-masing, pada tenant dan akun yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): 1 sampai 5, 7, 13 sampai 15, 17, 21, 23 sampai 27, 31, 32, 33, 37 sampai 39, 42, 45, 47. Muat ulang (F5) sesudah seeding API memastikan UI membaca state terbaru. Langkah 7, 17, 31, dan 37 menutup dialog dan, untuk blok Bulk Remove, mempertahankan seleksi sesuai Expected TC. Langkah 21, 45, dan 47 membuka surface yang dibutuhkan Expected TC yang tidak memberi langkah observasi toggle atau baris. Langkah 45 memuat Search untuk menemukan baris target (R-16).
- Langkah 9 dan 19 adalah asersi absence toast sesudah `[Cancel]`; pembanding positifnya adalah dialog tertutup (langkah 8 dan 18).
- Langkah 41 adalah asersi absence dialog D-09 dan D-11 dengan pembanding dialog D-01 pada langkah 40; langkah 46 adalah absence baris dengan pembanding toast sukses langkah 43.
- Copy bertanda `copy usulan, PRD 12 #1` (TC 1012 dan TC 1096: Body D-09 untuk Group Manager) di-assert literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - Seluruh TC di spec ini mensyaratkan login pada `Company Isolated` (Pre-setup #35); akun Total Control tenant itu tidak tertulis di Pre-setup #1 sampai #11 dan disediakan tim FE.
  - TC 1138 menyebut Dimas Pranata "berstatus Total Control (seed)" sekaligus pemegang Group Role di `Rack A1` (Pre-setup #35 menulisnya sebagai pemegang `Manage asset & TAG` tanpa status Total Control); spec menyiapkan status Total Control lewat seeding.
  - TC 1138 langkah 4 mencari Dimas Pranata di `Rack A1` Detail Role Group Role tanpa menyebut sub-tab; spec memakai langkah buka Detail Role `Manage asset & TAG` sesuai langkah TC.
  - TC 1138 Expected d mengobservasi toggle registrasi `Rack A1` tanpa menyebut surface; spec memakai panel Approval Settings Registration pada Detail Role `Manage asset & TAG`, dan perlu konfirmasi QA. TC 1011 Expected b menyebut toggle registrasi `Dock 1` tetap ON dan dibaca pada panel yang sama, dalam halaman Detail Role yang sama (langkah 12).
