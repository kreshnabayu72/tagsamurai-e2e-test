---
id: TC-AC-SU-E2E-137-modal-changelog-user-download-csv-dan-pagination
title: "Modal Changelog User: Download CSV tanpa Search dan Filter serta Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-476
  - TC-AC-SU-479
coverage:
  web: automated
---

# Modal Changelog User: Download CSV tanpa Search dan Filter serta Pagination

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata; unduhan dibaca dari berkas.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Kemampuan teknis: membaca berkas unduhan (nama berkas, header kolom, dan jumlah baris data) serta mengatur ukuran halaman lewat UI.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-137 | Status | Active | Inactive | Admin U |
| 2 | Activate | John Doe {runId}-137 | Status | Inactive | Active | Admin U |
| 3 | Activate | Jane Smith {runId}-137 | Role | Inactive | Active | Budi K |
| 4 | Assign | Mike Tan {runId}-137 | Group | - | Manager | Citra M |
| 5 | Assign | Jane Smith {runId}-137 | Group | - | Manager | Citra M |

- Tambahan seed untuk TC-AC-SU-479: 30 entri Changelog User terbaru (termasuk lima entri tabel di atas) dengan Action beragam dan sedikitnya satu entri ber-Action `Assign`; entri itu menjadi 30 baris teratas pada urutan Newest First. Jumlah baris sumber modal (N) dibaca lewat kemampuan baca sebelum aksi dan harus lebih dari 10 (precondition TC-AC-SU-476).
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-476: Download Modal Changelog: User sebagai CSV tanpa search/filter

2. Catat jumlah baris sumber Modal Changelog: User sebagai N (kemampuan baca disediakan tim FE/BE)
3. Hover icon Download
4. Verifikasi tooltip `Download` tampil
5. Klik icon Download
6. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
7. Klik `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Changelog-User.csv` terunduh
10. Verifikasi berkas memuat seluruh baris Modal Changelog: User (semua halaman): jumlah baris data sama dengan N
11. Verifikasi kolom berkas sesuai kolom yang visible pada tabel

### TC-AC-SU-479: Pagination Modal Changelog: User

12. Verifikasi tabel menampilkan 10 baris per halaman secara default
13. Klik dropdown page size
14. Verifikasi opsi page size 10, 25, 50, dan 100
15. Tutup dropdown page size tanpa mengubah pilihan
16. Klik halaman 2
17. Verifikasi halaman 2 menampilkan entri urutan 11 sampai 20
18. Ubah page size ke 25
19. Verifikasi tabel menampilkan 25 baris
20. Ketik `2` di input nomor halaman, tekan Enter
21. Verifikasi input nomor halaman membawa ke halaman 2
22. Ketik Search `Assign`, tekan Enter
23. Verifikasi tabel kembali ke halaman 1
24. Klik `(←)` pada kotak Search
25. Ubah page size ke 10

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): mencatat N, menutup dropdown page size, menutup input Search, dan mengembalikan page size ke 10 di akhir spec. Search di TC-AC-SU-479 menjadi langkah TC itu sendiri.
- TC-AC-SU-477 (Download XLSX dengan search/filter aktif) ada di spec 197 karena Expected-nya mengasersi nilai sel berkas (kelas harness binary buffer).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) TC-AC-SU-476 butir c mengasersi "seluruh baris" tanpa menyebut N; karena audit trail permanen dan tumbuh, spec membandingkan jumlah baris berkas dengan N yang dibaca sebelum aksi (8b butir 10). (2) TC-AC-SU-479 butir a tidak menyebut cara mengamati opsi page size dan butir b ("entri 11 sampai 20") hanya diamati sebagai 10 baris pada halaman 2 tanpa membandingkan identitas entri. (3) Dengan 30 entri teratas dan page size 25, halaman 2 hanya relevan sebagai nomor halaman aktif; TC tidak menyebut isi halaman 2 pada page size 25.
