---
id: TC-AC-SU-E2E-140-modal-changelog-global-role-search-siklus-per-kolom-dan-non-searchable
title: "Modal Changelog Global Role: Search Box, Search per Kolom, dan Kolom Non-Searchable"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-488
  - TC-AC-SU-489
  - TC-AC-SU-490
coverage:
  web: automated
---

# Modal Changelog Global Role: Search Box, Search per Kolom, dan Kolom Non-Searchable

## Prerequisites

- Mode: FE+BE. Semua data dan hasil Search berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-140` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Total Control) | Manage group | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage group | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage group | Update | Assigned | Active | Admin U |
| 4 | Assign | Manage user and role | Access | - | Assigned | Budi K |

- Date baris seed nomor 4 = `12 Jun 2026`; nilai itu tidak muncul di kolom searchable mana pun. Date Format General Settings entitas Principal menampilkan tanggal sebagai `12 Jun 2026` dan tidak diubah spec ini (tanpa pemulihan).
- Pencarian per kolom memakai nilai seed berikut:

| Kolom uji Search | Keyword substring | Keyword huruf kapital | Nilai yang dicari |
|---|---|---|---|
| Action | remo | REMO | Remove |
| Role Name | manage gr | MANAGE GR | Manage group |
| Field | upd | UPD | Update |
| Old Value | assig | ASSIG | Assigned |
| New Value | acti | ACTI | Active |
| Modified By | admin | ADMIN | Admin U |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-140`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-140` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-488: Siklus interaksi Search box

3. Hover icon Search
4. Verifikasi tooltip `Search` tampil
5. Klik icon Search
6. Verifikasi input Search melebar
7. Verifikasi kursor auto-focus di input Search
8. Verifikasi placeholder input Search `Search action, role, field, or value...`
9. Ketik `Remove` tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul
11. Verifikasi tabel belum tersaring (baris yang tidak memuat `Remove` masih tampil)
12. Tekan Enter
13. Verifikasi sedikitnya satu baris tampil di tabel
14. Verifikasi tabel hanya menampilkan baris yang memuat `Remove`
15. Klik icon `(✕)`
16. Verifikasi input Search kosong
17. Verifikasi search bar tetap terbuka
18. Verifikasi tabel tetap hanya menampilkan baris yang memuat `Remove` (hasil search terakhir)
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan semua data (baris yang tidak memuat `Remove` tampil kembali)
21. Ketik `Remove` lalu tekan Enter
22. Klik icon `(←)`
23. Verifikasi search bar collapse ke icon Search
24. Verifikasi keyword Search kosong
25. Verifikasi tabel langsung kembali menampilkan semua data

### TC-AC-SU-489: Search per kolom kelas teks

26. Untuk setiap baris tabel "Kolom uji Search" di Prerequisites, lakukan langkah 27 sampai 31
27. Ketik Search `<keyword substring pada iterasi>`, tekan Enter
28. Verifikasi tabel menampilkan baris yang memuat `<nilai pada iterasi>` pada kolom `<kolom pada iterasi>`
29. Ganti isi kotak search dengan `<keyword kapital pada iterasi>`, tekan Enter
30. Verifikasi tabel menampilkan baris yang memuat `<nilai pada iterasi>` pada kolom `<kolom pada iterasi>`
31. Klik `(←)` pada kotak Search

### TC-AC-SU-490: Kolom non-searchable tidak ikut dicari

32. Verifikasi kolom `Date` menampilkan `12 Jun 2026` pada baris `Manage user and role`
33. Ketik Search `12 Jun 2026`, tekan Enter
34. Verifikasi tabel menampilkan empty state `No results found` (nilai kolom Date tidak dicocokkan oleh Search)
35. Klik icon `(←)` pada kotak Search
36. Klik icon Filter
37. Verifikasi Filter Panel memuat field `Date` (penyaringan kolom Date tersedia lewat Filter Panel)
38. Klik icon Filter lagi untuk menutup Filter Panel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 27 sampai 31 (iterasi dari tabel "Kolom uji Search" di Prerequisites); `Verifikasi` tetap satu per keyword. Klik `(←)` pada kotak Search di akhir iterasi adalah langkah penghubung yang mereset tabel (S-03, S-09).
- Langkah penghubung (tanpa `Verifikasi`; S-03): membuka Detail, tab `Role`, dan sub-tab `Global Role` dijadikan satu langkah bersama klik icon `[📋]`. TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Panjang spec melewati sekitar 35 langkah (di atas smell) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: semua TC berada di satu surface (Modal Changelog: User > Global Role (Search)), satu akun, satu dataset, satu kelas harness; tiap TC berdiri sendiri dan state-nya dikembalikan di langkah penghubung sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: (1) TC-AC-SU-490 butir b ("Penyaringan kolom ini hanya tersedia lewat Filter Panel (bila Filterable)") berbentuk pernyataan; spec mengamatinya sebagai keberadaan field `Date` di Filter Panel. (2) TC-AC-SU-490 mengasumsikan format tampilan `12 Jun 2026` yang ditentukan General Settings; spec menyatakannya di Prerequisites.
