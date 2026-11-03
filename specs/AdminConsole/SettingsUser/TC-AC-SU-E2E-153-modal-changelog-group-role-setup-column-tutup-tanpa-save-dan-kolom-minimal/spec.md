---
id: TC-AC-SU-E2E-153-modal-changelog-group-role-setup-column-tutup-tanpa-save-dan-kolom-minimal
title: "Modal Changelog Group Role: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-527
  - TC-AC-SU-528
coverage:
  web: automated
---

# Modal Changelog Group Role: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-153` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama; dipakai sebagai precondition TC, tidak diasersi):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign | Manage distributor — Region A {runId}-153 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-153 | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-153 | Update | Assigned | Active | Admin U |
| 4 | Assign (via Read Only) | Manage partner — Region A {runId}-153 | Access | Inactive | Assigned | Default User |

- Konfigurasi kolom Modal Changelog: User > Group Role default sepanjang spec; spec ini tidak pernah menyimpan konfigurasi (tanpa `[Save]`), sehingga tidak ada pemulihan.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-153`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-153` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-527: Tutup popup tanpa Save membuang perubahan

3. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
4. Hapus centang kolom `Action` dan tarik kolom `Modified By` ke posisi pertama
5. Klik icon `(X)` pada popup
6. Verifikasi popup Setup Column tertutup
7. Verifikasi tidak ada dialog yang tampil
8. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default): Date | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By
9. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
10. Hapus centang kolom `Field`
11. Tekan `Esc`
12. Verifikasi popup Setup Column tertutup
13. Verifikasi tidak ada dialog yang tampil
14. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default): Date | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By

### TC-AC-SU-528: Satu kolom tersisa tidak bisa di-unceklis

15. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
16. Hapus centang satu per satu kolom `Action`, `Role Name — Group Name`, `Field`, `Old Value`, `New Value`, `Modified By`
17. Hover checkbox `Date`
18. Verifikasi checkbox `Date` tetap tampil, checked, dan disabled
19. Verifikasi tooltip `At least one column must remain visible.` tampil
20. Klik icon `(X)` pada popup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): penutupan popup Setup Column memakai `(X)` atau `Esc` sesuai TC (langkah 5, 11, dan 20). Membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah penghubung bersama klik icon `[📋]`.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
