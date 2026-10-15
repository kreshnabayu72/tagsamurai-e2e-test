---
id: TC-AC-PP-E2E-057-android-download-dan-sort-bottom-sheet
title: "Android: Download Susunan Kolom Default dan Sort lewat Bottom Sheet"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-192
  - TC-AC-PP-208
coverage:
  mobile: automated
---

# Android: Download Susunan Kolom Default dan Sort lewat Bottom Sheet

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD §4.6); tampilan berupa card list dengan bottom sheet toolbar.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang, serta kemampuan mengetuk elemen UI, memuat ulang halaman (reload aplikasi/layar), dan membaca file unduhan di perangkat.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`, `Spectra.env.AC_TC_PASSWORD`). Login di aplikasi Android dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active/John Doe 10 Aug 2026, Version 2/John Doe 02 Jul 2026, Version 1/Jane Smith 15 Jan 2026). Spec tidak membuat versi baru; hook `after` mengembalikan dataset ke Riwayat A.
- Penyimpanan urutan sort: Expected TC-AC-PP-208 menyatakan urutan card dan pilihan sort tetap setelah muat ulang halaman; kemampuan teknis tambahan untuk memuat ulang layar aplikasi tanpa logout.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).
- Dokumen Privacy Policy bersifat tunggal platform-wide sehingga suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PP-192: Download memakai susunan kolom default karena Column Visibility tidak tersedia

1. Buka Settings > Privacy Policy di aplikasi Android
2. Ketuk `[⋯]` pada toolbar sehingga bottom sheet terbuka
3. Verifikasi bottom sheet hanya berisi Filter, Sort, dan Download
4. Verifikasi tidak ada kontrol Column Visibility atau Setup Column di aplikasi Android
5. Pilih Download as CSV
6. Verifikasi file `Privacy-Policy-Version-History.csv` terunduh
7. Verifikasi tidak ada toast sukses
8. Buka file `Privacy-Policy-Version-History.csv`
9. Verifikasi file memuat kolom `Version`, `Published At`, `Published By` (susunan default)

### TC-AC-PP-208: Sort lewat bottom sheet toolbar mengurutkan card list tanpa mereset Search

10. Ketuk `[🔍]`, ketik "doe", lalu tekan Enter
11. Verifikasi card `Version 3` dan `Version 2` tampil
12. Ketuk `[⋯]` toolbar sehingga bottom sheet terbuka
13. Verifikasi bottom sheet berisi Filter, Sort, dan Download
14. Pilih Sort, kolom `Published At`, arah Oldest First
15. Verifikasi urutan card `Version 2` lalu `Version 3`
16. Verifikasi keyword `doe` tetap aktif
17. Tutup bottom sheet lalu buka lagi lewat `[⋯]` → Sort
18. Verifikasi pilihan `Published At` Oldest First ditandai aktif di bottom sheet
19. Tutup bottom sheet lalu muat ulang halaman
20. Verifikasi urutan card tetap `Version 2` lalu `Version 3`
21. Verifikasi keyword `doe` tetap aktif
22. Ketuk `[⋯]` toolbar → Sort, pilih kolom `Version`, arah turun
23. Verifikasi urutan card `Version 3` lalu `Version 2`
24. Verifikasi keyword `doe` tetap aktif
25. Buka lagi bottom sheet lewat `[⋯]` → Sort
26. Verifikasi pilihan `Version` turun ditandai aktif
27. Pilih Sort, kolom `Published At`, arah Oldest First
28. Verifikasi urutan card `Version 2` lalu `Version 3`
29. Ketuk `[⋯]` toolbar → Sort, pilih opsi `Default`
30. Verifikasi urutan card `Version 3` lalu `Version 2` (Published At Newest First)
31. Buka lagi bottom sheet lewat `[⋯]` → Sort
32. Verifikasi `Default` ditandai aktif
33. Verifikasi pilihan Sort lain tidak ditandai

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Spec Android: `coverage.mobile: automated` tanpa `coverage.web`. TC Android memakai TC universal; hanya aturan yang berbeda dari web (Download tanpa Column Visibility dan Sort lewat bottom sheet) ditulis di spec ini.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 17, 19, 25, dan 31 (membuka/menutup bottom sheet dan memuat ulang halaman untuk mengamati penanda pilihan sort yang aktif). TC hanya menyebut "amati penanda pilihan" tanpa menyatakan bahwa bottom sheet menutup setelah pilihan; spec membukanya lagi secara eksplisit sebelum mengasersi penanda.
- Urutan TC mengikuti TC sumber (TC-AC-PP-192 lalu TC-AC-PP-208); TC-AC-PP-192 berjalan tanpa Search aktif sehingga file unduhan memuat seluruh Riwayat A.
- Urutan di dalam TC-AC-PP-192 menyimpang dari TC: TC menyuruh memilih Download as CSV lebih dulu lalu memeriksa menu toolbar untuk Column Visibility; spec memeriksa isi bottom sheet (langkah 3 dan 4) sebelum memilih Download (langkah 5) karena bottom sheet sedang terbuka dan tertutup sesudah pilihan, sehingga pemeriksaan harus dilakukan lebih dulu.
- Temuan untuk QA:
  - TC-AC-PP-192 langkah 1 menulis "pilih Download as CSV" setelah bottom sheet tanpa merinci apakah ada submenu format; spec mengikuti kalimat TC.
  - Expected e TC-AC-PP-208 memuat dua urutan (setelah `Published At` Oldest First dan setelah `Default`) pada langkah 5 yang sama dengan "amati card dan penanda"; spec memisahkan menjadi pengamatan di langkah 28 (setelah Oldest First) dan langkah 30 (setelah `Default`).
  - Post Condition TC ("tidak ada perubahan data") tidak punya langkah observasi sendiri dan tidak diasersi.
