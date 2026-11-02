---
id: TC-AC-SU-E2E-138-modal-changelog-global-role-screening-isi-dan-state
title: "Modal Changelog Global Role: Screening, Cakupan Entri, Search Kosong, Loading, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-480
  - TC-AC-SU-481
  - TC-AC-SU-482
  - TC-AC-SU-484
  - TC-AC-SU-504
coverage:
  web: automated
---

# Modal Changelog Global Role: Screening, Cakupan Entri, Search Kosong, Loading, dan Empty State

## Prerequisites

- Mode: FE+BE. Penundaan respons (intercept parsial di atas backend nyata) hanya untuk mengamati state Loading TC-AC-SU-504; data dan state lain dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-138` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Total Control) | Manage group | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage group | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage group | Update | Assigned | Active | Admin U |
| 4 | Assign | Manage user and role | Access | - | Assigned | Budi K |

- Seed tambahan untuk TC-AC-SU-481: satu entri Group Role (Action `Assign`, Role Name — Group Name `Manage distributor — Region A {runId}-138`) dan satu entri Access Level (Field `Access Level`, Action `Edit`) untuk `Jane Smith {runId}-138`.
- Untuk TC-AC-SU-482: user `Andi Wijaya {runId}-138` (user seed tanpa entri Global Role; menggantikan target `Jane Smith` yang berisi entri).
- Kemampuan teknis tambahan: menahan respons data tabel Modal Changelog: User > Global Role selama 3000 ms lewat `Spectra.intercept()` dan melepasnya.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-138`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-138` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-480: Screening Modal Changelog: User > Global Role

3. Verifikasi header modal menampilkan Title `Changelog: User > Global Role` dan icon `[×]`
4. Verifikasi toolbar menampilkan `Search | Filter | Download`
5. Verifikasi kolom tabel: `Date (sortable) | Action (sortable) | Role Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
6. Verifikasi sedikitnya satu baris tampil di tabel
7. Verifikasi nilai kolom `Field` pada setiap baris terisi (`Access` atau nama permission)
8. Verifikasi default sort Date Newest First
9. Verifikasi footer menampilkan pagination standar

### TC-AC-SU-481: Modal Changelog Global Role tidak memuat entri Group Role maupun Access Level

10. Verifikasi entri Global Role seed `Manage group` tampil
11. Verifikasi entri Field `Access Level` dan entri Group Role (`Manage distributor — Region A {runId}-138`) tidak tampil

### TC-AC-SU-484: Empty state hasil Search tanpa kecocokan

12. Ketik Search `zzqx-tidak-ada`, tekan Enter
13. Verifikasi tabel menampilkan illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
14. Klik `(←)` pada kotak Search

### TC-AC-SU-504: Loading state Modal Changelog: User > Global Role

15. Tutup modal dengan klik icon `[×]`
16. Buka Settings > User lewat sidebar
17. Pasang intercept yang menunda respons data tabel Modal Changelog: User > Global Role selama 3000 ms
18. Ketik Search `Jane Smith {runId}-138`, tekan Enter
19. Buka Detail user `Jane Smith {runId}-138` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog
20. Verifikasi selama menunggu, tabel modal menampilkan 5 skeleton rows sesuai layout kolom
21. Verifikasi setelah respons diterima, baris data menggantikan skeleton
22. Lepas intercept

### TC-AC-SU-482: Empty state Modal Changelog: User > Global Role saat belum ada data

23. Tutup modal dengan klik icon `[×]`
24. Buka Settings > User lewat sidebar
25. Ketik Search `Andi Wijaya {runId}-138`, tekan Enter
26. Buka Detail user `Andi Wijaya {runId}-138` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog
27. Verifikasi tabel menampilkan illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
28. Verifikasi pagination tidak menampilkan baris data
29. Tutup modal dengan klik icon `[×]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: 480, 481, 484, 504, lalu 482 (S-10): TC-AC-SU-504 dimulai dari User List dan TC-AC-SU-482 memakai target lain, sehingga keduanya di akhir. Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): menutup input Search (langkah 14), menutup modal (langkah 15, 23, dan 29), kembali ke User List lewat sidebar (langkah 16 dan 24), dan melepas intercept (langkah 22). Langkah membuka Detail, tab `Role`, dan sub-tab `Global Role` dijadikan satu langkah penghubung dengan klik icon `[📋]`.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1, 18 dan 25); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: (1) TC-AC-SU-482 memakai target `Jane Smith` dengan sumber data Global Role berjumlah 0 baris, sedangkan TC-AC-SU-480 sampai 484 memakai Jane Smith yang berisi entri; spec memakai user seed tanpa entri untuk TC-AC-SU-482. (2) TC-AC-SU-481 tidak menyebut data Group Role dan Access Level yang ada; spec men-seed satu entri tiap jenis. (3) TC-AC-SU-504 tidak menyebut endpoint yang ditunda (S-13). (4) TC-AC-SU-480 butir d ("Field selalu terisi") bersifat universal; spec memverifikasi sedikitnya satu baris tampil terlebih dahulu.
