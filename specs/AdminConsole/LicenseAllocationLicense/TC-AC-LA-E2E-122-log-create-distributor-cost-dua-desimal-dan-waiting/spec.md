---
id: TC-AC-LA-E2E-122-log-create-distributor-cost-dua-desimal-dan-waiting
title: "Log Create oleh Distributor di Tiga Surface: Cost Dua Desimal, Pemisah Ribuan, dan Waiting for Approval"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-512
  - TC-AC-LA-514
  - TC-AC-LA-387
coverage:
  web: automated
---

# Log Create oleh Distributor di Tiga Surface: Cost Dua Desimal, Pemisah Ribuan, dan Waiting for Approval

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`, 1 Jan 2027 sampai 31 Dec 2027), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34: Concurrent User $365 per unit per tahun, Addon IT Inventory $100 per unit per tahun), Require Approval for Allocation OFF (Pre-setup #39) untuk blok TC-AC-LA-512 dan TC-AC-LA-514, ON (Pre-setup #38) untuk blok TC-AC-LA-387.
- Data Dinamis: alokasi dikenali lewat Allocation ID unik hasil Submit (`{idIT}`, `{idToko}`, `{idWait}`); entri log milik ID itu berbaseline nol (S-12).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk jam server dan jam browser dengan nilai absolut; fixture backend untuk menyetel Require Approval for Allocation ON atau OFF; pemulihan baseline alokasi dan saldo kantong di hook `after`.
- State global: jam server dan jam browser diatur ke `24 Dec 2026` (blok TC-AC-LA-512) dan `22 Dec 2026` (blok TC-AC-LA-514 dan TC-AC-LA-387) lalu dipulihkan sebelum Changelog, System Log, atau Activity Log dibuka (S-09); toggle Require Approval for Allocation diubah ke ON pada blok ketiga dan dipulihkan ke OFF di hook `after`; saldo kantong #33 dipulihkan fixture backend.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Cost dua desimal hasil pembulatan half-up (TC-AC-LA-512)

1. Atur jam server dan jam browser ke `24 Dec 2026` (nilai absolut)
2. Catat baseline Allocation ID baris di halaman pertama tab Current
3. Klik `[+ Allocation]`
4. Pilih Client `PT Sejahtera`
5. Pilih Target `SUBS-20260101-A1B2C`
6. Pilih Type `IT Inventory`
7. Isi Additional Quantity `3`
8. Klik `[Submit]`
9. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idIT}`
10. Pulihkan jam server dan jam browser ke waktu nyata
11. Klik ikon `Changelog` pada List
12. Ketik Search `{idIT}`, tekan Enter
13. Verifikasi Changelog memuat entri dengan Action `Create`, Field `Allocation Details`, Old Value `—`, New Value `Addon: IT Inventory to PT Sejahtera — Paid via wallet, Cost $6.58`
14. Verifikasi nominal Cost pada Changelog berformat `$[X,XXX.XX]` dengan dua desimal tetap (`$6.58`), bukan `$6.5753`
15. Tutup modal Changelog
16. Buka Detail User `Dewi Anggraini` > tab System Log
17. Ketik Search `{idIT}`, tekan Enter
18. Verifikasi System Log aktor memuat entri dengan New Value `Addon: IT Inventory to PT Sejahtera — Paid via wallet, Cost $6.58`
19. Verifikasi nominal Cost pada System Log berformat `$[X,XXX.XX]` dengan dua desimal tetap (`$6.58`), bukan `$6.5753`
20. Buka Activity Log Admin Console
21. Ketik Search `{idIT}`, tekan Enter
22. Verifikasi Activity Log memuat entri dengan New Value `Addon: IT Inventory to PT Sejahtera — Paid via wallet, Cost $6.58`, Modified By `Dewi A`
23. Verifikasi nominal Cost pada Activity Log berformat `$[X,XXX.XX]` dengan dua desimal tetap (`$6.58`), bukan `$6.5753`
24. Buka Allocation > License Allocation (tab Current)

### Cost 1.000 atau lebih dengan pemisah ribuan koma (TC-AC-LA-514)

25. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
26. Catat baseline Allocation ID baris di halaman pertama tab Current
27. Klik `[+ Allocation]`
28. Pilih Client `Toko Serba Ada`
29. Pilih Target `SUBS-20260819-00001`
30. Pilih Type `Concurrent User`
31. Isi Additional Quantity `10`
32. Klik `[Submit]`
33. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idToko}`
34. Pulihkan jam server dan jam browser ke waktu nyata
35. Klik ikon `Changelog` pada List
36. Ketik Search `{idToko}`, tekan Enter
37. Verifikasi Changelog memuat entri dengan Action `Create`, Field `Allocation Details`, Old Value `—`, New Value `Concurrent User +10 to Toko Serba Ada — Paid via wallet, Cost $3,650.00`
38. Verifikasi nominal Cost pada Changelog memakai pemisah ribuan koma dan dua desimal (`$3,650.00`), bukan `$3650.00`
39. Tutup modal Changelog
40. Buka Detail User `Dewi Anggraini` > tab System Log
41. Ketik Search `{idToko}`, tekan Enter
42. Verifikasi System Log aktor memuat entri dengan New Value `Concurrent User +10 to Toko Serba Ada — Paid via wallet, Cost $3,650.00`
43. Verifikasi nominal Cost pada System Log memakai pemisah ribuan koma dan dua desimal (`$3,650.00`), bukan `$3650.00`
44. Buka Activity Log Admin Console
45. Ketik Search `{idToko}`, tekan Enter
46. Verifikasi Activity Log memuat entri dengan New Value `Concurrent User +10 to Toko Serba Ada — Paid via wallet, Cost $3,650.00`, Modified By `Dewi A`
47. Verifikasi nominal Cost pada Activity Log memakai pemisah ribuan koma dan dua desimal (`$3,650.00`), bukan `$3650.00`
48. Buka Allocation > License Allocation (tab Current)

### Log Create saat Waiting for Approval (TC-AC-LA-387)

49. Setel Require Approval for Allocation ON (Pre-setup #38) lewat fixture backend
50. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
51. Catat baseline Allocation ID baris di halaman pertama tab Current
52. Klik `[+ Allocation]`
53. Pilih Client `PT Sejahtera`
54. Pilih Target `SUBS-20260101-A1B2C`
55. Pilih Type `Concurrent User`
56. Isi Additional Quantity `10`
57. Klik `[Submit]`
58. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idWait}`
59. Pulihkan jam server dan jam browser ke waktu nyata
60. Klik ikon `Changelog` pada List
61. Ketik Search `{idWait}`, tekan Enter
62. Verifikasi Changelog mencatat Action `Create` dengan New Value `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`, sama seperti kasus Completed
63. Tutup modal Changelog
64. Buka Detail User `Dewi Anggraini` > tab System Log
65. Ketik Search `{idWait}`, tekan Enter
66. Verifikasi System Log aktor requester `Dewi Anggraini` mencatat Action `Create` dengan New Value `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`
67. Buka Activity Log Admin Console
68. Ketik Search `{idWait}`, tekan Enter
69. Verifikasi Activity Log mencatat Action `Create` dengan New Value `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`

## Notes

- Alasan di atas sekitar 35 langkah: ketiga blok satu topik (pencatatan Create Distributor Dewi Anggraini pada tiga surface), satu kelas harness fungsional, masing-masing memakai record hasil Submit sendiri sehingga berdiri sendiri. Tiga kali pengisian form Allocate adalah langkah yang diulang per kasus format Cost, dan blok baca-log berpola tidak dihitung pada ambang smell.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 25, 34, 49, 50, dan 59 (mengatur jam dan toggle), langkah 12, 17, 21, 36, 41, 45, 61, 65, dan 68 (Search entri berdasarkan Allocation ID), langkah 15, 39, dan 63 (menutup modal Changelog), langkah 24 dan 48 (kembali ke List), langkah 2, 26, dan 51 (mencatat baseline Allocation ID halaman pertama tab Current sebelum [Submit]; baris baru adalah baris yang tidak ada di baseline).
- TC-AC-LA-512 butir d dan TC-AC-LA-514 butir d memakai satu `Verifikasi` format nominal per surface (langkah 14, 19, 23, 38, 43, dan 47).
- Temuan untuk QA:
  - TC-AC-LA-387 tidak menyebut tanggal acuan server; spec memakai `22 Dec 2026` agar Cost `$100.00` sama dengan kasus Completed TC-AC-LA-383.
  - TC-AC-LA-387 Expected butir a hanya berbunyi "sama seperti kasus Completed" dan tidak menyebut Modified By; spec tidak mengasersi Modified By pada blok ini.
  - TC-AC-LA-512 dan TC-AC-LA-514 tidak menyebut cara menemukan entri di tiga surface; spec memakai Search dengan Allocation ID unik.
  - TC-AC-LA-514 mensyaratkan Toko Serba Ada tanpa menyebut bahwa Target yang dipilih adalah term Pending; spec memakai `SUBS-20260819-00001` sesuai Langkah Uji TC.
