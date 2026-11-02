---
id: TC-AC-SU-E2E-142-modal-changelog-global-role-column-visibility-popup-toggle-dan-drag
title: "Modal Changelog Global Role: Column Visibility, Popup Setup Column, Toggle Kolom, dan Drag Reorder"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-495
  - TC-AC-SU-496
  - TC-AC-SU-497
  - TC-AC-SU-498
coverage:
  web: automated
---

# Modal Changelog Global Role: Column Visibility, Popup Setup Column, Toggle Kolom, dan Drag Reorder

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-142` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Total Control) | Manage group | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage group | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage group | Update | Assigned | Active | Admin U |
| 4 | Assign | Manage user and role | Access | - | Assigned | Budi K |

- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom Modal Changelog: User > Global Role dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Konfigurasi kolom Modal Changelog: User > Global Role default pada awal spec; tiap TC mengembalikannya ke default sebelum TC berikutnya.

| Kolom uji toggle |
|---|
| Date |
| Action |
| Role Name |
| Field |
| Old Value |
| New Value |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-142`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-142` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-495: Screening overlay Column Visibility

3. Hover header kolom Actions `⋯`
4. Verifikasi tooltip `Column Visibility` tampil
5. Klik header `⋯`
6. Verifikasi overlay terbuka dengan tombol `[Setup Column]` di atas
7. Verifikasi daftar kolom pada overlay berurutan default: Date | Action | Role Name | Field | Old Value | New Value | Modified By
8. Verifikasi setiap kolom pada overlay memiliki checkbox ☑ checked dan enabled (Hideable, Default Visible)
9. Verifikasi setiap kolom pada overlay memiliki drag handle
10. Klik header `⋯` lagi untuk menutup overlay Column Visibility

### TC-AC-SU-496: Screening popup Setup Column

11. Klik header `⋯`
12. Klik `[Setup Column]`
13. Verifikasi header popup menampilkan Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon `(X)`
14. Verifikasi body popup menampilkan daftar kolom: Date | Action | Role Name | Field | Old Value | New Value | Modified By
15. Verifikasi setiap baris daftar kolom memiliki checkbox ☑ checked dan enabled
16. Verifikasi setiap baris daftar kolom memiliki drag handle
17. Verifikasi setiap baris daftar kolom memiliki icon Pin
18. Verifikasi Live Preview menampilkan header dan isi sel sesuai tabel asli
19. Verifikasi footer popup menampilkan `[Reset to Default]` dan `[Save]` rata kanan
20. Verifikasi footer popup tidak memiliki tombol `[Cancel]`
21. Klik icon `(X)` pada popup Setup Column

### TC-AC-SU-497: Unceklis dan ceklis kolom lalu Save

22. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
23. Untuk setiap kolom pada tabel "Kolom uji toggle" di Prerequisites (`Date`, `Action`, `Role Name`, `Field`, `Old Value`, `New Value`), lakukan langkah 24 sampai 27
24. Hapus centang kolom `<kolom pada iterasi>`
25. Verifikasi Live Preview menyembunyikan kolom `<kolom pada iterasi>`
26. Centang kembali kolom `<kolom pada iterasi>`
27. Verifikasi Live Preview menampilkan kembali kolom `<kolom pada iterasi>`
28. Hapus centang kolom `Action`
29. Klik `[Save]`
30. Verifikasi kolom `Date`, `Role Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil di tabel
31. Verifikasi kolom `Action` tidak tampil di tabel
32. Muat ulang halaman dengan F5
33. Klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog
34. Verifikasi kolom `Date`, `Role Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil di tabel
35. Verifikasi kolom `Action` tetap tersembunyi di tabel (konfigurasi tetap setelah F5)
36. Buka popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-AC-SU-498: Drag reorder kolom lalu Save

37. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
38. Tarik kolom `Modified By` ke posisi pertama
39. Tarik kolom `Date` ke posisi terakhir
40. Verifikasi Live Preview mengikuti urutan baru: Modified By | Action | Role Name | Field | Old Value | New Value | Date
41. Klik `[Save]`
42. Verifikasi tabel memakai urutan baru: Modified By | Action | Role Name | Field | Old Value | New Value | Date
43. Muat ulang halaman dengan F5
44. Klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog
45. Verifikasi tabel tetap memakai urutan baru: Modified By | Action | Role Name | Field | Old Value | New Value | Date
46. Buka popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): pemulihan konfigurasi kolom lewat `[Reset to Default]` lalu `[Save]` sebelum TC berikutnya, pembukaan ulang modal sesudah F5, dan penutupan overlay atau panel lewat klik ulang icon/header (TC tidak menyatakan cara menutupnya). Membuka Detail, tab `Role`, dan sub-tab `Global Role` dijadikan satu langkah penghubung bersama klik icon `[📋]`.
- Penghapusan preferensi kolom Modal Changelog: User > Global Role di hook `before` dan `after` spec ini terdaftar di `suite.md` (bagian 4 konvensi).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Panjang spec melewati sekitar 35 langkah (di atas smell) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: semua TC berada di satu surface (Modal Changelog: User > Global Role (Setup Column)), satu akun, satu dataset, satu kelas harness; tiap TC berdiri sendiri dan state-nya dikembalikan di langkah penghubung sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Langkah penghubung (tanpa `Verifikasi`; S-03): langkah 30 dan 34 memverifikasi kolom lain yang tetap tampil sebagai pembanding sebelum asersi kolom `Action` tidak tampil (langkah 31 dan 35; bagian 8b butir 2).
- Langkah 24 sampai 27 diulang per kolom pada tabel "Kolom uji toggle" di Prerequisites; `Verifikasi` tiap iterasi tetap satu per klausa.
- Temuan untuk QA: (1) TC-AC-SU-495 menyebut "Hover header kolom Actions ⋯" sedangkan kolom itu berjudul Column Visibility (⋯); spec memakai header `⋯`. (2) Setelah F5 TC tidak menyatakan posisi halaman; spec membuka kembali tab `Role`, sub-tab `Global Role`, dan modal. (3) TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03). Pelaku seed `Budi K` pada kolom Modified By tidak terpetakan ke akun mana pun di Pre-setup; nilai dipakai apa adanya sebagai data seed, bukan akun login.
