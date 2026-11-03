---
id: TC-AC-SU-E2E-206-modal-changelog-global-role-setup-column-tutup-tanpa-save-dan-kolom-minimal
title: "Modal Changelog Global Role: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-501
  - TC-AC-SU-502
coverage:
  web: automated
---

# Modal Changelog Global Role: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-206` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Total Control) | Manage group | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage group | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage group | Update | Assigned | Active | Admin U |
| 4 | Assign | Manage user and role | Access | - | Assigned | Budi K |

Isi seed di atas tidak diasersi (bukan precondition TC); hanya memastikan Modal Changelog: User > Global Role memiliki entri.

- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom Modal Changelog: User > Global Role dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE). Konfigurasi default pada awal spec; TC-AC-SU-501 dan 502 tidak menyimpan konfigurasi.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-206`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-206` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-501: Tutup popup tanpa Save membuang perubahan

3. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
4. Uncheck kolom `Action` dan tarik kolom `Modified By` ke posisi pertama
5. Klik icon `(X)` pada popup
6. Verifikasi popup Setup Column tertutup
7. Verifikasi tidak ada dialog yang tampil
8. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default): Date | Action | Role Name | Field | Old Value | New Value | Modified By
9. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
10. Uncheck kolom `Field`
11. Tekan `Esc`
12. Verifikasi popup Setup Column tertutup
13. Verifikasi tidak ada dialog yang tampil
14. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default): Date | Action | Role Name | Field | Old Value | New Value | Modified By

### TC-AC-SU-502: Satu kolom tersisa tidak bisa di-unceklis

15. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
16. Uncheck satu per satu kolom `Action`, `Role Name`, `Field`, `Old Value`, `New Value`, `Modified By`
17. Hover checkbox `Date`
18. Verifikasi checkbox `Date` tetap tampil, checked, dan disabled
19. Verifikasi tooltip `At least one column must remain visible.` tampil
20. Klik icon `(X)` pada popup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 2 membuka Detail, tab `Role`, sub-tab `Global Role`, lalu klik icon `[📋]` Changelog; penutupan popup memakai `(X)` atau `Esc` sesuai TC.
- Suite perlu mendaftarkan penghapusan preferensi kolom Modal Changelog: User > Global Role di hook `after` suite (bagian 4 konvensi).
- Nama literal TC (mis. `Jane Smith`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis.
- Pembagian TC Modal Changelog Global Role Setup Column: TC-AC-SU-499 dan 500 di spec 143, TC-AC-SU-501 dan 502 di spec ini.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
