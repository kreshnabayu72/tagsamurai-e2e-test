---
id: TC-FA-LIC-E2E-171-changelog-concurrent-user-sort-date-dan-siklus-tiga-klik
title: "Sort Modal Changelog Concurrent User: Urutan Default Date dan Siklus Tiga Klik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-569
  - TC-FA-LIC-570
coverage:
  web: automated
---

# Sort Modal Changelog Concurrent User: Urutan Default Date dan Siklus Tiga Klik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Concurrent User #31 (4 entri) lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE).

  | Date | Action | User Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Force Logout | Budi Santoso | Session Status | Active | Force Logged Out | Rudi H |
  | 29/09/26 14:20 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |
  | 28/09/26 09:40 | Force Logout | Andi Pratama | Session Status | Active | Force Logged Out | Rudi H |
  | 27/09/26 16:05 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |

- Data Uji Sort alfabetis (TC-FA-LIC-569), dipakai langkah 10 sampai 15; klik 3 selalu kembali ke urutan default 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05:

  | Kolom | Klik 1 `↑` (urutan Date) | Klik 2 `↓` (urutan Date) |
  |---|---|---|
  | User Name | 28/09/26 09:40, 30/09/26 11:15, 29/09/26 14:20, 27/09/26 16:05 | 29/09/26 14:20, 27/09/26 16:05, 30/09/26 11:15, 28/09/26 09:40 |
  | Modified By | 29/09/26 14:20, 27/09/26 16:05, 30/09/26 11:15, 28/09/26 09:40 | 30/09/26 11:15, 28/09/26 09:40, 29/09/26 14:20, 27/09/26 16:05 |

- Spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar

### TC-FA-LIC-570: Sort kolom Date dan urutan default Date terbaru

2. Verifikasi urutan awal tanpa mengklik header: 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05
3. Verifikasi indikator sort aktif pada kolom `Date`
4. Klik header `Date` sekali
5. Verifikasi indikator `↑` dan urutan: 27/09/26 16:05, 28/09/26 09:40, 29/09/26 14:20, 30/09/26 11:15
6. Klik header `Date` kedua kali
7. Verifikasi indikator `↓` dan urutan: 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05
8. Klik header `Date` ketiga kali
9. Verifikasi kolom kembali ke urutan default

### TC-FA-LIC-569: Sort siklus 3-state kolom alfabetis (User Name, Modified By)

Untuk setiap baris tabel "Data Uji Sort alfabetis" (langkah 10 sampai 15):

10. Klik header kolom sekali
11. Verifikasi indikator `↑` dan urutan Date klik 1 pada baris tabel
12. Klik header kolom kedua kali
13. Verifikasi indikator `↓` dan urutan Date klik 2 pada baris tabel
14. Klik header kolom ketiga kali
15. Verifikasi kolom kembali ke urutan default

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Urutan blok: TC-FA-LIC-570 dijalankan sebelum TC-FA-LIC-569 karena memverifikasi urutan awal sebelum header lain diklik (S-10). Langkah yang diulang per baris tabel Data Uji: langkah 10 sampai 15 (2 iterasi) (bagian 8b butir 7). TC-FA-LIC-567, 568, dan 586 (Search) ada di spec `TC-FA-LIC-E2E-103`.
