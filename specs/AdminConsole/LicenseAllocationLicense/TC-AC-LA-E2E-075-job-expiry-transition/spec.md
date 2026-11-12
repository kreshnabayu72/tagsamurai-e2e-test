---
id: TC-AC-LA-E2E-075-job-expiry-transition
title: "Job Sistem Expiry Transition"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-269
  - TC-AC-LA-270
  - TC-AC-LA-271
  - TC-AC-LA-272
  - TC-AC-LA-273
coverage:
  web: automated
---

# Job Sistem Expiry Transition

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: Bengkel Cahaya Motor (#23, FAMS Professional Paid Active, End Date 31 Dec 2026), CV Mitra Sejati (#22), kantong wallet (#33). Zona waktu General Settings Plan Owner term Asia/Jakarta (UTC+07:00); hari End Date dan hari sesudahnya dihitung pada zona waktu itu. Margin terhadap batas End Date 1 menit: 31 Dec 2026 23:59 (1 menit sebelum batas) dan 1 Jan 2027 00:01 (1 menit sesudah batas), keduanya pada zona waktu Plan Owner.
- Data Dinamis (seeding per blok lewat langkah penghubung pada fixture backend yang disediakan tim FE/BE, bukan di hook `before`, supaya job time-travel satu blok tidak memproses seed blok lain; milik spec ini, bentuknya sama dengan Pre-setup yang disebut): alokasi `Active` Concurrent User +10 ke FAMS Professional Bengkel Cahaya Motor oleh `Dewi A` (bentuk #47) untuk TC-AC-LA-269; alokasi `Active` Addon Asset Control App ke `SUBS-20260105-K2L3M` CV Mitra Sejati (bentuk #53) untuk TC-AC-LA-270; alokasi `Active` Asset Control Station +2 `Client-wide` dan Storage +50 GB `Client-wide` Klinik Harapan Bunda (bentuk #52) untuk TC-AC-LA-271; alokasi `Expired` Concurrent User +3 PT Abadi Jaya oleh `Rian T` (bentuk #51) untuk TC-AC-LA-272; alokasi `Active` Concurrent User +10 Bengkel Cahaya Motor kedua untuk TC-AC-LA-273 (dibuat ulang karena seed 269 sudah `Expired` oleh job blok 269). Allocation ID dibaca dari hasil seeding. Hook `after` membersihkan seed yang tersisa.
- Baris Pre-setup yang terpaksa berubah: Subscription FAMS Professional Bengkel Cahaya Motor (#23) di-Renew oleh blok TC-AC-LA-273 (membuat term successor; efeknya pada Last Updated dan audit trail Subscription dicatat); dipulihkan ke keadaan awal (End Date 31 Dec 2026, tanpa term successor) oleh fixture backend yang disediakan tim FE/BE di langkah pembuka blok TC-AC-LA-273 (sebelum Renew), langkah penutup blok itu, dan hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): seeding satu notifikasi Plan Owner PT Maju Bersama yang tidak terkait seed 269 sehingga daftar notifikasi Plan Owner selalu memuat sedikitnya satu notifikasi lain sebagai anchor asersi absence; fixture waktu untuk mengatur jam server dan jam browser ke nilai absolut dalam zona waktu Plan Owner, menunggu satu siklus job. Jam dipulihkan sebelum membuka Activity Log, System Log, dan Changelog (S-09) dan di hook `after`. Baseline entri log dicatat per Allocation ID seed (nol karena seed baru, S-12).
- Jendela tunggu notifikasi in-app 5 detik tanpa memuat ulang halaman (langkah 26) adalah pilihan spec, bukan nilai TC atau PRD (bagian 6); anchor positif asersi absence notifikasi: langkah 25.
- State global yang diubah: jam server dan jam browser, Subscription Bengkel Cahaya Motor (Renew). Dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-269: Expiry Transition Active menjadi Expired pada hari setelah End Date

1. Seed alokasi `Active` Concurrent User +10 ke FAMS Professional Bengkel Cahaya Motor oleh `Dewi A` (seed 269) lewat fixture backend hingga tersimpan, lalu baca Allocation ID
2. Atur jam server dan jam browser ke 31 Dec 2026 23:59 (zona waktu Plan Owner), lalu tunggu satu siklus job
3. Pulihkan jam server dan jam browser, ketik Search Allocation ID seed 269 di tab Current, tekan Enter
4. Verifikasi status seed 269 tetap `Active`
5. Buka Subscription Detail > License Quota Bengkel Cahaya Motor
6. Verifikasi 10 unit masih efektif
7. Atur jam server dan jam browser ke 1 Jan 2027 00:01 (zona waktu Plan Owner), lalu tunggu satu siklus job
8. Pulihkan jam server dan jam browser
9. Buka Allocation > License Allocation tab History, ketik Search Allocation ID seed 269, tekan Enter
10. Verifikasi status seed 269 `Expired`
11. Verifikasi baris seed 269 pindah ke tab History
12. Buka Allocation Log seed 269
13. Verifikasi entri `Allocation expired` tampil dengan `Reason: Subscription term ended`
14. Tutup modal Allocation Log
15. Buka Allocation > License Allocation, klik tab `Current`
16. Buka Changelog, cari entri dengan Allocation ID seed 269
17. Verifikasi Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
18. Tutup modal Changelog
19. Buka Activity Log, cari entri dengan Allocation ID seed 269
20. Verifikasi Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
21. Buka System Log, ketik Search Allocation ID seed 269, tekan Enter
22. Verifikasi empty state `No results found` tampil pada System Log
23. Verifikasi tidak ada entri System Log untuk seed 269
24. Buka notifikasi Plan Owner PT Maju Bersama
25. Verifikasi daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain (daftar termuat, anchor)
26. Tunggu 5 detik tanpa memuat ulang halaman
27. Verifikasi tidak ada notifikasi ke Plan Owner untuk seed 269
28. Buka Subscription Detail > License Quota Bengkel Cahaya Motor
29. Verifikasi kuota term berkurang 10
30. Buka Wallet
31. Verifikasi Balance kantong Distributor PT Maju Bersama tampil di Wallet (anchor)
32. Verifikasi Balance kantong Distributor tidak dikembalikan (tanpa refund)

### TC-AC-LA-270: Asset Control App mati otomatis saat Expiry tanpa grandfathering

33. Seed alokasi `Active` Addon Asset Control App ke `SUBS-20260105-K2L3M` CV Mitra Sejati (seed 270) lewat fixture backend hingga tersimpan, lalu baca Allocation ID
34. Buka Subscription Detail `SUBS-20260105-K2L3M` CV Mitra Sejati
35. Verifikasi status Asset Control App `Active` tampil pada Subscription Detail (anchor)
36. Verifikasi tidak ada toggle OFF manual untuk Asset Control App
37. Atur jam server dan jam browser satu hari setelah End Date term CV Mitra Sejati, tunggu satu siklus Expiry Transition, lalu pulihkan jam
38. Buka tab History, ketik Search Allocation ID seed 270, tekan Enter
39. Verifikasi alokasi App seed 270 `Expired`
40. Buka Subscription Detail `SUBS-20260105-K2L3M`
41. Verifikasi status Asset Control App pada Subscription menjadi `Not Active`

### TC-AC-LA-271: Expiry tidak memproses Asset Control Station dan Storage

42. Seed alokasi `Active` Asset Control Station +2 `Client-wide` dan Storage +50 GB `Client-wide` Klinik Harapan Bunda (seed Station dan seed Storage) lewat fixture backend hingga tersimpan, lalu baca Allocation ID masing-masing
43. Buka tab Current, ketik Search Allocation ID seed Station, tekan Enter, lalu buka Allocation Log; catat jumlah entri sebagai baseline (juga untuk seed Storage)
44. Tutup modal Allocation Log
45. Buka Subscription Detail > License Quota Klinik Harapan Bunda dan catat kuota ledger Client sebagai baseline
46. Atur jam server dan jam browser jauh melewati End Date seluruh term Klinik Harapan Bunda, tunggu satu siklus Expiry Transition, lalu pulihkan jam
47. Buka Allocation > License Allocation tab Current, lalu buka Allocation Log seed Station dan seed Storage
48. Verifikasi alokasi Station dan Storage tetap `Active` di tab Current
49. Verifikasi entri `Allocation created by [PIC]` (PIC = pelaku seed) seed Station dan seed Storage tampil pada Allocation Log (anchor)
50. Verifikasi jumlah entri Allocation Log seed Station dan seed Storage sama dengan baseline
51. Tutup modal Allocation Log
52. Buka Subscription Detail > License Quota Klinik Harapan Bunda
53. Verifikasi tidak ada pengurangan kuota ledger Client (kuota ledger Client sama dengan baseline langkah 45)

### TC-AC-LA-272: Expiry ulang pada record Expired adalah no-op

54. Seed alokasi `Expired` Concurrent User +3 PT Abadi Jaya oleh `Rian T` (seed Expired) lewat fixture backend hingga tersimpan, lalu baca Allocation ID
55. Buka tab History, ketik Search Allocation ID seed Expired, tekan Enter, lalu buka Allocation Log; catat jumlah entri sebagai baseline
56. Tutup modal Allocation Log
57. Buka Subscription Detail > License Quota PT Abadi Jaya dan catat kuota ledger sebagai baseline
58. Atur jam server dan jam browser maju dua siklus Expiry Transition, tunggu dua siklus, lalu pulihkan jam
59. Buka Allocation > License Allocation tab History, ketik Search Allocation ID seed Expired, tekan Enter
60. Verifikasi status seed Expired tetap `Expired`
61. Buka Subscription Detail > License Quota PT Abadi Jaya
62. Verifikasi kuota tidak berkurang dua kali (kuota sama dengan baseline langkah 57)
63. Buka Allocation > License Allocation tab History, ketik Search Allocation ID seed Expired, tekan Enter, lalu buka Allocation Log seed Expired
64. Verifikasi entri `Allocation expired` seed tampil pada Allocation Log (anchor)
65. Verifikasi jumlah entri Allocation Log seed sama dengan baseline
66. Tutup modal Allocation Log

### TC-AC-LA-273: Renew tidak meng-cascade kedaluwarsa

67. Pulihkan Subscription FAMS Professional Bengkel Cahaya Motor ke keadaan awal (End Date 31 Dec 2026, tanpa term successor) dan seed alokasi `Active` Concurrent User +10 Bengkel Cahaya Motor kedua (seed 273) lewat fixture backend hingga tersimpan, lalu baca Allocation ID
68. Renew Subscription FAMS Professional Bengkel Cahaya Motor pada Subscription Detail
69. Tunggu aksi selesai (Renewal tersimpan dan Subscription Detail menampilkan term successor)
70. Catat status Subscription FAMS Professional Bengkel Cahaya Motor sebagai baseline
71. Atur jam server dan jam browser ke 1 Jan 2027 00:01 (zona waktu Plan Owner), tunggu satu siklus Expiry Transition, lalu pulihkan jam
72. Buka Allocation > License Allocation tab History, ketik Search Allocation ID seed 273, tekan Enter
73. Verifikasi alokasi term lama menjadi `Expired`
74. Buka Subscription Detail > License Quota term successor
75. Verifikasi term successor mulai tanpa 10 unit itu
76. Verifikasi status Subscription sama dengan status yang dicatat sebelum Expiry Transition
77. Buka form Allocate untuk term successor
78. Verifikasi alokasi baru ke term successor tidak menambah kuota term lama
79. Pulihkan Subscription FAMS Professional Bengkel Cahaya Motor ke keadaan awal lewat fixture backend hingga tersimpan

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 33, 42, 54, 67 (seed per blok lewat fixture backend: job time-travel satu blok tidak boleh memproses seed blok lain, S-09; langkah 67 juga memulihkan term Bengkel Cahaya Motor sebelum Renew karena seed 269 dan seed 273 berada pada term yang sama), 79 (memulihkan term setelah Renew), 3, 8, 37, 46, 58, 71 (memulihkan jam sebelum membuka log atau halaman, S-09), 5, 9, 12, 16, 19, 21, 24, 28 (membuka License Quota setelah pindah dari tab History, S-14), 30, 34, 38, 40, 43, 47, 52, 55, 59, 72, 77 (membuka surface dan Search untuk menemukan baris target, R-16; baseline S-12).
- Langkah 15 (membuka List tab Current sebelum membuka Changelog karena ikon Changelog hanya ada di tab Current, S-14), langkah 18 (menutup modal Changelog sebelum membuka Activity Log, S-09), langkah 70 (Catat status Subscription sebagai baseline sebelum job berjalan, S-12), langkah 74 (membuka License Quota term successor sebelum asersi kuota, S-14), langkah 14, 44, 51, 56, dan 66 (menutup modal Allocation Log sebelum membuka surface lain, S-09), langkah 45 dan 57 (baseline kuota ledger Client Klinik Harapan Bunda dan PT Abadi Jaya sebelum job berjalan, S-12), langkah 61 dan 63 (membuka Subscription Detail > License Quota atau List sebelum asersi pada surface itu, S-14), langkah 26 (jendela tunggu 5 detik tanpa Verifikasi sebelum asersi absence notifikasi, bagian 6), dan langkah 69 (Tunggu aksi selesai setelah Renew yang hasilnya tidak diasersi langsung, sebelum membuka surface lain, 8b butir 8) adalah langkah penghubung. Asersi tanpa pengurangan kuota ledger (langkah 53 dan 62) dibandingkan dengan baseline yang dicatat sebelum job.
- P-1: asersi tidak ada entri System Log (langkah 23), tidak ada notifikasi Plan Owner (27), jumlah entri log tidak berubah (49, 64), dan tidak ada toggle OFF (35) bergantung pada state berat time-travel dan berbaseline. Anchor positif: langkah 35, 49, 64 (entri atau status pada surface yang sama), langkah 22 (empty state `No results found` pada System Log setelah Search Allocation ID, pola spec 022), dan langkah 25 (daftar notifikasi Plan Owner termuat dan memuat notifikasi lain, dijamin kemampuan seeding notifikasi di Prerequisites; teks notifikasi lain itu tidak ada di katalog PRD sehingga tidak ditulis).
- Langkah 31 adalah anchor positif (Balance kantong Distributor tampil di Wallet) sebelum asersi absence refund pada langkah 32; langkah 30 membuka Wallet, dan anchor itu asersi tambahan di luar TC yang dicatat sesuai S-03 dan 8b butir 2.
- Spec melewati sekitar 35 langkah (79 langkah). Alasan pertahanan: seluruh blok satu kelas harness (job Expiry Transition) pada dataset Expiry yang sama dan berdiri sendiri dengan seed sendiri yang dibuat pada langkah pembuka blok, dan blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-269 sampai 272 menyebut "Tidak ada aktor login: job terjadwal sistem"; akun pengamat tidak ditulis. Spec memakai Pre-setup #10 dan Plan Owner PT Maju Bersama yang disediakan tim FE.
  - TC-AC-LA-270 Expected b ("Tidak ada toggle OFF manual yang tersedia sebelumnya") tidak menyebut lokasi toggle; spec memakai Subscription Detail Asset Control App dan memeriksanya sebelum jam digeser.
  - TC-AC-LA-271 Langkah 1 ("jauh melewati End Date") tidak menyebut nilai tanggal; spec memakai tanggal setelah End Date seluruh term.
  - TC-AC-LA-273 Expected c ("Alokasi baru ke term successor tidak menambah kuota term lama") menyebut alokasi baru, tetapi Langkah 2 hanya membuka form Allocate dan tidak men-Submit; spec mengikuti langkah TC dan asersi c tidak punya aksi pemicu Submit.
  - TC-AC-LA-273 Precondition b menyebut aktor Total Control Distributor tetapi Precondition a menyebut tidak ada aktor login; spec memakai Pre-setup #10 untuk Renew dan pengamatan.
  - TC-AC-LA-269 sampai 273 berbagi Pre-setup #23 (term Bengkel Cahaya Motor) tanpa seed per TC; spec membuat seed per blok dan memulihkan term sebelum Renew.
  - TC-AC-LA-269 Expected e ("Tidak ada notifikasi ke Plan Owner") tidak menyebut akun Plan Owner; disediakan tim FE.
  - TC-AC-LA-272 Precondition memakai Pre-setup #51 (Expired) tanpa menyebut asal; spec memakai seed milik spec dengan keadaan yang sama (S-06).
