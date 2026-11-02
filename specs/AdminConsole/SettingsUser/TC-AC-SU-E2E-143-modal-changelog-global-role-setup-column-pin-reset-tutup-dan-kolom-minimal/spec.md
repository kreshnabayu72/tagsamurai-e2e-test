---
id: TC-AC-SU-E2E-143-modal-changelog-global-role-setup-column-pin-reset-tutup-dan-kolom-minimal
title: "Modal Changelog Global Role: Setup Column Pin dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-499
  - TC-AC-SU-500
coverage:
  web: automated
---

# Modal Changelog Global Role: Setup Column Pin dan Reset to Default

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-143` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama; dipakai sebagai precondition TC, tidak diasersi):

| No | Action | Role Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Total Control) | Manage group | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage group | Update | Inactive | Active | Admin U |
| 3 | Remove | Manage group | Update | Assigned | Active | Admin U |
| 4 | Assign | Manage user and role | Access | - | Assigned | Budi K |

- Konfigurasi kolom disimpan di browser: hook `before` menghapus preferensi kolom Modal Changelog: User > Global Role dan hook `after` menghapusnya lagi (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Kemampuan teknis: mengatur lebar viewport 1280px agar tabel dapat di-scroll horizontal (TC-AC-SU-499) dan memulihkannya.
- Konfigurasi kolom Modal Changelog: User > Global Role default pada awal spec; TC-AC-SU-500 mengembalikannya ke default sebelum spec selesai.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-143`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-143` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-499: Pin dan unpin kolom

3. Atur lebar viewport 1280px sehingga tabel dapat di-scroll horizontal
4. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
5. Klik icon Pin pada kolom `Date`
6. Klik `[Save]`
7. Scroll tabel horizontal ke kanan
8. Verifikasi kolom `Date` tetap terlihat (sticky) saat tabel di-scroll horizontal
9. Muat ulang halaman dengan F5
10. Klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog
11. Scroll tabel horizontal ke kanan
12. Verifikasi kolom `Date` tetap terlihat (sticky) setelah F5
13. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
14. Klik icon Pin pada kolom `Date` untuk unpin
15. Klik `[Save]`
16. Scroll tabel horizontal ke kanan
17. Verifikasi kolom `Date` ikut ter-scroll
18. Pulihkan lebar viewport ke ukuran semula

### TC-AC-SU-500: Reset to Default

19. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
20. Hapus centang kolom `Action` (precondition TC: kolom tersembunyi)
21. Tarik kolom `Modified By` ke posisi pertama (precondition TC: urutan berubah)
22. Klik icon Pin pada kolom `Date` (precondition TC: pin aktif)
23. Klik `[Save]`
24. Buka popup Setup Column (klik header `⋯`, lalu klik `[Setup Column]`)
25. Klik `[Reset to Default]`
26. Verifikasi Live Preview kembali ke urutan default Date | Action | Role Name | Field | Old Value | New Value | Modified By dengan setiap kolom tampil
27. Verifikasi Live Preview tanpa kolom yang di-pin
28. Klik `[Save]`
29. Verifikasi tabel memakai konfigurasi default: Date | Action | Role Name | Field | Old Value | New Value | Modified By
30. Muat ulang halaman dengan F5
31. Klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog
32. Verifikasi tabel tetap memakai konfigurasi default: Date | Action | Role Name | Field | Old Value | New Value | Modified By

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): pemulihan konfigurasi kolom lewat `[Reset to Default]` lalu `[Save]`, pembukaan ulang modal sesudah F5, dan penutupan overlay atau panel lewat klik ulang icon/header (TC tidak menyatakan cara menutupnya). Membuka Detail, tab `Role`, dan sub-tab `Global Role` dijadikan satu langkah penghubung bersama klik icon `[📋]` Changelog.
- Penghapusan preferensi kolom Modal Changelog: User > Global Role di hook `before` dan `after` spec ini terdaftar di `suite.md` (bagian 4 konvensi).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Langkah TC-AC-SU-500 (Reset to Default) menyalin precondition TC (kolom tersembunyi, urutan berubah, pin aktif) sebagai langkah tanpa `Verifikasi` (S-04).
- Pembagian TC Modal Changelog Global Role Setup Column: TC-AC-SU-499 dan 500 di spec ini, TC-AC-SU-501 dan 502 di spec 206.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: TC-AC-SU-499 butir a ("tetap setelah F5") tidak menyebut langkah observasi setelah muat ulang; pin hanya teramati bila tabel di-scroll, sehingga spec menambah langkah scroll sebelum `Verifikasi` (S-14). Pelaku seed `Budi K` pada kolom Modified By tidak terpetakan ke akun mana pun di Pre-setup; nilai dipakai apa adanya sebagai data seed, bukan akun login.
