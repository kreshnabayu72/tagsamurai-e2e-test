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
9. Buka Allocation > License Allocation tab History, klik row action `Allocation Log` pada baris seed 263
10. Verifikasi entri `Allocation auto-canceled` tampil tanpa `by [PIC]`
11. Verifikasi Description `Reason: Approval timeout`
12. Buka Changelog, cari entri dengan Allocation ID seed 263
13. Verifikasi Action `Timeout Auto-Cancel`, Status `Waiting for Approval` ke `Canceled`, Modified By `System`
14. Buka Activity Log, cari entri dengan Allocation ID seed 263
15. Verifikasi Action `Timeout Auto-Cancel`, Status `Waiting for Approval` ke `Canceled`, Modified By `System`
16. Buka System Log, ketik Search Allocation ID seed 263, tekan Enter
17. Verifikasi empty state `No results found` tampil pada System Log
18. Verifikasi tidak ada entri System Log untuk Allocation ID seed 263
19. Buka notifikasi `Fajar Nugroho`
20. Verifikasi approver aktif menerima notifikasi `License allocation canceled automatically`
21. Buka Allocation > License Allocation tab History, ketik Search Allocation ID seed 263, tekan Enter
22. Verifikasi `Resubmit` tersedia pada baris Canceled seed 263 di tab History

### TC-AC-LA-484: Timeout Auto-Cancel tidak berjalan sebelum SLA dan berjalan sesudahnya

23. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 484, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
24. Atur jam server dan jam browser ke T0 Submit seed 484 + 2 hari 23 jam 59 menit, lalu tunggu satu siklus job
25. Pulihkan jam, ketik Search Allocation ID seed 484 di tab Current, tekan Enter, buka Wallet, dan buka Allocation Log seed 484
26. Verifikasi status seed 484 tetap `Waiting for Approval`
27. Verifikasi Reserve $150.00 utuh
28. Verifikasi entri `Allocation created by Dewi A` seed 484 tampil pada Allocation Log (anchor)
29. Verifikasi tidak ada entri `Allocation auto-canceled` pada Allocation Log seed 484
30. Atur jam server dan jam browser ke T0 Submit seed 484 + 3 hari 1 menit, lalu tunggu satu siklus job
31. Pulihkan jam, buka tab History, Search Allocation ID seed 484, tekan Enter
32. Verifikasi status `Canceled` oleh sistem
33. Buka Wallet Distributor PT Maju Bersama
34. Verifikasi Reserve dilepas
35. Buka Allocation > License Allocation tab History, ketik Search Allocation ID seed 484, tekan Enter, lalu buka Allocation Log seed 484
36. Verifikasi Allocation Log memuat `Allocation auto-canceled` dengan `Reason: Approval timeout`

### TC-AC-LA-264: Timeout tidak mengubah record yang sudah Canceled atau diputus

37. Seed satu alokasi `Canceled` manual dan satu alokasi `Rejected` Concurrent User +5 PT Sejahtera oleh `Dewi A` lewat fixture backend hingga tersimpan, lalu baca Allocation ID masing-masing
38. Catat jumlah entri Allocation Log seed Canceled dan seed Rejected sebagai baseline
39. Atur jam server dan jam browser melewati SLA 3 hari, tunggu satu siklus job, lalu pulihkan jam
40. Buka tab History, Search tiap seed, dan buka Allocation Log masing-masing
41. Verifikasi status seed Canceled manual tetap `Canceled` dan seed Rejected tetap `Rejected`
42. Verifikasi entri `Allocation canceled by [PIC]` (PIC = pelaku seed Canceled manual) seed Canceled tampil pada Allocation Log (anchor)
43. Verifikasi jumlah entri Allocation Log kedua seed sama dengan baseline
44. Buka notifikasi `Fajar Nugroho`
45. Verifikasi notifikasi `License allocation canceled automatically` seed 263 tampil pada daftar notifikasi `Fajar Nugroho` (anchor)
46. Verifikasi tidak ada notifikasi baru untuk kedua seed pada daftar notifikasi `Fajar Nugroho`

### TC-AC-LA-279: Job sistem tetap berjalan bila entitas pengalokasi Suspended

47. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 279, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
48. Atur status entitas Distributor PT Maju Bersama menjadi Suspended lewat fixture backend hingga tersimpan
49. Atur jam server dan jam browser melewati SLA 3 hari seed 279, tunggu satu siklus job, lalu pulihkan jam
50. Buka tab History, Search Allocation ID seed 279, tekan Enter, buka Allocation Log seed 279, dan buka Wallet
51. Verifikasi Timeout Auto-Cancel tetap membatalkan seed 279 (status `Canceled`, Allocation Log `Allocation auto-canceled`)
52. Verifikasi Reserve seed 279 dilepas (Release)
53. Pulihkan status entitas Distributor PT Maju Bersama menjadi aktif lewat fixture backend hingga tersimpan

### TC-AC-LA-265: Pre-timeout warning H-24 dikirim sekali ke approver aktif dan requester

54. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 265, Cost $150.00 di-Reserve) lewat fixture backend hingga tersimpan, lalu baca Allocation ID dan T0 Submit
55. Atur jam server dan jam browser ke T0 Submit seed 265 + 2 hari (sisa 24 jam), lalu tunggu dua siklus job
56. Pulihkan jam dan buka notifikasi `Fajar Nugroho`
57. Verifikasi approver aktif menerima notifikasi `Request <Allocation ID seed 265> will be automatically canceled in 24 hours if no decision is made. Please finish reviewing this request.`
58. Verifikasi notifikasi warning seed 265 pada `Fajar Nugroho` berjumlah tepat satu (idempotent)

### TC-AC-LA-266: Perubahan Approval Timeout menghitung ulang SLA

59. Seed alokasi `Waiting for Approval` Concurrent User +5 PT Sejahtera oleh `Dewi A` (seed 266, Cost $150.00 di-Reserve) dengan cap waktu Submit 2 hari sebelum waktu Save lewat fixture waktu, hingga tersimpan, lalu baca Allocation ID
60. Ganti akun: logout `Fajar Nugroho`, login sebagai `Hendra Wijaya` dengan `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`
61. Buka Plans & Licensing > Lifecycle Settings > Approval Settings, ubah Approval Timeout dari `3` menjadi `1` day(s), lalu klik `[Save]`
62. Tunggu aksi selesai (tombol `[Save]` aktif kembali), lalu catat waktu Save
63. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed 266, tekan Enter
64. Verifikasi status seed 266 tetap `Waiting for Approval`
65. Verifikasi deadline efektif seed 266 sama dengan waktu Save + 24 jam (dibaca lewat kemampuan baca SLA yang disediakan tim FE/BE)
66. Ganti akun: logout `Hendra W`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`, lalu buka notifikasi
67. Verifikasi approver aktif menerima segera `Request <Allocation ID seed 266> will be automatically canceled in 24 hours if no decision is made. Please finish reviewing this request.`
68. Ganti akun: logout `Fajar N`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`, lalu buka notifikasi
69. Verifikasi requester menerima `Your request is awaiting decision and will expire in 24 hours if not resolved.` untuk seed 266
70. Verifikasi requester menerima `License allocation canceled automatically` untuk seed 263
71. Verifikasi requester menerima `Your request is awaiting decision and will expire in 24 hours if not resolved.` untuk seed 265

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 23, 37, 47, 54, 59 (seed per blok lewat fixture backend: job time-travel satu blok tidak boleh memproses seed blok lain, S-09), 4, 25, 31, 39, 49, 50, 56 (memulihkan jam sebelum membuka log, S-09, dan membuka surface), 5, 9, 12, 14, 16, 40, 63 (Search/tab untuk menemukan baris target, R-16), 7, 19, 33 (Wallet dan notifikasi `Fajar Nugroho`, membuka surface), 21 (membuka List tab History dan Search seed 263 sebelum asersi `Resubmit`, S-14), 35 (membuka List tab History dan Allocation Log seed 484 setelah Wallet, S-14), 44 (membuka notifikasi `Fajar Nugroho` sebelum asersi absence notifikasi), 38 (baseline), 48 dan 53 (mengatur status entitas), 60, 66, 68 (ganti akun), 62 (Tunggu aksi selesai setelah `[Save]` Approval Timeout sebelum pindah surface, 8b.8; mencatat waktu Save untuk asersi deadline).
- Urutan blok TC-AC-LA-279 dipindah sebelum TC-AC-LA-265 agar seed 265 (yang tetap `Waiting for Approval`) tidak diproses job blok 279; TC-AC-LA-266 tetap terakhir karena mengubah Approval Timeout global.
- Pengamat berasal dari Fajar Nugroho (Pre-setup #10) karena TC job tidak punya aktor login. Notifikasi requester (langkah 69 sampai 71) dikumpulkan di akhir untuk menghindari ganti akun berulang; urutan TC dalam spec berubah karena alasan itu dan notifikasi seed 263 dan 265 tetap tersedia di daftar notifikasi `Dewi Anggraini`.
- P-1: asersi tidak ada entri `Allocation auto-canceled` (langkah 29), tidak ada entri System Log (langkah 18), serta jumlah entri dan notifikasi tidak berubah (langkah 43, 46) bergantung pada state berat time-travel yang dibangun di spec yang sama; semuanya berbaseline (S-12). Anchor positif: langkah 28 (entri `Allocation created by Dewi A`), langkah 17 (empty state `No results found` pada System Log setelah Search Allocation ID, pola spec 022), langkah 42 (entri `Allocation canceled by [PIC]` seed Canceled), dan langkah 45 (notifikasi seed 263 pada daftar yang sama dengan asersi absence notifikasi).
- Spec melewati sekitar 35 langkah (71 langkah). Alasan pertahanan: seluruh blok memakai kelas harness yang sama (job sistem Approval Timeout dengan dataset dan Pre-setup #40 yang sama), tiap blok memakai seed sendiri yang dibuat pada langkah pembuka blok, dan blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-263, 264, 265, 484, 279 menyebut "Tidak ada aktor login"; akun pengamat notifikasi, Wallet, dan log tidak ditulis. Spec memakai Pre-setup #10 untuk pengamat approver dan Pre-setup #4 untuk pengamat requester.
  - TC-AC-LA-265 dan TC-AC-LA-266 menyebut notifikasi requester tanpa menyebut login `Dewi Anggraini` sebagai Pre-setup; spec menambah ganti akun ke Pre-setup #4.
  - TC-AC-LA-263 Expected c menyebut "Changelog dan Activity Log" tanpa lokasi menu Activity Log dan System Log; lokasi menu mengikuti modul Global Settings dan tidak diasersi.
  - TC-AC-LA-266 Langkah 3 membuka notifikasi `Fajar Nugroho` dan `Dewi Anggraini` pada satu langkah tanpa menyebut ganti akun; spec memecahnya menjadi ganti akun eksplisit.
  - TC-AC-LA-266 Expected a ("deadline efektif menjadi waktu Save + 24 jam") tidak menyebut cara membaca deadline; langkah 65 memakai kemampuan baca SLA yang disediakan tim FE/BE.
  - TC-AC-LA-266 mengubah Approval Timeout global sehingga SLA alokasi `Waiting for Approval` lain ikut dihitung ulang (seed 265 ikut terdampak); TC tidak menyebut pengaruh ini.
  - TC-AC-LA-263, 484, 264, 265, 279, 266 berbagi Pre-setup #41 tanpa seed per TC; spec membuat seed per blok.
  - TC-AC-LA-266 Precondition c ("Alokasi dibuat 2 hari sebelum waktu Save lewat fixture waktu") tidak menyebut mekanisme; disediakan tim FE/BE.
  - TC-AC-LA-264 Expected a ("tidak ada entri log atau notifikasi baru") tidak menyebut surface log; spec memakai Allocation Log dan notifikasi.
  - TC-AC-LA-279 Expected b ("Aksi tulis aktor dari entitas itu tetap ditolak") diuji di Section 9 TC (TC-AC-LA-469 sampai 500, spec 078) dan tidak diasersi di sini.
  - TC-AC-LA-279 tidak menyebut akun admin dan mekanisme yang menyetel status Suspended; disediakan tim FE.
