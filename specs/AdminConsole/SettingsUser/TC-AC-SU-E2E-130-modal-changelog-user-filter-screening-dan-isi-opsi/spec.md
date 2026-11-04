---
id: TC-AC-SU-E2E-130-modal-changelog-user-filter-screening-dan-isi-opsi
title: "Modal Changelog User: Screening Filter Panel dan Isi Opsi Dropdown Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-456
  - TC-AC-SU-457
coverage:
  web: automated
---

# Modal Changelog User: Screening Filter Panel dan Isi Opsi Dropdown Filter

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-130 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-130 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-130 | Role | Inactive | Active | Budi K |

- User `Andi Wijaya {runId}-130` ada di User List tanpa entri Changelog (fixture membuat user tanpa entri Changelog; disediakan tim FE/BE).
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-456: Screening Filter Panel

2. Hover icon Filter
3. Verifikasi tooltip `Filter` tampil
4. Klik icon Filter
5. Verifikasi Filter Panel terbuka di bawah toolbar
6. Verifikasi field Filter Panel berurutan: `Date` (date range picker, placeholder `"Select date"`) | `Action` (multi-select searchable, placeholder `"All actions"`) | `User Name` (multi-select searchable, placeholder `"All users"`) | `Field` (multi-select searchable, placeholder `"All fields"`) | `Modified By` (multi-select searchable, placeholder `"All users"`)
7. Verifikasi footer Filter Panel menampilkan link `[Clear Field]` (kiri) dan `[Apply]` (kanan)
8. Klik icon Filter lagi untuk menutup Filter Panel

### TC-AC-SU-457: Isi opsi dropdown Filter dipopulasi dari data tabel

9. Klik icon Filter
10. Buka dropdown `User Name`
11. Ketik `{runId}-130` pada kotak search dropdown `User Name`
12. Verifikasi opsi dropdown `User Name` memuat `John Doe {runId}-130` dan `Jane Smith {runId}-130`
13. Verifikasi opsi `John Doe {runId}-130` muncul satu kali meski punya dua entri (DISTINCT)
14. Verifikasi opsi `Andi Wijaya {runId}-130` tidak muncul (user tanpa entri di tabel)
15. Tutup dropdown `User Name`
16. Buka dropdown `Action`
17. Ketik `activate` pada kotak search dropdown `Action`
18. Verifikasi opsi dropdown `Action` memuat `Deactivate` dan `Activate` (nilai Action yang tercatat)
19. Tutup dropdown `Action`
20. Buka dropdown `Modified By`
21. Ketik `Admin U` pada kotak search dropdown `Modified By`
22. Verifikasi opsi dropdown `Modified By` memuat `Admin U` (aktor yang tercatat)
23. Tutup dropdown `Modified By`
24. Klik icon Filter lagi untuk menutup Filter Panel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03): menutup dropdown dan Filter Panel, serta mengetik keyword pada kotak search dropdown (`{runId}-130`, `activate`, `Admin U`) agar daftar opsi tersaring ke nilai seed sebelum diverifikasi; keyword `{runId}-130` juga mencocokkan `Andi Wijaya {runId}-130`, sehingga ketidakhadirannya tetap bermakna. TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) TC-AC-SU-457 menuntut opsi sama dengan nilai DISTINCT seluruh baris tabel dan "nilai yang tidak ada di baris tabel tidak muncul"; karena Changelog entitas permanen dan lintas spec, spec hanya mengasersi nilai seed hadir, user tanpa entri tidak hadir, dan opsi tidak duplikat. TC tidak menyebut nilai pembanding yang pasti tidak tercatat untuk `Action` dan `Modified By`, sehingga absence untuk kedua dropdown itu tidak diasersi. (2) TC tidak menyebut apakah pembuatan user seed menghasilkan entri Changelog; spec mengandalkan fixture BE yang membuat user tanpa entri.
