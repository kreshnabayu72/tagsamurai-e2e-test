---
id: TC-GS-IMPORT-E2E-213-client-e-hasil-commit-setelah-custom-field-master-data-berubah-gate
title: "Client E: hasil commit setelah Custom Field/master data berubah (gate late-binding), baris gagal tidak membatalkan baris lain, baris error tetap, Brand existing tidak diperbarui"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-520
  - TC-GS-IMPORT-549
  - TC-GS-IMPORT-550
  - TC-GS-IMPORT-551
  - TC-GS-IMPORT-803
  - TC-GS-IMPORT-944
coverage:
  web: automated
---

# Client E: hasil commit setelah Custom Field/master data berubah (gate late-binding), baris gagal tidak membatalkan baris lain, baris error tetap, Brand existing tidak diperbarui

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit sungguhan di Client E (pembuat data, destruktif), memutasi Custom Field dan master data Client E (state global), dan menunggu worker commit nyata (batas tunggu 2 menit per commit) (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC2_PASSWORD` (nama env baru). Sesi API menghapus opsi Custom Field, mengganti tipe, menjadikan Required, dan menghapus Division; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > Brand Client E; Sub-Tab User Login dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Produk organisasi Client E: Global Settings dan Fixed Asset. Pre-setup Client E: Brand `Samsung`; Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`; Position `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor`, `Store Manager`; Custom Field Shift (Dropdown Pagi/Siang/Malam), Shift Notes, Overtime Hours (Numeric 2 desimal), Emergency Phone, Join Date (Optional, Active).
- Data Dinamis (draft commit Client E, disiapkan lewat skrip seed sebelum tiap TC; Client E direset tanpa draft, Kontrak Fixture R1):
  - D-54: draft User Login 8 baris `pending` (Rizky Pratama Shift `Siang`, Sinta Maharani Shift `Siang`, Doni Kurniawan, Eka Putri Overtime Hours `1.25` pada Row # 4, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata; Email dengan suffix per run `+{runId}-213`); dipakai TC-GS-IMPORT-520, 803, 944.
  - D-62: draft User Login 3 baris `pending` dari `user-login-ref.csv`: Row # 1 Division `Gudang` dan Position `Technician`, Row # 2 Division `Warehouse` dan Access `Global Settings;Fixed Asset`, Row # 3 Division `Marketing`; Position `Technician`, Access `Global Settings` dan `Global Settings;Fixed Asset`; dipakai TC-GS-IMPORT-550.
  - D-64: draft Brand 13 baris (`brand-13-autodel.csv`): Row 1 sampai 12 `Autodel 01` sampai `Autodel 12` `pending`, Row 13 Brand Name 121 karakter (huruf `A` diulang 121 kali) `error`; dipakai TC-GS-IMPORT-551.
  - `brand-case.csv` (header `Brand Name`; 2 baris `SAMSUNG` dan `Kodak`; upload UI): dipakai TC-GS-IMPORT-549.
  - Nama literal dipakai karena Client E khusus commit dan record hasil commit dihapus di hook `after`.
- Urutan TC: 549, 551, 520, 803, 944, 550 (TC-550 menghapus Division dan commit terakhir). Pemulihan dan pembersihan dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2, D-47) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh, D-47): hapus Brand `Kodak` dan `Autodel 01` sampai `Autodel 12`; hapus User Login hasil commit (Doni Kurniawan, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata, Rizky Pratama, Sinta Maharani, Citra Wulandari, Dedi Kurniawan); kembalikan opsi `Siang`, tipe `Overtime Hours` (Numeric, Decimal Places 2), Required `Overtime Hours` ke Optional; buat ulang Division `Gudang`; hapus draft; reset hasil commit terakhir dan penanda Banner Hasil Commit.
- Kemampuan teknis: pemilihan berkas; skrip seed D-54, D-62, D-64; skrip reset Client E (D-47); sesi API Admin kedua; worker commit berjalan normal.
- State global: Custom Field dan Division Client E (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Brand existing tidak diperbarui (TC-GS-IMPORT-549)

1. Klik `[Upload File]`
2. Pilih berkas `brand-case.csv`
3. Klik `[Confirm Mapping]`
4. Verifikasi Row # 1 `SAMSUNG` berstatus `duplicate`
5. Verifikasi Row # 2 `Kodak` berstatus `pending`
6. Klik `[Import (1)]`
7. Tunggu aksi selesai (permintaan mendapat respons)
8. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
9. Buka halaman Master Reference > Brand
10. Verifikasi daftar Brand memuat `Kodak`
11. Verifikasi daftar Brand memuat tepat satu `Samsung` dengan ejaan `Samsung` (tidak berubah menjadi `SAMSUNG`)
12. Pulihkan: hapus Brand `Kodak` dari Client E, buang draft Brand lewat skrip reset

### Baris error tidak hilang (TC-GS-IMPORT-551)

13. Seed draft D-64 lewat skrip seed, lalu buka Import > Brand
14. Klik `[Import (12)]`
15. Tunggu aksi selesai (permintaan mendapat respons)
16. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
17. Verifikasi Banner Hasil Commit bertone warning: "Success, record has been imported. Duplicate records were ignored. 1 error remains."
18. Verifikasi Staging Table masih memuat 1 baris berstatus `error`
19. Verifikasi Staging Metric Cards: Total Rows 1, Errors 1
20. Verifikasi Error Summary Callout memuat `Brand Name: Max. 120 characters` dengan badge "1 row"
21. Verifikasi ke-12 baris `pending` (`Autodel 01` sampai `Autodel 12`) sudah terkomit dan tidak tampil lagi di Staging Table
22. Tekan `F5` pada halaman Import
23. Verifikasi Staging Table masih memuat 1 baris berstatus `error` (Staging Metric Cards: Total Rows 1, Errors 1)
24. Verifikasi Error Summary Callout tetap memuat `Brand Name: Max. 120 characters` dengan badge "1 row"
25. Tekan `F5` sekali lagi
26. Verifikasi Staging Table masih memuat 1 baris berstatus `error` (Staging Metric Cards: Total Rows 1, Errors 1)
27. Verifikasi Error Summary Callout tetap memuat `Brand Name: Max. 120 characters` dengan badge "1 row"
28. Pulihkan: buang draft Brand (1 baris error) lewat Discard Draft, hapus Brand `Autodel 01` sampai `Autodel 12` dari Client E

### Gate commit menguji ulang opsi Dropdown (TC-GS-IMPORT-520)

29. Pindah ke Sub-Tab User Login, seed draft D-54 lewat skrip seed, muat ulang halaman
30. Admin kedua Client E (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan (halaman Import tidak dimuat ulang)
31. Klik `[Import (8)]`
32. Tunggu aksi selesai (permintaan mendapat respons)
33. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
34. Verifikasi Banner Hasil Commit bertone warning: "Success, record has been imported. Duplicate records were ignored. 2 errors remain."
35. Verifikasi Staging Table hanya memuat 2 baris `error` (bekas Row # 1 dan 2)
36. Verifikasi Error Summary Callout memuat `Shift: Invalid option` dengan badge "2 rows"
37. Buka halaman User > User List > Login User
38. Atur Rows per page 100
39. Verifikasi daftar Login User memuat 6 user baru: Doni Kurniawan, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, dan Indah Permata
40. Verifikasi Rizky Pratama dan Sinta Maharani tidak ada di daftar Login User
41. Pulihkan: Admin kedua menambahkan kembali opsi `Siang`, hapus 6 user hasil commit dari Client E, buang draft User Login lewat skrip reset

### Gate commit menguji ulang tipe Custom Field (TC-GS-IMPORT-803)

42. Seed draft D-54 lewat skrip seed, lalu buka Import > User Login
43. Admin kedua Client E (sesi API) mengganti tipe Custom Field `Overtime Hours` dari Numeric ke Date hingga tersimpan (halaman Import tidak dimuat ulang)
44. Klik `[Import (8)]`
45. Tunggu aksi selesai (permintaan mendapat respons)
46. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
47. Verifikasi Banner Hasil Commit bertone warning: "Success, record has been imported. Duplicate records were ignored. 1 error remains."
48. Verifikasi Staging Table hanya memuat bekas Row # 4 (Eka Putri) berstatus `error`
49. Verifikasi Error Summary Callout memuat `Overtime hours must be a valid date` dengan badge "1 row"
50. Buka halaman User > User List > Login User
51. Atur Rows per page 100
52. Verifikasi daftar Login User memuat 7 user baru: Rizky Pratama, Sinta Maharani, Doni Kurniawan, Fajar Hidayat, Gita Savitri, Hendra Gunawan, dan Indah Permata
53. Verifikasi Eka Putri tidak ada di daftar Login User
54. Pulihkan: Admin kedua mengembalikan tipe `Overtime Hours` ke Numeric (Decimal Places 2), hapus 7 user hasil commit dari Client E, buang draft User Login lewat skrip reset

### Gate commit menguji ulang flag Required (TC-GS-IMPORT-944)

55. Seed draft D-54 lewat skrip seed, lalu buka Import > User Login
56. Admin kedua Client E (sesi API) menjadikan Custom Field `Overtime Hours` Required hingga tersimpan (halaman Import tidak dimuat ulang)
57. Klik `[Import (8)]`
58. Tunggu aksi selesai (permintaan mendapat respons)
59. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
60. Verifikasi Banner Hasil Commit bertone warning: "Success, record has been imported. Duplicate records were ignored. 7 errors remain."
61. Verifikasi Staging Table memuat 7 baris `error`
62. Verifikasi Error Summary Callout memuat `Overtime hours must not be empty` dengan badge "7 rows"
63. Buka halaman User > User List > Login User
64. Atur Rows per page 100
65. Verifikasi daftar Login User memuat satu user baru: Eka Putri
66. Verifikasi tujuh user lain dari draft tidak ada di daftar Login User
67. Pulihkan: Admin kedua mengembalikan `Overtime Hours` ke Optional, hapus user hasil commit (Eka Putri) dari Client E, buang draft User Login lewat skrip reset

### Satu baris gagal tidak membatalkan baris lain (TC-GS-IMPORT-550)

68. Seed draft D-62 lewat skrip seed, lalu buka Import > User Login
69. Admin kedua Client E (sesi API) menghapus Division `Gudang` di User > Division hingga tersimpan (halaman Import tidak dimuat ulang)
70. Klik `[Import (3)]`
71. Tunggu aksi selesai (permintaan mendapat respons)
72. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
73. Verifikasi Banner Hasil Commit bertone warning: "Success, record has been imported. Duplicate records were ignored. 1 error remains."
74. Verifikasi Staging Table hanya memuat Row # 1 berstatus `error`
75. Verifikasi Error Summary Callout memuat `Division not found` dengan badge "1 row"
76. Buka halaman User > User List > Login User
77. Atur Rows per page 100
78. Verifikasi daftar Login User memuat 2 user baru: Citra Wulandari dan Dedi Kurniawan
79. Verifikasi Budi Santosa tidak ada di daftar Login User
80. Pulihkan: buat ulang Division `Gudang`, hapus 2 user hasil commit dari Client E, buang draft User Login lewat skrip reset

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 80 langkah, di atas 35 langkah. Alasan: enam blok commit berpola sama (seed draft, pemicu perubahan lewat sesi API, commit, tunggu worker, baca Banner dan Staging Table, baca daftar master data) pada satu client dan satu akun; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 12, 28, 41, 54, 67, 80), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca-log tidak ada; langkah tunggu worker (8, 16, 33, 46, 59, 72) adalah polling.
- P-2: Admin kedua hanya memicu perubahan Custom Field dan master data lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah pemulihan (12, 28, 41, 54, 67, 80) adalah aksi tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- Langkah 7, 15, 32, 45, 58, dan 71 (Tunggu aksi selesai, permintaan mendapat respons) adalah langkah penghubung tanpa `Verifikasi` sesudah klik `[Import (N)]` (D-1) sebelum polling.
- Langkah 38, 51, 64, dan 77 (Atur Rows per page 100) adalah langkah penghubung tanpa `Verifikasi` supaya daftar Login User memuat seluruh baris yang diasersi pada satu halaman (S-14); langkah 77 menjadi penghubung bagi asersi "tidak ada" Budi Santosa di langkah 79.
- Urutan 549, 551, 520, 803, 944, 550 menempatkan TC yang memutasi Division (TC-550) paling akhir; nomor TC di sourceTc tetap (S-05).
- Temuan untuk QA:
  - TC-GS-IMPORT-550 Expected c menyebut user baru "Citra Wulandari dan Dedi Kurniawan; Budi Santosa tidak ada", sedangkan D-62 (user-login-ref.csv) hanya mendefinisikan Division, Position, dan Access tanpa nama; nama pada Expected tidak cocok dengan berkas D-45 (Bambang Hartono, Citra Wulandari, Doni Kurniawan). Berkas data uji TC harus mendefinisikan nama user D-62. Spec mengasersi persis rumusan TC.
  - TC-GS-IMPORT-520, 803, 944 bergantung pada D-54 yang dibuat TC-GS-IMPORT-356 (kolom TC dependensi); spec menyiapkan D-54 lewat skrip seed, bukan menumpang spec lain.
  - TC-GS-IMPORT-520 Expected b tidak menyebut apakah Row # bekas Row # 1 dan 2 dinomori ulang; spec mengikuti "bekas Row # 1 dan 2".
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
