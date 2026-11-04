---
id: TC-AC-SU-E2E-154-modal-changelog-group-role-pagination
title: "Modal Changelog Group Role: Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-529
coverage:
  web: automated
---

# Modal Changelog Group Role: Pagination

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-154` (user seed milik spec ini; satu-satunya entri Changelog adalah 15 entri Group Role di bawah).
- Data Dinamis: 15 entri Group Role untuk `Jane Smith {runId}-154` (Action, Role Name — Group Name, Field, Old Value, New Value, dan Modified By beragam; Date berbeda) dan tanpa Filter atau Search aktif.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Hitungan 15 entri dan 5 entri sisa pada halaman 2 deterministik karena user adalah milik spec ini dan modal hanya memuat entri user ini, sehingga baseline entri adalah nol dan hitungan itu diasersi sebagai jumlah absolut, bukan selisih terhadap N yang dibaca.

## Test Steps

1. Ketik Search `Jane Smith {runId}-154`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-154` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-529: Pagination Modal Changelog Group Role

3. Verifikasi tabel menampilkan 10 baris per halaman secara default
4. Klik halaman 2
5. Verifikasi halaman 2 menampilkan 5 entri sisanya

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03): membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah bersama klik icon `[📋]`.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
