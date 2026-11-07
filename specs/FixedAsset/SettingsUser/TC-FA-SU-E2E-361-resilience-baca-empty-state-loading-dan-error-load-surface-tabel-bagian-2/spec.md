---
id: TC-FA-SU-E2E-361-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-2
title: "Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-469
  - TC-FA-SU-500
  - TC-FA-SU-536
coverage:
  web: automated
---

# Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada pembacaan data, resilience baca). Data Pre-setup: Client `FaUserMain` (#20), Responsibilities (#24), Responsibilities (#25). Pengguna tanpa data pada surface Detail: Hana Kusuma (Pending Activation) dari Client `FaUserMain`.
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP data surface di atas backend nyata (ditahan lambat, lalu respons 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan, sehingga spec lain tidak terpengaruh. Keyword Search tanpa hasil `zzzz` dipilih spec. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept.

## Test Steps

### TC-FA-SU-469: Empty state, hasil pencarian kosong, loading, dan error load Sub-tab Assigned Assets

1. Ketik Search `Hana Kusuma`, tekan Enter, lalu buka Detail Hana Kusuma > Tab Responsibilities > Sub-tab Assigned Assets
2. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No assigned assets` dan Description `This user has no assigned assets currently.`
3. Ketik Search `zzzz`, tekan Enter
4. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
5. Atur intercept respons data Sub-tab Assigned Assets menjadi lambat (ditahan)
6. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Assigned Assets
7. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
8. Ganti intercept respons data Sub-tab Assigned Assets menjadi 500
9. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Assigned Assets
10. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
11. Verifikasi tampilan fetch gagal bukan empty state
12. Lepas intercept respons data Sub-tab Assigned Assets
13. Klik `[Try Again]`
14. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

### TC-FA-SU-500: Empty state, hasil pencarian kosong, loading, dan error load Sub-tab Pending Approvals

15. Buka Detail Hana Kusuma > Tab Responsibilities > Sub-tab Pending Approvals
16. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No pending approvals` dan Description `Pending approval requests will appear here.`
17. Ketik Search `zzzz`, tekan Enter
18. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
19. Atur intercept respons data Sub-tab Pending Approvals menjadi lambat (ditahan)
20. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Pending Approvals
21. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
22. Ganti intercept respons data Sub-tab Pending Approvals menjadi 500
23. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Pending Approvals
24. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
25. Verifikasi tampilan fetch gagal bukan empty state
26. Lepas intercept respons data Sub-tab Pending Approvals
27. Klik `[Try Again]`
28. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

### TC-FA-SU-536: Empty state, hasil pencarian kosong, loading, dan error load Sub-tab Pending Tasks

29. Buka Detail Hana Kusuma > Tab Responsibilities > Sub-tab Pending Tasks
30. Verifikasi data kosong sungguhan menampilkan ilustrasi 100x100 dengan Title `No pending tasks` dan Description `This user has no pending confirmation tasks.`
31. Ketik Search `zzzz`, tekan Enter
32. Verifikasi Search tanpa hasil menampilkan Title `No results found` dan Description `Try adjusting your search or filter.`
33. Atur intercept respons data Sub-tab Pending Tasks menjadi lambat (ditahan)
34. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Pending Tasks
35. Verifikasi saat memuat, skeleton 5 baris sesuai kolom aktual tampil
36. Ganti intercept respons data Sub-tab Pending Tasks menjadi 500
37. Buka ulang Detail Hana Kusuma > Tab Responsibilities > Sub-tab Pending Tasks
38. Verifikasi fetch gagal menampilkan `Unable to load this data.` dengan tombol `[Try Again]`
39. Verifikasi tampilan fetch gagal bukan empty state
40. Lepas intercept respons data Sub-tab Pending Tasks
41. Klik `[Try Again]`
42. Verifikasi `[Try Again]` memuat ulang data: pesan `Unable to load this data.` tidak lagi tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): membuka ulang surface sebelum tiap kondisi lambat dan 500 (supaya permintaan data dikirim ulang dan Search tidak terbawa), serta mengatur, mengganti, dan melepas intercept (pemicu, bukan objek asersi).
- Langkah penghubung tambahan (S-03): Search nama `Hana Kusuma` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-469: format dan nama berkas TC-FA-SU-464 di spec 159, transformasi data TC-FA-SU-466 di spec 370, Download gagal TC-FA-SU-467 di spec 366.
  - TC-FA-SU-500: format dan nama berkas TC-FA-SU-495 di spec 167, transformasi data TC-FA-SU-497 di spec 371, Download gagal TC-FA-SU-498 di spec 366.
  - TC-FA-SU-536: format dan nama berkas TC-FA-SU-531 di spec 180, transformasi data TC-FA-SU-533 di spec 371, Download gagal TC-FA-SU-534 di spec 369.
- Pemetaan butir Expected: butir a, b, c, dan d TC masing-masing menjadi satu `Verifikasi` (butir d dipecah per klausa: tampilan fetch gagal beserta `[Try Again]`, bukan empty state, dan `[Try Again]` memuat ulang data).
- Alasan melewati sekitar 35 langkah (42 langkah tertulis, 42 dengan ekspansi; tidak ada langkah yang diulang per iterasi): seluruh blok berkelas b (kegagalan baca yang dipaksa), tiap blok berdiri sendiri dan melepas intercept-nya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail Hana Kusuma yang sama dipakai untuk ketiga sub-tab Responsibilities.
- Temuan untuk QA (S-15):
  - TC-FA-SU-469: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-500: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - TC-FA-SU-536: precondition b menyebut halaman target Budi Santoso, sedangkan Langkah Uji 1 membuka pengguna tanpa data (Hana Kusuma); spec mengikuti Langkah Uji 1.
  - Keyword Search tanpa hasil, cara melambatkan respons, dan jeda tahan tidak diberi nilai oleh TC; spec memakai `zzzz` dan intercept ditahan sampai kondisi `Verifikasi` selesai. Butir b menyebut "Search atau Filter" tanpa hasil, sedangkan Langkah Uji hanya memakai keyword (Search); Filter tanpa hasil tidak dijalankan.
  - Hasil akhir `[Try Again]` (butir d, "memuat ulang data") tidak dinyatakan TC; spec mengasersi pesan `Unable to load this data.` tidak lagi tampil setelah intercept dilepas. Langkah Uji "Ulangi" ditafsirkan sebagai membuka ulang surface (Search tidak terbawa) karena TC tidak menyatakan apakah keyword Search bertahan setelah muat ulang.
