---
id: TC-AC-SU-E2E-174-sinkron-global-settings-nonaktif-app-access-dan-hapus-user
title: "Sinkron dari Global Settings untuk Nonaktif User, Aktif Kembali, Cabut App Access Admin Console, dan Hapus User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-598
  - TC-AC-SU-599
  - TC-AC-SU-600
  - TC-AC-SU-643
coverage:
  web: automated
---

# Sinkron dari Global Settings untuk Nonaktif User, Aktif Kembali, Cabut App Access Admin Console, dan Hapus User

## Prerequisites

- Mode: FE+BE.
- Akun aktor blok TC-598 dan TC-599: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Akun aktor blok TC-600 dan TC-643: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login Total Control di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; ganti akun ke Default User dilakukan eksplisit pada langkah 14; hook `after` memulihkan sesi ke Default User.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `Jane Smith {runId}-174A` | `janesmith+{runId}-174a@qwertysystem.net` | Activated, Active di Admin Console, Active di Global Settings (TC-598) |
| U2 | `Jane Smith {runId}-174B` | `janesmith+{runId}-174b@qwertysystem.net` | Inactive di Admin Console dan nonaktif di Global Settings (TC-599) |
| U3 | `Mike Tan {runId}-174C` | `miketan+{runId}-174c@qwertysystem.net` | Activated, App Access Admin Console aktif, Global Role dan Group Role aktif (Region A dari Group Tree Pre-setup, tidak diubah) (TC-600) |
| U4 | `John Doe {runId}-174D` | `johndoe+{runId}-174d@qwertysystem.net` | Activated, memiliki Global Role "Manage group" (TC-643); role "Manage group" juga dimiliki sedikitnya satu user seeding lain agar tabel user Detail Role tidak kosong setelah U4 dihapus (lihat U5) |
| U5 | `Sarah Lee {runId}-174E` | `sarahlee+{runId}-174e@qwertysystem.net` | Activated, memiliki Global Role "Manage group" (user seeding lain untuk TC-643); dihapus atau dipulihkan hook `after` |

- U3 memiliki sedikitnya satu entri Changelog: User sebelum App Access dicabut (disediakan tim FE/BE; dipakai langkah 27).

- Kemampuan teknis: Fixture BE (seeding user, App Access, dan role). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-598: Nonaktif di Global Settings mengunci switch
1. Buka Global Settings > User, lalu nonaktifkan U1 (`Jane Smith {runId}-174A`)
2. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Jane Smith {runId}-174A`, tekan Enter
3. Hover switch Active baris U1
4. Verifikasi switch tetap OFF dan tampil disabled
5. Verifikasi tooltip `"This user is inactive in Global Settings. Contact a Global Settings admin to reactivate."`
6. Klik icon Changelog di toolbar, lalu ketik Search `Jane Smith {runId}-174A` pada Popup Changelog: User, tekan Enter
7. Verifikasi Popup Changelog: User menampilkan empty state `No results found` untuk U1 (tidak ada entri Changelog: User)
### TC-AC-SU-599: Aktif kembali di Global Settings
8. Tutup popup, buka Global Settings > User, lalu aktifkan U2 (`Jane Smith {runId}-174B`)
9. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Jane Smith {runId}-174B`, tekan Enter
10. Verifikasi switch Active baris U2 enabled di posisi OFF (tidak di-reset ke ON)
11. Klik switch Active baris U2
12. Verifikasi dialog Activate User tampil
13. Klik `[Cancel]` pada dialog Activate User
### TC-AC-SU-600: Cabut App Access Admin Console
14. Lakukan Logout dari akun Total Control
15. Login sebagai Default User, lalu buka Global Settings > User dan cabut App Access Admin Console U3 (`Mike Tan {runId}-174C`)
16. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-174C`, tekan Enter
17. Verifikasi U3 tidak ada di User List (hasil Search menampilkan empty state `No results found`)
18. Buka Global Settings > User dan berikan App Access Admin Console lagi kepada U3
19. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `Mike Tan {runId}-174C`, tekan Enter
20. Verifikasi U3 tampil di User List dengan `0 roles`
21. Klik Name baris U3 untuk membuka Detail, lalu klik Tab Role
22. Verifikasi sedikitnya satu switch Global Role tampil
23. Verifikasi sedikitnya satu baris Group Role tampil
24. Verifikasi seluruh switch Global Role OFF dan Group Role tanpa group
25. Verifikasi banner Total Control, Read Only, dan Group Manager tidak tampil
26. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-174C` pada Popup Changelog: User, tekan Enter
27. Verifikasi Popup Changelog: User masih memuat riwayat lama U3
### TC-AC-SU-643: Hapus user di Global Settings
28. Tutup popup, buka Global Settings > User, lalu hapus U4 (`John Doe {runId}-174D`)
29. Tunggu aksi selesai, klik menu Settings > User di sidebar, lalu ketik Search `John Doe {runId}-174D`, tekan Enter
30. Verifikasi U4 tidak ada di User List (hasil Search menampilkan empty state `No results found`)
31. Klik menu Settings > Role & Permission di sidebar, lalu buka Detail role "Manage group"
32. Verifikasi header tabel user Detail Role "Manage group" tampil
33. Ketik Search `{runId}-174` pada tabel user Detail Role "Manage group", tekan Enter
34. Verifikasi sedikitnya satu baris user tampil di tabel user Detail Role "Manage group"
35. Verifikasi U4 tidak ada di tabel user Detail Role "Manage group"

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): aksi di Global Settings > User, navigasi sidebar, Search nama target dan pembukaan Detail (R-16), dan menutup popup. Ganti akun eksplisit pada langkah 14 karena TC-600 dan TC-643 mensyaratkan Default User sedangkan TC-598 dan TC-599 mensyaratkan Total Control.
- Asersi absence mengikuti bagian 8b butir 2: empty state hasil Search (`No results found`) menjadi anchor untuk absence baris pada User List dan Popup Changelog: User; TC-643 butir b didahului Verifikasi bahwa U4 tidak ada di User List, dan absence U4 pada tabel user Detail Role didahului Search `{runId}-174` (membatasi tabel ke U4 dan U5), Verifikasi header tabel, dan Verifikasi sedikitnya satu baris user (U5) pada tabel user Detail Role tampil (anchor permukaan dan data).
- Aksi menghapus user (TC-643) ditaruh paling akhir (S-10). Empat blok TC independen dengan user seeding sendiri.
- Temuan untuk QA:
  - TC-599 mengakhiri alur dengan dialog Activate User terbuka tanpa menyatakan penutupannya; spec menutup lewat `[Cancel]` sebagai langkah penghubung agar tidak mengaktifkan user.
  - TC-600 butir c ("Riwayat Popup Changelog: User lama tetap ada") tidak menyebut entri yang diasersi; spec mengasersi keberadaan sedikitnya satu baris untuk U3 (riwayat seeding atau riwayat lama, disediakan Fixture BE).
  - TC-600 dan TC-643 menyebut Global Settings > User tanpa menyebut akun yang berhak; spec memakai Default User sesuai precondition TC.
  - TC memakai nama literal (`Jane Smith`, `Mike Tan`, `John Doe`); spec memakai nama bersuffix (S-12).
