---
id: TC-AC-SU-E2E-150-modal-changelog-group-role-filter-chip-dan-uncheck-group-name
title: "Modal Changelog Group Role: Filter Chip Opsi Group Name dan Hapus Opsi lewat Uncheck"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-519
  - TC-AC-SU-520
coverage:
  web: automated
---

# Modal Changelog Group Role: Filter Chip Opsi Group Name dan Hapus Opsi lewat Uncheck

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-150` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign | Manage distributor — Region A {runId}-150 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-150 | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-150 | Update | Assigned | Active | Admin U |
| 4 | Assign (via Read Only) | Manage partner — Region A {runId}-150 | Access | Inactive | Assigned | Default User |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-150`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-150` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-519: Chip opsi terpilih dan hapus lewat (X) chip

3. Klik icon Filter
4. Pilih `Region A {runId}-150` lalu `Region B {runId}-150` di field `Group Name`
5. Verifikasi chip `Region A {runId}-150` lalu chip `Region B {runId}-150` muncul berdampingan di dalam field `Group Name`
6. Klik `(X)` pada chip `Region A {runId}-150` tanpa membuka dropdown
7. Verifikasi chip `Region A {runId}-150` hilang
8. Verifikasi chip `Region B {runId}-150` tetap ada
9. Buka dropdown field `Group Name`
10. Verifikasi checkbox `Region A {runId}-150` tidak tercentang
11. Verifikasi checkbox `Region B {runId}-150` tetap tercentang
12. Klik `[Apply]`
13. Verifikasi sedikitnya satu baris tampil di tabel
14. Verifikasi tabel hanya menampilkan baris Group Name `Region B {runId}-150`
15. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-520: Hapus opsi lewat uncheck di dalam dropdown

16. Klik icon Filter
17. Pilih `Region A {runId}-150` lalu `Region B {runId}-150` di field `Group Name`
18. Buka dropdown `Group Name`, hapus centang `Region B {runId}-150`
19. Tutup dropdown
20. Verifikasi chip `Region A {runId}-150` tetap ada
21. Verifikasi chip `Region B {runId}-150` hilang dari field `Group Name`
22. Klik `[Apply]`
23. Verifikasi sedikitnya satu baris tampil di tabel
24. Verifikasi tabel hanya menampilkan baris Group Name `Region A {runId}-150`
25. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah bersama klik icon `[📋]`; setiap TC diakhiri `[Clear Field]` lalu `[Apply]`.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: TC-AC-SU-519 dan 520 menyebut baris Group Name `Region A` dan `Region B` pada kolom gabungan `Role Name — Group Name`; spec memakai field `Group Name` pada Filter Panel sesuai TC-AC-SU-515.
