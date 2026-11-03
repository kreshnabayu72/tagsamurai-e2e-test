---
id: TC-AC-SU-E2E-197-modal-changelog-user-download-xlsx-hasil-filter-dan-nilai-sel
title: "Modal Changelog User: Download XLSX dengan Filter Aktif dan Nilai Sel Berkas"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-477
coverage:
  web: automated
---

# Modal Changelog User: Download XLSX dengan Filter Aktif dan Nilai Sel Berkas

## Prerequisites

- Mode: FE+BE. Semua data berasal dari backend nyata; unduhan dibaca dari berkas.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, env var `AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > User lewat sidebar). Flag Guided Tooltip dikelola hook suite (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); sesi API aktor dan kemampuan seeding mengikuti `suite.md`.
- Nilai data dirujuk lewat `Fixture.settingsUser.<kunci>` (berkas `fixtures/settingsUser.json` belum ada; ditandai, disediakan tim FE). Nama tampil user seed memakai suffix `{runId}-NNN` dengan NNN = nomor spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): seeding user dan entri Changelog beserta Date, Modified By, Old Value, dan New Value; pembacaan jumlah baris sumber; pembersihan user seed.
- Kemampuan teknis: membaca isi berkas XLSX (nilai sel, format tanggal, dan jumlah baris data).
- Data Dinamis (seed Changelog, urutan Date terbaru ke terlama):

| No | Action | User Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| 1 | Deactivate | John Doe {runId}-197 | Status | Active | - | Admin U |
| 2 | Activate | Jane Smith {runId}-197 | Role | Inactive | Active | Budi K |
| 3 | Assign | Mike Tan {runId}-197 | Group | - | Manager | Citra M |

- Nilai `-` pada tabel mewakili nilai kosong `—` di UI dan harus tertulis `-` pada berkas.
- Date Format General Settings entitas Principal tidak diubah spec ini.
- Changelog adalah audit trail permanen: entri seed tidak dapat dihapus; hook `after` hanya menonaktifkan/menghapus user seed milik spec ini. Total entri tidak diasersi sebagai angka absolut (S-12).

## Test Steps

1. Klik icon Changelog di toolbar User List

### TC-AC-SU-477: Download Modal Changelog: User sebagai XLSX dengan search/filter aktif

2. Klik icon Filter
3. Pilih `Deactivate` di field `Action`, lalu klik `[Apply]`
4. Verifikasi sedikitnya satu baris tampil di tabel
5. Verifikasi tabel hanya menampilkan baris ber-Action `Deactivate`
6. Catat jumlah baris hasil filter sebagai N (kemampuan baca disediakan tim FE/BE)
7. Klik icon Download
8. Klik `Download as XLSX`
9. Verifikasi tidak ada toast sukses
10. Verifikasi berkas `Changelog-User.xlsx` terunduh
11. Verifikasi berkas memuat sedikitnya satu baris data
12. Verifikasi berkas hanya memuat baris ber-Action `Deactivate` dengan jumlah baris data sama dengan N
13. Verifikasi nilai Date pada berkas mengikuti format General Settings
14. Verifikasi nilai kosong `—` pada tabel tertulis `-` pada berkas
15. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini berdiri sendiri karena Expected butir b mengasersi nilai sel berkas (format tanggal dan nilai kosong), yaitu kelas binary buffer (bagian 3 prinsip 13f); nama berkas, kolom, dan jumlah baris termasuk asersi fungsional.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): mencatat N dan membersihkan Filter di langkah 15. Filter dipakai sebagai kondisi "search/filter aktif"; TC tidak membatasi bentuknya.
- Nama literal TC (mis. `John Doe`, `Jane Smith`, `Mike Tan`) ditulis bersuffix `{runId}-NNN` sesuai keputusan nama Data Dinamis; asersi yang bergantung pada nama persis memakai nama bersuffix itu.
- Entitas Principal punya audit trail permanen yang tumbuh: entri seed spec ini ditulis dengan Date terbaru sehingga berada di halaman pertama (Newest First), dan tidak ada total entri yang diasersi sebagai angka absolut (S-12, S-14).
- Temuan untuk QA: (1) TC-AC-SU-477 menyebut "filter/search" tanpa memilih salah satu; spec memakai Filter Action. (2) Format tanggal berkas "mengikuti format General Settings" tanpa menyebut nilai format; spec membandingkannya dengan format tampil tabel.
