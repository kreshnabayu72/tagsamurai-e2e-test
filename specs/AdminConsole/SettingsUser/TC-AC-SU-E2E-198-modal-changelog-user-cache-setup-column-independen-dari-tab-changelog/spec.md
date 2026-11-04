---
id: TC-AC-SU-E2E-198-modal-changelog-user-cache-setup-column-independen-dari-tab-changelog
title: "Modal Changelog User: Cache Setup Column Independen dari Tab Changelog Detail User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-475
coverage:
  web: automated
---

# Modal Changelog User: Cache Setup Column Independen dari Tab Changelog Detail User

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-198 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-198 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-198 | Role | Inactive | Active | Budi K |
| 4 | Assign | Mike Tan {runId}-198 | Group | - | Manager | Citra M |

Isi seed di atas tidak diasersi (bukan precondition TC); hanya memastikan Modal Changelog: User dan tab Changelog Detail user memiliki entri.

- User target Detail: `Jane Smith {runId}-198` (tab `Changelog` Detail user dengan sedikitnya satu entri).
- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom Modal Changelog: User dan tab Changelog Detail user sehingga kedua tabel default pada awal spec, dan hook `after` menghapusnya lagi sebagai pemulihan (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

### TC-AC-SU-475: Cache Setup Column Modal Changelog: User independen dari Tab Changelog

1. Klik icon Changelog di toolbar User List
2. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
3. Uncheck kolom `Field`, lalu klik `[Save]`
4. Tutup modal dengan klik icon `[×]`
5. Ketik Search `Jane Smith {runId}-198`, tekan Enter
6. Buka Detail user `Jane Smith {runId}-198` dengan klik Name baris itu di User List
7. Klik tab `Changelog`
8. Buka popup Setup Column pada tab `Changelog` (klik header `⋯`, lalu klik `[Setup Column]`)
9. Uncheck kolom `Modified By`, lalu klik `[Save]`
10. Verifikasi tab `Changelog` tetap menampilkan kolom `Field`
11. Buka popup Setup Column pada tab `Changelog` (klik header `⋯`, lalu klik `[Setup Column]`)
12. Check kembali kolom `Modified By`, lalu klik `[Save]`
13. Buka Settings > User lewat sidebar
14. Klik icon Changelog di toolbar User List
15. Verifikasi Modal Changelog: User tetap menampilkan kolom `Modified By`
16. Verifikasi Modal Changelog: User tetap menyembunyikan kolom `Field`
17. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
18. Check kembali kolom `Field`, lalu klik `[Save]`
19. Tutup modal dengan klik icon `[×]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini berdiri sendiri karena TC-AC-SU-475 melibatkan dua surface (Modal Changelog: User dan tab Changelog Detail user) dengan dua konfigurasi kolom tersimpan.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): menutup modal, membuka Detail dan tab `Changelog`, kembali ke User List lewat sidebar; langkah 11, 12, 17, dan 18 memulihkan centang kolom `Modified By` dan `Field` sebelum spec berakhir; hook `after` menghapus preferensi kolom sebagai pengaman. Urutan `Verifikasi` mengikuti urutan state: kolom tab `Changelog` diamati segera setelah `Modified By` disembunyikan (langkah 10), baru dipulihkan (langkah 11 dan 12) dan modal dibuka kembali.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 5); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: TC-AC-SU-475 langkah 4 menyebut "Buka Detail Jane Smith > tab Changelog" tanpa menyebut bahwa tab itu memiliki Setup Column sendiri; spec mengikuti Expected (cache terpisah per tabel, PRD 4.1.8). TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
