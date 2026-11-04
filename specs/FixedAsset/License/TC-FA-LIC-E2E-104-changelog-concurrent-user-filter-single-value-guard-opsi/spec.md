---
id: TC-FA-LIC-E2E-104-changelog-concurrent-user-filter-single-value-guard-opsi
title: "Filter Modal Changelog Concurrent User: Single-Value Guard, Opsi Dropdown, OR dan AND, Date Range, dan Paginasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-572
  - TC-FA-LIC-573
  - TC-FA-LIC-574
  - TC-FA-LIC-575
  - TC-FA-LIC-581
coverage:
  web: automated
---

# Filter Modal Changelog Concurrent User: Single-Value Guard, Opsi Dropdown, OR dan AND, Date Range, dan Paginasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (General Settings `dd/MM/yy`, `HH:mm`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hook `before` dan `after` memulihkannya lewat fixture BE pemulih riwayat): riwayat Changelog Concurrent User #31 (4 entri) lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE); sesi aktif Pre-setup #14 (Dewi Lestari dan Rudi Hartono memiliki sesi aktif tanpa entri Force Logout atas namanya).

  | Date | Action | User Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Force Logout | Budi Santoso | Session Status | Active | Force Logged Out | Rudi H |
  | 29/09/26 14:20 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |
  | 28/09/26 09:40 | Force Logout | Andi Pratama | Session Status | Active | Force Logged Out | Rudi H |
  | 27/09/26 16:05 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |

- Data Uji Filter per dropdown (TC-FA-LIC-573), dipakai langkah 13 sampai 17:

  | Dropdown | Opsi (DISTINCT data tabel saat ini) | Opsi dipilih | Hasil (Date) |
  |---|---|---|---|
  | User Name | Andi Pratama, Budi Santoso, Siti Rahma | `Siti Rahma` | 29/09/26 14:20, 27/09/26 16:05 |
  | Modified By | Dewi L, Rudi H | `Rudi H` | 30/09/26 11:15, 28/09/26 09:40 |

- Data untuk blok paginasi (TC-FA-LIC-581, langkah 33 sampai 47): riwayat Changelog Concurrent User 25 entri Force Logout: 4 entri Pre-setup #31 ditambah 21 entri fixture bertanggal sebelum 27/09/26 16:05 (Pre-setup #43, fixture BE disediakan tim FE/BE; Action `Force Logout`, Field `Session Status`, Old Value `Active`, New Value `Force Logged Out`). Pemulihan ke Pre-setup #31 oleh fixture BE pemulih riwayat di hook `after`.
- Spec ini tidak mengubah state global.
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: Urutan dan jumlah entri Changelog (langkah 11, 14, 16, 23, 25, 31, dan 46) diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.

## Test Steps

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar

### TC-FA-LIC-572: Screening Filter Panel: filter Action dan Field tidak tampil (Single-Value Guard)

2. Klik ikon Filter pada toolbar
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi panel tampil di bawah toolbar
5. Verifikasi field Date: date range picker, placeholder `Select date`
6. Verifikasi field User Name: dropdown multi-select searchable, placeholder `All users`
7. Verifikasi field Modified By: dropdown multi-select searchable, placeholder `All users`
8. Verifikasi tidak ada field filter `Action` dan `Field`
9. Verifikasi tombol `[Clear Field]` (kiri, text) dan `[Apply]` (kanan, filled)
10. Ketik Search `session`, tekan Enter
11. Verifikasi Search `session` menampilkan keempat entri (kolom Field tetap Searchable): 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05
12. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-573: Opsi dan penyaringan per dropdown (User Name, Modified By)

Untuk setiap baris tabel "Data Uji Filter per dropdown" (langkah 13 sampai 17):

13. Buka dropdown pada baris tabel
14. Verifikasi opsi dropdown sesuai kolom Opsi pada baris tabel
15. Pilih opsi pada kolom Opsi dipilih, klik `[Apply]`
16. Verifikasi tabel menampilkan Date pada kolom Hasil pada baris tabel yang sama
17. Klik `[Clear Field]`, klik `[Apply]`

18. Buka dropdown `User Name`
19. Verifikasi opsi `Andi Pratama`, `Budi Santoso`, dan `Siti Rahma` tampil pada dropdown User Name
20. Verifikasi `Dewi Lestari` dan `Rudi Hartono` tidak menjadi opsi User Name
21. Tutup dropdown `User Name`

### TC-FA-LIC-574: Dua opsi dalam satu field memakai OR, antar-field memakai AND

22. Pada `User Name` centang `Andi Pratama` dan `Budi Santoso`, klik `[Apply]`
23. Verifikasi `User Name` = `Andi Pratama` atau `Budi Santoso` (OR) menampilkan: 30/09/26 11:15, 28/09/26 09:40
24. Pada `Modified By` centang `Dewi L`, klik `[Apply]`
25. Verifikasi penambahan `Modified By` = `Dewi L` (AND) menampilkan empty state `No results found`
26. Klik `[Clear Field]`, klik `[Apply]`

### TC-FA-LIC-575: Filter date range picker (inklusif)

27. Verifikasi placeholder field Date `Select date`
28. Pada `Date` pilih rentang 28/09/26–29/09/26
29. Verifikasi teks tanggal terpilih mengikuti Date Format General Settings (`dd/MM/yy`)
30. Klik `[Apply]`
31. Verifikasi Date 28/09/26–29/09/26 menampilkan: 29/09/26 14:20, 28/09/26 09:40
32. Klik `[Clear Field]`, klik `[Apply]`

### TC-FA-LIC-581: Paginasi default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

33. Tutup modal dengan `[×]`
34. Jalankan fixture BE Pre-setup #43 (menambah 21 entri Force Logout) sampai riwayat berisi 25 entri
35. Klik ikon Changelog pada toolbar
36. Verifikasi default 10 baris per halaman
37. Verifikasi halaman 1 menampilkan 10 baris
38. Buka pilihan page size
39. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
40. Tutup pilihan page size tanpa memilih (klik di luar daftar)
41. Verifikasi page size tetap 10
42. Ketik nomor halaman 2 pada input, tekan Enter
43. Verifikasi input nomor halaman 2 langsung membuka halaman 2 pada page size 10
44. Verifikasi halaman 2 menampilkan 10 baris (baris ke-11 sampai ke-20)
45. Buka pilihan page size, pilih 25
46. Verifikasi seluruh 25 baris tampil dalam satu halaman
47. Verifikasi tabel kembali ke halaman 1

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 12, 17, 26, dan 32 membersihkan Search dan filter antar kasus (S-09); langkah 21 menutup dropdown; langkah 33 sampai 35 menutup modal, menambah entri, dan membuka kembali modal supaya 25 entri terbaca; langkah 40 menutup pilihan page size tanpa memilih.
- Langkah yang diulang per baris tabel Data Uji Filter: langkah 13 sampai 17 (2 iterasi) (bagian 8b butir 7).
- Spec di atas 35 langkah (47 langkah nominal dan sekitar 52 langkah dengan ekspansi): alasan dipertahankan, seluruh blok adalah Filter Panel dan paginasi modal Changelog Concurrent User yang sama dengan dataset yang sama, dan berdiri sendiri; tiap blok diakhiri `[Clear Field]` dan `[Apply]`, dan blok 25 entri berada di akhir sehingga kegagalannya tidak menutupi blok lain.
- Temuan untuk QA:
  - TC-FA-LIC-574 butir b menyebut penambahan `Modified By` = `Dewi L` menghasilkan empty state; hasil ini berasal dari irisan `User Name` {Andi Pratama, Budi Santoso} dengan entri `Dewi L` (Siti Rahma saja) dan spec mengikuti TC.
