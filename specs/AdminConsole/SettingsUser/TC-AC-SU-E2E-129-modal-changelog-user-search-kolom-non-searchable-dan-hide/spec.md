---
id: TC-AC-SU-E2E-129-modal-changelog-user-search-kolom-non-searchable-dan-hide
title: "Modal Changelog User: Search atas Kolom Non-Searchable dan Kolom yang Di-hide"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-454
  - TC-AC-SU-455
coverage:
  web: automated
---

# Modal Changelog User: Search atas Kolom Non-Searchable dan Kolom yang Di-hide

## Prerequisites

- Mode: FE+BE. Semua data dan hasil Search berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-129 | Status | Active | Inactive | Admin U |
| 2 | Activate | Jane Smith {runId}-129 | Role | Inactive | Active | Budi K |

- Date baris seed nomor 1 = `15 Jun 2026`; nilai itu tidak muncul di kolom searchable mana pun. `John Doe {runId}-129` hanya muncul di kolom `User Name`.
- Date Format General Settings entitas Principal menampilkan tanggal sebagai `15 Jun 2026` dan tidak diubah spec ini (tanpa pemulihan).
- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom tabel modal ini dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-454: Search Modal Changelog: User, kolom non-searchable tidak ikut dicari

2. Verifikasi kolom `Date` menampilkan `15 Jun 2026` pada baris `John Doe {runId}-129`
3. Ketik Search `15 Jun 2026`, tekan Enter
4. Verifikasi tabel menampilkan empty state `No results found` (nilai kolom Date tidak dicocokkan oleh Search)
5. Klik icon `(←)` pada kotak Search
6. Klik icon Filter
7. Verifikasi Filter Panel memuat field `Date` (penyaringan kolom Date tersedia lewat Filter Panel)
8. Klik icon Filter lagi untuk menutup Filter Panel

### TC-AC-SU-455: Search Modal Changelog: User, kolom yang di-hide tidak ikut dicari lalu kembali searchable saat di-unhide

9. Klik header `⋯`
10. Uncheck kolom `User Name` pada overlay Column Visibility
11. Ketik Search `John Doe {runId}-129`, tekan Enter
12. Verifikasi tabel menampilkan empty state `No results found` (keyword tidak mencocokkan baris saat `User Name` di-hide)
13. Klik `(←)` pada kotak Search
14. Klik header `⋯`
15. Check kolom `User Name` pada overlay Column Visibility
16. Ketik Search `John Doe {runId}-129`, tekan Enter
17. Verifikasi tabel menampilkan baris yang memuat `John Doe {runId}-129`
18. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): menutup input Search lewat `(←)` (langkah 13 dan 18) dan menutup Filter Panel di TC-AC-SU-454. TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
- Kolom `User Name` dikembalikan ke visible di TC-AC-SU-455 sendiri (check kembali), sehingga tidak ada state kolom yang tersisa.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Temuan untuk QA: (1) TC-AC-SU-454 butir b ("Penyaringan kolom ini hanya tersedia lewat Filter Panel (bila Filterable)") berbentuk pernyataan; spec mengamatinya sebagai keberadaan field `Date` di Filter Panel. (2) TC-AC-SU-454 mengasumsikan format tampilan `15 Jun 2026`, sedangkan format tanggal ditentukan General Settings; spec menyatakan format itu di Prerequisites. (3) Nama literal `John Doe` pada TC-AC-SU-455 ditulis bersuffix sehingga keyword Search unik per run.
