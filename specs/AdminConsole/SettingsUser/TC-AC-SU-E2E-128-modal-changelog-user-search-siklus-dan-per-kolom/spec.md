---
id: TC-AC-SU-E2E-128-modal-changelog-user-search-siklus-dan-per-kolom
title: "Modal Changelog User: Siklus Search Box dan Search per Kolom Kelas Teks"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-452
  - TC-AC-SU-453
coverage:
  web: automated
---

# Modal Changelog User: Siklus Search Box dan Search per Kolom Kelas Teks

## Prerequisites

- Mode: FE+BE. Semua data dan hasil Search berasal dari backend nyata.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-128 | Status | Active | Inactive | Admin U |
| 2 | Activate | Jane Smith {runId}-128 | Role | Inactive | Active | Budi K |
| 3 | Assign | Mike Tan {runId}-128 | Group | - | Manager | Citra M |
| 4 | Deactivate | Jane Smith {runId}-128 | Status | Active | Inactive | Admin U |

- Search hanya menyaring saat Enter. Pencarian per kolom memakai nilai seed berikut:

| Kolom uji Search | Keyword substring | Keyword huruf kapital | Nilai yang dicari |
|---|---|---|---|
| Action | deac | DEAC | Deactivate |
| User Name | john | JOHN | John Doe {runId}-128 |
| Field | stat | STAT | Status |
| Old Value | acti | ACTI | Active |
| New Value | inac | INAC | Inactive |
| Modified By | admin | ADMIN | Admin U |

- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-452: Siklus interaksi Search box

2. Hover icon Search
3. Verifikasi tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi kursor auto-focus di input Search
7. Verifikasi placeholder input Search `Search action, field, or value...`
8. Ketik `Deactivate` tanpa menekan Enter
9. Verifikasi icon `(✕)` muncul
10. Verifikasi tabel belum tersaring (baris yang tidak memuat `Deactivate` masih tampil)
11. Tekan Enter
12. Verifikasi sedikitnya satu baris tampil di tabel
13. Verifikasi tabel hanya menampilkan baris yang memuat `Deactivate`
14. Klik icon `(✕)`
15. Verifikasi input Search kosong
16. Verifikasi search bar tetap terbuka
17. Verifikasi tabel tetap hanya menampilkan baris yang memuat `Deactivate` (hasil search terakhir)
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali menampilkan semua data (baris yang tidak memuat `Deactivate` tampil kembali)
20. Ketik `Deactivate` lalu tekan Enter
21. Klik icon `(←)`
22. Verifikasi search bar collapse ke icon Search
23. Verifikasi keyword Search kosong
24. Verifikasi tabel langsung kembali menampilkan semua data

### TC-AC-SU-453: Search per kolom kelas teks

25. Untuk setiap baris tabel "Kolom uji Search" di Prerequisites, lakukan langkah 26 sampai 30
26. Ketik Search `<keyword substring pada iterasi>`, tekan Enter
27. Verifikasi tabel menampilkan baris yang memuat `<nilai pada iterasi>` pada kolom `<kolom pada iterasi>`
28. Ganti isi kotak search dengan `<keyword kapital pada iterasi>`, tekan Enter
29. Verifikasi tabel menampilkan baris yang memuat `<nilai pada iterasi>` pada kolom `<kolom pada iterasi>`
30. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 26 sampai 30 (iterasi dari tabel "Kolom uji Search" di Prerequisites); `Verifikasi` tetap satu per keyword. Langkah 30 (`(←)` pada kotak Search) adalah langkah penghubung yang mereset tabel antar iterasi (S-03, S-09).
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) Hasil Search dibaca pada halaman pertama (Newest First) yang memuat baris seed terbaru; TC tidak menyebut perilaku bila baris cocok berada di halaman lain (S-14). (2) Nilai `Modified By` pada TC-AC-SU-453 (`Admin U`) berformat [First Name] [Last Initial] (R-14); seed memakai nilai itu apa adanya.
