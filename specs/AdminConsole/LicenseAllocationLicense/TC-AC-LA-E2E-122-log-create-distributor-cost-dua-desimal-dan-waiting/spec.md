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
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`
4. Pilih Target `SUBS-20260101-A1B2C`
5. Pilih Type `IT Inventory`
6. Isi Additional Quantity `3`
7. Klik `[Submit]`
8. Catat Allocation ID baris baru sebagai `{idIT}`
9. Pulihkan jam server dan jam browser ke waktu nyata
10. Klik ikon `Changelog` pada List
11. Ketik Search `{idIT}`, tekan Enter
12. Verifikasi Changelog memuat entri dengan Action `Create`, Field `Allocation Details`, Old Value `—`, New Value `Addon: IT Inventory to PT Sejahtera — Paid via wallet, Cost $6.58`
13. Verifikasi nominal Cost pada Changelog berformat `$[X,XXX.XX]` dengan dua desimal tetap (`$6.58`), bukan `$6.5753`
14. Tutup modal Changelog
15. Buka Detail User `Dewi Anggraini` > tab System Log
16. Ketik Search `{idIT}`, tekan Enter
17. Verifikasi System Log aktor memuat entri dengan New Value `Addon: IT Inventory to PT Sejahtera — Paid via wallet, Cost $6.58`
18. Verifikasi nominal Cost pada System Log berformat `$[X,XXX.XX]` dengan dua desimal tetap (`$6.58`), bukan `$6.5753`
19. Buka Activity Log Admin Console
20. Ketik Search `{idIT}`, tekan Enter
21. Verifikasi Activity Log memuat entri dengan New Value `Addon: IT Inventory to PT Sejahtera — Paid via wallet, Cost $6.58`, Modified By `Dewi A`
22. Verifikasi nominal Cost pada Activity Log berformat `$[X,XXX.XX]` dengan dua desimal tetap (`$6.58`), bukan `$6.5753`
23. Buka Allocation > License Allocation (tab Current)

### Cost 1.000 atau lebih dengan pemisah ribuan koma (TC-AC-LA-514)

24. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
25. Klik `[+ Allocation]`
26. Pilih Client `Toko Serba Ada`
27. Pilih Target `SUBS-20260819-00001`
28. Pilih Type `Concurrent User`
29. Isi Additional Quantity `10`
30. Klik `[Submit]`
31. Catat Allocation ID baris baru sebagai `{idToko}`
32. Pulihkan jam server dan jam browser ke waktu nyata
33. Klik ikon `Changelog` pada List
34. Ketik Search `{idToko}`, tekan Enter
35. Verifikasi Changelog memuat entri dengan Action `Create`, Field `Allocation Details`, Old Value `—`, New Value `Concurrent User +10 to Toko Serba Ada — Paid via wallet, Cost $3,650.00`
36. Verifikasi nominal Cost pada Changelog memakai pemisah ribuan koma dan dua desimal (`$3,650.00`), bukan `$3650.00`
37. Tutup modal Changelog
38. Buka Detail User `Dewi Anggraini` > tab System Log
39. Ketik Search `{idToko}`, tekan Enter
40. Verifikasi System Log aktor memuat entri dengan New Value `Concurrent User +10 to Toko Serba Ada — Paid via wallet, Cost $3,650.00`
41. Verifikasi nominal Cost pada System Log memakai pemisah ribuan koma dan dua desimal (`$3,650.00`), bukan `$3650.00`
42. Buka Activity Log Admin Console
43. Ketik Search `{idToko}`, tekan Enter
44. Verifikasi Activity Log memuat entri dengan New Value `Concurrent User +10 to Toko Serba Ada — Paid via wallet, Cost $3,650.00`, Modified By `Dewi A`
45. Verifikasi nominal Cost pada Activity Log memakai pemisah ribuan koma dan dua desimal (`$3,650.00`), bukan `$3650.00`
46. Buka Allocation > License Allocation (tab Current)

### Log Create saat Waiting for Approval (TC-AC-LA-387)

47. Setel Require Approval for Allocation ON (Pre-setup #38) lewat fixture backend
48. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
49. Klik `[+ Allocation]`
50. Pilih Client `PT Sejahtera`
51. Pilih Target `SUBS-20260101-A1B2C`
52. Pilih Type `Concurrent User`
53. Isi Additional Quantity `10`
54. Klik `[Submit]`
55. Catat Allocation ID baris baru sebagai `{idWait}`
56. Pulihkan jam server dan jam browser ke waktu nyata
57. Klik ikon `Changelog` pada List
58. Ketik Search `{idWait}`, tekan Enter
59. Verifikasi Changelog mencatat Action `Create` dengan New Value `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`, sama seperti kasus Completed
60. Tutup modal Changelog
61. Buka Detail User `Dewi Anggraini` > tab System Log
62. Ketik Search `{idWait}`, tekan Enter
63. Verifikasi System Log aktor requester `Dewi Anggraini` mencatat Action `Create` dengan New Value `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`
64. Buka Activity Log Admin Console
65. Ketik Search `{idWait}`, tekan Enter
66. Verifikasi Activity Log mencatat Action `Create` dengan New Value `Concurrent User +10 to PT Sejahtera — Paid via wallet, Cost $100.00`

## Notes

- Alasan di atas sekitar 35 langkah: ketiga blok satu topik (pencatatan Create Distributor Dewi Anggraini pada tiga surface), satu kelas harness fungsional, masing-masing memakai record hasil Submit sendiri sehingga berdiri sendiri. Tiga kali pengisian form Allocate adalah langkah yang diulang per kasus format Cost, dan blok baca-log berpola tidak dihitung pada ambang smell.
- Langkah penghubung (S-03, R-16): langkah 1, 9, 24, 32, 47, 48, dan 56 (mengatur jam dan toggle), langkah 11, 16, 20, 34, 39, 43, 58, 62, dan 65 (Search entri berdasarkan Allocation ID), langkah 14, 37, dan 60 (menutup modal Changelog), langkah 23 dan 46 (kembali ke List).
- TC-AC-LA-512 butir d dan TC-AC-LA-514 butir d memakai satu `Verifikasi` format nominal per surface (langkah 13, 18, 22, 36, 41, dan 45).
- Temuan untuk QA:
  - TC-AC-LA-387 tidak menyebut tanggal acuan server; spec memakai `22 Dec 2026` agar Cost `$100.00` sama dengan kasus Completed TC-AC-LA-383.
  - TC-AC-LA-387 Expected butir a hanya berbunyi "sama seperti kasus Completed" dan tidak menyebut Modified By; spec tidak mengasersi Modified By pada blok ini.
  - TC-AC-LA-512 dan TC-AC-LA-514 tidak menyebut cara menemukan entri di tiga surface; spec memakai Search dengan Allocation ID unik.
  - TC-AC-LA-514 mensyaratkan Toko Serba Ada tanpa menyebut bahwa Target yang dipilih adalah term Pending; spec memakai `SUBS-20260819-00001` sesuai Langkah Uji TC.
