---
id: TC-AC-PP-E2E-033-search-version-history
title: "Search Version History: Siklus Interaksi dan Pencocokan Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-11
  - TC-AC-PP-96
  - TC-AC-PP-97
  - TC-AC-PP-98
  - TC-AC-PP-100
  - TC-AC-PP-101
  - TC-AC-PP-102
coverage:
  web: automated
---

# Search Version History: Siklus Interaksi dan Pencocokan Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe` 10 Aug 2026, Version 2 `John Doe` 02 Jul 2026, Version 1 `Jane Smith` 15 Jan 2026 akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (dipakai TC-AC-PP-100). Spec tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat A.
- State UI yang diubah spec dan dipulihkan: kolom `Published By` disembunyikan lalu ditampilkan kembali (TC-AC-PP-102; konfigurasi kolom tersimpan di cache browser), keyword Search dikosongkan di antara TC. Hook `after` menampilkan kembali semua kolom sebagai cadangan.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-96: Reveal search box: icon Search membuka input dengan auto-focus, placeholder, dan tooltip

1. Hover icon Search di toolbar
2. Verifikasi tooltip "Search" tampil
3. Klik icon Search
4. Verifikasi search bar melebar (reveal)
5. Verifikasi kursor otomatis fokus di input
6. Verifikasi placeholder input "Search version or published by..."
7. Verifikasi icon panah kembali `(←)` tampil di kiri input

### TC-AC-PP-97: Siklus interaksi Search: ketik tidak memfilter, Enter memfilter, (✕) menghapus teks tanpa reset tabel, Enter pada input kosong mereset, (←) menutup dan mereset langsung

8. Klik icon `(←)` untuk menutup search bar
9. Klik icon Search
10. Ketik "jane" di input (jangan tekan Enter)
11. Verifikasi icon (✕) muncul di sisi kanan input
12. Verifikasi tabel masih menampilkan 3 baris (belum tersaring)
13. Tekan Enter
14. Verifikasi tabel hanya menampilkan baris `Version 1` (Published By `Jane S`)
15. Klik icon (✕) pada input
16. Verifikasi input kosong
17. Verifikasi search bar tetap terbuka dengan kursor fokus
18. Verifikasi tabel masih hanya menampilkan `Version 1`
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan 3 baris
21. Ketik "jane" di input lalu tekan Enter
22. Klik icon `(←)`
23. Verifikasi search bar menutup kembali menjadi icon Search
24. Verifikasi keyword kosong
25. Verifikasi tabel langsung menampilkan 3 baris

### TC-AC-PP-98: Search kolom Published By mencocokkan nama lengkap snapshot secara substring dan tidak peka huruf besar-kecil

26. Klik icon Search, ketik "DOE", tekan Enter
27. Verifikasi baris `Version 3` dan `Version 2` tampil
28. Verifikasi baris `Version 1` tidak tampil
29. Ganti keyword dengan "oh", tekan Enter
30. Verifikasi baris `Version 3` dan `Version 2` tampil
31. Ganti keyword dengan "john d", tekan Enter
32. Verifikasi baris `Version 3` dan `Version 2` tampil (cocok dengan nama lengkap `John Doe`)
33. Ganti keyword dengan "Smith", tekan Enter
34. Verifikasi hanya baris `Version 1` tampil (cocok dengan nama lengkap `Jane Smith`)
35. Klik icon `(←)` untuk menutup search bar dan mereset keyword

### TC-AC-PP-100: Kolom Published At tidak dapat dicari lewat Search

36. Klik icon Search, ketik "10 Aug 26", tekan Enter
37. Verifikasi tidak ada baris yang cocok
38. Verifikasi tabel menampilkan Title "No results found"
39. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
40. Ganti keyword dengan "Jul", tekan Enter
41. Verifikasi tabel menampilkan empty state "No results found"
42. Ganti keyword dengan "26", tekan Enter
43. Verifikasi tabel menampilkan empty state "No results found" (nilai tanggal tidak ikut dicari)
44. Klik icon `(←)` untuk menutup search bar dan mereset keyword

### TC-AC-PP-101: Spasi di awal dan akhir keyword di-trim saat Enter

45. Klik icon Search, ketik "  Smith  " (spasi di awal dan akhir), tekan Enter
46. Verifikasi hanya baris `Version 1` tampil
47. Verifikasi isi input di layar tidak berubah (spasi tetap terlihat)
48. Verifikasi tidak ada pesan atau indikator
49. Ganti isi input dengan 3 spasi saja, tekan Enter
50. Verifikasi tabel kembali menampilkan 3 baris (query kosong setelah trim diperlakukan seperti input kosong)
51. Klik icon `(←)` untuk menutup search bar dan mereset keyword

### TC-AC-PP-11: Search tanpa hasil menampilkan empty state pencarian yang berbeda dari first-time setup

52. Klik icon Search di toolbar
53. Ketik "zzzz" lalu tekan Enter
54. Verifikasi body tabel menampilkan Title "No results found"
55. Verifikasi body tabel menampilkan Description "Try adjusting your search or filter."
56. Verifikasi table head dan toolbar tetap tampil
57. Verifikasi button [Create Privacy Policy] tidak tampil
58. Verifikasi Title "No Privacy Policy has been published yet." tidak tampil
59. Klik icon (✕) pada kotak search, lalu tekan Enter pada input kosong
60. Verifikasi 3 baris Riwayat A tampil kembali
61. Klik icon `(←)` untuk menutup search bar

### TC-AC-PP-102: Search terikat visibilitas kolom: kolom yang di-hide tidak dapat dicari dan kembali dapat dicari setelah di-unhide

62. Klik header kolom Actions `(⋯)` untuk membuka overlay Column Visibility
63. Uncheck `Published By`
64. Tutup overlay
65. Klik icon Search, ketik "Smith", tekan Enter
66. Verifikasi tidak ada baris yang cocok
67. Verifikasi tabel menampilkan empty state "No results found"
68. Klik header `(⋯)`
69. Check kembali `Published By`
70. Tutup overlay
71. Tekan Enter lagi pada keyword "Smith"
72. Verifikasi baris `Version 1` tampil kembali (keyword yang sama cocok lagi)
73. Klik icon `(←)` untuk menutup search bar dan mereset keyword

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah menutup search bar yang masih terbuka dari TC-AC-PP-96 supaya TC-AC-PP-97 mulai dari icon Search seperti langkah 1 TC, langkah menutup search bar dan mengosongkan keyword di akhir tiap blok TC, langkah menutup overlay Column Visibility pada blok TC-AC-PP-102.
- Urutan TC di dalam spec: 96, 97, 98, 100, 101, 11, 102 (bukan urutan nomor). Alasan: screening reveal (96) paling awal; TC-AC-PP-102 mengubah konfigurasi kolom sehingga ditaruh paling akhir.
- TC-AC-PP-103 (karakter khusus dan payload script pada Search, kelas a defense-in-depth) dipindah ke spec `TC-AC-PP-E2E-058` sesuai prinsip 13a.
- Ukuran spec melewati sekitar 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Seluruh blok TC berbagi dataset Riwayat A yang hanya dibaca, satu topik (Search tabel Version History) dan satu kelas (fungsional), dan tiap blok diawali dari search bar tertutup dengan keyword kosong sehingga kegagalan satu blok tidak membuat blok lain tidak bermakna; spec tidak dipecah.
- TC-AC-PP-105 (Search Riwayat S) ada di spec `TC-AC-PP-E2E-002`; TC-AC-PP-99 dan 104 (Search Riwayat B) ada di spec `TC-AC-PP-E2E-040`.
- Temuan untuk QA:
  - TC-AC-PP-98 Expected c menyebut keyword `john d` cocok dengan nama lengkap `John Doe`, sedangkan sel tabel hanya menampilkan `John D`; spec mengikuti TC (pencocokan pada nama lengkap snapshot).
  - TC-AC-PP-100 langkah awal menyebut precondition General Settings Date Format `dd MMM yy` tetapi tidak menyebut cara men-setnya; spec menetapkannya sebagai default environment di Prerequisites.
  - TC-AC-PP-102 tidak menyebut apakah konfigurasi kolom dipulihkan setelah TC; spec memulihkannya sendiri dengan mencentang kembali `Published By` pada blok TC-AC-PP-102.
