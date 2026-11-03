---
id: TC-AC-SU-E2E-136-modal-changelog-user-setup-column-tutup-tanpa-save-dan-kolom-minimal
title: "Modal Changelog User: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-473
  - TC-AC-SU-474
coverage:
  web: automated
---

# Modal Changelog User: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-136 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-136 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-136 | Role | Inactive | Active | Budi K |
| 4 | Assign | Mike Tan {runId}-136 | Group | - | Manager | Citra M |

- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom tabel modal ini dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Konfigurasi tersimpan Modal Changelog: User = default pada awal spec; spec tidak menekan `[Save]` sehingga tidak ada konfigurasi yang tersisa.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-473: Tutup popup tanpa Save membuang perubahan

2. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
3. Uncheck kolom `Action` dan tarik kolom `Modified By` ke posisi pertama
4. Klik icon `(X)` pada popup
5. Verifikasi popup Setup Column tertutup
6. Verifikasi tidak ada dialog yang tampil
7. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default): Date | Action | User Name | Field | Old Value | New Value | Modified By
8. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
9. Uncheck kolom `Field`
10. Tekan `Esc`
11. Verifikasi popup Setup Column tertutup
12. Verifikasi tidak ada dialog yang tampil
13. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default): Date | Action | User Name | Field | Old Value | New Value | Modified By

### TC-AC-SU-474: Satu kolom tersisa tidak bisa di-unceklis

14. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
15. Uncheck satu per satu kolom `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`
16. Hover checkbox `Date`
17. Verifikasi checkbox `Date` tetap tampil, checked, dan disabled
18. Verifikasi tooltip `At least one column must remain visible.` tampil
19. Klik icon `(X)` pada popup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03): menutup popup Setup Column dengan `(X)` di akhir TC-AC-SU-474 tanpa `[Save]`.
- TC-AC-SU-475 (cache Setup Column independen dari Tab Changelog) ada di spec 198 karena melibatkan dua surface.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
