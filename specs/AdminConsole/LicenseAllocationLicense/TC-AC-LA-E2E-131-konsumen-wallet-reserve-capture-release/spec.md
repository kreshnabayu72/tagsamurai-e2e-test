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
3. Klik `[+ Allocation]`
4. Pilih Client `PT Sejahtera`
5. Pilih Target `SUBS-20260101-A1B2C`
6. Pilih Type `Concurrent User`
7. Isi Additional Quantity `10` (Cost `$100.00`)
8. Klik `[Submit]`
9. Catat Allocation ID baris baru sebagai `{idApprove}`
10. Verifikasi Reserved kantong naik `$100.00`
11. Verifikasi Available kantong turun `$100.00`
12. Verifikasi Balance kantong tetap
13. Klik `[+ Allocation]`
14. Pilih Client `PT Sejahtera`
15. Pilih Target `SUBS-20260101-A1B2C`
16. Pilih Type `Concurrent User`
17. Isi Additional Quantity `10` (Cost `$100.00`)
18. Klik `[Submit]`
19. Catat Allocation ID baris baru sebagai `{idReject}`
20. Verifikasi Reserved kantong naik `$100.00` terhadap pembacaan sebelumnya
21. Verifikasi Available kantong turun `$100.00` terhadap pembacaan sebelumnya
22. Verifikasi Balance kantong tetap
23. Klik `[+ Allocation]`
24. Pilih Client `PT Sejahtera`
25. Pilih Target `SUBS-20260101-A1B2C`
26. Pilih Type `Concurrent User`
27. Isi Additional Quantity `10` (Cost `$100.00`)
28. Klik `[Submit]`
29. Catat Allocation ID baris baru sebagai `{idCancel}`
30. Verifikasi Reserved kantong naik `$100.00` terhadap pembacaan sebelumnya
31. Verifikasi Available kantong turun `$100.00` terhadap pembacaan sebelumnya
32. Verifikasi Balance kantong tetap
33. Ketik Search `{idCancel}`, tekan Enter
34. Klik row action `Cancel Allocation` pada baris `{idCancel}`
35. Klik `[Cancel Request]`
36. Verifikasi Reserved kantong turun `$100.00`
37. Verifikasi Available kantong pulih `$100.00`
38. Verifikasi Balance kantong tidak berubah

### Transaction History untuk pemotongan alokasi (TC-AC-LA-428)

39. Setel Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend
40. Klik `[+ Allocation]`
41. Pilih Client `PT Sejahtera`
42. Pilih Target `SUBS-20260101-A1B2C`
43. Pilih Type `Concurrent User`
44. Isi Additional Quantity `10` (Cost `$100.00`)
45. Klik `[Submit]`
46. Catat Allocation ID baris baru sebagai `{idTx}`
47. Pulihkan jam server dan jam browser ke waktu nyata
48. Buka Wallet > Transaction History
49. Verifikasi baris transaksi baru untuk alokasi `{idTx}` dengan nominal Cost `$100.00`

### Capture saat Approve dan Release saat Reject oleh approver (TC-AC-LA-427 butir b, TC-AC-LA-493 butir b)

50. Ganti akun: Logout dari Dewi Anggraini
51. Login sebagai Fajar Nugroho (`totalControlDistLic`, password `Spectra.env.AC_LA_TC_DIST_PASSWORD`)
52. Catat Balance, Reserved, dan Available kantong Distributor PT Maju Bersama sebagai baseline approver
53. Buka Approvals > License Allocation
54. Klik `[Review]` pada alokasi `{idApprove}`
55. Pilih Approve
56. Klik Submit
57. Verifikasi Reserved kantong turun `$100.00`
58. Verifikasi Balance kantong berkurang `$100.00`
59. Catat Balance, Reserved, dan Available kantong sebagai baseline Reject
60. Klik `[Review]` pada alokasi `{idReject}`
61. Pilih Reject
62. Isi Rejection Reason `Kuota tidak sesuai`
63. Klik Submit
64. Verifikasi Reserved kantong turun `$100.00`
65. Verifikasi Available kantong pulih
66. Verifikasi Balance kantong tidak berubah

## Notes

- Alasan di atas sekitar 35 langkah: seluruh blok satu topik (mutasi kantong Wallet akibat siklus alokasi), satu kelas harness fungsional, dan alokasi yang dibuat saling terpisah. Pengisian form Allocate empat kali adalah langkah yang diulang per TC dengan Cost yang sama ($100.00), dan tiga `Verifikasi` per pembacaan kantong (Reserved, Available, Balance) adalah klausa terpisah menurut S-01.
- Urutan berbeda dari sourceTc: ketiga Submit toggle ON dilakukan berturut-turut, Cancel dilakukan sebelum toggle diubah, lalu keputusan Approve dan Reject oleh Fajar Nugroho dilakukan terakhir agar ganti akun hanya satu kali (S-07).
- Langkah penghubung (S-03, R-16): langkah 2 dan 47 (mengatur dan memulihkan jam), langkah 33 (Search baris berdasarkan Allocation ID), langkah 39 (menyetel toggle), langkah 50 sampai 53 (ganti akun dan membuka Approvals).
- Temuan untuk QA:
  - TC-AC-LA-427, 493, dan 494 menyebut "catat kantong" tanpa menyebut halaman maupun cara membaca Balance, Reserved, dan Available; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-AC-LA-427 butir b ("Reserved turun $100.00 dan Balance berkurang $100.00") tidak menyebut Available; spec tidak mengasersi Available pada Approve.
  - TC-AC-LA-428 tidak menyebut kolom pengenal baris Transaction History (misalnya Allocation ID) dan menyebut Cost tanpa nilai; spec memakai Cost `$100.00` dengan jam `22 Dec 2026` dan mengenali baris lewat Allocation ID `{idTx}` bila UI menampilkannya.
  - TC-AC-LA-427 dan 493 menyebut Target tanpa nilai; spec memakai `SUBS-20260101-A1B2C` seperti TC-AC-LA-383.
