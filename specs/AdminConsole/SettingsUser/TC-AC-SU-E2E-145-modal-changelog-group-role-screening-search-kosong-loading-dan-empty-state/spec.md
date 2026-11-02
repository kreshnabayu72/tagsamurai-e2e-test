---
id: TC-AC-SU-E2E-145-modal-changelog-group-role-screening-search-kosong-loading-dan-empty-state
title: "Modal Changelog Group Role: Screening, Search Kosong, Loading, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-505
  - TC-AC-SU-506
  - TC-AC-SU-508
  - TC-AC-SU-530
coverage:
  web: automated
---

# Modal Changelog Group Role: Screening, Search Kosong, Loading, dan Empty State

## Prerequisites

- Mode: FE+BE. Penundaan respons (intercept parsial di atas backend nyata) hanya untuk mengamati state Loading TC-AC-SU-530; data dan state lain dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-145` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama; dipakai sebagai precondition TC, tidak diasersi):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign | Manage distributor — Region A {runId}-145 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-145 | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-145 | Update | Assigned | Active | Admin U |
| 4 | Assign (via Read Only) | Manage partner — Region A {runId}-145 | Access | Inactive | Assigned | Default User |

- Untuk TC-AC-SU-506: user `Andi Wijaya {runId}-145` (user seed tanpa entri Group Role; menggantikan target `Jane Smith` yang berisi entri).
- Kemampuan teknis tambahan: menahan respons data tabel Modal Changelog: User > Group Role selama 3000 ms lewat `Spectra.intercept()` dan melepasnya.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-145`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-145` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-505: Screening Modal Changelog: User > Group Role

3. Verifikasi header modal menampilkan Title `Changelog: User > Group Role` dan icon `[×]`
4. Verifikasi toolbar menampilkan `Search | Filter | Download`
5. Verifikasi kolom tabel: `Date (sortable) | Action (sortable) | Role Name — Group Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
6. Verifikasi default sort Date Newest First
7. Verifikasi footer menampilkan pagination standar

### TC-AC-SU-508: Empty state hasil Search tanpa kecocokan

8. Ketik Search `zzqx-tidak-ada`, tekan Enter
9. Verifikasi tabel menampilkan illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
10. Klik `(←)` pada kotak Search

### TC-AC-SU-530: Loading state Modal Changelog: User > Group Role

11. Tutup modal dengan klik icon `[×]`
12. Buka Settings > User lewat sidebar
13. Pasang intercept yang menunda respons data tabel Modal Changelog: User > Group Role selama 3000 ms
14. Ketik Search `Jane Smith {runId}-145`, tekan Enter
15. Buka Detail user `Jane Smith {runId}-145` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog
16. Verifikasi selama menunggu, tabel modal menampilkan 5 skeleton rows sesuai layout kolom
17. Verifikasi setelah respons diterima, baris data menggantikan skeleton
18. Lepas intercept

### TC-AC-SU-506: Empty state Modal Changelog: User > Group Role saat belum ada data

19. Tutup modal dengan klik icon `[×]`
20. Buka Settings > User lewat sidebar
21. Ketik Search `Andi Wijaya {runId}-145`, tekan Enter
22. Buka Detail user `Andi Wijaya {runId}-145` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog
23. Verifikasi tabel menampilkan illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
24. Verifikasi pagination tidak menampilkan baris data
25. Tutup modal dengan klik icon `[×]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: 505, 508, 530, lalu 506 (S-10): TC-AC-SU-530 dimulai dari User List dan TC-AC-SU-506 memakai target lain, sehingga keduanya di akhir. Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): menutup input Search (langkah 10), menutup modal (langkah 11, 19, dan 25), kembali ke User List lewat sidebar (langkah 12 dan 20), dan melepas intercept (langkah 18). Langkah membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah penghubung dengan klik icon `[📋]`.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1, 14 dan 21); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: (1) TC-AC-SU-506 memakai target `Jane Smith` dengan sumber data Group Role berjumlah 0 baris, sedangkan TC-AC-SU-505 sampai 508 memakai Jane Smith yang berisi entri; spec memakai user seed tanpa entri untuk TC-AC-SU-506. (2) TC-AC-SU-530 tidak menyebut endpoint yang ditunda (S-13). (3) TC-AC-SU-505 menyebut entri `Assign (via Read Only)`; nilai Action itu di-seed apa adanya.
