---
id: TC-AC-SU-E2E-133-modal-changelog-user-filter-search-dropdown-dan-irisan-search-filter
title: "Modal Changelog User: Search di Dropdown Filter serta Irisan Search dan Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-464
  - TC-AC-SU-465
  - TC-AC-SU-466
coverage:
  web: automated
---

# Modal Changelog User: Search di Dropdown Filter serta Irisan Search dan Filter

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-133 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-133 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-133 | Role | Inactive | Active | Budi K |
| 4 | Assign | Mike Tan {runId}-133 | Group | - | Manager | Citra M |
| 5 | Edit | Andi Wijaya {runId}-133 | Tier | Basic | Pro | Dewi L |

- Opsi dropdown `User Name` berisi lebih dari 3 nilai; `Jane Smith {runId}-133` memuat `jan`. Baris yang memuat `Status` ada untuk `John Doe {runId}-133` dan nilai lain.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-464: Search di dalam dropdown User Name

2. Klik icon Filter
3. Buka dropdown `User Name`
4. Ketik `jan` di kotak search dropdown
5. Verifikasi sedikitnya satu opsi tampil di dropdown
6. Verifikasi opsi menyempit ke yang memuat `jan` (case-insensitive)
7. Ganti isi kotak search dropdown dengan `zzqx`
8. Verifikasi dropdown menampilkan state tidak ada opsi cocok
9. Tutup dropdown `User Name`
10. Klik icon Filter lagi untuk menutup Filter Panel

### TC-AC-SU-465: Search lalu Filter, hasil irisan

11. Ketik Search `Status`, tekan Enter
12. Klik icon Filter
13. Pilih `John Doe {runId}-133` di field `User Name`
14. Klik `[Apply]`
15. Verifikasi sedikitnya satu baris tampil di tabel
16. Verifikasi tabel hanya menampilkan baris yang memuat `Status` dan ber-User Name `John Doe {runId}-133`
17. Verifikasi keyword Search `Status` tetap terisi setelah Apply
18. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
19. Klik `(←)` pada kotak Search

### TC-AC-SU-466: Filter lalu Search, hasil irisan

20. Klik icon Filter
21. Pilih `John Doe {runId}-133` di field `User Name`
22. Klik `[Apply]`
23. Ketik Search `Status`, tekan Enter
24. Verifikasi sedikitnya satu baris tampil di tabel
25. Verifikasi tabel hanya menampilkan baris ber-User Name `John Doe {runId}-133` yang memuat `Status`
26. Klik `(←)` pada kotak Search
27. Verifikasi filter User Name `John Doe {runId}-133` tetap aktif: tabel hanya menampilkan baris ber-User Name `John Doe {runId}-133`
28. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): menutup dropdown dan Filter Panel, membersihkan Filter dan Search di akhir tiap TC. TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) TC-AC-SU-464 menyebut "state tidak ada opsi cocok" tanpa teksnya; spec mengasersi state itu tanpa teks karangan (S-02). (2) TC-AC-SU-466 butir b mengasersi filter tetap aktif setelah Search ditutup; spec membandingkannya dengan tabel yang hanya memuat baris User Name terpilih.
