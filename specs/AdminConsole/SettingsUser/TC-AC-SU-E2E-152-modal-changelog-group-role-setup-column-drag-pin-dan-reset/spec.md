---
id: TC-AC-SU-E2E-152-modal-changelog-group-role-setup-column-drag-pin-dan-reset
title: "Modal Changelog Group Role: Setup Column Drag Reorder, Pin, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-524
  - TC-AC-SU-525
  - TC-AC-SU-526
coverage:
  web: automated
---

# Modal Changelog Group Role: Setup Column Drag Reorder, Pin, dan Reset to Default

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-152` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama; dipakai sebagai precondition TC, tidak diasersi):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign | Manage distributor — Region A {runId}-152 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-152 | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-152 | Update | Assigned | Active | Admin U |
| 4 | Assign (via Read Only) | Manage partner — Region A {runId}-152 | Access | Inactive | Assigned | Default User |

- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom Modal Changelog: User > Group Role dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Kemampuan teknis: mengatur lebar viewport 1280px agar tabel dapat di-scroll horizontal (TC-AC-SU-525) dan memulihkannya; drag and drop baris pada popup Setup Column.
- Konfigurasi kolom Modal Changelog: User > Group Role default pada awal spec; tiap TC mengembalikannya ke default sebelum TC berikutnya.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-152`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-152` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-524: Drag reorder kolom lalu Save

3. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
4. Tarik kolom `Modified By` ke posisi pertama
5. Tarik kolom `Date` ke posisi terakhir
6. Verifikasi Live Preview mengikuti urutan baru: Modified By | Action | Role Name — Group Name | Field | Old Value | New Value | Date
7. Klik `[Save]`
8. Verifikasi tabel memakai urutan baru: Modified By | Action | Role Name — Group Name | Field | Old Value | New Value | Date
9. Muat ulang halaman dengan F5
10. Klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog
11. Verifikasi tabel tetap memakai urutan baru: Modified By | Action | Role Name — Group Name | Field | Old Value | New Value | Date
12. Buka popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-AC-SU-525: Pin dan unpin kolom

13. Atur lebar viewport 1280px sehingga tabel dapat di-scroll horizontal
14. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
15. Klik icon Pin pada kolom `Date`
16. Klik `[Save]`
17. Scroll tabel horizontal ke kanan
18. Verifikasi kolom `Date` tetap terlihat (sticky) saat tabel di-scroll horizontal
19. Muat ulang halaman dengan F5
20. Klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog
21. Scroll tabel horizontal ke kanan
22. Verifikasi kolom `Date` tetap terlihat (sticky) setelah F5
23. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
24. Klik icon Pin pada kolom `Date` untuk unpin
25. Klik `[Save]`
26. Scroll tabel horizontal ke kanan
27. Verifikasi kolom `Date` ikut ter-scroll
28. Pulihkan lebar viewport ke ukuran semula

### TC-AC-SU-526: Reset to Default

29. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
30. Hapus centang kolom `Action` (precondition TC: kolom tersembunyi)
31. Tarik kolom `Modified By` ke posisi pertama (precondition TC: urutan berubah)
32. Klik icon Pin pada kolom `Date` (precondition TC: pin aktif)
33. Klik `[Save]`
34. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
35. Klik `[Reset to Default]`
36. Verifikasi Live Preview kembali ke urutan default Date | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By dengan setiap kolom tampil
37. Verifikasi Live Preview tanpa kolom yang di-pin
38. Klik `[Save]`
39. Verifikasi tabel memakai konfigurasi default: Date | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By
40. Muat ulang halaman dengan F5
41. Klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog
42. Verifikasi tabel tetap memakai konfigurasi default: Date | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): pemulihan konfigurasi kolom lewat `[Reset to Default]` lalu `[Save]` sebelum TC berikutnya, pembukaan ulang modal sesudah F5, dan penutupan overlay atau panel lewat klik ulang icon/header (TC tidak menyatakan cara menutupnya). Membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah penghubung bersama klik icon `[📋]`.
- Penghapusan preferensi kolom Modal Changelog: User > Group Role di hook `before` dan `after` spec ini terdaftar di `suite.md` (bagian 4 konvensi).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah TC-AC-SU-526 (Reset to Default) menyalin precondition TC (kolom tersembunyi, urutan berubah, pin aktif) sebagai langkah tanpa `Verifikasi` (S-04).
- Panjang spec melewati sekitar 35 langkah (di atas smell) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: semua TC berada di satu surface (Modal Changelog: User > Group Role (Setup Column)), satu akun, satu dataset, satu kelas harness; tiap TC berdiri sendiri dan state-nya dikembalikan di langkah penghubung sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: TC-AC-SU-525 butir a ("tetap setelah F5") tidak menyebut langkah observasi setelah muat ulang; pin hanya teramati bila tabel di-scroll, sehingga spec menambah langkah scroll sebelum `Verifikasi` (S-14).
