---
id: TC-AC-LA-E2E-131-konsumen-wallet-reserve-capture-release
title: "Konsumen Wallet: Reserve, Capture, Release, dan Transaction History"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-427
  - TC-AC-LA-493
  - TC-AC-LA-494
  - TC-AC-LA-428
coverage:
  web: automated
---

# Konsumen Wallet: Reserve, Capture, Release, dan Transaction History

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Ganti akun ke Fajar Nugroho dilakukan eksplisit pada blok keputusan approver; hook `after` mengembalikan sesi ke akun default suite. Flag Guided Tooltip diatur hook `before` suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update (requester) | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (approver) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34), Require Approval for Allocation ON (Pre-setup #38) untuk TC-AC-LA-427, 493, dan 494, OFF (Pre-setup #39) untuk TC-AC-LA-428.
- Data Dinamis: alokasi dikenali lewat Allocation ID unik hasil Submit di spec ini: `{idApprove}` (TC-AC-LA-427), `{idReject}` (TC-AC-LA-493), `{idCancel}` (TC-AC-LA-494), `{idTx}` (TC-AC-LA-428).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk jam server dan jam browser dengan nilai absolut; fixture backend untuk menyetel Require Approval for Allocation ON atau OFF; kemampuan membaca Balance, Reserved, dan Available kantong Distributor PT Maju Bersama (TC tidak menyebut halamannya); pemulihan baseline alokasi dan saldo kantong di hook `after`.
- State global: jam server dan jam browser diatur ke `22 Dec 2026` selama keempat Submit dan dipulihkan sebelum ganti akun; toggle Require Approval for Allocation diubah ke OFF sebelum blok TC-AC-LA-428 dan dipulihkan di hook `after`; saldo kantong #33 dipulihkan fixture backend.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Reserve saat Submit, Release saat Cancel (TC-AC-LA-427 butir a, TC-AC-LA-493 butir a, TC-AC-LA-494)

1. Catat Balance, Reserved, dan Available kantong Distributor PT Maju Bersama sebagai baseline
2. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
3. Catat baseline Allocation ID baris di halaman pertama tab Current
4. Klik `[+ Allocation]`
5. Pilih Client `PT Sejahtera`
6. Pilih Target `SUBS-20260101-A1B2C`
7. Pilih Type `Concurrent User`
8. Isi Additional Quantity `10` (Cost `$100.00`)
9. Klik `[Submit]`
10. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idApprove}`
11. Verifikasi Reserved kantong naik `$100.00`
12. Verifikasi Available kantong turun `$100.00`
13. Verifikasi Balance kantong tetap
14. Catat baseline Allocation ID baris di halaman pertama tab Current
15. Klik `[+ Allocation]`
16. Pilih Client `PT Sejahtera`
17. Pilih Target `SUBS-20260101-A1B2C`
18. Pilih Type `Concurrent User`
19. Isi Additional Quantity `10` (Cost `$100.00`)
20. Klik `[Submit]`
21. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idReject}`
22. Verifikasi Reserved kantong naik `$100.00` terhadap pembacaan sebelumnya
23. Verifikasi Available kantong turun `$100.00` terhadap pembacaan sebelumnya
24. Verifikasi Balance kantong tetap
25. Catat baseline Allocation ID baris di halaman pertama tab Current
26. Klik `[+ Allocation]`
27. Pilih Client `PT Sejahtera`
28. Pilih Target `SUBS-20260101-A1B2C`
29. Pilih Type `Concurrent User`
30. Isi Additional Quantity `10` (Cost `$100.00`)
31. Klik `[Submit]`
32. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idCancel}`
33. Verifikasi Reserved kantong naik `$100.00` terhadap pembacaan sebelumnya
34. Verifikasi Available kantong turun `$100.00` terhadap pembacaan sebelumnya
35. Verifikasi Balance kantong tetap
36. Ketik Search `{idCancel}`, tekan Enter
37. Klik row action `Cancel Allocation` pada baris `{idCancel}`
38. Klik `[Cancel Request]`
39. Verifikasi Reserved kantong turun `$100.00`
40. Verifikasi Available kantong pulih `$100.00`
41. Verifikasi Balance kantong tidak berubah

### Transaction History untuk pemotongan alokasi (TC-AC-LA-428)

42. Setel Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend
43. Klik `(←)` pada kotak Search
44. Catat baseline Allocation ID baris di halaman pertama tab Current
45. Klik `[+ Allocation]`
46. Pilih Client `PT Sejahtera`
47. Pilih Target `SUBS-20260101-A1B2C`
48. Pilih Type `Concurrent User`
49. Isi Additional Quantity `10` (Cost `$100.00`)
50. Klik `[Submit]`
51. Catat Allocation ID baris yang tidak ada di baseline sebagai `{idTx}`
52. Pulihkan jam server dan jam browser ke waktu nyata
53. Buka Wallet > Transaction History
54. Verifikasi baris transaksi baru untuk alokasi `{idTx}` dengan nominal Cost `$100.00`

### Capture saat Approve dan Release saat Reject oleh approver (TC-AC-LA-427 butir b, TC-AC-LA-493 butir b)

55. Ganti akun: Logout dari Dewi Anggraini
56. Login sebagai Fajar Nugroho (`totalControlDistLic`, password `Spectra.env.AC_LA_TC_DIST_PASSWORD`)
57. Catat Balance, Reserved, dan Available kantong Distributor PT Maju Bersama sebagai baseline approver
58. Buka Approvals > License Allocation
59. Klik `[Review]` pada alokasi `{idApprove}`
60. Pilih Approve
61. Klik Submit
62. Verifikasi Reserved kantong turun `$100.00`
63. Verifikasi Balance kantong berkurang `$100.00`
64. Catat Balance, Reserved, dan Available kantong sebagai baseline Reject
65. Klik `[Review]` pada alokasi `{idReject}`
66. Pilih Reject
67. Isi Rejection Reason `Kuota tidak sesuai`
68. Klik Submit
69. Verifikasi Reserved kantong turun `$100.00`
70. Verifikasi Available kantong pulih
71. Verifikasi Balance kantong tidak berubah

## Notes

- Alasan di atas sekitar 35 langkah: seluruh blok satu topik (mutasi kantong Wallet akibat siklus alokasi), satu kelas harness fungsional, dan alokasi yang dibuat saling terpisah. Pengisian form Allocate empat kali adalah langkah yang diulang per TC dengan Cost yang sama ($100.00), dan tiga `Verifikasi` per pembacaan kantong (Reserved, Available, Balance) adalah klausa terpisah menurut S-01.
- Urutan berbeda dari sourceTc: ketiga Submit toggle ON dilakukan berturut-turut, Cancel dilakukan sebelum toggle diubah, lalu keputusan Approve dan Reject oleh Fajar Nugroho dilakukan terakhir agar ganti akun hanya satu kali (S-07).
- Langkah penghubung (S-03, R-16): langkah 2 dan 52 (mengatur dan memulihkan jam), langkah 36 (Search baris berdasarkan Allocation ID), langkah 42 (menyetel toggle), langkah 55 sampai 58 (ganti akun dan membuka Approvals), langkah 3, 14, 25, 43, dan 44 (membersihkan Search dan mencatat baseline Allocation ID halaman pertama tab Current sebelum [Submit]; baris baru adalah baris yang tidak ada di baseline).
- Temuan untuk QA:
  - TC-AC-LA-427, 493, dan 494 menyebut "catat kantong" tanpa menyebut halaman maupun cara membaca Balance, Reserved, dan Available; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-AC-LA-427 butir b ("Reserved turun $100.00 dan Balance berkurang $100.00") tidak menyebut Available; spec tidak mengasersi Available pada Approve.
  - TC-AC-LA-428 tidak menyebut kolom pengenal baris Transaction History (misalnya Allocation ID) dan menyebut Cost tanpa nilai; spec memakai Cost `$100.00` dengan jam `22 Dec 2026` dan mengenali baris lewat Allocation ID `{idTx}` bila UI menampilkannya.
  - TC-AC-LA-427 dan 493 menyebut Target tanpa nilai; spec memakai `SUBS-20260101-A1B2C` seperti TC-AC-LA-383.
