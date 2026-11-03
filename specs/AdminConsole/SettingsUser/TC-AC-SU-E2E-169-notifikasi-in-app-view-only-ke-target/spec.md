---
id: TC-AC-SU-E2E-169-notifikasi-in-app-view-only-ke-target
title: "Notifikasi In-App View-Only ke Target untuk Event Remove dan Auto-Revert Tier atau Group Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-579
  - TC-AC-SU-580
  - TC-AC-SU-581
  - TC-AC-SU-582
  - TC-AC-SU-583
  - TC-AC-SU-584
  - TC-AC-SU-641
coverage:
  web: automated
---

# Notifikasi In-App View-Only ke Target untuk Event Remove dan Auto-Revert Tier atau Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Konteks kedua: jendela browser privat untuk target (objek asersi notifikasi), dibuka per blok TC dan ditutup bersama sesi loginnya sebelum blok berikutnya (S-09); password target dari `Spectra.env.AC_SU_SEEDED_PASSWORD` (nama env baru, didaftarkan pemilik repo). Spec memuat konteks UI kedua sebagai objek uji (kelas c).
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (target dapat login ke Admin Console, Activated). Region A dari Group Tree Pre-setup hanya menjadi group Group Manager dan tidak diubah.

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Rina Putri {runId}-169A` | `rinaputri+{runId}-169a@qwertysystem.net` | bertier Total Control (TC-579) |
| U2 | `Budi Santoso {runId}-169B` | `budisantoso+{runId}-169b@qwertysystem.net` | bertier Read Only (TC-580) |
| U3 | `Rina Putri {runId}-169C` | `rinaputri+{runId}-169c@qwertysystem.net` | bertier Total Control (TC-581) |
| U4 | `Budi Santoso {runId}-169D` | `budisantoso+{runId}-169d@qwertysystem.net` | bertier Read Only (TC-582) |
| U5 | `Dedi Kurnia {runId}-169E` | `dedikurnia+{runId}-169e@qwertysystem.net` | Group Manager di Region A (TC-583) |
| U6 | `Dedi Kurnia {runId}-169F` | `dedikurnia+{runId}-169f@qwertysystem.net` | Group Manager di Region A dengan full CRUD pada "Manage distributor" (TC-584) |
| U7 | `Dedi Kurnia {runId}-169G` | `dedikurnia+{runId}-169g@qwertysystem.net` | Group Manager di Region A (TC-641) |

- Kemampuan teknis: Fixture BE (seeding user, tier, dan Group Manager); konteks browser kedua. Tanggal pada Body notifikasi adalah tanggal aksi dalam format General Settings yang berlaku (tidak diubah spec ini). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-579: Remove Total Control
1. Klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu remove U1 (`Rina Putri {runId}-169A`) dari Total Control
2. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U1, lalu klik lonceng notifikasi navbar
3. Verifikasi notifikasi baru: Title "Your Total Control access was removed", Body "Default User removed your Total Control access on [tanggal aksi]."
4. Verifikasi notifikasi hanya memiliki tombol `[Mark as Read]` dan tidak memiliki tombol `[Detail]`
### TC-AC-SU-580: Remove Read Only
5. Tutup konteks kedua dan hapus sesi loginnya, klik menu Settings > Role & Permission di sidebar, klik Tab Read Only, lalu remove U2 (`Budi Santoso {runId}-169B`) dari Read Only
6. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U2, lalu klik lonceng notifikasi navbar
7. Verifikasi notifikasi baru: Title "Your Read Only access was removed", Body "Default User removed your Read Only access on [tanggal aksi]."
8. Verifikasi notifikasi hanya memiliki tombol `[Mark as Read]` dan tidak memiliki tombol `[Detail]`
### TC-AC-SU-581: Auto-Revert Total Control
9. Tutup konteks kedua dan hapus sesi loginnya, buka Detail U3 (`Rina Putri {runId}-169C`) lewat Search nama, klik Tab Role, lalu sub-tab Global Role
10. Uncheck Delete pada "Manage group", lalu klik `[Remove]` pada dialog Remove Total Control
11. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U3, lalu klik lonceng notifikasi navbar
12. Verifikasi notifikasi baru: Title "Your Total Control access was removed", Body "Your Total Control access was automatically removed after Default User edited your role on [tanggal aksi]."
13. Verifikasi notifikasi hanya memiliki tombol `[Mark as Read]` dan tidak memiliki tombol `[Detail]`
### TC-AC-SU-582: Auto-Revert Read Only
14. Tutup konteks kedua dan hapus sesi loginnya, klik menu Settings > User di sidebar, buka Detail U4 (`Budi Santoso {runId}-169D`) lewat Search nama, klik Tab Role, lalu sub-tab Global Role
15. Centang Create pada "Manage group", lalu klik `[Remove]` pada dialog Remove Read Only
16. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U4, lalu klik lonceng notifikasi navbar
17. Verifikasi notifikasi baru: Title "Your Read Only access was removed", Body "Your Read Only access was automatically removed after Default User edited your role on [tanggal aksi]."
18. Verifikasi notifikasi hanya memiliki tombol `[Mark as Read]` dan tidak memiliki tombol `[Detail]`
### TC-AC-SU-583: Remove Group Manager
19. Tutup konteks kedua dan hapus sesi loginnya, klik menu Settings > Role & Permission di sidebar, klik Tab Group Manager, lalu remove Group Manager Region A dari U5 (`Dedi Kurnia {runId}-169E`)
20. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U5, lalu klik lonceng notifikasi navbar
21. Verifikasi notifikasi baru: Title "You are no longer Group Manager for Region A", Body "Default User removed your Group Manager status for Region A on [tanggal aksi]."
22. Verifikasi notifikasi hanya memiliki tombol `[Mark as Read]` dan tidak memiliki tombol `[Detail]`
### TC-AC-SU-584: Auto-Revert Group Manager
23. Tutup konteks kedua dan hapus sesi loginnya, klik menu Settings > User di sidebar, buka Detail U6 (`Dedi Kurnia {runId}-169F`) lewat Search nama, klik Tab Role, lalu sub-tab Group Role
24. Klik `[Assign Group]` pada baris "Manage distributor" (Group Manager Region A dengan full CRUD), uncheck Delete pada baris Region A, klik `[Save]`, lalu klik `[Remove]` pada dialog Remove Group Manager
25. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U6, lalu klik lonceng notifikasi navbar
26. Verifikasi notifikasi baru: Title "You are no longer Group Manager for Region A", Body "Your Group Manager status for Region A was automatically removed after Default User edited your role on [tanggal aksi]."
27. Verifikasi notifikasi hanya memiliki tombol `[Mark as Read]` dan tidak memiliki tombol `[Detail]`
### TC-AC-SU-641: Group Manager dilepas saat target diberi Total Control
28. Tutup konteks kedua dan hapus sesi loginnya, klik menu Settings > Role & Permission di sidebar, klik Tab Total Control, lalu assign U7 (`Dedi Kurnia {runId}-169G`) ke Total Control
29. Tunggu aksi selesai, buka konteks kedua (jendela privat), login sebagai U7, lalu klik lonceng notifikasi navbar
30. Verifikasi notifikasi baru: Title "You are no longer Group Manager for Region A", Body "Default User removed your Group Manager status for Region A on [tanggal aksi]."
31. Verifikasi notifikasi hanya memiliki tombol `[Mark as Read]` dan tidak memiliki tombol `[Detail]`
32. Tutup konteks kedua, klik menu Settings > User di sidebar, buka Detail U7 lewat Search nama, lalu klik Tab Role
33. Verifikasi banner Tab Role `"This user has Total Control access."`

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): navigasi sidebar, Search nama target dan pembukaan Detail (R-16), pembukaan konteks kedua dan login target (langkah 2 dan langkah serupa), menutup konteks kedua beserta sesi loginnya (S-09), dan pemilihan tab.
- Konteks kedua target adalah objek asersi (notifikasi diamati di sesi target), sehingga spec ini kelas c dan bukan `P-2`; satu konteks kedua per blok, ditutup sebelum blok berikutnya. Pemicu perubahan tier atau Group Manager dilakukan Default User di konteks utama.
- Tujuh blok TC berpola sama (pemicu, konteks target, dua asersi notifikasi) dan berdiri sendiri dengan user seeding sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Body notifikasi memuat `[Date]` tanpa pola tegas; spec mengasersi tanggal aksi dalam format General Settings. Nilai `[Admin Name]` diasersi `Default User` sesuai Expected TC.
  - TC-579 sampai TC-584 dan TC-641 tidak menyebut jumlah notifikasi lain yang sudah ada milik target; spec mengasersi notifikasi dengan Title dan Body yang disebut tanpa asersi jumlah.
  - TC-579 sampai TC-584 menyebut target dengan nama literal (`Rina Putri`, `Budi Santoso`, `Dedi Kurnia`) yang dipakai ulang dengan state berbeda; spec memakai user bersuffix per blok (S-12). Password target seeding memakai env baru `AC_SU_SEEDED_PASSWORD`.
