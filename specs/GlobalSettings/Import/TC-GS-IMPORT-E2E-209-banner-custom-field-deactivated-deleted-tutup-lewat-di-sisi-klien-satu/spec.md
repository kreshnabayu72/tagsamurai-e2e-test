---
id: TC-GS-IMPORT-E2E-209-banner-custom-field-deactivated-deleted-tutup-lewat-di-sisi-klien-satu
title: "Banner Custom Field (Deactivated, Deleted): tutup lewat [×] di sisi klien, satu banner per field, kondisi tampil, label terakhir pada rename lalu hapus"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-955
  - TC-GS-IMPORT-956
  - TC-GS-IMPORT-957
  - TC-GS-IMPORT-961
  - TC-GS-IMPORT-962
coverage:
  web: automated
---

# Banner Custom Field (Deactivated, Deleted): tutup lewat [×] di sisi klien, satu banner per field, kondisi tampil, label terakhir pada rename lalu hapus

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client A (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD` (nama env baru). Sesi API menonaktifkan, mengganti nama, dan menghapus Custom Field di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-05: draft User Login 8 baris `pending` dari `user-login-8.csv` pada Client A (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong pada Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4; Custom Field Active `Shift Notes` Optional dan kosong pada seluruh baris), disiapkan lewat skrip seed dan dibuat ulang sebelum tiap TC (Kontrak Fixture R2).
- Custom Field Client A (Pre-setup, Optional, Active): Shift, Shift Notes, Overtime Hours (Numeric 2 desimal), Emergency Phone, Join Date. Nama literal dipakai (pengecualian S-12 butir (ii): nama field menentukan teks Banner). Nama sementara `Extra Hours` (TC-GS-IMPORT-961 dan 962) literal karena teks Banner diasersi.
- Urutan TC: 955, 956, 957, 961, 962 (961 dan 962 menghapus Custom Field `Overtime Hours` paling akhir). Pemulihan Custom Field dan draft D-05 dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): `Shift` dan `Shift Notes` diaktifkan kembali; `Overtime Hours` dikembalikan namanya atau dibuat ulang (Numeric, Decimal Places 2, Optional, Active); draft User Login Client A dipulihkan ke D-05.
- Kemampuan teknis: skrip seed D-05; sesi API Admin kedua.
- State global: Custom Field Client A (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Banner ditutup di sisi klien (TC-GS-IMPORT-955)

1. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
2. Tekan `F5` pada halaman Import
3. Verifikasi Banner Custom Field (severity warning) tampil di atas Staging Metric Cards
4. Verifikasi Banner Custom Field hanya memuat tombol `[×]`, tanpa tombol aksi lain
5. Klik `[×]` pada Banner Custom Field
6. Verifikasi banner tertutup
7. Verifikasi tidak ada dialog maupun toast
8. Verifikasi Staging Table dan Staging Metric Cards tidak berubah
9. Tekan `F5` pada halaman Import
10. Verifikasi banner tampil lagi
11. Klik `[×]` pada Banner Custom Field
12. Klik Sub-Tab User Non Login lalu Sub-Tab User Login
13. Verifikasi banner tampil lagi pada Sub-Tab User Login
14. Pulihkan: Admin kedua mengaktifkan kembali `Shift`, buat ulang draft D-05, muat ulang halaman

### Dua Custom Field, satu banner per field (TC-GS-IMPORT-956)

15. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` dan menghapus Custom Field `Overtime Hours` hingga tersimpan
16. Tekan `F5` pada halaman Import
17. Verifikasi tampil dua Banner Custom Field terpisah, masing-masing dengan tombol `[×]`
18. Verifikasi banner "Shift is deactivated. Its values stay hidden on users until it is activated." tampil dengan severity warning
19. Verifikasi banner "Overtime Hours has been deleted. Its values will not be imported." tampil dengan severity warning
20. Verifikasi header memuat kolom Shift
21. Verifikasi header tidak memuat kolom Overtime Hours
22. Verifikasi seluruh 8 baris berstatus `pending`
23. Verifikasi Staging Metric Cards: Ready to Import 8, Errors 0
24. Klik `[×]` pada banner Shift
25. Verifikasi hanya banner Overtime Hours yang tampil
26. Tekan `F5` pada halaman Import
27. Verifikasi kedua banner tampil lagi
28. Pulihkan: Admin kedua mengaktifkan kembali `Shift`, membuat ulang `Overtime Hours` (Numeric, Decimal Places 2, Optional, Active), buat ulang draft D-05, muat ulang halaman

### Banner hanya untuk field bernilai tersimpan dan hanya di Tab User (TC-GS-IMPORT-957)

29. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift Notes` hingga tersimpan
30. Tekan `F5` pada halaman Import > User Login
31. Verifikasi Staging Metric Cards: Ready to Import 8, Errors 0
32. Verifikasi header tidak memuat kolom Shift Notes
33. Verifikasi tidak ada Banner Custom Field (tidak ada nilai tersimpan)
34. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
35. Tekan `F5` pada halaman Import > User Login
36. Verifikasi hanya satu banner yang tampil, yaitu untuk Shift
37. Verifikasi tidak ada banner untuk Shift Notes
38. Klik Sub-Tab Brand
39. Verifikasi Breadcrumb `Import > Brand`
40. Verifikasi tidak ada Banner Custom Field pada Sub-Tab Brand
41. Pulihkan: Admin kedua mengaktifkan kembali `Shift` dan `Shift Notes`, buat ulang draft D-05, muat ulang halaman Import > User Login

### Rename lalu hapus, dengan pembacaan di antaranya (TC-GS-IMPORT-961)

42. Admin kedua Client A (sesi API) mengganti nama Custom Field `Overtime Hours` menjadi `Extra Hours` hingga tersimpan
43. Tekan `F5` pada halaman Import
44. Verifikasi header memuat kolom `Extra Hours`
45. Verifikasi header tidak memuat `Overtime Hours`
46. Admin kedua Client A (sesi API) menghapus Custom Field `Extra Hours` hingga tersimpan
47. Tekan `F5` pada halaman Import
48. Verifikasi header tidak memuat kolom `Extra Hours`
49. Verifikasi header tidak memuat kolom `Overtime Hours`
50. Verifikasi tampil satu Banner Custom Field (severity warning, hanya tombol `[×]`) dengan teks "Extra Hours has been deleted. Its values will not be imported."
51. Verifikasi tidak ada banner yang menyebut `Overtime Hours`
52. Verifikasi seluruh 8 baris berstatus `pending`
53. Verifikasi Staging Metric Cards: Ready to Import 8, Errors 0
54. Pulihkan: Admin kedua membuat ulang `Overtime Hours` (Numeric, Decimal Places 2, Optional, Active), buat ulang draft D-05, muat ulang halaman

### Rename lalu hapus tanpa pembacaan di antaranya (TC-GS-IMPORT-962)

55. Admin kedua Client A (sesi API) mengganti nama Custom Field `Overtime Hours` menjadi `Extra Hours` hingga tersimpan
56. Admin kedua Client A (sesi API) menghapus Custom Field `Extra Hours` hingga tersimpan, tanpa ada yang memuat Staging Table di antara langkah 55 dan 56
57. Total Control: tekan `F5` pada halaman Import > User Login
58. Verifikasi tampil satu Banner Custom Field (severity warning) dengan teks "Overtime Hours has been deleted. Its values will not be imported." (label terakhir yang tercatat di draft), bukan "Extra Hours has been deleted..."
59. Verifikasi header tidak memuat kolom `Overtime Hours`
60. Verifikasi header tidak memuat kolom `Extra Hours`
61. Verifikasi seluruh 8 baris berstatus `pending`
62. Verifikasi Staging Metric Cards: Ready to Import 8, Errors 0
63. Pulihkan: Admin kedua membuat ulang `Overtime Hours` (Numeric, Decimal Places 2, Optional, Active), buat ulang draft D-05

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 63 langkah, di atas 35 langkah. Alasan: lima blok berpola sama (mutasi Custom Field lewat sesi API, F5, baca banner dan header Staging Table User Login) pada satu Sub-Tab dan satu dataset D-05; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 14, 28, 41, 54, 63).
- P-2: Admin kedua hanya memicu perubahan Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 14, 28, 41, 54, dan 63 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- Langkah 31 (Staging Metric Cards) dan langkah 39 (Breadcrumb `Import > Brand`) adalah anchor positif untuk asersi absence berikutnya (langkah 32 dan 33; langkah 40) (bagian 8b butir 2, S-03).
- TC-GS-IMPORT-961 dan 962 menghapus Custom Field `Overtime Hours` dan diletakkan paling akhir.
- Temuan untuk QA:
  - TC-GS-IMPORT-962 Precondition d mensyaratkan Total Control membuka Import > User Login tanpa memuat ulang sampai `F5` pada langkah 3; hook `beforeEach` membuka halaman itu sebelum langkah 55, dan `F5` pada langkah 57 adalah pemuatan pertama sesudah rename dan hapus.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
