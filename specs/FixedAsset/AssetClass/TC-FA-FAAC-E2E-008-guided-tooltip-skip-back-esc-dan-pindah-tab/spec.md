---
id: TC-FA-FAAC-E2E-008-guided-tooltip-skip-back-esc-dan-pindah-tab
title: "Guided Tooltip Tab Asset Class: Back, Skip, Klik Overlay, Esc Menyimpan Flag, dan Pindah Halaman Tidak Menyimpan Flag"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-51
  - TC-FA-FAAC-49
  - TC-FA-FAAC-50
  - TC-FA-FAAC-54
  - TC-FA-FAAC-55
coverage:
  web: automated
---

# Guided Tooltip Tab Asset Class: Back, Skip, Klik Overlay, Esc Menyimpan Flag, dan Pindah Halaman Tidak Menyimpan Flag

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini. Pengecualian atas hook `beforeEach` dan hook suite: spec Guided Tooltip menguji kunjungan pertama dan membuka layarnya sendiri lewat sidebar; hook suite tidak menyetel flag `guided_tooltip_seen_fa-asset-class` true untuk spec ini, dan spec mengaturnya per blok. Hook `after` memulihkan flag ke nilai awal dan mengembalikan sesi ke akun default suite.
- Kemampuan teknis: mengatur dan memulihkan flag `guided_tooltip_seen_fa-asset-class` untuk akun Total Control; disediakan tim FE/BE (lihat `suite.md`).
- Jeda "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 18, 29, dan 40) adalah pilihan spec sebagai jendela asersi absence, bukan nilai TC atau PRD.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah flag Guided Tooltip akun aktor.

## Test Steps

### TC-FA-FAAC-51: Tombol Back kembali ke step sebelumnya

1. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
2. Klik menu Accounting di sidebar
3. Klik tab Asset Class
4. Klik `[Next]` sekali hingga Step 2 of 8
5. Verifikasi tombol `[Back]` tampil pada Step 2
6. Klik `[Back]`
7. Verifikasi tooltip kembali ke `Step 1 of 8` dengan Title `Set Up in Order`
8. Verifikasi tombol `[Back]` Hidden pada Step 1

### TC-FA-FAAC-49: Klik Skip pada tengah walkthrough

9. Klik menu Dashboard di sidebar
10. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
11. Klik menu Accounting di sidebar
12. Klik tab Asset Class
13. Klik `[Next]` dua kali hingga Step 3
14. Klik link `[Skip]`
15. Verifikasi walkthrough tertutup
16. Refresh halaman
17. Klik tab Asset Class
18. Tunggu 5 detik tanpa memuat ulang halaman
19. Verifikasi tab `Asset Class` aktif dengan tabel Asset Class tampil
20. Verifikasi walkthrough tidak muncul lagi

### TC-FA-FAAC-50: Klik overlay gelap memperlakukan walkthrough sebagai Skip

21. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
22. Klik menu Accounting di sidebar
23. Klik tab Asset Class
24. Klik area overlay gelap di luar spotlight
25. Verifikasi walkthrough tertutup
26. Klik menu Dashboard di sidebar
27. Klik menu Accounting di sidebar
28. Klik tab Asset Class
29. Tunggu 5 detik tanpa memuat ulang halaman
30. Verifikasi tab `Asset Class` aktif dengan tabel Asset Class tampil
31. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-FA-FAAC-54: Tombol Esc menutup walkthrough seperti Skip

32. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
33. Klik menu Accounting di sidebar
34. Klik tab Asset Class
35. Tekan Esc
36. Verifikasi walkthrough tertutup
37. Klik menu Dashboard di sidebar
38. Klik menu Accounting di sidebar
39. Klik tab Asset Class
40. Tunggu 5 detik tanpa memuat ulang halaman
41. Verifikasi tab `Asset Class` aktif dengan tabel Asset Class tampil
42. Verifikasi walkthrough tidak muncul otomatis lagi (flag seen tersimpan)

### TC-FA-FAAC-55: Pindah halaman saat walkthrough berjalan tidak menyimpan flag seen

43. Atur flag `guided_tooltip_seen_fa-asset-class` belum tersimpan untuk akun Total Control
44. Klik menu Accounting di sidebar
45. Klik tab Asset Class
46. Klik menu Dashboard di sidebar saat walkthrough berjalan
47. Verifikasi walkthrough tertutup saat halaman Dashboard tampil
48. Klik menu Accounting di sidebar
49. Klik tab Asset Class
50. Verifikasi walkthrough muncul lagi dari `Step 1 of 8`

## Notes

- Spec melewati sekitar 35 langkah (50 langkah): kelima blok adalah satu kelas (Guided Tooltip fungsional) pada layar dan dataset yang sama, tiap blok memulai walkthrough sendiri dari flag belum tersimpan, dan memisahnya hanya menggandakan login, hook, dan pemulihan flag. Penambahan langkah berasal dari pengaturan flag dan pembuktian kunjungan berikutnya per blok.
- Langkah penghubung (S-03): langkah 1, 10, 21, 32, dan 43 (mengatur flag belum tersimpan sebagai precondition tiap TC), langkah 9 (menutup walkthrough blok sebelumnya dengan pindah halaman), langkah 18, 29, dan 40 (jendela asersi absence), langkah 26 dan 27, 37 dan 38 (kunjungan berikutnya sesudah menyimpan flag).
- Urutan TC dalam spec: 51, 49, 50, 54, 55. Blok yang menyimpan flag diikuti pembuktian lewat kunjungan berikutnya; TC-FA-FAAC-55 di akhir karena flag tetap belum tersimpan.
- Anchor absence (langkah 20, 31, 42): langkah 19, 30, dan 41 membuktikan halaman sudah termuat sebelum absence walkthrough diasersi (8b butir 2, R-21).
- Temuan untuk QA:
  - TC-FA-FAAC-50 dan TC-FA-FAAC-54 butir "flag seen tersimpan" tidak memberi langkah observasi; spec membuktikannya lewat kunjungan berikutnya (langkah 26 sampai 31 dan 37 sampai 42).
  - TC-FA-FAAC-55 butir a berbunyi "tertutup saat berpindah halaman"; spec memakai menu Dashboard sebagai tujuan sesuai langkah 2 TC.
