---
id: TC-AC-LA-E2E-121-log-create-distributor-concurrent-user-station-storage-addon
title: "Log Create oleh Distributor di Tiga Surface: Concurrent User, Station, Storage, dan Addon"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-383
  - TC-AC-LA-385
  - TC-AC-LA-386
coverage:
  web: automated
---

# Log Create oleh Distributor di Tiga Surface: Concurrent User, Station, Storage, dan Addon

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Bengkel Cahaya Motor (Pre-setup #23; FAMS Professional Paid Active, End Date 31 Dec 2026, belum punya Asset Control App), Klinik Harapan Bunda (Pre-setup #24), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34: Concurrent User $365 per unit per tahun, Addon Audit $365, Asset Control App flat $150, Asset Control Station $50.00 per Station, Storage $2 per GB), Require Approval for Allocation OFF (Pre-setup #39).
- Data Dinamis: alokasi tidak punya nama bebas, sehingga dikenali lewat Allocation ID unik hasil Submit di spec ini (`{idCU}`, `{idStation}`, `{idStorage}`, `{idAudit}`, `{idApp}`); entri log milik ID itu berbaseline nol (S-12).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk jam server dan jam browser dengan nilai absolut; pemulihan baseline alokasi, saldo kantong, dan record Asset Control App milik spec ini di hook `after`.
- State global: jam server dan jam browser diatur ke `22 Dec 2026` pada blok TC-AC-LA-383 dan TC-AC-LA-386, lalu dipulihkan sebelum Changelog, System Log, atau Activity Log dibuka (S-09); hook `after` memulihkan jam sebagai cadangan. Saldo kantong #33 berkurang akibat Submit dan dipulihkan fixture backend.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Log Create Concurrent User (TC-AC-LA-383)

1. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
2. Catat baseline Allocation ID baris di halaman pertama tab Current
3. Klik `[+ Allocation]`
4. Pilih Client `PT Sejahtera`
5. Pilih Target `SUBS-20260101-A1B2C`
6. Pilih Type `Concurrent User`
7. Isi Additional Quantity `10`
8. Klik `[Submit]`
9. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idCU}`
10. Pulihkan jam server dan jam browser ke waktu nyata
11. Klik ikon `Changelog` pada List
12. Ketik Search `{idCU}`, tekan Enter
13. Verifikasi Changelog memuat entri dengan Action `Create`, Allocation ID `{idCU}`, Field `Allocation Details`, Old Value `—`, New Value `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`, Modified By `Dewi A`
14. Tutup modal Changelog
15. Buka Detail User `Dewi Anggraini` > tab System Log
16. Ketik Search `{idCU}`, tekan Enter
17. Verifikasi System Log aktor memuat entri dengan Action `Create`, Object `License Allocation`, Name `{idCU}`, Field `Allocation Details`, Old `—`, New `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`
18. Buka Activity Log Admin Console
19. Ketik Search `{idCU}`, tekan Enter
20. Verifikasi Activity Log memuat entri dengan Action `Create`, Object `License Allocation`, Name `{idCU}`, Field `Allocation Details`, Old `—`, New `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`, Modified By `Dewi A`
21. Verifikasi teks New Value pada Changelog, System Log, dan Activity Log persis sama
22. Verifikasi teks New Value tidak menyisipkan status transaksi
23. Buka Allocation > License Allocation (tab Current)

### Log Create Asset Control Station dan Storage (TC-AC-LA-385)

24. Catat baseline Allocation ID baris di halaman pertama tab Current
25. Klik `[+ Allocation]`
26. Pilih Client `Klinik Harapan Bunda`
27. Pilih Target `Client-wide`
28. Pilih Type `Asset Control Station`
29. Isi Additional Quantity `10`
30. Klik `[Submit]`
31. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idStation}`
32. Catat baseline Allocation ID baris di halaman pertama tab Current
33. Klik `[+ Allocation]`
34. Pilih Client `Klinik Harapan Bunda`
35. Pilih Target `Client-wide`
36. Pilih Type `Storage`
37. Isi Additional Quantity `50`
38. Klik `[Submit]`
39. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idStorage}`
40. Klik ikon `Changelog` pada List
41. Ketik Search `{idStation}`, tekan Enter
42. Verifikasi Changelog untuk `{idStation}` memuat New Value `Asset Control Station +10 to Klinik Harapan Bunda — Paid via wallet, Cost $500.00`
43. Ganti isi kotak search dengan `{idStorage}`, tekan Enter
44. Verifikasi Changelog untuk `{idStorage}` memuat New Value `Storage +50 GB to Klinik Harapan Bunda — Paid via wallet, Cost $100.00`
45. Tutup modal Changelog
46. Buka Activity Log Admin Console
47. Ketik Search `{idStation}`, tekan Enter
48. Verifikasi Activity Log untuk `{idStation}` memuat New Value `Asset Control Station +10 to Klinik Harapan Bunda — Paid via wallet, Cost $500.00`
49. Ganti isi kotak search dengan `{idStorage}`, tekan Enter
50. Verifikasi Activity Log untuk `{idStorage}` memuat New Value `Storage +50 GB to Klinik Harapan Bunda — Paid via wallet, Cost $100.00`
51. Buka Allocation > License Allocation (tab Current)

### Log Create Addon dan Asset Control App tanpa angka (TC-AC-LA-386)

52. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
53. Catat baseline Allocation ID baris di halaman pertama tab Current
54. Klik `[+ Allocation]`
55. Pilih Client `PT Sejahtera`
56. Pilih Target `SUBS-20260101-A1B2C`
57. Pilih Type `Audit`
58. Isi Additional Quantity `30`
59. Klik `[Submit]`
60. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idAudit}`
61. Catat baseline Allocation ID baris di halaman pertama tab Current
62. Klik `[+ Allocation]`
63. Pilih Client `Bengkel Cahaya Motor`
64. Pilih Target term FAMS Professional Bengkel Cahaya Motor (`{targetBengkel}`)
65. Pilih Type `Asset Control App`
66. Klik `[Submit]`
67. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idApp}`
68. Pulihkan jam server dan jam browser ke waktu nyata
69. Klik ikon `Changelog` pada List
70. Ketik Search `{idAudit}`, tekan Enter
71. Verifikasi Changelog untuk `{idAudit}` memuat New Value `Addon: Audit to PT Sejahtera — Paid via wallet, Cost $300.00`
72. Ganti isi kotak search dengan `{idApp}`, tekan Enter
73. Verifikasi Changelog untuk `{idApp}` memuat New Value `Addon: Asset Control App to Bengkel Cahaya Motor — Paid via wallet, Cost $150.00`
74. Tutup modal Changelog
75. Buka Activity Log Admin Console
76. Ketik Search `{idAudit}`, tekan Enter
77. Verifikasi Activity Log untuk `{idAudit}` memuat New Value `Addon: Audit to PT Sejahtera — Paid via wallet, Cost $300.00`
78. Ganti isi kotak search dengan `{idApp}`, tekan Enter
79. Verifikasi Activity Log untuk `{idApp}` memuat New Value `Addon: Asset Control App to Bengkel Cahaya Motor — Paid via wallet, Cost $150.00`

## Notes

- Alasan di atas sekitar 35 langkah: seluruh blok satu topik (pencatatan Create oleh Distributor Dewi Anggraini), satu kelas harness fungsional, dan berdiri sendiri dengan record hasil Submit sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Lima kali pengisian form Allocate adalah langkah yang diulang per Type, dan blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung pada ambang smell.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 52, dan 68 (mengatur dan memulihkan jam), langkah 12, 16, 19, 41, 43, 47, 49, 70, 72, 76, dan 78 (Search untuk menemukan entri berdasarkan Allocation ID), langkah 14, 45, dan 74 (menutup modal Changelog), langkah 23 dan 51 (kembali ke List), langkah 2, 24, 32, 53, dan 61 (mencatat baseline Allocation ID halaman pertama tab Current sebelum [Submit]; baris baru adalah baris yang tidak ada di baseline).
- TC-AC-LA-383 butir d ("terlepas toggle ON atau OFF") hanya diasersi untuk toggle OFF di spec ini (langkah 21 dan 22); varian toggle ON ada di spec 122 (TC-AC-LA-387).
- Temuan untuk QA:
  - TC-AC-LA-383, 385, dan 386 tidak menyebut cara menemukan entri di Changelog, System Log, dan Activity Log; spec memakai Search dengan Allocation ID unik.
  - TC-AC-LA-385 tidak menyebut Target; spec memakai `Client-wide` sesuai TC-AC-LA-519. TC-AC-LA-385 juga tidak menyebut tanggal acuan server; spec tidak mengatur jam pada blok itu karena Cost Station dan Storage bukan prorata.
  - TC-AC-LA-386 tidak menyebut Target untuk Addon `Audit` (spec memakai `SUBS-20260101-A1B2C` seperti TC-AC-LA-383) dan Target Asset Control App pada Bengkel Cahaya Motor (ID Subscription term FAMS Professional tidak tertulis di Pre-setup #23). Label Type `Audit` untuk Addon mengikuti penulisan TC (TC-AC-LA-512 memakai Type `IT Inventory`).
  - TC-AC-LA-383 butir a mensyaratkan Modified By `Dewi A` pada Changelog dan Activity Log, sedangkan Expected butir b tidak menyebut Modified By pada System Log; spec mengikuti TC.
  - Pembuatan record Asset Control App pada Bengkel Cahaya Motor (Pre-setup #23, yang semula belum punya App) mengubah data Pre-setup bersama; pemulihannya lewat fixture backend yang disediakan tim FE/BE.
