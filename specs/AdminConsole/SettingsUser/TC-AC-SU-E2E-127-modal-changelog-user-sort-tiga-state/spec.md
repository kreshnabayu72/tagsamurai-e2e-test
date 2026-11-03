---
id: TC-AC-SU-E2E-127-modal-changelog-user-sort-tiga-state
title: "Modal Changelog User: Sort 3-State Kelas Teks, Campuran, dan Tanggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-449
  - TC-AC-SU-450
  - TC-AC-SU-451
coverage:
  web: automated
---

# Modal Changelog User: Sort 3-State Kelas Teks, Campuran, dan Tanggal

## Prerequisites

- Mode: FE+BE. Semua data dan urutan berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-127 | Status | 10 | Alpha | Admin U |
| 2 | Activate | Jane Smith {runId}-127 | Role | 2 | - | Budi K |
| 3 | Assign | Mike Tan {runId}-127 | Group | - | beta | Citra M |
| 4 | Edit | Andi Wijaya {runId}-127 | Tier | Zulu | 100 | Dewi L |

- Setiap baris seed punya Date berbeda (selisih lebih dari satu menit); seluruh baris seed dibatasi dengan Filter User Name pada keempat user seed (langkah penghubung) sehingga urutan sort teramati pada baris seed saja (S-14); nilai kosong `-` mewakili nilai kosong `—` pada tabel.

| Kolom uji Sort kelas teks |
|---|
| Action |
| User Name |
| Field |
| Modified By |

| Kolom uji Sort kelas campuran |
|---|
| Old Value |
| New Value |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List
2. Klik icon Filter
3. Pilih keempat user seed di field `User Name`, lalu klik `[Apply]`
4. Verifikasi sedikitnya satu baris tampil di tabel

### TC-AC-SU-449: Sort 3-state kelas teks

5. Untuk setiap kolom pada tabel "Kolom uji Sort kelas teks" di Prerequisites (`Action`, `User Name`, `Field`, `Modified By`), lakukan langkah 6 sampai 11
6. Klik header `<kolom pada iterasi>` (klik 1)
7. Verifikasi kolom `<kolom pada iterasi>` terurut A–Z dengan ikon sort ↑
8. Klik header `<kolom pada iterasi>` lagi (klik 2)
9. Verifikasi kolom `<kolom pada iterasi>` terurut Z–A dengan ikon sort ↓
10. Klik header `<kolom pada iterasi>` lagi (klik 3)
11. Verifikasi tabel kembali ke sort default (Date Newest First)

### TC-AC-SU-450: Sort 3-state kelas campuran

12. Untuk setiap kolom pada tabel "Kolom uji Sort kelas campuran" di Prerequisites (`Old Value`, `New Value`), lakukan langkah 13 sampai 18
13. Klik header `<kolom pada iterasi>` (klik 1)
14. Verifikasi kolom `<kolom pada iterasi>` terurut numerik dulu lalu teks, nilai kosong di akhir, dengan ikon sort ↑
15. Klik header `<kolom pada iterasi>` lagi (klik 2)
16. Verifikasi kolom `<kolom pada iterasi>` terurut kebalikannya, nilai kosong di awal, dengan ikon sort ↓
17. Klik header `<kolom pada iterasi>` lagi (klik 3)
18. Verifikasi tabel kembali ke sort default (Date Newest First)

### TC-AC-SU-451: Sort 3-state kelas tanggal

19. Klik header `Date` (klik 1)
20. Verifikasi kolom `Date` terurut Oldest First dengan ikon sort ↑
21. Klik header `Date` lagi (klik 2)
22. Verifikasi kolom `Date` terurut Newest First dengan ikon sort ↓
23. Klik header `Date` lagi (klik 3)
24. Verifikasi tabel kembali ke sort default (Date Newest First)
25. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-14): membatasi tabel pada user seed lewat Filter `User Name` (langkah 2 sampai 3) agar urutan sort teramati pada baris seed, dan membersihkan Filter di langkah 25 (S-09).
- Langkah yang diulang per kolom: langkah 6 sampai 11 (kelas teks, iterasi dari tabel "Kolom uji Sort kelas teks") dan langkah 13 sampai 18 (kelas campuran, tabel "Kolom uji Sort kelas campuran"); `Verifikasi` tiap klik tetap satu per klausa.
- Spec ini sengaja satu spec dengan tiga TC: satu modal, satu akun, satu dataset, dan tiap TC berdiri sendiri karena sort dikembalikan ke default pada klik ketiga.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) TC-AC-SU-451: klik 2 menghasilkan Newest First (ikon ↓) dan klik 3 "kembali ke sort default (Date Newest First)", sehingga urutan klik 2 dan klik 3 sama dan hanya ikon yang membedakan; spec mengikuti TC. (2) TC-AC-SU-449 sampai 451 tidak menyebut pembatas dataset; karena Changelog entitas bersifat permanen dan lintas user, spec menambah Filter `User Name` pada user seed sebagai langkah penghubung. (3) Urutan numerik-lalu-teks pada TC-AC-SU-450 dinilai pada baris seed saja (nilai `10`, `2`, `100` dan teks).
