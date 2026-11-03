---
id: TC-AC-SU-E2E-126-modal-changelog-user-screening-isi-dan-state
title: "Modal Changelog User: Screening, Isi Lintas User, Loading, Empty Search, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-443
  - TC-AC-SU-444
  - TC-AC-SU-445
  - TC-AC-SU-446
  - TC-AC-SU-448
coverage:
  web: automated
---

# Modal Changelog User: Screening, Isi Lintas User, Loading, Empty Search, dan Empty State

## Prerequisites

- Mode: FE+BE. Penundaan respons (intercept parsial di atas backend nyata) hanya untuk mengamati state Loading TC-AC-SU-446; data dan state lain dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-126 | Status | Active | Inactive | Admin U |
| 2 | Activate | Jane Smith {runId}-126 | Status | Inactive | Active | Admin U |
| 3 | Deactivate | Mike Tan {runId}-126 | Status | Active | Inactive | Admin U |
| 4 | Activate | John Doe {runId}-126 | Status | Inactive | Active | Admin U |
| 5 | Deactivate | Jane Smith {runId}-126 | Status | Active | Inactive | Admin U |

- Data entitas lain: satu entri Changelog `Sarah Lee {runId}-126` (Action `Deactivate`, Field `Status`) di entitas Distributor Nusantara dengan Date paling baru dari seluruh entri (dipakai TC-AC-SU-444 butir b).
- Kemampuan teknis tambahan: menahan respons data tabel Modal Changelog: User selama 3000 ms lewat `Spectra.intercept()` dan melepasnya; mengondisikan sumber data modal berjumlah 0 baris untuk TC-AC-SU-445.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

### TC-AC-SU-443: Screening Modal Changelog: User

1. Klik icon Changelog di toolbar User List
2. Verifikasi header modal menampilkan Title `Changelog: User` dan icon `[×]`
3. Verifikasi toolbar menampilkan `Search | Filter | Download`
4. Verifikasi kolom tabel: `Date (sortable) | Action (sortable) | User Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable — header = overlay Column Visibility, tanpa row action)`
5. Verifikasi nilai kolom `User Name` berupa plain text, bukan link
6. Verifikasi default sort Date Newest First
7. Verifikasi footer menampilkan pagination standar

### TC-AC-SU-444: Modal Changelog: User memuat entri lintas semua user entitas

8. Verifikasi entri `John Doe {runId}-126`, `Jane Smith {runId}-126`, dan `Mike Tan {runId}-126` tampil dalam satu tabel
9. Verifikasi entri user milik entitas lain (`Sarah Lee {runId}-126`) tidak tampil di halaman pertama yang berurut Date Newest First

### TC-AC-SU-446: Loading state Modal Changelog: User

10. Tutup modal dengan klik icon `[×]`
11. Pasang intercept yang menunda respons data tabel Modal Changelog: User selama 3000 ms
12. Klik icon Changelog di toolbar User List
13. Verifikasi selama menunggu, tabel menampilkan 5 skeleton rows sesuai layout kolom
14. Verifikasi setelah respons diterima, baris data menggantikan skeleton
15. Lepas intercept

### TC-AC-SU-448: Empty state hasil Search tanpa kecocokan

16. Ketik Search `zzqx-tidak-ada`, tekan Enter
17. Verifikasi tabel menampilkan illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
18. Klik `(←)` pada kotak Search

### TC-AC-SU-445: Empty state Modal Changelog: User saat belum ada data

19. Tutup modal dengan klik icon `[×]`
20. Kondisikan sumber data Modal Changelog: User berjumlah 0 baris (kemampuan disediakan tim FE/BE)
21. Klik icon Changelog di toolbar User List
22. Verifikasi tabel menampilkan illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
23. Verifikasi pagination tidak menampilkan baris data
24. Pulihkan sumber data Modal Changelog: User ke keadaan sebelum langkah 20 (kemampuan disediakan tim FE/BE)
25. Tutup modal dengan klik icon `[×]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: 443, 444, 446, 448, lalu 445 (S-10): TC-AC-SU-445 mengondisikan sumber data menjadi kosong sehingga ditaruh di akhir agar TC lain memakai data seed. Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): menutup modal (langkah 10, 19, dan 25), melepas intercept (langkah 15), menutup input Search (langkah 18), mengondisikan dan memulihkan sumber data (langkah 20 dan 24).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) TC-AC-SU-445 mensyaratkan sumber data modal berjumlah 0 baris, padahal entitas yang sama dipakai TC-AC-SU-443 dan 444 (berisi entri) dan Changelog adalah audit trail permanen; TC tidak menyebut cara mengosongkan sumber, sehingga spec menulisnya sebagai kemampuan yang disediakan tim FE/BE. (2) TC-AC-SU-444 butir b tidak menyebut data entitas lain; spec men-seed entri user di Distributor Nusantara dengan Date terbaru agar kebocoran terlihat di halaman pertama. (3) TC-AC-SU-446 tidak menyebut endpoint yang ditunda; spec menunda respons data tabel modal tanpa menulis endpoint (S-13). (4) TC-AC-SU-443 butir d ("User Name berupa plain text, bukan link") tidak menyebut cara pengamatan; spec memverifikasi tidak ada tautan pada nilai kolom.
