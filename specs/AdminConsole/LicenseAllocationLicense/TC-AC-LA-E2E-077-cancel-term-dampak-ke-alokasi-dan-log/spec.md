---
id: TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log
title: "Cancel Term: Dampak ke Alokasi Active, Pending, Station, Storage, dan Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-274
  - TC-AC-LA-275
  - TC-AC-LA-276
  - TC-AC-LA-277
  - TC-AC-LA-397
  - TC-AC-LA-527
coverage:
  web: automated
---

# Cancel Term: Dampak ke Alokasi Active, Pending, Station, Storage, dan Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (target aksi Cancel Subscription): Bengkel Cahaya Motor (#23), Toko Serba Ada (#21) dengan term Pending `SUBS-20260819-00001`, Klinik Harapan Bunda (#24) dengan FAMS Professional dan SAMS Growth Paid Active; kantong wallet (#33), Product Price (#34). Term yang di-Cancel adalah data Pre-setup yang tidak dapat dimiliki spec (satu Client hanya punya satu term Pending dan Subscription Paid Active yang dibatalkan), sehingga dipulihkan oleh fixture backend yang disediakan tim FE/BE di hook `before`, `after`, dan langkah penghubung antar blok (S-06, pengecualian 2026-10-30). Efek pada Last Updated Subscription dan audit trail dicatat di hook `after`.
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup yang disebut): alokasi `Active` Concurrent User +10 Bengkel Cahaya Motor oleh `Dewi A` (bentuk #47) untuk TC-AC-LA-274; alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke `SUBS-20260819-00001` Toko Serba Ada (bentuk #46, Cost $3,650.00 di-Reserve) untuk TC-AC-LA-275, TC-AC-LA-397, dan TC-AC-LA-527 (dibuat ulang oleh fixture backend sebelum tiap blok); alokasi `Active` Asset Control Station +2 `Client-wide` dan Storage +50 GB `Client-wide` Klinik Harapan Bunda (bentuk #52) untuk TC-AC-LA-276 dan TC-AC-LA-277. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca saldo kantong (Balance, Reserved, Available) Distributor PT Maju Bersama untuk baseline Balance sebelum Cancel Subscription (TC dan PRD tidak menyebut halaman atau endpointnya); fixture backend yang memulihkan term yang di-Cancel dan seed alokasinya; tanggal acuan server uji 22 Dec 2026 (fixture waktu) untuk TC-AC-LA-527. Baseline entri log dicatat per Allocation ID seed (baseline nol karena seed baru, S-12).
- State global yang diubah: status Subscription pada Pre-setup #21, #23, #24; dipulihkan lewat fixture backend. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-274: Cancel term, alokasi Active menjadi Expired seketika tanpa refund

1. Cancel Subscription pada term FAMS Professional Bengkel Cahaya Motor yang memuat seed 274
2. Tunggu aksi selesai (dialog pembatalan tertutup)
3. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 274, tekan Enter
4. Verifikasi alokasi seed 274 `Expired` seketika
5. Verifikasi baris seed 274 berada di tab History
6. Buka Wallet
7. Verifikasi Capture atas alokasi seed 274 tampil pada Wallet (anchor)
8. Verifikasi Balance kantong tidak dikembalikan (tanpa refund)
9. Buka Allocation > License Allocation, klik tab `Current`
10. Buka Changelog, cari entri dengan Allocation ID seed 274
11. Verifikasi Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
12. Tutup modal Changelog
13. Buka Activity Log, cari entri dengan Allocation ID seed 274
14. Verifikasi Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
15. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 274, tekan Enter
16. Buka Allocation Log seed 274
17. Verifikasi entri `Allocation expired` dengan `Reason: Subscription canceled`
18. Tutup modal Allocation Log
19. Pulihkan term Bengkel Cahaya Motor lewat fixture backend hingga tersimpan

### TC-AC-LA-275: Cancel term, alokasi Pending menjadi Expired seketika dengan Release Reserve

20. Catat Balance kantong Distributor PT Maju Bersama (dibaca lewat kemampuan baca saldo kantong)
21. Cancel Subscription pada term Pending `SUBS-20260819-00001` Toko Serba Ada yang memuat seed 275
22. Tunggu aksi selesai (dialog pembatalan tertutup)
23. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 275, tekan Enter
24. Verifikasi alokasi Pending seed 275 `Expired` seketika
25. Buka Wallet
26. Verifikasi Reserve $3,650.00 dilepas (Release), Balance sama dengan Balance yang dicatat sebelum Cancel Subscription
27. Buka Allocation > License Allocation, klik tab `Current`
28. Buka Changelog, cari entri dengan Allocation ID seed 275
29. Verifikasi Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
30. Tutup modal Changelog
31. Buka Activity Log, cari entri dengan Allocation ID seed 275
32. Verifikasi Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
33. Pulihkan term Pending Toko Serba Ada dan seed alokasinya lewat fixture backend hingga tersimpan

### TC-AC-LA-397: Log Auto-Expire karena Cancel term pada alokasi Pending

34. Cancel term `SUBS-20260819-00001` Toko Serba Ada yang memuat seed 397
35. Tunggu aksi selesai (dialog pembatalan tertutup)
36. Buka Allocation > License Allocation, klik tab `Current`
37. Buka Changelog, cari entri dengan Allocation ID seed 397
38. Verifikasi entri tampil dengan Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
39. Tutup modal Changelog
40. Buka Activity Log, cari entri dengan Allocation ID seed 397
41. Verifikasi Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
42. Buka System Log, ketik Search Allocation ID seed 397, tekan Enter
43. Verifikasi empty state `No results found` tampil pada System Log (anchor)
44. Verifikasi tidak ada entri System Log untuk seed 397
45. Pulihkan term Pending Toko Serba Ada dan seed alokasinya lewat fixture backend hingga tersimpan

### TC-AC-LA-527: Event Allocation Log Allocation expired karena Cancel term

46. Atur tanggal acuan server uji 22 Dec 2026 (fixture waktu)
47. Cancel Subscription pada term Pending `SUBS-20260819-00001` Toko Serba Ada yang memuat seed 527
48. Tunggu aksi selesai (dialog pembatalan tertutup)
49. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 527, tekan Enter, lalu klik row action `Allocation Log` pada baris itu
50. Verifikasi judul `Allocation expired` tanpa `by [PIC]`
51. Verifikasi Description `Reason: Subscription canceled`
52. Verifikasi entri memuat Date & Time sesuai General Settings
53. Verifikasi baris judul berupa teks biasa, bukan badge
54. Tutup modal Allocation Log
55. Pulihkan term Pending Toko Serba Ada dan tanggal acuan server lewat fixture backend hingga tersimpan

### TC-AC-LA-276: Cancel term tidak memengaruhi alokasi Station dan Storage Client

56. Buka Subscription Detail > License Quota Klinik Harapan Bunda, lalu catat ledger Client sebagai baseline
57. Cancel Subscription FAMS Professional Klinik Harapan Bunda
58. Tunggu aksi selesai (dialog pembatalan tertutup)
59. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed Station, tekan Enter
60. Verifikasi alokasi Station tetap `Active` di tab Current
61. Ganti isi kotak search dengan Allocation ID seed Storage, tekan Enter
62. Verifikasi alokasi Storage tetap `Active` di tab Current
63. Buka Subscription Detail > License Quota Klinik Harapan Bunda
64. Verifikasi alokasi pada ledger term yang dibatalkan Expired sedangkan ledger Client sama dengan ledger Client yang dicatat sebelum Cancel Subscription

### TC-AC-LA-277: Station tetap Active tanpa job dan tanpa refund saat Client kehilangan semua Subscription Paid Active

65. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed Station, tekan Enter, lalu buka Allocation Log alokasi Station dan catat jumlah entri sebagai baseline
66. Tutup modal Allocation Log
67. Cancel Subscription SAMS Growth Klinik Harapan Bunda sehingga seluruh Subscription Paid Active Client di-Cancel
68. Tunggu aksi selesai (dialog pembatalan tertutup)
69. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed Station, tekan Enter, lalu buka Allocation Log alokasi Station
70. Verifikasi status alokasi Station tetap `Active` dan entri `Allocation created by [PIC]` (PIC = pelaku seed) Station tampil pada Allocation Log (anchor)
71. Verifikasi jumlah entri Allocation Log Station sama dengan baseline, tidak ada entri log baru
72. Tutup modal Allocation Log
73. Buka Wallet
74. Verifikasi Capture atas alokasi Station tampil pada Wallet (anchor)
75. Verifikasi tidak ada refund wallet
76. Pulihkan seluruh Subscription Klinik Harapan Bunda dan seed alokasinya lewat fixture backend hingga tersimpan

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC mengikuti pengelompokan Pre-setup: TC-AC-LA-397 dan TC-AC-LA-527 sebelum TC-AC-LA-276 dan TC-AC-LA-277 yang membatalkan seluruh Subscription Client.
- Langkah penghubung (S-03): langkah 3, 15, 23, 49, 59, 61 (tab dan Search untuk menemukan baris target, R-16; langkah 15 membuka List dari Activity Log lalu mengetik Search pada kotak yang kosong di halaman yang baru dimuat, tanpa `✕`, S-14), 6, 10, 13, 16, 25, 28, 31, 37, 40, 42 (termasuk Search Allocation ID di System Log), 63, 69, 73 (membuka surface), 19, 33, 45, 55, 76 (memulihkan term lewat fixture backend), 46 (tanggal acuan).
- Langkah 9, 27, dan 36 (membuka List tab Current sebelum membuka Changelog karena ikon Changelog hanya ada di tab Current, S-14), langkah 12, 30, dan 39 (menutup modal Changelog sebelum membuka Activity Log, S-09), langkah 20 (Catat baseline Balance kantong sebelum Cancel Subscription, S-12), serta langkah 65 dan 66 (membuka Allocation Log Station dan mencatat baseline jumlah entri, lalu menutup modalnya, sebelum Cancel Subscription, S-12), langkah 56 (membuka Subscription Detail > License Quota Klinik Harapan Bunda dan mencatat baseline ledger Client sebelum Cancel Subscription, S-12) adalah langkah penghubung.
- Langkah 2, 22, 35, 48, 58, dan 68 (Tunggu aksi selesai setelah Cancel Subscription yang hasilnya tidak diasersi langsung, sebelum membuka surface lain, 8b butir 8) serta langkah 18, 54, dan 72 (menutup modal Allocation Log sebelum membuka surface lain, S-09) adalah langkah penghubung tanpa Verifikasi. Langkah 7 dan 74 adalah anchor positif asersi tanpa refund pada langkah 8 dan 75 (entri Capture tampil pada Wallet yang sama, 8b butir 2).
- P-1: langkah 44 (tidak ada entri System Log) dan 71 (tidak ada entri log baru) berbaseline (S-12). Anchor positif langkah 44: langkah 43 (empty state `No results found` pada System Log setelah Search Allocation ID seed 397, pola spec 022 dan 072), karena anchor Changelog dan Activity Log (langkah 38, 41) berada di surface lain. Anchor positif langkah 71: langkah 70.
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu topik aksi (Cancel term) dengan dataset yang sama, tiap blok berdiri sendiri lewat pemulihan fixture, dan blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-274 sampai 277, 397, 527 tidak menyebut jalur Cancel Subscription (halaman dan akun); spec memakai Subscription Detail dengan Pre-setup #10 dan jalur halaman disediakan tim FE.
  - TC-AC-LA-275, 397, 527 memakai satu alokasi Pre-setup #46 pada satu-satunya term Pending Toko Serba Ada; Cancel term sekali memakai habis term itu sehingga setiap blok memulihkan term dan seed lewat fixture backend.
  - TC-AC-LA-274 Expected a menulis "(dalam transaksi Cancel)"; sifat transaksi tidak teramati di UI dan hanya status `Expired` yang diasersi.
  - TC-AC-LA-276 Expected b ("ledger Client tidak berubah") tidak menyebut cara pengamatan ledger; spec memakai Subscription Detail > License Quota.
  - TC-AC-LA-277 Precondition b menyebut seluruh Subscription Paid Active di-Cancel tanpa langkah; spec menyalinnya sebagai langkah 67 dan memakai Post Condition tanpa observasi tambahan.
