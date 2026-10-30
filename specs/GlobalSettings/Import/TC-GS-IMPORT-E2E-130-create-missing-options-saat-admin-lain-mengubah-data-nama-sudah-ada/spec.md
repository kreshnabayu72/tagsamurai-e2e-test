---
id: TC-GS-IMPORT-E2E-130-create-missing-options-saat-admin-lain-mengubah-data-nama-sudah-ada
title: "Create Missing Options saat admin lain mengubah data: nama sudah ada, Custom Field dinonaktifkan atau dihapus, baris dihapus, dan Discard"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-914
  - TC-GS-IMPORT-915
  - TC-GS-IMPORT-916
  - TC-GS-IMPORT-917
  - TC-GS-IMPORT-929
coverage:
  web: automated
---

# Create Missing Options saat admin lain mengubah data: nama sudah ada, Custom Field dinonaktifkan atau dihapus, baris dihapus, dan Discard

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` hanya memicu perubahan state lewat sesi API (P-2) dengan `Spectra.env.GS_CLIENTC_TC2_PASSWORD`; tidak ada sesi UI kedua.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Client C); langkah pertama spec ini berpindah ke Tab User Login dan tidak menguji navigasi.
- Data Pre-setup (tidak diubah permanen; dipulihkan sesudah tiap TC, Kontrak Fixture R1-R2): Client C tanpa draft Tab User Login; Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`; `Lembur` dan `Piket` belum menjadi opsi.
- Data Dinamis (fixture baru, berkas CSV disediakan tim QA/FE; nilai literal dari TC dan bukan nama unik per run karena menentukan hasil staging):
  - `Fixture.import.userLoginShiftLembur` (user-login-shift-lembur.csv, D-79): 3 baris User Login, Shift `Lembur` (#1), `lembur ` (#2), `Siang` (#3); hasil staging #1 dan #2 `error`, #3 `pending`.
  - `Fixture.import.userLoginShiftTwo` (user-login-shift-two.csv, D-84): 2 baris, Shift `Lembur` (#1) dan `Piket` (#2); kedua baris `error`.
  - `Fixture.import.userLoginShiftSame` (user-login-shift-same.csv, D-85): 2 baris, Shift `Lembur` pada kedua baris; kedua baris `error`.
- Kemampuan teknis yang disediakan tim FE/BE: reset draft Client C ke tanpa draft; sesi API Admin kedua Client C untuk menambah opsi, menonaktifkan, menghapus Custom Field `Shift`, dan menghapus baris Staging Table; pemulihan Custom Field `Shift` (termasuk membuat ulang bila dihapus) ke kondisi Pre-setup; hook umur draft D-76 varian 1 (`created_at` dimundurkan 25 jam).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus draft Client C, hapus opsi `Lembur` dan `Piket` dari `Shift`, aktifkan kembali atau buat ulang Custom Field `Shift` bila berubah, pulihkan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- State global: Custom Field `Shift` Client C dan draft Client C berubah; suite berjalan serial (`parallel: false`), dinyatakan di `suite.md`.
- Env var yang dipakai: `GS_CLIENTC_TC_PASSWORD`, `GS_CLIENTC_TC2_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-914: Opsi sudah dibuat admin lain tepat sebelum klik

1. Buka Tab User Login pada halaman Import
2. Klik [Upload File] di toolbar dan pilih berkas user-login-shift-lembur.csv
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Admin kedua Client C (sesi API) menambahkan opsi `Lembur` ke Custom Field `Shift` hingga tersimpan
5. Tanpa memuat ulang halaman Import, klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
6. Verifikasi toast error "Error, failed to create option."
7. Verifikasi UI membaca ulang Staging Table dan ketiga baris berstatus `pending` tanpa muat ulang manual
8. Verifikasi Error Summary Callout tidak tampil
9. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
10. Verifikasi Value Setting `Shift` memuat `Lembur` tepat satu kali (`Pagi`, `Siang`, `Malam`, `Lembur`)
11. Pulihkan state: hapus draft Client C dan hapus opsi `Lembur` dari `Shift` lewat fixture, lalu buka Tab User Login pada halaman Import

### TC-GS-IMPORT-915: Halaman basi setelah Custom Field dinonaktifkan atau dihapus (varian 1 dan varian 2)

12. Klik [Upload File] di toolbar dan pilih berkas user-login-shift-lembur.csv
13. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
14. Varian 1: Admin kedua Client C (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
15. Tanpa memuat ulang halaman Import, klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
16. Verifikasi tidak ada dialog yang tampil
17. Verifikasi tidak ada toast yang tampil
18. Muat ulang halaman Import > User Login
19. Verifikasi kolom Shift tampil tanpa lencana
20. Verifikasi Banner Custom Field Deactivated tampil
21. Verifikasi baris #1 dan #2 tetap berstatus `error`
22. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "2 rows"
23. Verifikasi Error Summary Callout tidak memiliki tombol `[Create Missing Options]`
24. Buka Global Settings > User > Custom Field
25. Verifikasi Custom Field `Shift` berstatus Inactive
26. Verifikasi Value Setting `Shift` tetap `Pagi, Siang, Malam`
27. Pulihkan state: aktifkan kembali Custom Field `Shift` dan hapus draft Client C lewat fixture, lalu buka Tab User Login pada halaman Import
28. Klik [Upload File] di toolbar dan pilih berkas user-login-shift-lembur.csv
29. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
30. Varian 2: Admin kedua Client C (sesi API) menghapus Custom Field `Shift` hingga tersimpan
31. Tanpa memuat ulang halaman Import, klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
32. Verifikasi tidak ada dialog yang tampil
33. Verifikasi tidak ada toast yang tampil
34. Muat ulang halaman Import > User Login
35. Verifikasi Banner Custom Field Deleted tampil
36. Verifikasi kolom Shift tidak tampil
37. Verifikasi Error Summary Callout tidak memuat "Shift: Invalid option"
38. Buka Global Settings > User > Custom Field
39. Verifikasi Custom Field lain (`Emergency Phone`) tampil di daftar
40. Verifikasi Custom Field `Shift` tidak ada di daftar
41. Pulihkan state: buat ulang Custom Field `Shift` (Dropdown, opsi `Pagi`, `Siang`, `Malam`) dan hapus draft Client C lewat fixture, lalu buka Tab User Login pada halaman Import

### TC-GS-IMPORT-916: Bulk Create Missing Options saat baris sumber dihapus admin lain

42. Klik [Upload File] di toolbar dan pilih berkas user-login-shift-two.csv
43. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
44. Admin kedua Client C (sesi API) menghapus baris #2 hingga tersimpan
45. Tanpa memuat ulang halaman Import, klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
46. Verifikasi toast sukses sebagian "Success, option has been created. Some items were skipped."
47. Verifikasi draft menampilkan 1 baris `pending` dengan Shift `Lembur`
48. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
49. Verifikasi Value Setting `Shift` memuat `Pagi`, `Siang`, `Malam`, `Lembur`
50. Verifikasi opsi `Piket` tidak ditambahkan
51. Pulihkan state: hapus opsi `Lembur` dari `Shift` dan hapus draft Client C lewat fixture, lalu buka Tab User Login pada halaman Import

### TC-GS-IMPORT-917: Create Missing Options per-baris pada baris yang sudah dihapus admin lain

52. Klik [Upload File] di toolbar dan pilih berkas user-login-shift-same.csv
53. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
54. Klik `⋯` pada baris #1 (jangan muat ulang halaman setelahnya)
55. Admin kedua Client C (sesi API) menghapus baris #1 hingga tersimpan
56. Pilih `[Create Missing Options]` pada menu baris #1
57. Verifikasi tidak ada dialog yang tampil
58. Verifikasi tidak ada toast yang tampil
59. Verifikasi draft menampilkan 1 baris `error` dengan Shift `Lembur`
60. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
61. Verifikasi Value Setting `Shift` tetap `Pagi, Siang, Malam`
62. Pulihkan state: hapus draft Client C lewat fixture, lalu buka Tab User Login pada halaman Import

### TC-GS-IMPORT-929: Opsi hasil Create Missing Options tetap ada setelah Discard Draft

63. Klik [Upload File] di toolbar dan pilih berkas user-login-shift-lembur.csv
64. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
65. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
66. Tunggu aksi selesai (Error Summary Callout tidak tampil dan ketiga baris berstatus `pending`)
67. Mundurkan umur draft 25 jam lewat hook umur draft (D-76 varian 1), lalu muat ulang halaman Import > User Login
68. Klik [Discard] pada Unsaved Banner
69. Klik [Discard Draft] pada dialog
70. Verifikasi toast sukses "Success, draft has been discarded."
71. Verifikasi Tab User Login menampilkan Dropzone (belum ada draft)
72. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
73. Verifikasi Value Setting `Shift` memuat `Pagi`, `Siang`, `Malam`, `Lembur`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-914, 915, 916, 917, 929).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan; TC-GS-IMPORT-929 (Discard Draft) tetap paling akhir karena menghapus draft.
- P-2: Admin kedua Client C hanya memicu perubahan state (tambah opsi, nonaktif atau hapus Custom Field, hapus baris) lewat sesi API; hasilnya diasersi di sesi Total Control, sehingga tidak ada sesi UI kedua (kelas c).
- TC-GS-IMPORT-915 memuat dua varian (Custom Field dinonaktifkan, lalu dihapus). Keduanya dijalankan berurutan sebagai langkah 12 sampai 27 (varian 1) dan 28 sampai 41 (varian 2), masing-masing dengan draft baru.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (berpindah ke Tab User Login), langkah 11, 27, 41, 51, 62 (pemulihan Custom Field `Shift` dan draft sesuai Kontrak Fixture R1-R2, serta kembali ke Tab User Login), langkah 66 (menunggu aksi selesai karena langkah berikutnya mengubah umur draft dan memuat ulang halaman), langkah 9, 24, 38, 48, 60, 72 (berpindah ke Custom Field untuk observasi Expected).
- Anchor absence: "tidak ada dialog" dan "tidak ada toast" pada TC-915 dan TC-917 diletakkan segera setelah pemicu (klik `[Create Missing Options]`), sesuai bagian 8b butir 11; buktinya menyusul pada `Verifikasi` hasil (Banner, daftar Custom Field, draft 1 baris). Absence "Shift tidak ada di daftar" didahului `Verifikasi` Custom Field `Emergency Phone` tampil. Absence "Callout tidak memuat Shift: Invalid option" didahului `Verifikasi` Banner Custom Field Deleted tampil.
- Spec ini di atas sekitar 35 langkah (73 langkah). Alasan: kelima TC adalah blok homogen (upload draft, ubah state oleh Admin kedua, klik Create Missing Options, periksa hasil) yang berdiri sendiri dengan draft baru dan pemulihan di antaranya; kegagalan satu blok tidak membuat blok lain kehilangan makna. Tiga baris pertama tiap blok (upload, auto-match, Confirm Mapping) adalah prefix yang identik antar-TC.
- Kelas harness: Create Missing Options adalah fitur fungsional Import; request langsung ke server tidak dipakai. Lima TC konflik kunci (338, 725, 726, 727, 919) ada di spec 126, bukan di sini.
- Temuan untuk QA:
  - TC-GS-IMPORT-929 membutuhkan draft berumur 25 jam (Unsaved Banner dengan `[Discard]`) tetapi kolom D-ref hanya merujuk D-79 dan tidak merujuk D-76; spec memakai D-76 varian 1 sesuai langkah 4 TC.
  - TC-GS-IMPORT-915 langkah 3 berbunyi "ubah Custom Field `Shift` sesuai varian" dan Expected a berbunyi "UI hanya di-refresh"; spec menurunkan keduanya menjadi dua varian berurutan dan tidak punya langkah terpisah untuk "UI hanya di-refresh" (teramati lewat hasil sesudah muat ulang).
  - TC-GS-IMPORT-915 Expected b varian 2 tidak menyatakan keadaan baris #1 dan #2 setelah Custom Field dihapus, hanya bahwa kolom Shift dan pesan "Shift: Invalid option" tidak tampil; spec hanya mengasersi dua hal itu.
  - TC-GS-IMPORT-915 Post Condition (Custom Field `Shift` dipulihkan; draft dihapus) tidak punya langkah observasi, sehingga tidak diasersi.
  - Pemulihan Custom Field `Shift` yang dihapus (membuat ulang dengan opsi Pre-setup) tidak punya mekanisme di TC; dicatat sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-IMPORT-914 sampai 917 bertanda FE Test `Need API` (permintaan lewat fixture) tanpa menyebut endpoint; spec tidak menyebut endpoint (S-13).
