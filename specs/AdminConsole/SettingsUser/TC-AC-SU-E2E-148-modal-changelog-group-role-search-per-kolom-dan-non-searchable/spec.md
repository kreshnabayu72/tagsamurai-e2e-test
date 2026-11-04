---
id: TC-AC-SU-E2E-148-modal-changelog-group-role-search-per-kolom-dan-non-searchable
title: "Modal Changelog Group Role: Search per Kolom Kelas Teks dan Kolom Non-Searchable"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-513
  - TC-AC-SU-514
coverage:
  web: automated
---

# Modal Changelog Group Role: Search per Kolom Kelas Teks dan Kolom Non-Searchable

## Prerequisites

- Mode: FE+BE. Semua data dan hasil Search berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-148` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign | Manage distributor — Region A {runId}-148 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-148 | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-148 | Update | Assigned | Active | Admin U |
| 4 | Assign (via Read Only) | Manage partner — Region A {runId}-148 | Access | Inactive | Assigned | Default User |

- Date baris seed nomor 3 = `11 Jun 2026`; nilai itu tidak muncul di kolom searchable mana pun. Date Format General Settings entitas Principal menampilkan tanggal sebagai `11 Jun 2026` dan tidak diubah spec ini (tanpa pemulihan).
- Pencarian per kolom memakai nilai seed berikut:

| Kolom uji Search | Keyword substring | Keyword huruf kapital | Nilai yang dicari |
|---|---|---|---|
| Action | assi | ASSI | Assign |
| Role Name — Group Name | region a | REGION A | Manage distributor — Region A {runId}-148 |
| Field | acc | ACC | Access |
| Old Value | inac | INAC | Inactive |
| New Value | assig | ASSIG | Assigned |
| Modified By | default | DEFAULT | Default User |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-148`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-148` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-513: Search per kolom kelas teks

3. Untuk setiap baris tabel "Kolom uji Search" di Prerequisites, lakukan langkah 4 sampai 8
4. Ketik Search `<keyword substring pada iterasi>`, tekan Enter
5. Verifikasi tabel menampilkan baris yang memuat `<nilai pada iterasi>` pada kolom `<kolom pada iterasi>`
6. Ganti isi kotak search dengan `<keyword kapital pada iterasi>`, tekan Enter
7. Verifikasi tabel menampilkan baris yang memuat `<nilai pada iterasi>` pada kolom `<kolom pada iterasi>`
8. Klik `(←)` pada kotak Search

### TC-AC-SU-514: Kolom non-searchable tidak ikut dicari

9. Verifikasi kolom `Date` menampilkan `11 Jun 2026` pada baris `Manage partner — Region B {runId}-148` dengan Action `Remove`
10. Ketik Search `11 Jun 2026`, tekan Enter
11. Verifikasi tabel menampilkan empty state `No results found` (nilai kolom Date tidak dicocokkan oleh Search)
12. Klik icon `(←)` pada kotak Search
13. Klik icon Filter
14. Verifikasi Filter Panel memuat field `Date` (penyaringan kolom Date tersedia lewat Filter Panel)
15. Klik icon Filter lagi untuk menutup Filter Panel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 4 sampai 8 (iterasi dari tabel "Kolom uji Search" di Prerequisites); `Verifikasi` tetap satu per keyword. Klik `(←)` pada kotak Search di akhir iterasi adalah langkah penghubung yang mereset tabel (S-03, S-09).
- Langkah penghubung (tanpa `Verifikasi`; S-03): membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah bersama klik icon `[📋]`. TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Alasan ekspansi di atas ±35 langkah (15 langkah nominal, sekitar 40 dengan ekspansi blok berulang): semua TC berada di satu surface (Modal Changelog: User > Group Role (Search)), satu akun, satu dataset; tiap TC berdiri sendiri dan tiap iterasi kolom diakhiri `(←)` yang mereset tabel sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: (1) TC-AC-SU-514 butir b ("Penyaringan kolom ini hanya tersedia lewat Filter Panel (bila Filterable)") berbentuk pernyataan; spec mengamatinya sebagai keberadaan field `Date` di Filter Panel. (2) TC-AC-SU-514 mengasumsikan format tampilan `11 Jun 2026` yang ditentukan General Settings; spec menyatakannya di Prerequisites. (3) Pada TC-AC-SU-513 nilai kolom `Role Name — Group Name` memuat nama grup bersuffix; keyword `region a` tetap cocok sebagai substring.
