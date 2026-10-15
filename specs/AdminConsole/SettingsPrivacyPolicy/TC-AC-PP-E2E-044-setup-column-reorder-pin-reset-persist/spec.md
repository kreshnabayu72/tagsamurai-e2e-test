---
id: TC-AC-PP-E2E-044-setup-column-reorder-pin-reset-persist
title: "Setup Column: Hide, Reorder, Pin, Reset, dan Persistensi Konfigurasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-131
  - TC-AC-PP-132
  - TC-AC-PP-133
  - TC-AC-PP-135
  - TC-AC-PP-137
coverage:
  web: automated
---

# Setup Column: Hide, Reorder, Pin, Reset, dan Persistensi Konfigurasi

## Prerequisites

- Mode: FE+BE. Dipertahankan sebagai FE+BE (bukan mock) karena TC-AC-PP-137 melakukan logout dan login ulang sungguhan sebagai Total Control; selain itu daftar riwayat versi dibaca dari backend (Riwayat A).
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`; nama env ini sudah terdaftar di `spectra.config.ts` dan `.env.example`).
- Dataset: Riwayat A (Version 3 Active, John Doe, 10 Aug 2026; Version 2, John Doe, 02 Jul 2026; Version 1, Jane Smith, 15 Jan 2026). Hook `before` men-seed Riwayat A lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat append-only sehingga tidak bisa dihapus lewat UI).
- Konfigurasi kolom tersimpan di cache browser; hook `before` mengosongkan cache konfigurasi kolom sehingga spec mulai dari konfigurasi default dan hook `after` memulihkannya.
- Kemampuan teknis: mengubah lebar viewport (TC-AC-PP-133) dan memulihkannya; browser yang sama untuk logout lalu login (TC-AC-PP-137).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Suite berjalan serial (`parallel: false`) karena konfigurasi kolom tersimpan di cache browser yang sama dengan spec lain dalam suite.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-131: Ceklis dan unceklis tiap kolom di popup Setup Column diterapkan setelah Save dan bertahan setelah refresh

1. Buka Settings > Privacy Policy lewat sidebar
2. Klik header `(⋯)` lalu klik "Setup Column..."
3. Uncheck `Version`
4. Verifikasi kolom `Version` hilang dari Live Preview
5. Verifikasi kolom `Version` hilang dari tabel di belakang popup
6. Klik `[Save]`
7. Verifikasi kolom `Version` tetap hilang dari tabel
8. Buka popup Setup Column, check kembali `Version`, lalu klik `[Save]`
9. Buka popup Setup Column, uncheck `Published At`
10. Verifikasi kolom `Published At` hilang dari Live Preview
11. Verifikasi kolom `Published At` hilang dari tabel di belakang popup
12. Klik `[Save]`
13. Verifikasi kolom `Published At` tetap hilang dari tabel
14. Buka popup Setup Column, check kembali `Published At`, lalu klik `[Save]`
15. Buka popup Setup Column, uncheck `Published By`
16. Verifikasi kolom `Published By` hilang dari Live Preview
17. Verifikasi kolom `Published By` hilang dari tabel di belakang popup
18. Klik `[Save]`
19. Verifikasi kolom `Published By` tetap hilang dari tabel
20. Muat ulang halaman dengan F5
21. Verifikasi kolom `Published By` tersembunyi pada konfigurasi terakhir yang disimpan
22. Verifikasi kolom `Version` dan `Published At` tampil pada konfigurasi terakhir yang disimpan
23. Buka popup Setup Column, check kembali `Published By`, lalu klik `[Save]`

### TC-AC-PP-132: Drag reorder kolom di popup Setup Column diterapkan setelah Save dan bertahan setelah refresh

24. Buka popup Setup Column
25. Tarik `Published By` ke posisi pertama
26. Tarik `Version` ke posisi terakhir
27. Verifikasi Live Preview menampilkan urutan `Published By`, `Published At`, `Version`
28. Klik `[Save]`
29. Verifikasi tabel menampilkan urutan `Published By`, `Published At`, `Version`
30. Muat ulang halaman dengan F5
31. Verifikasi urutan tetap `Published By`, `Published At`, `Version`
32. Buka popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-AC-PP-133: Pin dan Unpin tiap kolom di popup Setup Column membekukan kolom di sisi kiri dan bertahan setelah refresh

33. Buka popup Setup Column, klik icon Pin pada `Version`, lalu klik `[Save]`
34. Perkecil lebar viewport hingga tabel dapat di-scroll horizontal
35. Scroll tabel ke kanan
36. Verifikasi kolom `Version` tetap di sisi kiri saat tabel di-scroll horizontal
37. Buka popup Setup Column, klik icon Pin pada `Version` (Unpin), klik icon Pin pada `Published At`, lalu klik `[Save]`
38. Scroll tabel ke kanan
39. Verifikasi kolom `Published At` tetap di sisi kiri
40. Verifikasi kolom `Version` ikut bergeser
41. Buka popup Setup Column, klik icon Pin pada `Published At` (Unpin), klik icon Pin pada `Published By`, lalu klik `[Save]`
42. Scroll tabel ke kanan
43. Verifikasi kolom `Published By` tetap di sisi kiri
44. Muat ulang halaman dengan F5
45. Scroll tabel ke kanan (lebar viewport masih diperkecil)
46. Verifikasi pin pada `Published By` tetap berlaku setelah F5
47. Buka popup Setup Column, klik icon Pin pada `Published By` (Unpin), lalu klik `[Save]`
48. Scroll tabel ke kanan
49. Verifikasi tidak ada kolom yang beku
50. Verifikasi kolom `Version`, `Published At`, dan `Published By` ikut bergeser saat scroll
51. Pulihkan lebar viewport ke ukuran semula

### TC-AC-PP-135: Reset to Default mengembalikan konfigurasi ke default setelah Save

52. Buka popup Setup Column, uncheck `Published At`, tarik `Published By` ke posisi pertama, lalu klik `[Save]` (konfigurasi awal TC: `Published At` hidden dan urutan `Published By`, `Version`)
53. Buka popup Setup Column
54. Klik `[Reset to Default]`
55. Verifikasi Live Preview menampilkan `Version`, `Published At`, `Published By` dalam urutan default, semua visible
56. Klik `[Save]`
57. Verifikasi tabel menampilkan urutan dan visibilitas default
58. Muat ulang halaman dengan F5
59. Verifikasi konfigurasi default tetap berlaku

### TC-AC-PP-137: Konfigurasi kolom tersimpan per tabel dan bertahan setelah logout lalu login kembali

60. Buka popup Setup Column, uncheck `Published At`, lalu klik `[Save]` (konfigurasi awal TC: `Published At` disembunyikan dan disimpan)
61. Logout
62. Login kembali sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`) di browser yang sama
63. Buka Settings > Privacy Policy
64. Verifikasi tabel menampilkan hanya `Version` dan `Published By`
65. Verifikasi konfigurasi tidak hilang setelah logout dan login
66. Buka popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE (lihat Prerequisites). Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sesuai TC sumber (131, 132, 133, 135, 137). TC-137 di akhir karena memakai login ulang dan menyisakan konfigurasi tersembunyi yang direset di langkah 66 (S-10).
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 8, 14, 23 (kembalikan kolom yang di-uncheck ke checked agar kolom berikutnya diuji dari state netral, sesuai langkah 3 TC-131), langkah 32 (kembali ke default sebelum TC-133), langkah 45 (scroll tabel ke kanan setelah F5 agar pin teramati; S-14), langkah 51 (pulihkan viewport), langkah 66 (kembali ke default). Langkah 52 dan 60 menyalin precondition TC-135 dan TC-137 (S-04) karena TC tersebut mensyaratkan konfigurasi yang sudah diubah dan tersimpan.
- Langkah 61 sampai 62 adalah ganti sesi eksplisit pada akun yang sama (objek uji TC-137); sesi dipulihkan ke akun default suite di hook `after`.
- Spec tidak membuat data dan tidak mengubah Pre-setup; konfigurasi kolom hanya di cache browser.
- Temuan untuk QA: (1) TC-133 Expected c ("Setelah F5 pin pada Published By tetap berlaku") tidak menyebut langkah observasi setelah muat ulang; pin hanya teramati bila tabel di-scroll sehingga spec menambah langkah scroll (langkah 45) sebelum `Verifikasi` langkah 46. (2) TC-137 menyebut "Konfigurasi kolom tersimpan per tabel" tetapi tidak ada langkah yang membandingkan dengan tabel lain; spec mengikuti Expected TC (hanya konfigurasi tabel Version History).
- Panjang spec (66 langkah) melewati perkiraan 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: TC dalam spec satu topik, satu akun, dan satu dataset; tiap bagian dipisah subjudul TC dan tetap bermakna walau bagian sebelumnya gagal karena state dikembalikan di langkah penghubung (batas ukuran konvensi bagian 3 bukan jumlah langkah).
