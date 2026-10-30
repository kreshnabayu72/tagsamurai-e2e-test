---
id: TC-GS-IMPORT-E2E-207-custom-field-required-yang-dinonaktifkan-atau-dihapus-tidak-dievaluasi
title: "Custom Field Required yang dinonaktifkan atau dihapus tidak dievaluasi; aktif kembali berlaku retroaktif"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-939
  - TC-GS-IMPORT-940
  - TC-GS-IMPORT-952
  - TC-GS-IMPORT-953
coverage:
  web: automated
---

# Custom Field Required yang dinonaktifkan atau dihapus tidak dievaluasi; aktif kembali berlaku retroaktif

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client A (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD` (nama env baru). Sesi API mengubah Required, status Active, dan menghapus Custom Field di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-05: draft User Login 8 baris `pending` dari `user-login-8.csv` pada Client A (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong pada Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4; Custom Field Active `Shift Notes` (Text Area) Optional dan kosong pada seluruh baris), disiapkan lewat skrip seed dan dibuat ulang sebelum tiap TC (Kontrak Fixture R2).
- Custom Field Client A (Pre-setup, Optional, Active): Shift (Dropdown Pagi/Siang/Malam), Shift Notes, Overtime Hours, Emergency Phone, Join Date. Nama literal dipakai (pengecualian S-12 butir (ii): nama field menentukan teks pesan error `Shift must not be empty`).
- Urutan TC: 939, 952, 953, 940 (hapus Custom Field `Shift Notes` paling akhir). Pemulihan Custom Field dan draft D-05 dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): `Shift` dan `Shift Notes` diaktifkan, dibuat ulang bila dihapus (Optional, Active; `Shift` Dropdown Pagi/Siang/Malam), draft User Login Client A dipulihkan ke D-05.
- Kemampuan teknis: skrip seed D-05; sesi API Admin kedua.
- State global: Custom Field Client A (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Shift Notes Required lalu dinonaktifkan (TC-GS-IMPORT-939)

1. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift Notes` Required hingga tersimpan
2. Tekan `F5` pada halaman Import
3. Verifikasi seluruh 8 baris berstatus `error`
4. Verifikasi Staging Metric Cards: Ready to Import 0, Errors 8
5. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift Notes` hingga tersimpan
6. Tekan `F5` pada halaman Import
7. Verifikasi kolom `Shift Notes` tidak tampil
8. Verifikasi tidak ada Banner Custom Field (tidak ada nilai tersimpan pada seluruh baris)
9. Verifikasi seluruh 8 baris berstatus `pending`
10. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0
11. Verifikasi Error Summary Callout tidak tampil
12. Pulihkan: Admin kedua mengaktifkan kembali `Shift Notes` dan mengembalikannya ke Optional, buat ulang draft D-05, muat ulang halaman

### Shift Required dinonaktifkan: Save berhasil (TC-GS-IMPORT-952)

13. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift` Required hingga tersimpan
14. Tekan `F5` pada halaman Import
15. Verifikasi Row # 4 sampai 8 berstatus `error`
16. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 3, Errors 5
17. Verifikasi Error Summary Callout memuat `Shift must not be empty` dengan badge "5 rows"
18. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
19. Tekan `F5` pada halaman Import
20. Verifikasi kolom Shift tampil tanpa lencana
21. Verifikasi Banner Custom Field Deactivated tampil
22. Verifikasi sel Shift Row # 4 sampai 8 kosong tanpa border `danger`
23. Verifikasi seluruh 8 baris berstatus `pending`
24. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0
25. Verifikasi Error Summary Callout tidak tampil
26. Klik row action `⋯` pada Row # 4 lalu Edit
27. Tambahkan `X` di akhir nilai Last Name pada Row # 4
28. Klik `[Save]`
29. Verifikasi muncul toast sukses: "Success, row has been updated." walau sel Shift Row # 4 kosong
30. Verifikasi Row # 4 berstatus `pending`
31. Pulihkan: Admin kedua mengaktifkan kembali `Shift` dan mengembalikannya ke Optional, buat ulang draft D-05, muat ulang halaman

### Aktif kembali, Required retroaktif (TC-GS-IMPORT-953)

32. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift` Required hingga tersimpan
33. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
34. Tekan `F5` pada halaman Import
35. Verifikasi seluruh 8 baris berstatus `pending`
36. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0
37. Verifikasi Banner Custom Field Deactivated tampil
38. Admin kedua Client A (sesi API) mengaktifkan kembali Custom Field `Shift` hingga tersimpan
39. Tekan `F5` pada halaman Import
40. Verifikasi Banner Custom Field tidak tampil
41. Verifikasi Row # 4 sampai 8 berstatus `error` dengan sel Shift kosong berborder `danger`
42. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 3, Errors 5
43. Verifikasi Error Summary Callout memuat `Shift must not be empty` dengan badge "5 rows"
44. Pulihkan: Admin kedua mengembalikan `Shift` ke Optional, buat ulang draft D-05, muat ulang halaman

### Shift Notes Required lalu dihapus (TC-GS-IMPORT-940)

45. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift Notes` Required hingga tersimpan
46. Tekan `F5` pada halaman Import
47. Verifikasi seluruh 8 baris berstatus `error`
48. Verifikasi Staging Metric Cards: Ready to Import 0, Errors 8
49. Admin kedua Client A (sesi API) menghapus Custom Field `Shift Notes` hingga tersimpan
50. Tekan `F5` pada halaman Import
51. Verifikasi kolom `Shift Notes` tidak tampil
52. Verifikasi tidak ada Banner Custom Field (tidak ada nilai tersimpan pada seluruh baris)
53. Verifikasi seluruh 8 baris berstatus `pending`
54. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0
55. Verifikasi Error Summary Callout tidak tampil
56. Pulihkan: Admin kedua membuat ulang Custom Field `Shift Notes` (Text Area, Optional, Active), buat ulang draft D-05

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 56 langkah, di atas 35 langkah. Alasan: empat blok berpola sama (mutasi Required/Active/hapus lewat sesi API, F5, baca Staging Table) pada satu Sub-Tab dan satu dataset D-05; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 12, 31, 44, 56).
- P-2: Admin kedua hanya memicu perubahan Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 12, 31, 44, dan 56 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- Urutan 939, 952, 953, 940 menempatkan penghapusan Custom Field (TC-940) paling akhir; nomor TC di sourceTc tetap.
- Temuan untuk QA:
  - TC-GS-IMPORT-939 dan 940 Expected b menyebut "tidak ada Banner Custom Field karena tidak ada nilai tersimpan"; alasan sebab-akibat tidak diasersi, hanya ketiadaan banner (didahului kolom `Shift Notes` tidak tampil dan 8 baris `pending`).
  - TC-GS-IMPORT-953 langkah 1-2 menjalankan dua perubahan berurutan tanpa F5 di antaranya; spec mengikuti urutan itu.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
