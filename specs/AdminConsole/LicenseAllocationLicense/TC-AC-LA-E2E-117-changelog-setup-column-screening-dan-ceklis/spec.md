---
id: TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis
title: "Modal Changelog Setup Column: Screening, Ceklis, Reset, Guard, dan Cache"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-373
  - TC-AC-LA-374
  - TC-AC-LA-375
  - TC-AC-LA-376
  - TC-AC-LA-377
  - TC-AC-LA-378
coverage:
  web: automated
---

# Modal Changelog Setup Column: Screening, Ceklis, Reset, Guard, dan Cache

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status dan 25 entri Changelog) bersifat baca-saja untuk spec ini; spec tidak menulis data alokasi.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column Changelog. Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-373: Screening overlay Column Visibility Changelog

1. Klik ikon Changelog
2. Klik `⋯` pada header kolom Actions Changelog
3. Verifikasi ketujuh kolom `Date`, `Action`, `Allocation ID`, `Field`, `Old Value`, `New Value`, dan `Modified By` tercentang dan enabled
4. Verifikasi item `Setup Column...` tersedia

### TC-AC-LA-374: Screening Popup Setup Column Changelog

5. Klik `Setup Column...`
6. Verifikasi Header: judul `Setup Column`
7. Verifikasi Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
8. Verifikasi Header: tombol silang `(X)`
9. Verifikasi Body: tujuh kolom tampil
10. Verifikasi checkbox tersedia pada tiap kolom
11. Verifikasi drag handle tersedia pada tiap kolom
12. Verifikasi ikon Pin tersedia pada tiap kolom
13. Verifikasi Live Preview tampil
14. Verifikasi Footer: `[Reset to Default]` dan `[Save]`
15. Verifikasi tidak ada `[Cancel]`

### TC-AC-LA-375: Ceklis dan unceklis kolom Hideable Changelog

16. Hapus centang `Date`, `Action`, dan `Allocation ID`
17. Klik `[Save]`
18. Verifikasi ketiga kolom itu hilang dari tabel
19. Muat ulang halaman (F5)
20. Klik ikon Changelog
21. Verifikasi `Date`, `Action`, dan `Allocation ID` tetap tersembunyi
22. Buka Popup Setup Column
23. Centang kembali `Date`, `Action`, dan `Allocation ID`
24. Hapus centang `Field`, `Old Value`, `New Value`, dan `Modified By`
25. Klik `[Save]`
26. Verifikasi `Date`, `Action`, dan `Allocation ID` tampil lagi di tabel
27. Verifikasi `Field`, `Old Value`, `New Value`, dan `Modified By` hilang dari tabel
28. Muat ulang halaman (F5)
29. Klik ikon Changelog
30. Verifikasi `Field`, `Old Value`, `New Value`, dan `Modified By` tetap tersembunyi
31. Buka Popup Setup Column
32. Centang kembali `Field`, `Old Value`, `New Value`, dan `Modified By`
33. Klik `[Save]`
34. Verifikasi `Field`, `Old Value`, `New Value`, dan `Modified By` tampil lagi di tabel

### TC-AC-LA-376: Reset to Default dan discard

35. Buka Popup Setup Column
36. Hapus centang `Field`
37. Klik `(X)`
38. Verifikasi perubahan dibuang: kolom `Field` tampil di tabel
39. Buka Popup Setup Column
40. Hapus centang `Field`
41. Klik `[Reset to Default]`
42. Klik `[Save]`
43. Verifikasi tabel kembali ke konfigurasi default (ketujuh kolom tampil, tanpa pin)

### TC-AC-LA-377: Guard satu kolom tersisa dan pin keempat

44. Klik `⋯` pada header kolom Actions Changelog
45. Hapus centang semua kolom kecuali `Date` di overlay
46. Hover checkbox `Date`
47. Verifikasi tooltip `At least one column must remain visible.`
48. Centang kembali kolom lain yang dihapus centangnya pada langkah 45
49. Tekan `Esc` untuk menutup overlay
50. Buka Popup Setup Column
51. Klik ikon Pin pada `Date`, `Action`, dan `Allocation ID`
52. Hover ikon Pin kolom `Field`
53. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
54. Klik `(X)`

### TC-AC-LA-378: Cache Changelog independen dari List

55. Buka Popup Setup Column
56. Hapus centang `Field`
57. Klik `[Save]`
58. Klik `[×]` pada Modal Changelog
59. Verifikasi kolom List tidak berubah: sepuluh kolom Hideable `Allocation ID`, `License Type`, `Product`, `Client`, `Subscription ID`, `Quantity`, `Plan Owner`, `Allocated By`, `Status`, dan `Last Updated` tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-489 dan TC-AC-LA-490 (drag dan pin Changelog) ada di spec 118.
- Langkah `Buka Popup Setup Column` berarti: klik `⋯` pada header kolom Actions Changelog, lalu klik `Setup Column...`. Popup dari TC-AC-LA-374 (langkah 5) tetap terbuka sebagai awal TC-AC-LA-375 (langkah 16).
- Langkah 16, 23, 24, 32 menangani beberapa kolom sekaligus; `Verifikasi` yang menyebut kolom-kolom itu adalah daftar elemen yang disebut utuh dan sama-sama hilang atau tampil (S-01, daftar elemen).
- Langkah penghubung (S-03): langkah 20 dan 29 (membuka Modal Changelog lagi sesudah muat ulang halaman menutupnya), langkah 48 dan 49 (memulihkan dan menutup overlay), langkah 54 dan 58 (menutup Popup dan modal).
- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (Setup Column Modal Changelog) pada satu dataset baca-saja; tiap blok memulihkan konfigurasi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-LA-374 menyebut "deskripsi" tanpa teks; spec memakai teks deskripsi Popup Setup Column List (TC-AC-LA-321).
  - TC-AC-LA-376 langkah 1 dan 2 ("Ubah konfigurasi") tidak menyebut kolom yang diubah; spec memakai kolom `Field`.
  - TC-AC-LA-377 tidak menyebut kolom yang disisakan dan yang dipin; spec memakai `Date` (disisakan) serta `Date`, `Action`, `Allocation ID` (dipin).
  - TC-AC-LA-378 Expected ("Kolom List tidak berubah") tidak menyebut baseline kolom List; spec mengasersi sepuluh kolom Hideable default tampil.
