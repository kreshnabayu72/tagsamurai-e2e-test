---
id: TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi
title: "Setup Column List: Guard Satu Kolom, Guard Pin Keempat, Konfigurasi Antar Tab, dan Cache Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-329
  - TC-AC-LA-330
  - TC-AC-LA-331
  - TC-AC-LA-332
  - TC-AC-LA-333
  - TC-AC-LA-334
coverage:
  web: automated
---

# Setup Column List: Guard Satu Kolom, Guard Pin Keempat, Konfigurasi Antar Tab, dan Cache Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab dan 25 entri Changelog) bersifat baca-saja untuk spec ini; spec tidak menulis data alokasi.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column. Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-329: Guard satu kolom tersisa

1. Klik `⋯` pada header kolom Actions
2. Hapus centang semua kolom kecuali `Allocation ID` di overlay Column Visibility
3. Hover checkbox `Allocation ID`
4. Verifikasi checkbox `Allocation ID` disabled dengan tooltip `At least one column must remain visible.`
5. Centang `License Type`
6. Verifikasi checkbox `Allocation ID` kembali enabled
7. Centang kembali kolom lain yang dihapus centangnya pada langkah 2
8. Tekan `Esc` untuk menutup overlay

### TC-AC-LA-330: Guard pin keempat

9. Buka Popup Setup Column
10. Klik ikon Pin pada `Allocation ID`, `License Type`, dan `Product`
11. Hover ikon Pin kolom `Client`
12. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
13. Klik ikon Pin pada `Product` untuk Unpin
14. Verifikasi icon Pin kolom `Client` aktif kembali
15. Klik `(X)`

### TC-AC-LA-331: Overlay menerapkan perubahan langsung

16. Klik `⋯` pada header kolom Actions
17. Hapus centang `Product` di overlay
18. Geser `Status` ke posisi pertama di overlay
19. Tekan `Esc` untuk menutup overlay
20. Verifikasi tabel langsung menerapkan perubahan: kolom `Product` hilang dan `Status` berada di posisi pertama
21. Muat ulang halaman (F5)
22. Verifikasi perubahan tersimpan tanpa tombol Save: kolom `Product` tetap hilang dan `Status` tetap di posisi pertama
23. Klik `⋯` pada header kolom Actions
24. Centang `Product` di overlay
25. Tekan `Esc` untuk menutup overlay

### TC-AC-LA-332: Konfigurasi dibagi antara tab Current dan History

26. Buka Popup Setup Column
27. Hapus centang `Client`
28. Klik ikon Pin pada `Allocation ID`
29. Klik `[Save]`
30. Klik tab `History`
31. Verifikasi tab History menampilkan kolom `Client` tersembunyi
32. Verifikasi tab History menampilkan `Allocation ID` ter-pin
33. Buka Popup Setup Column
34. Klik `[Reset to Default]`
35. Klik `[Save]`
36. Verifikasi tab History kembali ke konfigurasi default (kolom `Client` tampil, tanpa pin)
37. Klik tab `Current`
38. Verifikasi tab Current kembali ke konfigurasi default (kolom `Client` tampil, tanpa pin)

### TC-AC-LA-333: Cache Modal Changelog independen

39. Buka Popup Setup Column
40. Hapus centang `Client`
41. Klik `[Save]`
42. Klik ikon Changelog
43. Verifikasi kolom Modal Changelog tidak berubah: `Date`, `Action`, `Allocation ID`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil
44. Klik `[✕]` pada Modal Changelog

### TC-AC-LA-334: Maksimum kolom tampil

45. Buka Popup Setup Column
46. Centang seluruh 14 kolom
47. Verifikasi semua checkbox tetap enabled
48. Hover checkbox kolom terakhir
49. Verifikasi tooltip `Maximum {limit} columns can be shown at once.` tidak tampil
50. Klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah `Buka Popup Setup Column` berarti: klik `⋯` pada header kolom Actions, lalu klik `Setup Column...`.
- Langkah penghubung (S-03): langkah 7, 8, 19, 23 sampai 25 (memulihkan dan menutup overlay), langkah 15 (menutup Popup tanpa Save), langkah 44 (menutup modal).
- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (konfigurasi Setup Column List) pada satu dataset baca-saja; tiap blok memulihkan konfigurasi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-LA-329 langkah 1 tidak menyebut kolom yang disisakan; spec menyisakan `Allocation ID`.
  - TC-AC-LA-330 Expected a ("Icon Pin kolom lain disabled") dan langkah 2 tidak menyebut tiga kolom yang dipin; spec memakai `Allocation ID`, `License Type`, `Product`.
  - TC-AC-LA-331 Expected ("tersimpan tanpa tombol Save") tidak menyebut cara membuktikan; spec memakai muat ulang halaman (langkah 21) sebagai langkah observasi.
  - TC-AC-LA-332 Expected b (`[Reset to Default]` untuk kedua tab) tidak menyebut tab asal reset; spec mereset dari tab History dan mengasersi kedua tab.
  - TC-AC-LA-334 menyebut teks tooltip `Maximum {limit} columns can be shown at once.` dengan placeholder `{limit}`; spec mengasersi ketidakhadirannya, dengan checkbox enabled (langkah 47) sebagai anchor.
