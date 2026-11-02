---
id: TC-AC-SU-E2E-149-modal-changelog-group-role-filter-panel-dua-field-and-dan-satu-opsi
title: "Modal Changelog Group Role: Filter Panel Role Name dan Group Name, AND, Satu Opsi per Field, dan Rentang Date"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-515
  - TC-AC-SU-516
  - TC-AC-SU-517
  - TC-AC-SU-518
coverage:
  web: automated
---

# Modal Changelog Group Role: Filter Panel Role Name dan Group Name, AND, Satu Opsi per Field, dan Rentang Date

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-149` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign | Manage distributor — Region A {runId}-149 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-149 | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-149 | Update | Assigned | Active | Admin U |
| 4 | Assign | Manage partner — Region A {runId}-149 | Access | Inactive | Assigned | Default User |
| 5 | Edit | Manage distributor — Region A {runId}-149 | Update | Inactive | Active | Admin U |
| 6 | Edit | Manage distributor — Region A {runId}-149 | Update | Inactive | Active | Admin U |
| 7 | Edit | Manage distributor — Region A {runId}-149 | Update | Inactive | Active | Admin U |

- Baris seed nomor 5, 6, dan 7 ber-Date eksplisit pada bulan berjalan: tanggal 02, 05, dan 08. Date Format General Settings entitas Principal tidak diubah spec ini. Role Name tersedia sebagai opsi: `Manage distributor` dan `Manage partner`; Group Name: `Region A {runId}-149` dan `Region B {runId}-149`.

| Field uji Filter | Opsi |
|---|---|
| Action | Edit |
| Field | Update |
| Modified By | Admin U |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-149`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-149` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-515: Filter Panel Modal Group Role: kolom Role Name — Group Name menjadi dua field

3. Klik icon Filter
4. Verifikasi field Filter Panel berurutan: `Date` (date range, placeholder `"Select date"`) | `Action` (placeholder `"All actions"`) | `Role Name` (placeholder `"All roles"`) | `Group Name` (placeholder `"All groups"`) | `Field` (placeholder `"All fields"`) | `Modified By` (placeholder `"All users"`)
5. Buka dropdown `Role Name`
6. Verifikasi opsi dropdown `Role Name` tepat `Manage distributor` dan `Manage partner` (DISTINCT dari entri)
7. Tutup dropdown `Role Name`
8. Buka dropdown `Group Name`
9. Verifikasi opsi dropdown `Group Name` tepat `Region A {runId}-149` dan `Region B {runId}-149` (DISTINCT dari entri)
10. Tutup dropdown `Group Name`

### TC-AC-SU-516: Filter Role Name dan Group Name diterapkan bersamaan (AND)

11. Pilih `Manage distributor` di `Role Name`
12. Pilih `Region A {runId}-149` di `Group Name`
13. Klik `[Apply]`
14. Verifikasi sedikitnya satu baris tampil di tabel
15. Verifikasi tabel hanya menampilkan entri `Manage distributor — Region A {runId}-149`
16. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-517: Filter multi-select, satu opsi per field

17. Untuk setiap baris tabel "Field uji Filter" di Prerequisites (`Action`, `Field`, `Modified By`), lakukan langkah 18 sampai 25
18. Klik icon Filter
19. Pilih opsi `<opsi pada iterasi>` pada field `<field pada iterasi>`, klik `[Apply]`
20. Verifikasi sedikitnya satu baris tampil di tabel
21. Verifikasi tabel hanya menampilkan baris dengan `<field pada iterasi>` `<opsi pada iterasi>`
22. Verifikasi icon Filter menampilkan badge titik (filter ter-Apply)
23. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
24. Verifikasi tabel kembali menampilkan semua baris (baris dengan nilai lain tampil kembali)
25. Verifikasi badge titik pada icon Filter hilang

### TC-AC-SU-518: Filter date range Date inklusif

26. Klik icon Filter
27. Klik field `Date` (placeholder `"Select date"`)
28. Pilih tanggal awal 02 dan tanggal akhir 05
29. Verifikasi isi field `Date` tampil sesuai Date Format General Settings
30. Klik `[Apply]`
31. Verifikasi tabel menampilkan baris seed ber-Date tanggal 02 dan 05 (baris seed nomor 5 dan 6), batas inklusif
32. Verifikasi baris seed ber-Date tanggal 08 (baris seed nomor 7) tidak tampil
33. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per field: langkah 18 sampai 25 (iterasi dari tabel "Field uji Filter" di Prerequisites); `Verifikasi` tetap satu per klausa.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah bersama klik icon `[📋]`; menutup dropdown; membersihkan Filter di langkah 33 dan di akhir TC lain. Filter Panel dibiarkan terbuka dari TC-AC-SU-515 ke TC-AC-SU-516 (TC tidak menyatakan cara menutupnya).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Alasan ekspansi di atas ±35 langkah (33 langkah nominal, sekitar 49 dengan ekspansi blok berulang): semua TC berada di satu surface (Modal Changelog: User > Group Role (Filter Panel)), satu akun, satu dataset; tiap TC berdiri sendiri dan diakhiri `[Clear Field]` lalu `[Apply]` sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: (1) TC-AC-SU-515 mensyaratkan entri `Manage distributor — Region A` dan `Manage partner — Region B`; opsi `Role Name` dan `Group Name` diamati tepat dua nilai karena data user seed milik spec. (2) TC-AC-SU-518 memakai tanggal 02, 05, dan 08 bulan berjalan; pada awal bulan tanggal 05 dan 08 berada di masa depan sehingga seeding Date eksplisit dan pemilih tanggal Filter dapat menolaknya; TC tidak menyebut perilaku ini.
