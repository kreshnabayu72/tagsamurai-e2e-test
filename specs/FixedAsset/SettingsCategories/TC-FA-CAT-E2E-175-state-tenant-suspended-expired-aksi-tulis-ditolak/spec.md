---
id: TC-FA-CAT-E2E-175-state-tenant-suspended-expired-aksi-tulis-ditolak
title: "State Tenant Suspended dan Expired: Aksi Create, Add Subcategory, Edit, Delete, dan Bulk Delete Ditolak dengan Toast Baku"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-504
  - TC-FA-CAT-505
  - TC-FA-CAT-506
  - TC-FA-CAT-507
coverage:
  web: automated
---

# State Tenant Suspended dan Expired: Aksi Create, Add Subcategory, Edit, Delete, dan Bulk Delete Ditolak dengan Toast Baku

## Prerequisites

- Mode: FE+BE.
- Kelas harness h (state tenant: write-lockdown Client Suspended dan Expired).
- Akun login hook `before` spec ini: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatSuspended (Pre-setup #35, status Suspended, kategori `Susp A`, `Susp B`, `Susp C`), password dari `Spectra.env.FA_TC_PASSWORD`. Halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control CatMain). Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- State global yang diubah spec: status client CatSuspended diubah menjadi Expired pada langkah 52 lewat fixture backend (disediakan tim FE/BE; akun pelaku tidak tertulis di TC, PRD, atau LLD sehingga ditulis "disediakan tim FE", S-13). Hook `after` memulihkan status CatSuspended ke Suspended. Suite berjalan serial (`parallel: false`).
- Data Pre-setup #35 (`Susp A`, `Susp B`, `Susp C`) menjadi target aksi yang selalu ditolak server; spec hanya membaca dan tidak mengubahnya (S-06). Nama baru yang dikirim pada Create dan Add Subcategory bersuffix `{runId}-175` dan tidak pernah tersimpan: `Susp New {runId}-175` dan `Susp Sub {runId}-175`.
- Kemampuan teknis (disediakan tim FE/BE, S-13): pengamatan respons jaringan browser atas Submit, Save, dan Delete untuk membaca status 403; konfirmasi dialog `beforeunload` saat muat ulang (kemampuan dinyatakan di sini untuk S-08).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.

## Test Steps

### TC-FA-CAT-504: Create dan Add Subcategory pada entitas Suspended

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Susp New {runId}-175`
3. Klik `[Submit]`
4. Verifikasi server menolak Submit dengan 403 Forbidden
5. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
6. Verifikasi halaman tetap Fixed Asset > Settings > Categories tanpa redirect
7. Verifikasi tabel dan sidebar di-refresh dan data tidak berubah: `Susp A`, `Susp B`, dan `Susp C` tampil, `Susp New {runId}-175` tidak ada
8. Muat ulang halaman Categories
9. Klik elipsis (⋯) pada baris `Susp A` > `+ Add Subcategory`
10. Isi Category Name `Susp Sub {runId}-175`
11. Klik `[Submit]`
12. Verifikasi server menolak Submit dengan 403 Forbidden
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
14. Verifikasi halaman tetap Fixed Asset > Settings > Categories tanpa redirect
15. Verifikasi tabel dan sidebar di-refresh dan data tidak berubah: `Susp A`, `Susp B`, dan `Susp C` tampil, `Susp Sub {runId}-175` tidak ada
16. Muat ulang halaman Categories
17. Klik elipsis (⋯) pada baris `Susp A`
18. Verifikasi item `Detail` pada menu elipsis tersedia
19. Verifikasi ikon Changelog pada Table Tools tersedia
20. Tutup menu elipsis dengan `Esc`

### TC-FA-CAT-505: Edit pada entitas Suspended

21. Klik elipsis (⋯) pada baris `Susp A` > `Edit`
22. Ubah Description menjadi `Susp desc`
23. Klik `[Save]`
24. Verifikasi server menolak Save dengan 403 Forbidden
25. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
26. Verifikasi halaman tetap Fixed Asset > Settings > Categories tanpa redirect
27. Verifikasi tabel dan sidebar di-refresh dan data tidak berubah: Description `Susp A` tetap kosong
28. Muat ulang halaman Categories
29. Klik elipsis (⋯) pada baris `Susp A`
30. Verifikasi item `Detail` pada menu elipsis tersedia
31. Verifikasi ikon Changelog pada Table Tools tersedia
32. Tutup menu elipsis dengan `Esc`

### TC-FA-CAT-506: Delete dan Bulk Delete pada entitas Suspended

33. Klik elipsis (⋯) pada baris `Susp A` > `Delete`
34. Klik `[Delete]` pada dialog
35. Verifikasi server menolak Delete dengan 403 Forbidden
36. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
37. Verifikasi halaman tetap Fixed Asset > Settings > Categories tanpa redirect
38. Verifikasi tabel dan sidebar di-refresh dan data tidak berubah: `Susp A` masih tampil
39. Muat ulang halaman Categories
40. Centang baris `Susp B` dan `Susp C`
41. Klik Bulk Delete pada bulk bar
42. Klik `[Delete]` pada dialog
43. Verifikasi server menolak Bulk Delete dengan 403 Forbidden
44. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.`
45. Verifikasi halaman tetap Fixed Asset > Settings > Categories tanpa redirect
46. Verifikasi tabel dan sidebar di-refresh dan data tidak berubah: `Susp B` dan `Susp C` masih tampil
47. Muat ulang halaman Categories
48. Klik elipsis (⋯) pada baris `Susp A`
49. Verifikasi item `Detail` pada menu elipsis tersedia
50. Verifikasi ikon Changelog pada Table Tools tersedia
51. Tutup menu elipsis dengan `Esc`

### TC-FA-CAT-507: Aksi tulis pada entitas Expired

52. Ubah status client CatSuspended menjadi Expired lewat fixture backend hingga tersimpan
53. Muat ulang halaman Categories
54. Klik elipsis (⋯) pada baris `Susp A` > `Edit`
55. Ubah Description menjadi `Susp desc`
56. Klik `[Save]`
57. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` dengan copy yang sama seperti pada Suspended
58. Verifikasi tidak ada perubahan: Description `Susp A` tetap kosong

## Notes

- Spec melewati sekitar 35 langkah (58 langkah). Alasan: seluruh blok satu kelas harness (h) dan berdiri sendiri; tiap blok memulai dari data Pre-setup #35 yang tidak berubah (semua aksi ditolak) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pola aksi, 403, toast, tanpa redirect, data tidak berubah, dan aksi baca diulang per jenis aksi tulis.
- Langkah penghubung (S-03): langkah 8, 16, 28, 39, 47, 53 (muat ulang halaman supaya form atau dialog yang mungkin masih terbuka sesudah penolakan tidak terbawa; dialog `beforeunload` dikonfirmasi, kemampuan tertulis di Prerequisites), langkah 17 dan 20, 29 dan 32, 48 dan 51 (membuka dan menutup menu elipsis untuk mengamati aksi baca), langkah 40 (memilih baris untuk Bulk Delete), langkah 52 (pemicu state Expired).
- Asersi tabel dan sidebar tidak berubah pada langkah 7, 15, 27, 38, 46, 58 memakai toast hasil server yang sudah diasersi sebagai anchor (bagian 8b butir 2).
- `P-2` tidak dipakai: pemicu state Expired lewat fixture backend bukan konteks kedua.
- Temuan untuk QA:
  - TC-FA-CAT-504 sampai TC-FA-CAT-506 menulis "UI di-refresh tanpa redirect" tanpa menyebut keadaan popup form sesudah penolakan; spec menutupnya lewat muat ulang halaman.
  - TC-FA-CAT-504 sampai TC-FA-CAT-506 menyebut "aksi baca (Detail dan Changelog) tetap tersedia" tanpa langkah; spec mengamati ketersediaan item `Detail` dan ikon Changelog, tidak membuka kontennya. Nama item menu `Detail` mengikuti TC dan belum diverifikasi terhadap UI.
  - TC-FA-CAT-506 langkah Bulk Delete tidak menyebut dialog konfirmasi; spec menambahkan `[Delete]` pada dialog mengikuti pola Delete lain di TC-FA-CAT-580.
  - TC-FA-CAT-507 menyebut Pre-setup #35 "dengan status Expired" tanpa menyebut cara memicu status; spec memakai fixture backend disediakan tim FE/BE.
  - TC-FA-CAT-504 tidak menyebut isi Code dan Category Name untuk Create dan Add Subcategory; spec hanya mengisi Category Name bersuffix.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
