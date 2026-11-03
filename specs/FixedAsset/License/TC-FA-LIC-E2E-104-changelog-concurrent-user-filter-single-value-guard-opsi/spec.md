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

- Data untuk blok paginasi (TC-FA-LIC-581, langkah 32 sampai 42): riwayat Changelog Concurrent User ditambah sampai 25 entri Force Logout lewat fixture BE (disediakan tim FE/BE; entri Pre-setup #31 termasuk di dalamnya). Pemulihan ke Pre-setup #31 oleh fixture BE pemulih riwayat di hook `after`.
- Spec ini tidak mengubah state global.

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
19. Verifikasi `Dewi Lestari` dan `Rudi Hartono` tidak menjadi opsi User Name (opsi `Andi Pratama`, `Budi Santoso`, dan `Siti Rahma` tampil)
20. Tutup dropdown `User Name`

### TC-FA-LIC-574: Dua opsi dalam satu field memakai OR, antar-field memakai AND

21. Pada `User Name` centang `Andi Pratama` dan `Budi Santoso`, klik `[Apply]`
22. Verifikasi `User Name` = `Andi Pratama` atau `Budi Santoso` (OR) menampilkan: 30/09/26 11:15, 28/09/26 09:40
23. Pada `Modified By` centang `Dewi L`, klik `[Apply]`
24. Verifikasi penambahan `Modified By` = `Dewi L` (AND) menampilkan empty state `No results found`
25. Klik `[Clear Field]`, klik `[Apply]`

### TC-FA-LIC-575: Filter date range picker (inklusif)

26. Verifikasi placeholder field Date `Select date`
27. Pada `Date` pilih rentang 28/09/26–29/09/26
28. Verifikasi teks tanggal terpilih mengikuti Date Format General Settings (`dd/MM/yy`)
29. Klik `[Apply]`
30. Verifikasi Date 28/09/26–29/09/26 menampilkan: 29/09/26 14:20, 28/09/26 09:40
31. Klik `[Clear Field]`, klik `[Apply]`

### TC-FA-LIC-581: Paginasi default 10 per halaman, pilihan 10/25/50/100, input nomor halaman

32. Tutup modal dengan `[×]`
33. Tambah entri Force Logout lewat fixture BE sampai riwayat berisi 25 entri
34. Klik ikon Changelog pada toolbar
35. Verifikasi default 10 baris per halaman
36. Ketik nomor halaman 2 pada input, tekan Enter
37. Verifikasi input nomor halaman 2 langsung membuka halaman 2
38. Buka pilihan page size
39. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
40. Pilih 25
41. Verifikasi seluruh 25 baris tampil dalam satu halaman
42. Verifikasi tabel kembali ke halaman 1

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 12, 17, 25, dan 31 membersihkan Search dan filter antar kasus (S-09); langkah 20 menutup dropdown; langkah 32 sampai 34 menutup modal, menambah entri, dan membuka kembali modal supaya 25 entri terbaca.
- Langkah yang diulang per baris tabel Data Uji Filter: langkah 13 sampai 17 (2 iterasi) (bagian 8b butir 7).
- Perubahan urutan di TC-FA-LIC-581: lompat ke halaman 2 (langkah 36 dan 37) dilakukan sebelum mengganti page size ke 25, karena dengan 25 entri dan page size 25 halaman 2 tidak ada. TC menulis lompat sesudah ganti page size dengan frasa "bila tersedia".
- Spec di atas 35 langkah (42 langkah nominal dan sekitar 47 langkah dengan ekspansi): alasan dipertahankan, seluruh blok adalah Filter Panel dan paginasi modal Changelog Concurrent User yang sama dengan dataset yang sama, dan berdiri sendiri; tiap blok diakhiri `[Clear Field]` dan `[Apply]`, dan blok 25 entri berada di akhir sehingga kegagalannya tidak menutupi blok lain.
- Temuan untuk QA:
  - TC-FA-LIC-574 butir b menyebut penambahan `Modified By` = `Dewi L` menghasilkan empty state; hasil ini berasal dari irisan `User Name` {Andi Pratama, Budi Santoso} dengan entri `Dewi L` (Siti Rahma saja) dan spec mengikuti TC.
  - TC-FA-LIC-581 komposisi 24 entri tambahan tidak didefinisikan; spec hanya mensyaratkan total 25 entri.
  - TC-FA-LIC-581 langkah 4 dan 5 membuat halaman 2 tidak tersedia pada page size 25 dengan 25 entri; butir d memakai frasa "(bila tersedia)".
