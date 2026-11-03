---
id: TC-AC-SU-E2E-139-modal-changelog-global-role-sort-tiga-state
title: "Modal Changelog Global Role: Sort 3-State Kelas Teks, Campuran, dan Tanggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-485
  - TC-AC-SU-486
  - TC-AC-SU-487
coverage:
  web: automated
---

# Modal Changelog Global Role: Sort 3-State Kelas Teks, Campuran, dan Tanggal

## Prerequisites

- Mode: FE+BE. Semua data dan urutan berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- User target Detail: `Jane Smith {runId}-139` (user seed milik spec ini, tanpa entri Changelog selain seed di bawah).
- Data Dinamis (seed Changelog user target, urutan Date terbaru ke terlama):

| No | Action | Role Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Assign (via Total Control) | Manage group | Access | Inactive | Assigned | Default User |
| 2 | Edit | Manage group | Update | 3 | 12 | Admin U |
| 3 | Remove | Manage user and role | Create | Assigned | - | Budi K |
| 4 | Assign | Manage partner | Access | - | Active | Citra M |

- Setiap baris seed punya Date berbeda (selisih lebih dari satu menit); nilai `-` mewakili nilai kosong `—` pada tabel.

| Kolom uji Sort kelas teks |
|---|
| Action |
| Role Name |
| Field |
| Modified By |

| Kolom uji Sort kelas campuran |
|---|
| Old Value |
| New Value |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Ketik Search `Jane Smith {runId}-139`, tekan Enter
2. Buka Detail user `Jane Smith {runId}-139` dengan klik Name baris itu di User List, klik tab `Role`, klik sub-tab `Global Role`, lalu klik icon `[📋]` Changelog

### TC-AC-SU-485: Sort 3-state kelas teks

3. Untuk setiap kolom pada tabel "Kolom uji Sort kelas teks" di Prerequisites (`Action`, `Role Name`, `Field`, `Modified By`), lakukan langkah 4 sampai 11
4. Klik header `<kolom pada iterasi>` (klik 1)
5. Verifikasi kolom `<kolom pada iterasi>` terurut A–Z
6. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↑
7. Klik header `<kolom pada iterasi>` lagi (klik 2)
8. Verifikasi kolom `<kolom pada iterasi>` terurut Z–A
9. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↓
10. Klik header `<kolom pada iterasi>` lagi (klik 3)
11. Verifikasi tabel kembali ke sort default (Date Newest First)

### TC-AC-SU-486: Sort 3-state kelas campuran

12. Untuk setiap kolom pada tabel "Kolom uji Sort kelas campuran" di Prerequisites (`Old Value`, `New Value`), lakukan langkah 13 sampai 22
13. Klik header `<kolom pada iterasi>` (klik 1)
14. Verifikasi kolom `<kolom pada iterasi>` terurut numerik dulu lalu teks
15. Verifikasi nilai kosong pada kolom `<kolom pada iterasi>` berada di akhir
16. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↑
17. Klik header `<kolom pada iterasi>` lagi (klik 2)
18. Verifikasi kolom `<kolom pada iterasi>` terurut kebalikannya
19. Verifikasi nilai kosong pada kolom `<kolom pada iterasi>` berada di awal
20. Verifikasi kolom `<kolom pada iterasi>` menampilkan ikon sort ↓
21. Klik header `<kolom pada iterasi>` lagi (klik 3)
22. Verifikasi tabel kembali ke sort default (Date Newest First)

### TC-AC-SU-487: Sort 3-state kelas tanggal

23. Klik header `Date` (klik 1)
24. Verifikasi kolom `Date` terurut Oldest First
25. Verifikasi kolom `Date` menampilkan ikon sort ↑
26. Klik header `Date` lagi (klik 2)
27. Verifikasi kolom `Date` terurut Newest First
28. Verifikasi kolom `Date` menampilkan ikon sort ↓
29. Klik header `Date` lagi (klik 3)
30. Verifikasi tabel kembali ke sort default (Date Newest First)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 4 sampai 11 (kelas teks, tabel "Kolom uji Sort kelas teks") dan langkah 13 sampai 22 (kelas campuran, tabel "Kolom uji Sort kelas campuran"); `Verifikasi` tiap klik tetap satu per klausa. Membuka Detail, tab `Role`, dan sub-tab `Global Role` dijadikan satu langkah penghubung bersama klik icon `[📋]` (S-03).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Alasan ekspansi di atas ±35 langkah (30 langkah nominal, sekitar 64 dengan ekspansi blok berulang): semua TC berada di satu surface (Modal Changelog: User > Global Role (Sort)), satu akun, satu dataset; tiap TC berdiri sendiri dan tiap iterasi kolom diakhiri kembali ke sort default sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`; S-03, R-16): Search untuk menemukan baris target sebelum membuka Detail (langkah 1); baris user seed tidak dijamin berada di halaman pertama User List.
- Temuan untuk QA: TC-AC-SU-487: klik 2 menghasilkan Newest First (ikon ↓) dan klik 3 "kembali ke sort default (Date Newest First)", sehingga urutan klik 2 dan klik 3 sama dan hanya ikon yang membedakan; spec mengikuti TC. Pelaku seed `Budi K` dan `Citra M` pada kolom Modified By tidak terpetakan ke akun mana pun di Pre-setup; nilai dipakai apa adanya sebagai data seed, bukan akun login.
