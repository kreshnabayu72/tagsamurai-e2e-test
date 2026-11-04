---
id: TC-AC-SU-E2E-134-modal-changelog-user-column-visibility-screening-popup-dan-toggle-kolom
title: "Modal Changelog User: Screening Column Visibility, Popup Setup Column, dan Toggle Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-467
  - TC-AC-SU-468
  - TC-AC-SU-469
coverage:
  web: automated
---

# Modal Changelog User: Screening Column Visibility, Popup Setup Column, dan Toggle Kolom

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-134 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-134 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-134 | Role | Inactive | Active | Budi K |
| 4 | Assign | Mike Tan {runId}-134 | Group | - | Manager | Citra M |

- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom tabel modal ini dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE).

| Kolom uji toggle |
|---|
| Date |
| Action |
| User Name |
| Field |
| Old Value |
| New Value |

- Konfigurasi kolom Modal Changelog: User default pada awal spec; spec menyimpan konfigurasi hanya di TC-AC-SU-469 dan mengembalikannya ke default di akhir TC itu.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-467: Screening overlay Column Visibility

2. Hover header kolom Actions `⋯`
3. Verifikasi tooltip `Column Visibility` tampil
4. Klik header `⋯`
5. Verifikasi overlay terbuka dengan tombol `[Setup Column]` di atas
6. Verifikasi daftar kolom pada overlay berurutan default: Date | Action | User Name | Field | Old Value | New Value | Modified By
7. Verifikasi setiap kolom pada overlay memiliki checkbox ☑ checked dan enabled (Hideable, Default Visible)
8. Verifikasi setiap kolom pada overlay memiliki drag handle
9. Klik header `⋯` lagi untuk menutup overlay Column Visibility

### TC-AC-SU-468: Screening popup Setup Column

10. Klik header `⋯`
11. Klik `[Setup Column]`
12. Verifikasi header popup menampilkan Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon `(X)`
13. Verifikasi body popup menampilkan daftar kolom: Date | Action | User Name | Field | Old Value | New Value | Modified By
14. Verifikasi setiap baris daftar kolom memiliki checkbox ☑ checked dan enabled
15. Verifikasi setiap baris daftar kolom memiliki drag handle
16. Verifikasi setiap baris daftar kolom memiliki icon Pin
17. Verifikasi Live Preview menampilkan header dan isi sel sesuai tabel asli
18. Verifikasi footer popup menampilkan `[Reset to Default]` dan `[Save]` rata kanan
19. Verifikasi footer popup tidak memiliki tombol `[Cancel]`
20. Klik icon `(X)` pada popup Setup Column

### TC-AC-SU-469: Unceklis dan ceklis kolom lalu Save

21. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
22. Untuk setiap kolom pada tabel "Kolom uji toggle" di Prerequisites (`Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`), lakukan langkah 23 sampai 26
23. Uncheck kolom `<kolom pada iterasi>`
24. Verifikasi Live Preview menyembunyikan kolom `<kolom pada iterasi>`
25. Check kembali kolom `<kolom pada iterasi>`
26. Verifikasi Live Preview menampilkan kembali kolom `<kolom pada iterasi>`
27. Uncheck kolom `Action`
28. Klik `[Save]`
29. Verifikasi kolom `Date`, `User Name`, `Field`, `Old Value`, dan `New Value` tetap tampil di tabel
30. Verifikasi kolom `Action` tidak tampil di tabel
31. Muat ulang halaman dengan F5
32. Klik icon Changelog di toolbar User List
33. Verifikasi kolom `Date`, `User Name`, `Field`, `Old Value`, dan `New Value` tetap tampil di tabel
34. Verifikasi kolom `Action` tetap tersembunyi di tabel (konfigurasi tetap setelah F5)
35. Buka popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): pemulihan konfigurasi kolom lewat `[Reset to Default]` lalu `[Save]` sebelum TC berikutnya, pembukaan ulang modal sesudah F5, dan penutupan overlay atau panel lewat klik ulang icon/header (TC tidak menyatakan cara menutupnya).
- Konfigurasi tersimpan lewat `[Save]` di TC-AC-SU-469 dikembalikan lewat `[Reset to Default]` dan `[Save]` di langkah 35. Suite perlu mendaftarkan penghapusan preferensi kolom Modal Changelog: User di hook `after` suite (bagian 4 konvensi).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Temuan untuk QA: (1) TC-AC-SU-467 menyebut "Hover header kolom Actions ⋯" sedangkan kolom itu berjudul Column Visibility (⋯); spec memakai header `⋯`. (2) TC-AC-SU-469 butir a mengasersi Live Preview tiap kolom yang di-toggle; spec mengulang langkah per kolom dari tabel Prerequisites. (3) TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
