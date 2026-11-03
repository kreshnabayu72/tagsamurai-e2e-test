---
id: TC-AC-LA-E2E-099-filter-list-screening-dan-opsi
title: "Filter List: Screening Panel, Opsi Status, Opsi DISTINCT, dan Number Range"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-291
  - TC-AC-LA-293
  - TC-AC-LA-294
  - TC-AC-LA-295
coverage:
  web: automated
---

# Filter List: Screening Panel, Opsi Status, Opsi DISTINCT, dan Number Range

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab; Quantity `+2`, `+5`, `+10`, `+50 GB`, `—`; Cost `$100.00`, `$150.00`, `$480.00`, `$3,650.00`, `—`) bersifat baca-saja untuk spec ini. Himpunan nilai distinct Client dan License Type tab Current (butir TC-AC-LA-294) diturunkan dari seeding #54, bukan dibaca dari satu halaman tabel.
- Data Pre-setup TC-AC-LA-294: Client `Kafe Baru` = Pre-setup #31 (Client Active tanpa Client Subscription; tidak muncul di dropdown Client). Langkah 24 sampai 26 (membuat alokasi untuk `Kafe Baru` lewat sesi API aktor, token tidak dihitung sebagai sesi web; lihat `suite.md`, lalu memeriksa Client itu muncul sebagai opsi) DITAHAN: Client tanpa Client Subscription tidak dapat menerima alokasi (TC-AC-LA-449), sehingga langkah 24 tidak dapat berjalan sampai TC-AC-LA-294 d direvisi agar menunjuk Client ber-Subscription tanpa alokasi. Langkah 24 sampai 26 dipertahankan hanya demi pemetaan Expected c; jangan dieksekusi.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column (menampilkan `Cost`). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-291: Screening Filter Panel

1. Klik ikon Filter
2. Verifikasi ikon Filter menjadi gelap saat panel terbuka
3. Verifikasi field berurutan: `License Type` (multi-select searchable, `All types`), `Product` (`All products`), `Client` (`All clients`), `Subscription ID` (`All subscription IDs`), `Plan` (`All plans`), `Quantity` (Min dan Max), `Plan Owner` (`All owners`), `Allocated By` (`All users`), `Paid From` (`All sources`), `Cost` (Min dan Max), `Status` (`All statuses`), `Last Updated` (date range picker, `Select date`)
4. Verifikasi maksimum 4 field per baris
5. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan
6. Verifikasi tidak ada field Allocation ID maupun Payment

### TC-AC-LA-293: Opsi Status DISTINCT per tab

7. Buka dropdown Status
8. Verifikasi opsi hanya status yang ada pada baris tab Current: `Waiting for Approval`, `Pending`, `Active`
9. Verifikasi tidak ada status milik tab lain (`Expired`, `Rejected`, `Canceled`)
10. Klik ikon Filter
11. Klik tab `History`
12. Klik ikon Filter
13. Buka dropdown Status
14. Verifikasi opsi hanya status yang ada pada baris tab History: `Expired`, `Rejected`, `Canceled`
15. Verifikasi tidak ada status milik tab lain (`Waiting for Approval`, `Pending`, `Active`)

### TC-AC-LA-294: Opsi dropdown DISTINCT dari data tabel

16. Klik ikon Filter
17. Klik tab `Current`
18. Klik ikon Filter
19. Buka dropdown Client
20. Verifikasi opsi Client hanya Client yang muncul pada baris tabel tab Current
21. Verifikasi Client `Kafe Baru` tidak muncul sebagai opsi
22. Buka dropdown License Type
23. Verifikasi opsi License Type hanya License Type yang muncul pada baris tabel tab Current
24. Buat alokasi baru untuk Client `Kafe Baru` lewat sesi API hingga alokasi tersimpan
25. Buka dropdown Client tanpa memuat ulang halaman
26. Verifikasi Client `Kafe Baru` muncul sebagai opsi

### TC-AC-LA-295: Number range Quantity dan Cost

27. Tekan `Esc` untuk menutup dropdown
28. Verifikasi placeholder input Quantity `Min` dan `Max`
29. Isi Quantity Min `5` dan Max `10`
30. Klik `[Apply]`
31. Verifikasi sedikitnya satu baris tampil
32. Verifikasi hasil memuat nilai Quantity 5 sampai 10 inklusif
33. Klik ikon Filter
34. Kosongkan Quantity Max
35. Klik `[Apply]`
36. Verifikasi hasil dengan hanya Min memuat nilai Quantity 5 ke atas
37. Klik ikon Filter
38. Klik `[Clear Field]` lalu `[Apply]`
39. Klik `⋯` pada header kolom Actions
40. Klik `Setup Column...`
41. Centang `Cost`
42. Klik `[Save]`
43. Klik ikon Filter
44. Verifikasi placeholder input Cost `Min` dan `Max`
45. Isi Cost Min `100` dan Max `150`
46. Klik `[Apply]`
47. Verifikasi sedikitnya satu baris tampil
48. Verifikasi hasil memuat nilai Cost 100 sampai 150 inklusif
49. Verifikasi baris Cost `—` tidak tampil
50. Klik ikon Filter
51. Klik `[Clear Field]` lalu `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-292 ada di spec 120 dan TC-AC-LA-296 serta TC-AC-LA-297 ada di spec 100.
- Langkah penghubung (S-03): langkah 10, 12, 16, 17, 18 (menutup dan membuka panel serta berpindah tab), langkah 27 (menutup dropdown), langkah 38 dan 51 (membersihkan filter), langkah 39 sampai 42 (menampilkan kolom Cost agar hasil Cost dapat diperiksa).
- Alasan spec melewati sekitar 35 langkah: semua blok satu kelas harness (fungsional) dan satu dataset (#54, baca-saja); tiap blok berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-LA-294 langkah 2 ("Buat alokasi baru dengan Client yang belum ada pada tabel") tidak menyebut cara, akun, Product, License Type, status akhir, dan pemulihan alokasi; modul tidak punya aksi hapus alokasi. Spec memakai sesi API aktor dan mekanismenya "disediakan tim FE" tanpa endpoint (S-13). Client `Kafe Baru` adalah Pre-setup #31 (Client Active tanpa Client Subscription), sehingga tidak dapat diberi alokasi (TC-AC-LA-449): langkah 24 sampai 26 ditahan sampai TC-AC-LA-294 d direvisi agar menunjuk Client ber-Subscription tanpa alokasi. Butuh keputusan QA.
  - TC-AC-LA-295 Expected c memeriksa nilai Cost sedangkan kolom Cost tersembunyi secara default; TC tidak menyebut langkah menampilkannya, spec menambah langkah penghubung 39 sampai 42.
  - TC-AC-LA-293 tidak menyebut apakah Filter Panel bertahan saat berpindah tab; spec menutup panel sebelum pindah tab dan membukanya lagi.
