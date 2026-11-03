---
id: TC-AC-SU-E2E-141-modal-changelog-global-role-filter-panel
title: "Modal Changelog Global Role: Screening Filter Panel, Satu Opsi per Field, Rentang Date, dan OR/AND"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-491
  - TC-AC-SU-492
  - TC-AC-SU-493
  - TC-AC-SU-494
coverage:
  web: automated
---

# Modal Changelog Global Role: Screening Filter Panel, Satu Opsi per Field, Rentang Date, dan OR/AND

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-141` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target):

| No | Action | Role Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Total Control) | Manage group | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage group | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage group | Update | Assigned | Active | Admin U |
| 4 | Assign | Manage user and role | Access | - | Assigned | Budi K |
| 5 | Edit | Manage partner | Update | Inactive | Active | Citra M |
| 6 | Edit | Manage partner | Update | Inactive | Active | Citra M |
| 7 | Edit | Manage partner | Update | Inactive | Active | Citra M |

- Baris seed nomor 5, 6, dan 7 ber-Date eksplisit pada bulan berjalan: tanggal 02, 05, dan 08. Date Format General Settings entitas Principal tidak diubah spec ini.

| Field uji Filter | Opsi |
|---|---|
| Action | Assign (via Total Control) |
| Role Name | Manage group |
| Field | Access |
| Modified By | Default User |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-141`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-141` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-491: Screening Filter Panel

3. Hover icon Filter
4. Verifikasi tooltip `Filter` tampil
5. Klik icon Filter
6. Verifikasi Filter Panel terbuka di bawah toolbar
7. Verifikasi field Filter Panel berurutan: `Date` (date range picker, placeholder `"Select date"`) | `Action` (multi-select searchable, placeholder `"All actions"`) | `Role Name` (multi-select searchable, placeholder `"All roles"`) | `Field` (multi-select searchable, placeholder `"All fields"`) | `Modified By` (multi-select searchable, placeholder `"All users"`)
8. Verifikasi footer Filter Panel menampilkan link `[Clear Field]` (kiri) dan `[Apply]` (kanan)
9. Klik icon Filter lagi untuk menutup Filter Panel

### TC-AC-SU-492: Filter multi-select, satu opsi per field

10. Untuk setiap baris tabel "Field uji Filter" di Prerequisites (`Action`, `Role Name`, `Field`, `Modified By`), lakukan langkah 11 sampai 18
11. Klik icon Filter
12. Pilih opsi `<opsi pada iterasi>` pada field `<field pada iterasi>`, klik `[Apply]`
13. Verifikasi sedikitnya satu baris tampil di tabel
14. Verifikasi tabel hanya menampilkan baris dengan `<field pada iterasi>` `<opsi pada iterasi>`
15. Verifikasi icon Filter menampilkan badge titik (filter ter-Apply)
16. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
17. Verifikasi tabel kembali menampilkan semua baris (baris dengan nilai lain tampil kembali)
18. Verifikasi badge titik pada icon Filter hilang

### TC-AC-SU-493: Filter date range Date inklusif

19. Klik icon Filter
20. Klik field `Date` (placeholder `"Select date"`)
21. Pilih tanggal awal 02 dan tanggal akhir 05
22. Verifikasi isi field `Date` tampil sesuai Date Format General Settings
23. Klik `[Apply]`
24. Verifikasi tabel menampilkan baris seed ber-Date tanggal 02 dan 05 (baris seed nomor 5 dan 6), batas inklusif
25. Verifikasi baris seed ber-Date tanggal 08 (baris seed nomor 7) tidak tampil
26. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-494: Filter OR di dalam satu field, AND antar field

27. Klik icon Filter
28. Pilih `Assign` dan `Remove` di field `Action`
29. Klik `[Apply]`
30. Verifikasi sedikitnya satu baris tampil di tabel
31. Verifikasi tabel hanya menampilkan baris dengan Action `Assign` atau `Remove`
32. Klik icon Filter, tambah `Manage group` di field `Role Name`
33. Klik `[Apply]`
34. Verifikasi sedikitnya satu baris tampil di tabel
35. Verifikasi tabel hanya menampilkan baris dengan (Action `Assign` atau `Remove`) dan Role Name `Manage group`
36. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per field: langkah 11 sampai 18 (iterasi dari tabel "Field uji Filter" di Prerequisites); `Verifikasi` tetap satu per klausa.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): membuka Detail, tab `Role`, dan sub-tab `Global Role` dijadikan satu langkah bersama klik icon `[📋]`; menutup Filter Panel; membersihkan Filter di langkah 26 dan di akhir TC. TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: (1) TC-AC-SU-493 memakai tanggal 02, 05, dan 08 bulan berjalan; pada awal bulan tanggal 05 dan 08 berada di masa depan sehingga seeding Date eksplisit dan pemilih tanggal Filter dapat menolaknya; TC tidak menyebut perilaku ini. (2) Nilai `Assign (via Total Control)` pada TC-AC-SU-492 adalah satu nilai Action utuh; TC-AC-SU-494 memakai `Assign` dan `Remove` sebagai nilai terpisah, sehingga seed memuat kedua bentuk Action. Pelaku seed `Budi K` dan `Citra M` pada kolom Modified By tidak terpetakan ke akun mana pun di Pre-setup; nilai dipakai apa adanya sebagai data seed, bukan akun login.
- Jumlah langkah 36 (di atas smell 35 langkah; sekitar 60 dengan ekspansi iterasi): langkah 11 sampai 18 adalah iterasi per field dari tabel "Field uji Filter" yang ditulis sebagai satu daftar, dan langkah 1 (Search) adalah langkah penghubung tanpa `Verifikasi`. Semua TC berada di satu surface (Modal Changelog: User > Global Role (Filter Panel)), satu akun, satu dataset; tiap TC berdiri sendiri dan diakhiri `[Clear Field]` lalu `[Apply]` sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, sedangkan pemecahan menggandakan seeding dan pembukaan Detail.
