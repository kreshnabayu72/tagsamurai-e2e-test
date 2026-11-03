---
id: TC-AC-SU-E2E-147-modal-changelog-group-role-search-siklus-interaksi-search-box
title: "Modal Changelog Group Role: Siklus Interaksi Search Box"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-512
coverage:
  web: automated
---

# Modal Changelog Group Role: Siklus Interaksi Search Box

## Prerequisites

- Mode: FE+BE. Semua data dan hasil Search berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-147` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign | Manage distributor — Region A {runId}-147 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-147 | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-147 | Update | Assigned | Active | Admin U |
| 4 | Assign (via Read Only) | Manage partner — Region A {runId}-147 | Access | Inactive | Assigned | Default User |

- Search hanya menyaring saat Enter. Keyword Search: `Region A {runId}-147` (baris seed nomor 1 dan 4 memuatnya di kolom `Role Name — Group Name`).
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-147`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-147` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-512: Siklus interaksi Search box

3. Hover icon Search
4. Verifikasi tooltip `Search` tampil
5. Klik icon Search
6. Verifikasi input Search melebar
7. Verifikasi kursor auto-focus di input Search
8. Verifikasi placeholder input Search `Search action, role, field, or value...`
9. Ketik `Region A {runId}-147` tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul
11. Verifikasi tabel belum tersaring (baris yang tidak memuat `Region A {runId}-147` masih tampil)
12. Tekan Enter
13. Verifikasi sedikitnya satu baris tampil di tabel
14. Verifikasi tabel hanya menampilkan baris yang memuat `Region A {runId}-147`
15. Klik icon `(✕)`
16. Verifikasi input Search kosong
17. Verifikasi search bar tetap terbuka
18. Verifikasi tabel tetap hanya menampilkan baris yang memuat `Region A {runId}-147` (hasil search terakhir)
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan semua data (baris yang tidak memuat `Region A {runId}-147` tampil kembali)
21. Ketik `Region A {runId}-147` lalu tekan Enter
22. Klik icon `(←)`
23. Verifikasi search bar collapse ke icon Search
24. Verifikasi keyword Search kosong
25. Verifikasi tabel langsung kembali menampilkan semua data

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03): membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah bersama klik icon `[📋]`.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: TC-AC-SU-512 memakai keyword `Region A` pada nama grup literal; spec memakai `Region A {runId}-147` sehingga keyword unik per run.
