---
id: TC-AC-SU-E2E-132-modal-changelog-user-filter-or-and-chip-dan-uncheck
title: "Modal Changelog User: Filter OR dalam Field, AND antar Field, Chip, dan Uncheck Opsi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-461
  - TC-AC-SU-462
  - TC-AC-SU-463
coverage:
  web: automated
---

# Modal Changelog User: Filter OR dalam Field, AND antar Field, Chip, dan Uncheck Opsi

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-132 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-132 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-132 | Role | Inactive | Active | Budi K |
| 4 | Assign | Mike Tan {runId}-132 | Group | - | Manager | Citra M |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-461: Filter OR di dalam satu field, AND antar field

2. Klik icon Filter
3. Pilih `Activate` dan `Deactivate` di field `Action`
4. Klik `[Apply]`
5. Verifikasi sedikitnya satu baris tampil di tabel
6. Verifikasi tabel hanya menampilkan baris dengan Action `Activate` atau `Deactivate`
7. Klik icon Filter, tambah `John Doe {runId}-132` di field `User Name`
8. Klik `[Apply]`
9. Verifikasi sedikitnya satu baris tampil di tabel
10. Verifikasi tabel hanya menampilkan baris dengan (Action `Activate` atau `Deactivate`) dan User Name `John Doe {runId}-132`
11. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-462: Chip opsi terpilih dan hapus lewat (X) chip

12. Klik icon Filter
13. Pilih `John Doe {runId}-132` lalu `Jane Smith {runId}-132` di field `User Name`
14. Verifikasi chip `John Doe {runId}-132` lalu chip `Jane Smith {runId}-132` muncul berdampingan di dalam field `User Name`
15. Klik `(X)` pada chip `John Doe {runId}-132` tanpa membuka dropdown
16. Verifikasi chip `John Doe {runId}-132` hilang
17. Verifikasi chip `Jane Smith {runId}-132` tetap ada
18. Buka dropdown field `User Name`
19. Verifikasi checkbox `John Doe {runId}-132` ter-uncheck
20. Verifikasi checkbox `Jane Smith {runId}-132` tetap tercentang
21. Klik `[Apply]`
22. Verifikasi sedikitnya satu baris tampil di tabel
23. Verifikasi tabel hanya menampilkan baris User Name `Jane Smith {runId}-132`
24. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-SU-463: Hapus opsi lewat uncheck di dalam dropdown

25. Klik icon Filter
26. Pilih `John Doe {runId}-132` lalu `Jane Smith {runId}-132` di field `User Name`
27. Buka dropdown `User Name`, uncheck `Jane Smith {runId}-132`
28. Tutup dropdown
29. Verifikasi chip `Jane Smith {runId}-132` hilang dari field `User Name`
30. Verifikasi chip `John Doe {runId}-132` tetap ada
31. Klik `[Apply]`
32. Verifikasi sedikitnya satu baris tampil di tabel
33. Verifikasi tabel hanya menampilkan baris User Name `John Doe {runId}-132`
34. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): setiap TC diakhiri `[Clear Field]` lalu `[Apply]` agar TC berikutnya mulai tanpa Filter aktif.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: TC-AC-SU-461 tidak menyebut apakah hasil Apply pertama harus memuat baris user lain; spec memverifikasi hanya batasan Action (ATAU) lalu batasan gabungan (DAN) sesuai Expected.
