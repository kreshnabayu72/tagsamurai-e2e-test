---
id: TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24
title: "Job Sistem Timeout Auto-Cancel dan Warning H-24"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-263
  - TC-AC-LA-264
  - TC-AC-LA-265
  - TC-AC-LA-266
  - TC-AC-LA-484
  - TC-AC-LA-279
coverage:
  web: automated
---

# Job Sistem Timeout Auto-Cancel dan Warning H-24

## Prerequisites

- Mode: FE+BE.
- Akun pengamat pertama: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10, approver aktif), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4, requester seed), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19), kantong wallet (#33), Product Price (#34), Approval Timeout 3 hari (#40). Entitas Distributor PT Maju Bersama berstatus Suspended hanya pada blok TC-AC-LA-279 (diatur dan dipulihkan fixture backend yang disediakan tim FE/BE di langkah penghubung serta hook `after`).
- Data Dinamis (seeding per blok lewat langkah penghubung pada fixture backend yang disediakan tim FE/BE, bukan di hook `before`, supaya job time-travel satu blok tidak memproses seed blok lain; milik spec ini, bentuknya sama dengan Pre-setup #41, #48, #50 tetapi bukan baris bersama): alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (Cost $150.00 di-Reserve) untuk TC-AC-LA-263, TC-AC-LA-484, TC-AC-LA-279, TC-AC-LA-265, dan TC-AC-LA-266, satu seed per blok (seed 266 dibuat dengan cap waktu Submit 2 hari sebelum waktu Save lewat fixture waktu); satu alokasi `Canceled` manual dan satu `Rejected` untuk TC-AC-LA-264. Allocation ID dan T0 (waktu Submit) tiap seed dibaca dari hasil seeding (baseline log nol karena seed baru, S-12). Hook `after` membersihkan seed yang tersisa.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk mengatur jam server dan jam browser ke nilai absolut (T0 = waktu Submit seed dibaca lewat seeding), menunggu satu siklus job, mengubah Approval Timeout, dan membaca deadline SLA efektif sebuah alokasi `Waiting for Approval` (untuk TC-AC-LA-266 a). Margin terhadap batas SLA 1 menit (T0 + 2 hari 23 jam 59 menit dan T0 + 3 hari 1 menit; batas T0 + 3 hari). Jam dipulihkan sebelum membuka Changelog, Activity Log, atau System Log (S-09). Approval Timeout dipulihkan ke 3 day(s) di hook `after`.
- Jendela tunggu notifikasi in-app 5 detik tanpa memuat ulang halaman (langkah 55) adalah pilihan spec, bukan nilai TC atau PRD (bagian 6); anchor positif asersi absence notifikasi: langkah 54.
- State global yang diubah: jam server dan jam browser, Approval Timeout (#40), status entitas Distributor PT Maju Bersama. Semuanya dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-263: Timeout Auto-Cancel membatalkan Waiting for Approval setelah SLA lewat

1. Seed alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera oleh `Dewi A` (seed 263, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
2. Atur jam server dan jam browser ke T0 Submit seed 263 + 3 hari 1 menit
3. Tunggu satu siklus job
4. Pulihkan jam server dan jam browser ke waktu nyata
5. Klik tab `History`, ketik Search Allocation ID seed 263, tekan Enter
6. Verifikasi baris seed 263 berstatus `Canceled`
7. Buka Wallet Distributor PT Maju Bersama
8. Verifikasi Reserve $150.00 dilepas
9. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 263, tekan Enter, lalu klik row action `Allocation Log` pada baris seed 263
10. Verifikasi entri `Allocation auto-canceled` tampil tanpa `by [PIC]`
11. Verifikasi Description `Reason: Approval timeout`
12. Tutup modal Allocation Log
13. Buka Allocation > License Allocation, klik tab `Current`
14. Buka Changelog, cari entri dengan Allocation ID seed 263
15. Verifikasi Action `Timeout Auto-Cancel`, Status `Waiting for Approval` ke `Canceled`, Modified By `System`
16. Tutup modal Changelog
17. Buka Activity Log, cari entri dengan Allocation ID seed 263
18. Verifikasi Action `Timeout Auto-Cancel`, Status `Waiting for Approval` ke `Canceled`, Modified By `System`
19. Buka System Log, ketik Search Allocation ID seed 263, tekan Enter
20. Verifikasi empty state `No results found` tampil pada System Log
21. Verifikasi tidak ada entri System Log untuk Allocation ID seed 263
22. Buka notifikasi `Fajar Nugroho`
23. Verifikasi approver aktif menerima notifikasi `License allocation canceled automatically`
24. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 263, tekan Enter
25. Verifikasi `Resubmit` tersedia pada baris Canceled seed 263 di tab History

### TC-AC-LA-484: Timeout Auto-Cancel tidak berjalan sebelum SLA dan berjalan sesudahnya

26. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 484, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
27. Atur jam server dan jam browser ke T0 Submit seed 484 + 2 hari 23 jam 59 menit, lalu tunggu satu siklus job
28. Pulihkan jam server dan jam browser, klik tab `Current`, kosongkan kotak search: klik `✕` pada Search, tekan Enter, ketik Search Allocation ID seed 484, tekan Enter
29. Verifikasi status seed 484 tetap `Waiting for Approval`
30. Buka Wallet Distributor PT Maju Bersama
31. Verifikasi Reserve $150.00 utuh
32. Buka Allocation > License Allocation, klik tab `Current`, ketik Search Allocation ID seed 484, tekan Enter, lalu buka Allocation Log seed 484
33. Verifikasi entri `Allocation created by Dewi A` seed 484 tampil pada Allocation Log (anchor)
34. Verifikasi tidak ada entri `Allocation auto-canceled` pada Allocation Log seed 484
35. Tutup modal Allocation Log
36. Atur jam server dan jam browser ke T0 Submit seed 484 + 3 hari 1 menit, lalu tunggu satu siklus job
37. Pulihkan jam, klik tab `History`, kosongkan kotak search: klik `✕` pada Search, tekan Enter, ketik Search Allocation ID seed 484, tekan Enter
38. Verifikasi status `Canceled` oleh sistem
39. Buka Wallet Distributor PT Maju Bersama
40. Verifikasi Reserve dilepas
41. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 484, tekan Enter, lalu buka Allocation Log seed 484
42. Verifikasi Allocation Log memuat `Allocation auto-canceled` dengan `Reason: Approval timeout`
43. Tutup modal Allocation Log

### TC-AC-LA-264: Timeout tidak mengubah record yang sudah Canceled atau diputus

44. Seed satu alokasi `Canceled` manual dan satu alokasi `Rejected` Concurrent User +5 PT Sejahtera oleh `Dewi A` lewat fixture backend hingga tersimpan, lalu baca Allocation ID masing-masing
45. Catat jumlah entri Allocation Log seed Canceled dan seed Rejected sebagai baseline
46. Catat jumlah notifikasi pada daftar notifikasi `Fajar Nugroho` sebagai baseline
47. Atur jam server dan jam browser melewati SLA 3 hari, tunggu satu siklus job, lalu pulihkan jam
48. Buka tab History, Search tiap seed, dan buka Allocation Log masing-masing
49. Verifikasi status seed Canceled manual tetap `Canceled` dan seed Rejected tetap `Rejected`
50. Verifikasi entri `Allocation canceled by [PIC]` (PIC = pelaku seed Canceled manual) seed Canceled tampil pada Allocation Log (anchor)
51. Verifikasi jumlah entri Allocation Log kedua seed sama dengan baseline
52. Tutup modal Allocation Log
53. Buka notifikasi `Fajar Nugroho`
54. Verifikasi notifikasi `License allocation canceled automatically` seed 263 tampil pada daftar notifikasi `Fajar Nugroho` (anchor)
55. Tunggu 5 detik tanpa memuat ulang halaman
56. Verifikasi jumlah notifikasi pada daftar notifikasi `Fajar Nugroho` sama dengan baseline, tidak ada notifikasi baru untuk kedua seed

### TC-AC-LA-279: Job sistem tetap berjalan bila entitas pengalokasi Suspended

57. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 279, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
58. Atur status entitas Distributor PT Maju Bersama menjadi Suspended lewat fixture backend hingga tersimpan
59. Atur jam server dan jam browser melewati SLA 3 hari seed 279, tunggu satu siklus job, lalu pulihkan jam
60. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 279, tekan Enter, lalu buka Allocation Log seed 279
61. Verifikasi Timeout Auto-Cancel tetap membatalkan seed 279 (status `Canceled`, Allocation Log `Allocation auto-canceled`)
62. Tutup modal Allocation Log
63. Buka Wallet Distributor PT Maju Bersama
64. Verifikasi Reserve seed 279 dilepas (Release)
65. Pulihkan status entitas Distributor PT Maju Bersama menjadi aktif lewat fixture backend hingga tersimpan

### TC-AC-LA-265: Pre-timeout warning H-24 dikirim sekali ke approver aktif dan requester

66. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 265, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
67. Atur jam server dan jam browser ke T0 Submit seed 265 + 2 hari (sisa 24 jam), lalu tunggu dua siklus job
68. Pulihkan jam dan buka notifikasi `Fajar Nugroho`
69. Verifikasi approver aktif menerima notifikasi `Request <Allocation ID seed 265> will be automatically canceled in 24 hours if no decision is made. Please finish reviewing this request.`
70. Verifikasi notifikasi warning seed 265 pada `Fajar Nugroho` berjumlah tepat satu (idempotent)

### TC-AC-LA-266: Perubahan Approval Timeout menghitung ulang SLA

71. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 266, Cost $150.00 di-Reserve) dengan cap waktu Submit 2 hari sebelum waktu Save lewat fixture waktu, hingga tersimpan, lalu baca Allocation ID
72. Ganti akun: logout `Fajar Nugroho`, login sebagai `Hendra Wijaya` dengan `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`
73. Buka Plans & Licensing > Lifecycle Settings > Approval Settings, ubah Approval Timeout dari `3` menjadi `1` day(s), lalu klik `[Save]`
74. Tunggu aksi selesai (tombol `[Save]` aktif kembali), lalu catat waktu Save
75. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed 266, tekan Enter
76. Verifikasi status seed 266 tetap `Waiting for Approval`
77. Verifikasi deadline efektif seed 266 sama dengan waktu Save + 24 jam (dibaca lewat kemampuan baca SLA yang disediakan tim FE/BE)
78. Ganti akun: logout `Hendra W`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`, lalu buka notifikasi
79. Verifikasi approver aktif menerima segera `Request <Allocation ID seed 266> will be automatically canceled in 24 hours if no decision is made. Please finish reviewing this request.`
80. Ganti akun: logout `Fajar N`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`, lalu buka notifikasi
81. Verifikasi requester menerima `Your request is awaiting decision and will expire in 24 hours if not resolved.` untuk seed 266
82. Verifikasi requester menerima `License allocation canceled automatically` untuk seed 263
83. Verifikasi requester menerima `Your request is awaiting decision and will expire in 24 hours if not resolved.` untuk seed 265

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 26, 44, 57, 66, 71 (seed per blok lewat fixture backend: job time-travel satu blok tidak boleh memproses seed blok lain, S-09), 4, 28, 37, 47, 59, 60, 68 (memulihkan jam sebelum membuka log, S-09, dan membuka surface), 5, 9, 14, 17, 19, 48, 75 (Search/tab untuk menemukan baris target, R-16), 7, 22, 39 (Wallet dan notifikasi `Fajar Nugroho`, membuka surface), 24 (membuka List tab History dan Search seed 263 sebelum asersi `Resubmit`, S-14), 41 (membuka List tab History dan Allocation Log seed 484 setelah Wallet, S-14), 53 (membuka notifikasi `Fajar Nugroho` sebelum asersi absence notifikasi), 45 (baseline), 58 dan 65 (mengatur status entitas), 72, 78, 80 (ganti akun), 74 (Tunggu aksi selesai setelah `[Save]` Approval Timeout sebelum pindah surface, 8b.8; mencatat waktu Save untuk asersi deadline).
- Setelah pindah modul (Wallet, notifikasi, Changelog), langkah 9, 24, 32, 41, dan 60 membuka List, klik tab, lalu mengetik Search pada kotak yang kosong di halaman yang baru dimuat, tanpa `✕` (S-14, 8b butir 9). Langkah 28 dan 37 (masih di halaman List yang sama) mengosongkan kotak Search dengan klik `✕` lalu Enter sesudah pindah tab sebelum Search baru; spec tidak mengandalkan sisa isi kotak Search (S-14, 8b butir 9).
- Langkah 13 (membuka List tab Current sebelum membuka Changelog karena ikon Changelog hanya ada di tab Current, S-14), langkah 16 (menutup modal Changelog sebelum membuka Activity Log, S-09), langkah 46 (Catat baseline jumlah notifikasi sebelum pemicu job), langkah 12, 35, 43, 52, dan 62 (menutup modal Allocation Log sebelum membuka surface lain, S-09), langkah 30, 32, dan 63 (membuka Wallet atau List sebelum asersi pada surface itu, S-14), serta langkah 55 (jendela tunggu 5 detik sebelum asersi absence notifikasi, bagian 6) adalah langkah penghubung tanpa Verifikasi.
- Urutan blok TC-AC-LA-279 dipindah sebelum TC-AC-LA-265 agar seed 265 (yang tetap `Waiting for Approval`) tidak diproses job blok 279; TC-AC-LA-266 tetap terakhir karena mengubah Approval Timeout global.
- Pengamat berasal dari Fajar Nugroho (Pre-setup #10) karena TC job tidak punya aktor login. Notifikasi requester (langkah 81 sampai 83) dikumpulkan di akhir untuk menghindari ganti akun berulang; urutan TC dalam spec berubah karena alasan itu dan notifikasi seed 263 dan 265 tetap tersedia di daftar notifikasi `Dewi Anggraini`.
- P-1: asersi tidak ada entri `Allocation auto-canceled` (langkah 34), tidak ada entri System Log (langkah 21), serta jumlah entri dan notifikasi tidak berubah (langkah 51, 56) bergantung pada state berat time-travel yang dibangun di spec yang sama; semuanya berbaseline (S-12). Anchor positif: langkah 33 (entri `Allocation created by Dewi A`), langkah 20 (empty state `No results found` pada System Log setelah Search Allocation ID, pola spec 022), langkah 50 (entri `Allocation canceled by [PIC]` seed Canceled), dan langkah 54 (notifikasi seed 263 pada daftar yang sama dengan asersi absence notifikasi).
- Spec melewati sekitar 35 langkah (83 langkah). Alasan pertahanan: seluruh blok memakai kelas harness yang sama (job sistem Approval Timeout dengan dataset dan Pre-setup #40 yang sama), tiap blok memakai seed sendiri yang dibuat pada langkah pembuka blok, dan blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-263, 264, 265, 484, 279 menyebut "Tidak ada aktor login"; akun pengamat notifikasi, Wallet, dan log tidak ditulis. Spec memakai Pre-setup #10 untuk pengamat approver dan Pre-setup #4 untuk pengamat requester.
  - TC-AC-LA-265 dan TC-AC-LA-266 menyebut notifikasi requester tanpa menyebut login `Dewi Anggraini` sebagai Pre-setup; spec menambah ganti akun ke Pre-setup #4.
  - TC-AC-LA-263 Expected c menyebut "Changelog dan Activity Log" tanpa lokasi menu Activity Log dan System Log; lokasi menu mengikuti modul Global Settings dan tidak diasersi.
  - TC-AC-LA-266 Langkah 3 membuka notifikasi `Fajar Nugroho` dan `Dewi Anggraini` pada satu langkah tanpa menyebut ganti akun; spec memecahnya menjadi ganti akun eksplisit.
  - TC-AC-LA-266 Expected a ("deadline efektif menjadi waktu Save + 24 jam") tidak menyebut cara membaca deadline; langkah 77 memakai kemampuan baca SLA yang disediakan tim FE/BE.
  - TC-AC-LA-266 mengubah Approval Timeout global sehingga SLA alokasi `Waiting for Approval` lain ikut dihitung ulang (seed 265 ikut terdampak); TC tidak menyebut pengaruh ini.
  - TC-AC-LA-263, 484, 264, 265, 279, 266 berbagi Pre-setup #41 tanpa seed per TC; spec membuat seed per blok.
  - TC-AC-LA-266 Precondition c ("Alokasi dibuat 2 hari sebelum waktu Save lewat fixture waktu") tidak menyebut mekanisme; disediakan tim FE/BE.
  - TC-AC-LA-264 Expected a ("tidak ada entri log atau notifikasi baru") tidak menyebut surface log; spec memakai Allocation Log dan notifikasi.
  - TC-AC-LA-279 Expected b ("Aksi tulis aktor dari entitas itu tetap ditolak") diuji di Section 9 TC (TC-AC-LA-469 sampai 500, spec 078) dan tidak diasersi di sini.
  - TC-AC-LA-279 tidak menyebut akun admin dan mekanisme yang menyetel status Suspended; disediakan tim FE.
