---
id: TC-FA-LIC-E2E-097-changelog-allocation-quota-sort-per-kelas-kolom-default
title: "Sort Modal Changelog Allocation Quota: Siklus Tiga Klik per Kelas Kolom, Urutan Default, dan Pindah Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-336
  - TC-FA-LIC-337
  - TC-FA-LIC-338
  - TC-FA-LIC-339
  - TC-FA-LIC-340
coverage:
  web: automated
---

# Sort Modal Changelog Allocation Quota: Siklus Tiga Klik per Kelas Kolom, Urutan Default, dan Pindah Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota #27 (6 entri) lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` (fixture belum ada, disediakan tim FE). Tiap kolom yang diurutkan punya sedikitnya dua nilai distinct (S-11).

  | Date | Action | Group Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Edit | — | Quota Alert Level | Normal | Low | System |
  | 29/09/26 10:05 | Edit | Divisi Logistik | Allocated Quota | 500 | 600 | Rudi H |
  | 28/09/26 15:30 | Edit | Divisi IT | Allocated Quota | — | 100 | Dewi L |
  | 27/09/26 09:00 | Remove Allocation | Gudang A | Allocated Quota | 100 | — | Rudi H |
  | 26/09/26 11:20 | Edit | Divisi Keuangan | Allocated Quota | — | 50 | Dewi L |
  | 25/09/26 08:45 | Remove Allocation | Divisi IT | Allocated Quota | 100 | — | Rudi H |

- Urutan default (Date terbaru): 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45.
- Data Uji Sort per kolom (dipakai langkah 2 sampai 7 dan 8 sampai 13; klik 3 selalu kembali ke urutan default):

  | TC | Kolom | Klik 1 `↑` (urutan Date) | Klik 2 `↓` (urutan Date) |
  |---|---|---|---|
  | 336 | Action | 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 26/09/26 11:20, 27/09/26 09:00, 25/09/26 08:45 | 27/09/26 09:00, 25/09/26 08:45, 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 26/09/26 11:20 |
  | 336 | Group Name | 28/09/26 15:30, 25/09/26 08:45, 26/09/26 11:20, 29/09/26 10:05, 27/09/26 09:00, 30/09/26 11:15 | 30/09/26 11:15, 27/09/26 09:00, 29/09/26 10:05, 26/09/26 11:20, 28/09/26 15:30, 25/09/26 08:45 |
  | 336 | Field | 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45, 30/09/26 11:15 | 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45 |
  | 336 | Modified By | 28/09/26 15:30, 26/09/26 11:20, 29/09/26 10:05, 27/09/26 09:00, 25/09/26 08:45, 30/09/26 11:15 | 30/09/26 11:15, 29/09/26 10:05, 27/09/26 09:00, 25/09/26 08:45, 28/09/26 15:30, 26/09/26 11:20 |
  | 337 | Old Value | 27/09/26 09:00, 25/09/26 08:45, 29/09/26 10:05, 30/09/26 11:15, 28/09/26 15:30, 26/09/26 11:20 | 28/09/26 15:30, 26/09/26 11:20, 30/09/26 11:15, 29/09/26 10:05, 27/09/26 09:00, 25/09/26 08:45 |
  | 337 | New Value | 26/09/26 11:20, 28/09/26 15:30, 29/09/26 10:05, 30/09/26 11:15, 27/09/26 09:00, 25/09/26 08:45 | 27/09/26 09:00, 25/09/26 08:45, 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 26/09/26 11:20 |
  | 338 | Date | 25/09/26 08:45, 26/09/26 11:20, 27/09/26 09:00, 28/09/26 15:30, 29/09/26 10:05, 30/09/26 11:15 | 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45 |

- Spec ini hanya membaca data dan tidak mengubah state global.
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: Urutan penuh entri Changelog (tabel Data Uji Sort dan langkah 15, 17, 19, 21) diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #27 dan #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.

## Test Steps

### TC-FA-LIC-336: Sort siklus 3-state kolom alfabetis (Action, Group Name, Field, Modified By)

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota

Untuk setiap baris TC 336 pada tabel "Data Uji Sort per kolom" (langkah 2 sampai 7):

2. Klik header kolom sekali
3. Verifikasi indikator `↑` dan urutan Date klik 1 pada baris tabel
4. Klik header kolom kedua kali
5. Verifikasi indikator `↓` dan urutan Date klik 2 pada baris tabel
6. Klik header kolom ketiga kali
7. Verifikasi kolom kembali ke urutan default

### TC-FA-LIC-337: Sort siklus 3-state kolom angka dan kosong (Old Value, New Value)

Untuk setiap baris TC 337 pada tabel "Data Uji Sort per kolom" (langkah 8 sampai 13):

8. Klik header kolom sekali
9. Verifikasi indikator `↑` dan urutan Date klik 1 pada baris tabel
10. Klik header kolom kedua kali
11. Verifikasi indikator `↓` dan urutan Date klik 2 pada baris tabel
12. Klik header kolom ketiga kali
13. Verifikasi kolom kembali ke urutan default

### TC-FA-LIC-338: Sort siklus 3-state kolom tanggal (Date)

14. Klik header `Date` sekali
15. Verifikasi indikator `↑` dan urutan: 25/09/26 08:45, 26/09/26 11:20, 27/09/26 09:00, 28/09/26 15:30, 29/09/26 10:05, 30/09/26 11:15
16. Klik header `Date` kedua kali
17. Verifikasi indikator `↓` dan urutan: 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45
18. Klik header `Date` ketiga kali
19. Verifikasi kolom kembali ke urutan default 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45

### TC-FA-LIC-339: Urutan default Date terbaru lebih dulu

20. Tutup modal dengan `[×]`, lalu buka kembali lewat ikon Changelog pada toolbar Level 1 Groups Quota
21. Verifikasi urutan awal tanpa mengklik header: 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45
22. Verifikasi indikator sort aktif pada kolom `Date`

### TC-FA-LIC-340: Berpindah kolom mereset kolom sebelumnya dan tidak menghapus Search

23. Klik header `Date` sekali
24. Klik header `Modified By` sekali
25. Verifikasi kolom `Date` kembali netral (indikator hilang)
26. Verifikasi kolom `Modified By` memulai dari Ascending (`↑`)
27. Ketik Search `Edit`, tekan Enter
28. Klik header `Modified By` kedua kali
29. Verifikasi kata kunci Search `Edit` tetap aktif pada kotak Search
30. Klik header `Modified By` ketiga kali, lalu klik icon panah `(←)` di kiri toolbar

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 20 membuka ulang modal supaya urutan awal TC-FA-LIC-339 teramati tanpa klik header sebelumnya; langkah 30 mengembalikan sort ke netral dan menutup Search (S-09).
- Langkah yang diulang per baris tabel Data Uji Sort: langkah 2 sampai 7 (4 iterasi) dan langkah 8 sampai 13 (2 iterasi) (bagian 8b butir 7).
- Spec ini memuat 30 langkah nominal dan sekitar 48 langkah dengan ekspansi. Alasan: seluruh blok adalah Sort pada modal yang sama dengan dataset yang sama dan berdiri sendiri; tiap kolom diakhiri klik ketiga yang mengembalikan urutan default, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-340 butir b ("mengubah arah sort tidak mereset kata kunci Search yang aktif") tidak menyebut hasil baris; spec mengasersi kata kunci Search tetap aktif pada kotak.
  - Hasil sort kolom Field klik 2 `↓` pada TC-FA-LIC-336 butir c sama dengan urutan default (nilai Field hanya dua nilai distinct); spec mengikuti TC.
