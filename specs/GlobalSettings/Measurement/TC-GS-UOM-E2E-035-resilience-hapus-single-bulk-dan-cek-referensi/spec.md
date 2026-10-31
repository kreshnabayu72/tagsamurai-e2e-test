---
id: TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi
title: "Resilience Hapus: Cek Referensi Gagal, Delete Gagal, Timeout, dan Bulk Delete Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-104
  - TC-GS-UOM-105
  - TC-GS-UOM-106
  - TC-GS-UOM-107
  - TC-GS-UOM-108
  - TC-GS-UOM-124
  - TC-GS-UOM-261
  - TC-GS-UOM-262
  - TC-GS-UOM-353
  - TC-GS-UOM-354
coverage:
  web: automated
---

# Resilience Hapus: Cek Referensi Gagal, Delete Gagal, Timeout, dan Bulk Delete Gagal

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi). Spec mengasersi state backend (unit tetap ada di tabel sesudah dimuat dari server), sehingga tidak `Mode: mock`.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data dinamis (seeding lewat API di hook `before`, semuanya bebas relasi; tidak menumpang spec lain; menggantikan `Pack`, `Meter`, `Milliliter`, `Ton`, `Hectares`, dan `Basket` Pre-setup atau Population pada TC sumber agar baris bersama tidak termutasi, S-06):
  - `Res A {runId}-035` / `ra35` (TC-GS-UOM-104, 105, 106, 107).
  - `Res B {runId}-035` / `rb35` dan `Res C {runId}-035` / `rc35` (TC-GS-UOM-261, 262, 124).
  - `Hect {runId}-035` / `ht35` (TC-GS-UOM-108; dihapus sungguhan).
  - `Basket {runId}-035` / `bk35` (D-36; TC-GS-UOM-353 dan 354; dihapus sungguhan di TC-354).
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada request ke endpoint Measurement dan dilepas segera setelah dipakai:
  - respons Check References (`POST /v2/enterprise-management/measurements/check-references`, single dan bulk) dipaksa HTTP 500;
  - respons Check References dipaksa timeout (sekali untuk TC-GS-UOM-353, tahan berulang untuk TC-GS-UOM-107 dan 262);
  - respons Delete single (`DELETE /v2/enterprise-management/measurements`) dipaksa HTTP 500 (TC-GS-UOM-104) dan dipaksa timeout (TC-GS-UOM-105, 354);
  - respons Delete bulk (`DELETE /v2/enterprise-management/measurements`) dipaksa HTTP 500 (TC-GS-UOM-124);
  - respons Delete ditahan 2 detik (TC-GS-UOM-108).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): lepaskan semua intercept; hapus lewat API semua unit yang namanya memuat ` {runId}-035` bila masih ada.
- Kemampuan teknis: pembacaan tombol `[Try Again]` pada toast; klik ganda cepat pada `[Delete]`.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan

1. Ketik Search `{runId}-035`, tekan Enter
2. Verifikasi sedikitnya satu baris tampil di tabel

### TC-GS-UOM-106: Cek awal Check References gagal saat klik Delete

3. Paksa respons Check References HTTP 500 (intercept)
4. Klik `⋯` baris `Res A {runId}-035` > Delete
5. Verifikasi toast `Error, failed to delete unit.`
6. Tutup toast
7. Verifikasi dialog konfirmasi tidak tampil
8. Verifikasi baris `Res A {runId}-035` tetap ada di tabel

### TC-GS-UOM-107: Cek awal Check References timeout

9. Lepas intercept 500, paksa respons Check References timeout (intercept)
10. Klik `⋯` baris `Res A {runId}-035` > Delete
11. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
12. Verifikasi dialog tidak tampil
13. Tutup toast
14. Lepas intercept timeout

### TC-GS-UOM-104: Delete gagal 5xx tidak menghapus unit

15. Paksa respons Delete HTTP 500 (intercept)
16. Klik `⋯` baris `Res A {runId}-035` > Delete
17. Klik [Delete]
18. Verifikasi toast `Error, failed to delete unit.`
19. Verifikasi baris `Res A {runId}-035` tetap ada di tabel
20. Verifikasi dialog tetap terbuka untuk retry manual
21. Tutup toast

### TC-GS-UOM-105: Delete timeout menampilkan toast koneksi

22. Lepas intercept 500, paksa respons Delete timeout (intercept)
23. Klik [Delete] pada dialog yang masih terbuka dari langkah 16
24. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
25. Tutup toast
26. Lepas intercept timeout
27. Klik [Cancel] pada dialog

### TC-GS-UOM-353: Try Again pada toast koneksi cek awal Check References mengulang cek dan menampilkan dialog Delete

28. Paksa respons Check References timeout sekali (intercept)
29. Klik `⋯` baris `Basket {runId}-035` > Delete
30. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
31. Verifikasi dialog konfirmasi tidak tampil
32. Pulihkan respons normal (lepas intercept)
33. Klik [Try Again] pada toast
34. Verifikasi Check References diulang dan dialog `Delete Unit` dengan bullet `Basket {runId}-035` tampil
35. Klik [Cancel] pada dialog
36. Verifikasi dialog tertutup
37. Verifikasi baris `Basket {runId}-035` tetap ada di tabel

### TC-GS-UOM-261: Bulk Delete, cek awal Check References gagal 5xx

38. Paksa respons Check References HTTP 500 (intercept)
39. Centang `Res B {runId}-035` dan `Res C {runId}-035`
40. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
41. Verifikasi toast `Error, failed to delete unit.`
42. Tutup toast
43. Verifikasi dialog konfirmasi tidak tampil
44. Verifikasi `Res B {runId}-035` dan `Res C {runId}-035` tetap ada di tabel
45. Verifikasi centang `Res B {runId}-035` dan `Res C {runId}-035` tetap terpilih
46. Verifikasi Bulk Action Bar tetap tampil

### TC-GS-UOM-262: Bulk Delete, cek awal Check References timeout

47. Lepas intercept 500, paksa respons Check References timeout (intercept)
48. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete` (seleksi masih tercentang dari langkah 39)
49. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
50. Tutup toast
51. Verifikasi dialog konfirmasi tidak tampil
52. Verifikasi `Res B {runId}-035` dan `Res C {runId}-035` tetap ada di tabel
53. Verifikasi centang `Res B {runId}-035` dan `Res C {runId}-035` tetap terpilih
54. Verifikasi Bulk Action Bar tetap tampil
55. Lepas intercept timeout
56. Klik `[✕]` pada Bulk Action Bar

### TC-GS-UOM-354: Try Again pada toast koneksi Delete mengulang penghapusan

57. Paksa respons Delete timeout sekali (intercept)
58. Klik `⋯` baris `Basket {runId}-035` > Delete, klik [Delete] pada dialog
59. Verifikasi toast `Connection problem. Please try again.` dengan tombol `[Try Again]`
60. Verifikasi baris `Basket {runId}-035` masih ada di tabel
61. Pulihkan respons normal (lepas intercept)
62. Klik [Try Again] pada toast
63. Verifikasi toast `Success, unit has been deleted.`
64. Verifikasi baris `Basket {runId}-035` hilang dari tabel

### TC-GS-UOM-108: Klik ganda Delete hanya memproses satu penghapusan

65. Tutup toast
66. Tahan respons Delete selama 2 detik (intercept)
67. Klik `⋯` baris `Hect {runId}-035` > Delete
68. Klik [Delete] dua kali cepat
69. Verifikasi tepat satu toast `Success, unit has been deleted.`
70. Verifikasi tidak ada toast error dari klik kedua
71. Lepas intercept respons Delete

### TC-GS-UOM-124: Bulk Delete gagal 5xx tidak menghapus apa pun dan seleksi dipertahankan

72. Paksa respons Delete HTTP 500 (intercept)
73. Centang `Res B {runId}-035` dan `Res C {runId}-035`
74. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`, lalu klik [Delete] di dialog
75. Verifikasi toast `Error, failed to delete unit.`
76. Verifikasi `Res B {runId}-035` dan `Res C {runId}-035` tetap ada di tabel
77. Verifikasi seleksi `Res B {runId}-035` dan `Res C {runId}-035` dipertahankan
78. Lepas intercept respons Delete

## Notes

- Mode: FE+BE dengan intercept parsial. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: fault injection (prinsip 13b); TC-GS-UOM-108 (menahan respons hanya untuk mengamati) dan sisi sukses TC-GS-UOM-354 (setelah Try Again) tidak berkelas b sendiri dan ditempatkan di sini karena memakai pemicu intercept yang sama pada endpoint Delete.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 78.
- Urutan TC dalam spec: 106, 107, 104, 105, 353, 261, 262, 354, 108, 124 (urutan sumber 104, 105, 106, 107, 108, 124, 261, 262, 353, 354). Alasan: kegagalan cek referensi lebih dulu, kegagalan Delete sesudahnya, lalu bulk, sedangkan penghapusan sukses (TC-354, TC-108) setelah semua kasus yang membutuhkan baris itu; TC-GS-UOM-124 di akhir karena TC tidak menyebut keadaan dialog sesudah Bulk Delete gagal sehingga tidak ada langkah sesudahnya yang bergantung pada dialog (lihat Temuan untuk QA). TC-105 melanjutkan dialog yang masih terbuka dari TC-104 (TC-104 mengharapkan dialog tetap terbuka untuk retry manual). TC-354 bergantung pada TC-353 (kolom Dependensi): baris `Basket` yang sama dipakai, tidak dihapus di TC-353.
- Spec ini 78 langkah (di atas batas 35 langkah); alasan pertahanan: seluruhnya satu kelas harness (fault injection pada endpoint hapus) di atas satu dataset milik spec, tiap blok memakai unit sendiri, dan hanya TC-354 dan TC-108 yang menghapus data (di akhir). Tiga rantai bergantung: TC-105 melanjutkan dialog TC-104 (langkah 23 memakai dialog dari langkah 16), TC-262 melanjutkan seleksi TC-261 (langkah 48 memakai seleksi dari langkah 39), dan TC-354 memakai baris `Basket` dari TC-353; di luar ketiga rantai itu kegagalan satu blok tidak membuat blok lain kehilangan makna. Sepuluh TC ini satu spec karena kelas ringan (b) cukup satu spec per modul (bagian 3 konvensi).
- Langkah 2 adalah `Verifikasi` pembanding (butir 2 bagian 8b), bukan dari Expected TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search `{runId}-035` untuk menemukan baris, tersaring pada unit milik spec), semua langkah "Tutup toast" dan "Lepas intercept" (S-09: toast error berulang di-dismiss sebelum diasersi lagi, intercept dilepas segera setelah pemicu), langkah 27 (menutup dialog TC-104/105 lewat `[Cancel]`, TC tidak menyebut penutupan), langkah 56 (membersihkan seleksi), dan langkah 65 (menutup toast sukses TC-354 sebelum menghitung toast TC-108, butir 8b).
- Asersi absence baris pada langkah 64 memakai toast sukses langkah 63 sebagai anchor (butir 2 bagian 8b); langkah 8, 19, 37, 44, 52, 60, dan 76 mengasersi baris tetap ada (bukan absence).
- TC-GS-UOM-108: TC sumber memakai `Hectares` (hasil rename `Hectare` dari TC-88); spec memakai unit milik sendiri `Hect {runId}-035`. Dependensi TC-88 dipenuhi seeding spec sendiri.
- Tidak ada pembagian TC lintas spec lain; kasus record sudah dihapus admin lain ada di spec 060.
- Temuan untuk QA:
  - TC-GS-UOM-124 tidak menyatakan keadaan dialog `Delete Units` setelah Bulk Delete gagal 5xx (tetap terbuka seperti TC-104 untuk single, atau tertutup). Spec tidak mengasersinya dan menaruh TC itu di akhir spec; langkah sesudahnya tidak ada. Perlu konfirmasi PRD.
  - TC-GS-UOM-104 dan 105 menyebut dialog tetap terbuka untuk retry hanya pada TC-104; TC-105 tidak menyatakan keadaan dialog setelah timeout. Spec TC-105 melanjutkan dialog yang sama dan menutupnya lewat `[Cancel]` pada langkah 27; bila dialog sudah tertutup, langkah 27 gagal.
  - TC-GS-UOM-353 dan 354 tidak menjelaskan cara memicu "timeout sekali" (satu kali permintaan lalu respons normal); spec menulisnya sebagai intercept satu kali di Prerequisites.
