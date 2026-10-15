---
id: TC-AC-PP-E2E-038-sort-default-dan-siklus-tiga-klik
title: "Sort Tabel Version History: Urutan Default, Siklus Tiga Klik, dan Header Actions"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-120
  - TC-AC-PP-123
  - TC-AC-PP-125
  - TC-AC-PP-127
coverage:
  web: automated
---

# Sort Tabel Version History: Urutan Default, Siklus Tiga Klik, dan Header Actions

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe` 10 Aug 2026, Version 2 `John Doe` 02 Jul 2026, Version 1 `Jane Smith` 15 Jan 2026 akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Spec tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat A.
- State UI yang diubah spec dan dipulihkan: sort aktif dikembalikan ke netral (default Published At Newest First) di antara TC; overlay Column Visibility ditutup.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-120: Urutan default tabel Version History adalah Published At Newest First

1. Klik menu Settings > Privacy Policy di sidebar
2. Verifikasi urutan baris dari atas: `Version 3` (10 Aug 26), `Version 2` (02 Jul 26), `Version 1` (15 Jan 26)
3. Verifikasi baris teratas adalah versi dengan Published At terbaru

### TC-AC-PP-123: Sort kolom Published At mengikuti siklus tiga klik Oldest First, Newest First, netral

4. Klik header `Published At` satu kali
5. Verifikasi ikon `↑` aktif pada header `Published At`
6. Verifikasi urutan `Version 1` (15 Jan 26), `Version 2` (02 Jul 26), `Version 3` (10 Aug 26) (Oldest First)
7. Klik header `Published At` kedua kali
8. Verifikasi ikon `↓` aktif pada header `Published At`
9. Verifikasi urutan `Version 3`, `Version 2`, `Version 1` (Newest First)
10. Klik header `Published At` ketiga kali
11. Verifikasi indikator sort pada header `Published At` hilang
12. Verifikasi urutan kembali ke default Published At Newest First (`Version 3`, `Version 2`, `Version 1`)

### TC-AC-PP-125: Berpindah kolom sort mereset kolom sebelumnya ke netral dan memulai siklus dari ascending

13. Klik header `Version` satu kali
14. Klik header `Published At` satu kali
15. Verifikasi ikon `↑` aktif hanya pada header `Published At`
16. Verifikasi indikator sort pada header `Version` hilang (netral)
17. Verifikasi urutan baris mengikuti Published At Oldest First: `Version 1`, `Version 2`, `Version 3`
18. Klik header `Published At` dua kali lagi sampai indikator sort hilang (kembali ke default)

### TC-AC-PP-127: Header kolom Actions `(⋯)` tidak memiliki icon sort

19. Amati header kolom `Version`, `Published At`, `Published By`, dan `(⋯)`
20. Verifikasi header `Version` memiliki icon sort
21. Verifikasi header `Published At` memiliki icon sort
22. Verifikasi header `Published By` memiliki icon sort
23. Verifikasi header `(⋯)` tidak memiliki icon sort
24. Klik header `(⋯)`
25. Verifikasi overlay Column Visibility terbuka
26. Verifikasi urutan baris tidak berubah (klik tidak mengurutkan)
27. Tutup overlay Column Visibility

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah mengembalikan sort ke netral di akhir blok TC-AC-PP-125 (supaya TC-AC-PP-127 mulai dari urutan default) dan langkah menutup overlay Column Visibility di akhir blok TC-AC-PP-127.
- Urutan TC mengikuti urutan sumber setelah screening default (120, 123, 125, 127); tidak ada penyimpangan.
- Pembagian TC lintas spec: sort kolom Version dan Published By pada dataset khusus ada di `TC-AC-PP-E2E-002` (TC-AC-PP-124, Riwayat S), `TC-AC-PP-E2E-039` (TC-AC-PP-121, Riwayat T), dan `TC-AC-PP-E2E-040` (TC-AC-PP-122 dan 126, Riwayat B).
- Temuan untuk QA:
  - TC-AC-PP-125 langkah 1 menulis "Klik header `Version` satu kali" tanpa Expected untuk keadaan tengah itu; spec tidak mengasersi keadaan setelah klik pertama dan hanya mengasersi hasil akhir sesuai Expected a dan b.
  - TC-AC-PP-127 Expected b menyebut "klik membuka overlay Column Visibility (bukan mengurutkan)"; spec memecahnya menjadi verifikasi overlay terbuka dan urutan baris tidak berubah.
