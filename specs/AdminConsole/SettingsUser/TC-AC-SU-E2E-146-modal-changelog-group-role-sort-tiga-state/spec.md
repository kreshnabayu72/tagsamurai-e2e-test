---
id: TC-AC-SU-E2E-146-modal-changelog-group-role-sort-tiga-state
title: "Modal Changelog Group Role: Sort 3-State Kelas Teks, Campuran, dan Tanggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-509
  - TC-AC-SU-510
  - TC-AC-SU-511
coverage:
  web: automated
---

# Modal Changelog Group Role: Sort 3-State Kelas Teks, Campuran, dan Tanggal

## Prerequisites

- Mode: FE+BE. Semua data dan urutan berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-146` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name — Group Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Read Only) | Manage distributor — Region A {runId}-146 | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage distributor — Region B {runId}-146 | Update | 3 | 12 | Admin U |
| 3 | Remove | Manage partner — Region B {runId}-146 | Create | Assigned | - | Budi K |
| 4 | Assign | Manage partner — Region A {runId}-146 | Access | - | Active | Citra M |

- Setiap baris seed punya Date berbeda (selisih lebih dari satu menit); nilai `-` mewakili nilai kosong `—` pada tabel.

| Kolom uji Sort kelas teks |
|---|
| Action |
| Role Name — Group Name |
| Field |
| Modified By |

| Kolom uji Sort kelas campuran |
|---|
| Old Value |
| New Value |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-146`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-146` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Group Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-509: Sort 3-state kelas teks

3. Verifikasi tabel menampilkan sedikitnya dua baris data uji
4. Untuk setiap kolom pada tabel "Kolom uji Sort kelas teks" di Prerequisites (`Action`, `Role Name — Group Name`, `Field`, `Modified By`), lakukan langkah 5 sampai 12
5. Klik header `<kolom pada iterasi>` (klik 1)
6. Verifikasi kolom `<kolom pada iterasi>` terurut A–Z
7. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↑
8. Klik header `<kolom pada iterasi>` lagi (klik 2)
9. Verifikasi kolom `<kolom pada iterasi>` terurut Z–A
10. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↓
11. Klik header `<kolom pada iterasi>` lagi (klik 3)
12. Verifikasi tabel kembali ke sort default (Date Newest First)

### TC-AC-SU-510: Sort 3-state kelas campuran

13. Untuk setiap kolom pada tabel "Kolom uji Sort kelas campuran" di Prerequisites (`Old Value`, `New Value`), lakukan langkah 14 sampai 23
14. Klik header `<kolom pada iterasi>` (klik 1)
15. Verifikasi kolom `<kolom pada iterasi>` terurut numerik dulu lalu teks
16. Verifikasi nilai kosong pada kolom `<kolom pada iterasi>` berada di akhir
17. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↑
18. Klik header `<kolom pada iterasi>` lagi (klik 2)
19. Verifikasi kolom `<kolom pada iterasi>` terurut kebalikannya
20. Verifikasi nilai kosong pada kolom `<kolom pada iterasi>` berada di awal
21. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↓
22. Klik header `<kolom pada iterasi>` lagi (klik 3)
23. Verifikasi tabel kembali ke sort default (Date Newest First)

### TC-AC-SU-511: Sort 3-state kelas tanggal

24. Klik header `Date` (klik 1)
25. Verifikasi kolom `Date` terurut Oldest First
26. Verifikasi kolom `Date` menampilkan ikon sort ↑
27. Klik header `Date` lagi (klik 2)
28. Verifikasi kolom `Date` terurut Newest First
29. Verifikasi kolom `Date` menampilkan ikon sort ↓
30. Klik header `Date` lagi (klik 3)
31. Verifikasi tabel kembali ke sort default (Date Newest First)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 5 sampai 12 (kelas teks, tabel "Kolom uji Sort kelas teks") dan langkah 14 sampai 23 (kelas campuran, tabel "Kolom uji Sort kelas campuran"); `Verifikasi` tiap klik tetap satu per klausa. Membuka Detail, tab `Role`, dan sub-tab `Group Role` dijadikan satu langkah penghubung bersama klik icon `[📋]` (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Alasan ekspansi di atas ±35 langkah (31 langkah nominal, sekitar 65 dengan ekspansi blok berulang): semua TC berada di satu surface (Modal Changelog: User > Group Role (Sort)), satu akun, satu dataset; tiap TC berdiri sendiri dan tiap iterasi kolom diakhiri kembali ke sort default sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: TC-AC-SU-511: klik 2 menghasilkan Newest First (ikon ↓) dan klik 3 "kembali ke sort default (Date Newest First)", sehingga urutan klik 2 dan klik 3 sama dan hanya ikon yang membedakan; spec mengikuti TC. Pelaku seed `Budi K` dan `Citra M` pada kolom Modified By tidak terpetakan ke akun mana pun di Pre-setup; nilai dipakai apa adanya sebagai data seed, bukan akun login.
