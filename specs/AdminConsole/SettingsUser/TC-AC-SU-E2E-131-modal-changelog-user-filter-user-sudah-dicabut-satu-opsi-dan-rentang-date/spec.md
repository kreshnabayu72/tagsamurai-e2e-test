---
id: TC-AC-SU-E2E-131-modal-changelog-user-filter-user-sudah-dicabut-satu-opsi-dan-rentang-date
title: "Modal Changelog User: Filter User Name Akses Dicabut, Satu Opsi per Field, dan Rentang Date"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-458
  - TC-AC-SU-459
  - TC-AC-SU-460
coverage:
  web: automated
---

# Modal Changelog User: Filter User Name Akses Dicabut, Satu Opsi per Field, dan Rentang Date

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-131 | Status | Active | Inactive | Admin U |
| 2 | Activate | Jane Smith {runId}-131 | Role | Inactive | Active | Budi K |
| 3 | Deactivate | Sarah Lee {runId}-131 | Status | Active | Inactive | Admin U |
| 4 | Assign | Mike Tan {runId}-131 | Group | - | Manager | Citra M |

- Seed untuk TC-AC-SU-458: user `Sarah Lee {runId}-131` punya entri nomor 3 lalu App Access Admin Console-nya dicabut di Global Settings (dilakukan fixture BE di hook `before`, dipakai sebagai precondition TC, tidak diasersi); user `Andi Wijaya {runId}-131` ada di User List tanpa entri Changelog.
- Seed untuk TC-AC-SU-460: tiga entri tambahan ber-Date relatif terhadap hari uji (T-N berarti N hari sebelum hari uji): T-10 (`Rina Putri {runId}-131`, Action `Edit`), T-7 (`Budi Santoso {runId}-131`, Action `Edit`), dan T-4 (`Dewi Lestari {runId}-131`, Action `Edit`), masing-masing Field `Tier`, Modified By `Admin U`.
- Date Format General Settings entitas Principal tidak diubah spec ini.

| Field uji Filter | Opsi |
|---|---|
| Action | Deactivate |
| User Name | John Doe {runId}-131 |
| Field | Status |
| Modified By | Admin U |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-458: Filter User Name, user yang sudah dicabut App Access tetap jadi opsi

2. Klik icon Filter
3. Buka dropdown `User Name`
4. Verifikasi opsi `Sarah Lee {runId}-131` muncul (snapshot entri log)
5. Verifikasi opsi `Andi Wijaya {runId}-131` tidak muncul (0 entri)
6. Tutup dropdown `User Name`
7. Klik icon Filter lagi untuk menutup Filter Panel

### TC-AC-SU-459: Filter multi-select, satu opsi per field

8. Untuk setiap baris tabel "Field uji Filter" di Prerequisites (`Action`, `User Name`, `Field`, `Modified By`), lakukan langkah 9 sampai 16
9. Klik icon Filter
10. Pilih opsi `<opsi pada iterasi>` pada field `<field pada iterasi>`, klik `[Apply]`
11. Verifikasi sedikitnya satu baris tampil di tabel
12. Verifikasi tabel hanya menampilkan baris dengan `<field pada iterasi>` `<opsi pada iterasi>`
13. Verifikasi icon Filter menampilkan badge titik (filter ter-Apply)
14. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
15. Verifikasi tabel kembali menampilkan semua baris (baris dengan nilai lain tampil kembali)
16. Verifikasi badge titik pada icon Filter hilang

### TC-AC-SU-460: Filter date range Date inklusif

17. Klik icon Filter
18. Klik field `Date` (placeholder `"Select date"`)
19. Pilih tanggal awal T-10 dan tanggal akhir T-7
20. Verifikasi isi field `Date` tampil sesuai Date Format General Settings
21. Pilih opsi `Rina Putri {runId}-131`, `Budi Santoso {runId}-131`, dan `Dewi Lestari {runId}-131` pada field `User Name`
22. Klik `[Apply]`
23. Verifikasi tabel menampilkan baris seed ber-Date T-10 dan T-7 (`Rina Putri {runId}-131` dan `Budi Santoso {runId}-131`), batas inklusif
24. Verifikasi baris seed ber-Date T-4 (`Dewi Lestari {runId}-131`) tidak tampil
25. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per field: langkah 9 sampai 16 (iterasi dari tabel "Field uji Filter" di Prerequisites); `Verifikasi` tetap satu per klausa.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): menutup dropdown dan Filter Panel, serta memilih user seed pada field `User Name` sebagai Filter pembatas di langkah 21 (agar asersi Date tidak bercampur entri run lain pada audit trail se-entitas, S-14), serta membersihkan Filter di langkah 25. TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) TC-AC-SU-458 menyebut pencabutan App Access sebagai precondition tanpa menyebut cara; spec menyerahkannya ke fixture BE (disediakan tim FE/BE). (2) TC-AC-SU-460 tidak menyebut user pemilik baris T-10, T-7, dan T-4; spec memakai user Pre-setup lain (`Rina Putri`, `Budi Santoso`, `Dewi Lestari`) bersuffix agar baris dapat diidentifikasi.
