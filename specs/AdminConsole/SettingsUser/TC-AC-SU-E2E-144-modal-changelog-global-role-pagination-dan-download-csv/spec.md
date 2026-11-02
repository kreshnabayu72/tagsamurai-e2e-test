---
id: TC-AC-SU-E2E-144-modal-changelog-global-role-pagination-dan-download-csv
title: "Modal Changelog Global Role: Pagination dan Download CSV"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-503
  - TC-AC-SU-646
coverage:
  web: automated
---

# Modal Changelog Global Role: Pagination dan Download CSV

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata; unduhan dibaca dari berkas.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Kemampuan teknis tambahan: membaca berkas unduhan (nama berkas dan jumlah baris data).
- User target Detail: `Jane Smith {runId}-144` (user seed milik spec ini; satu-satunya entri Changelog adalah 15 entri Global Role di bawah).
- Data Dinamis: 15 entri Global Role untuk `Jane Smith {runId}-144` (Action, Role Name, Field, Old Value, New Value, dan Modified By beragam; Date berbeda) dan tanpa Filter atau Search aktif.
- Nama berkas unduhan diturunkan dari nama user seed: spasi pada nama menjadi tanda hubung (`Changelog-Jane-Smith-{runId}-144-Global-Role.csv`).
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Hitungan 15 entri dan 5 entri sisa pada halaman 2 deterministik karena user adalah milik spec ini dan modal hanya memuat entri user ini, sehingga hitungan itu diasersi (S-12 tidak berlaku).

## Test Steps

1. Ketik Search `Jane Smith {runId}-144`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-144` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-503: Pagination Modal Changelog Global Role

3. Verifikasi tabel menampilkan 10 baris per halaman secara default
4. Klik halaman 2
5. Verifikasi halaman 2 menampilkan 5 entri sisanya

### TC-AC-SU-646: Download Modal Changelog: User > Global Role sebagai CSV

6. Klik icon Download
7. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
8. Klik `Download as CSV`
9. Verifikasi tidak ada toast sukses
10. Verifikasi berkas `Changelog-Jane-Smith-{runId}-144-Global-Role.csv` terunduh
11. Verifikasi berkas memuat 15 baris data sesuai baris modal tanpa search atau filter aktif

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03): membuka Detail, tab `Role`, dan sub-tab `Global Role` dijadikan satu langkah bersama klik icon `[📋]`. Modal tetap pada halaman 2 saat Download; TC-AC-SU-646 menyebut berkas sesuai search/filter aktif, dan tidak ada Search atau Filter aktif (halaman tidak memengaruhi isi berkas).
- TC-AC-SU-646 berada di spec ini karena topiknya Download Modal Changelog: User > Global Role dan datasetnya sama dengan Pagination (15 entri Global Role).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: (1) TC-AC-SU-646 menyebut nama berkas `Changelog-Jane-Smith-Global-Role.csv` dari nama literal; dengan nama user bersuffix spec mengasumsikan penurunan nama berkas (spasi menjadi tanda hubung); TC tidak menyatakan aturan penurunannya. (2) TC-AC-SU-646 mengasersi berkas "sesuai search/filter aktif" tanpa Search atau Filter aktif; spec mengasersi seluruh 15 baris.
