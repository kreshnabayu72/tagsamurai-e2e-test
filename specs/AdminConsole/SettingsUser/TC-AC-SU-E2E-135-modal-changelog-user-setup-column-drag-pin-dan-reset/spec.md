---
id: TC-AC-SU-E2E-135-modal-changelog-user-setup-column-drag-pin-dan-reset
title: "Modal Changelog User: Setup Column Drag Reorder, Pin, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-470
  - TC-AC-SU-471
  - TC-AC-SU-472
coverage:
  web: automated
---

# Modal Changelog User: Setup Column Drag Reorder, Pin, dan Reset to Default

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-135 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-135 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-135 | Role | Inactive | Active | Budi K |
| 4 | Assign | Mike Tan {runId}-135 | Group | - | Manager | Citra M |

- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom tabel modal ini dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Kemampuan teknis: mengatur lebar viewport 1280px agar tabel dapat di-scroll horizontal (TC-AC-SU-471) dan memulihkannya; drag and drop baris pada popup Setup Column.
- Konfigurasi kolom Modal Changelog: User default pada awal spec; tiap TC mengembalikannya ke default sebelum TC berikutnya.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-470: Drag reorder kolom lalu Save

2. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
3. Tarik kolom `Modified By` ke posisi pertama
4. Tarik kolom `Date` ke posisi terakhir
5. Verifikasi Live Preview mengikuti urutan baru: Modified By | Action | User Name | Field | Old Value | New Value | Date
6. Klik `[Save]`
7. Verifikasi tabel memakai urutan baru: Modified By | Action | User Name | Field | Old Value | New Value | Date
8. Muat ulang halaman dengan F5
9. Klik icon Changelog di toolbar User List
10. Verifikasi tabel tetap memakai urutan baru: Modified By | Action | User Name | Field | Old Value | New Value | Date
11. Buka popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-AC-SU-471: Pin dan unpin kolom

12. Atur lebar viewport 1280px sehingga tabel dapat di-scroll horizontal
13. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
14. Klik icon Pin pada kolom `Date`
15. Klik `[Save]`
16. Scroll tabel horizontal ke kanan
17. Verifikasi kolom `Date` tetap terlihat (sticky) saat tabel di-scroll horizontal
18. Muat ulang halaman dengan F5
19. Klik icon Changelog di toolbar User List
20. Scroll tabel horizontal ke kanan
21. Verifikasi kolom `Date` tetap terlihat (sticky) setelah F5
22. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
23. Klik icon Pin pada kolom `Date` untuk unpin
24. Klik `[Save]`
25. Scroll tabel horizontal ke kanan
26. Verifikasi kolom `Date` ikut ter-scroll
27. Pulihkan lebar viewport ke ukuran semula

### TC-AC-SU-472: Reset to Default

28. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
29. Uncheck kolom `Action` (precondition TC: kolom tersembunyi)
30. Tarik kolom `Modified By` ke posisi pertama (precondition TC: urutan berubah)
31. Klik icon Pin pada kolom `Date` (precondition TC: pin aktif)
32. Klik `[Save]`
33. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
34. Klik `[Reset to Default]`
35. Verifikasi Live Preview kembali ke urutan default Date | Action | User Name | Field | Old Value | New Value | Modified By dengan setiap kolom tampil
36. Verifikasi Live Preview tanpa kolom yang di-pin
37. Klik `[Save]`
38. Verifikasi tabel memakai konfigurasi default: Date | Action | User Name | Field | Old Value | New Value | Modified By
39. Muat ulang halaman dengan F5
40. Klik icon Changelog di toolbar User List
41. Verifikasi tabel tetap memakai konfigurasi default: Date | Action | User Name | Field | Old Value | New Value | Modified By

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): pemulihan konfigurasi kolom lewat `[Reset to Default]` lalu `[Save]` sebelum TC berikutnya, pembukaan ulang modal sesudah F5, dan penutupan overlay atau panel lewat klik ulang icon/header (TC tidak menyatakan cara menutupnya).
- Langkah TC-AC-SU-472 (Reset to Default) menyalin precondition TC (kolom tersembunyi, urutan berubah, pin aktif) sebagai langkah tanpa `Verifikasi` (S-04); pembersihan preferensi kolom dilakukan hook `after` suite.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Panjang spec melewati sekitar 35 langkah (di atas smell) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: semua TC berada di satu surface (Modal Changelog: User dengan popup Setup Column), satu akun, satu dataset, satu kelas harness; tiap TC berdiri sendiri dan state-nya dikembalikan di langkah penghubung sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA: (1) TC-AC-SU-471 butir a ("tetap setelah F5") tidak menyebut langkah observasi setelah muat ulang; pin hanya teramati bila tabel di-scroll, sehingga spec menambah langkah scroll sebelum `Verifikasi` (S-14). (2) TC tidak menyatakan cara menutup Filter Panel atau overlay Column Visibility; spec memakai klik ulang icon Filter atau header `⋯` sebagai langkah penghubung (S-03).
