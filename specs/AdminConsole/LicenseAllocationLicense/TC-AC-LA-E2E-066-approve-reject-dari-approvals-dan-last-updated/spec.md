---
id: TC-AC-LA-E2E-066-approve-reject-dari-approvals-dan-last-updated
title: "Approve dan Reject dari Approvals: Reject, Last Updated, Tanpa Inline, dan Notifikasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-259
  - TC-AC-LA-260
  - TC-AC-LA-248
  - TC-AC-LA-262
coverage:
  web: automated
---

# Approve dan Reject dari Approvals: Reject, Last Updated, Tanpa Inline, dan Notifikasi

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho (akun pertama); halaman License Allocation dibuka hook `beforeEach` suite (tab Current). Ganti akun ke Dewi Anggraini dilakukan eksplisit pada langkah 52 dan 53; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (approver) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update (requester, pengamat notifikasi Reject) | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: PT Sejahtera (Pre-setup #19), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34), Require Approval ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before` oleh requester Dewi Anggraini; tidak memakai baris Pre-setup #41 dan #42 bersama): empat alokasi `Waiting for Approval` Concurrent User ke `SUBS-20260101-A1B2C` PT Sejahtera: `{idInline}` (+5, Cost $150.00), `{idNotif}` (+5, Cost $150.00; menghasilkan notifikasi `Waiting for your approval` ke Fajar Nugroho yang belum dibaca), `{idApprove}` (+5, Cost $150.00), `{idReject}` (+10, Cost $300.00).
- Data uji: Rejection Reason `Kuota tidak sesuai`.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, kemampuan membaca saldo kantong (Balance, Reserved), kuota term, entri Allocation Log (waktu entri terbaru), jumlah entri Changelog modul (baseline dicatat di hook `before`), serta status Read/Unread notifikasi.
- State global: saldo kantong dan kuota berubah akibat Approve dan Reject; dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Approve dan Reject hanya dari Approvals (tanpa tombol inline)

1. Ketik Search `{idInline}`, tekan Enter
2. Klik menu `⋯` pada baris `Waiting for Approval`
3. Verifikasi menu baris menampilkan row action `Allocation Log`
4. Verifikasi tidak ada tombol Approve, Reject, atau `[Review]` pada menu baris
5. Verifikasi tidak ada tombol Approve, Reject, atau `[Review]` pada baris List
6. Klik row action `Allocation Log`
7. Verifikasi modal Allocation Log menampilkan entri riwayat record
8. Verifikasi tidak ada tombol Approve, Reject, atau `[Review]` pada modal Allocation Log
9. Tutup modal Allocation Log
10. Buka Approvals > License Allocation
11. Verifikasi `[Review]` tersedia pada alokasi `{idInline}` (keputusan hanya dapat diambil dari Approvals > License Allocation)

### Notifikasi Waiting for your approval

12. Buka daftar notifikasi in-app
13. Klik tombol `[Detail]` pada notifikasi `Waiting for your approval` untuk `{idNotif}`
14. Verifikasi `[Detail]` membuka Detail Approval alokasi `{idNotif}`
15. Pilih Approve
16. Keluar dari Detail Approval tanpa Submit
17. Kembali ke daftar notifikasi
18. Verifikasi notifikasi tetap Unread
19. Klik tombol `[Detail]` pada notifikasi `Waiting for your approval` untuk `{idNotif}`
20. Pilih Approve
21. Klik Submit
22. Kembali ke daftar notifikasi
23. Verifikasi notifikasi menjadi Read

### Approve dan Reject, Last Updated, dan Allocation Log

24. Buka Allocation > License Allocation
25. Ketik Search `{idApprove}`, tekan Enter
26. Catat Last Updated `{idApprove}` pada List sebagai baseline
27. Ganti isi kotak search dengan `{idReject}`, tekan Enter
28. Catat Last Updated `{idReject}` pada List sebagai baseline
29. Buka Approvals > License Allocation
30. Klik `[Review]` pada alokasi `{idApprove}`
31. Pilih Approve
32. Klik Submit
33. Klik `[Review]` pada alokasi `{idReject}`
34. Pilih Reject
35. Isi Rejection Reason `Kuota tidak sesuai`
36. Klik Submit
37. Verifikasi toast sukses: "Success, transaction has been rejected."
38. Verifikasi Status `{idReject}` menjadi `Rejected`
39. Verifikasi kuota term tidak berubah
40. Verifikasi Reserved turun `$300.00`
41. Verifikasi Balance kantong tidak berubah
42. Buka Allocation > License Allocation
43. Ketik Search `{idApprove}`, tekan Enter
44. Verifikasi Last Updated `{idApprove}` berubah dari baseline menjadi waktu entri Allocation Log terbaru (Approve)
45. Klik tab `History`
46. Ketik Search `{idReject}`, tekan Enter
47. Verifikasi Last Updated `{idReject}` berubah dari baseline menjadi waktu entri Allocation Log terbaru (Reject)
48. Klik row action `Allocation Log`
49. Verifikasi Allocation Log memuat entri `Allocation rejected by Fajar N` dengan `Rejection Reason: Kuota tidak sesuai`
50. Tutup modal Allocation Log
51. Verifikasi Changelog modul tidak memuat entri baru untuk kedua alokasi: jumlah entri sama dengan baseline

### Pengamat requester

52. Ganti akun: Logout dari Fajar Nugroho
53. Login sebagai Dewi Anggraini (`dewiFullLic`, password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`)
54. Buka daftar notifikasi in-app
55. Verifikasi requester menerima notifikasi `License allocation rejected` untuk `{idReject}`

## Notes

- Alasan di atas sekitar 35 langkah: keempat TC satu topik (keputusan Approve dan Reject dari Approvals oleh Fajar Nugroho), kelas harness fungsional yang sama, tiap blok memakai record seed sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Reject pada langkah 33 sampai 36 menjalankan sekaligus aksi TC-AC-LA-248 dan aksi Reject TC-AC-LA-262 atas record `{idReject}`; Approve pada langkah 30 sampai 32 adalah aksi Approve TC-AC-LA-262. Expected TC-AC-LA-248 butir a sampai e dipenuhi pada langkah 37 sampai 41, 49, 51, dan 55; Expected TC-AC-LA-262 butir a pada langkah 44 dan 47, butir b pada langkah 51.
- Urutan blok berbeda dari urutan TC (259, 260, 262, 248): satu aksi Reject melayani TC-AC-LA-248 dan 262, dan pengamat requester dijalankan terakhir supaya ganti akun hanya sekali (S-07).
- Langkah penghubung (S-03, R-16): langkah 1 (Search untuk menemukan baris seed), langkah 9, 10, 24, 25, 27, 29, 42, 43, 45, 46, dan 50 (berpindah halaman, Search, pindah tab, dan menutup modal), langkah 12, 16, 17, 22, dan 54 (membuka notifikasi dan keluar dari Detail Approval), langkah 26 dan 28 (baseline Last Updated).
- Tidak ada asersi absence pada langkah 4, 5, dan 8 tanpa anchor: langkah 3 dan 7 adalah anchor positif pada surface yang sama (8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-260 langkah 2 ("Pilih Approve lalu Cancel/keluar tanpa Submit") tidak menyebut cara keluar; spec menulis "Keluar dari Detail Approval tanpa Submit". Butir c ("Setelah keputusan Submit: notifikasi menjadi Read") tidak punya langkah Submit di LK; langkah 19 sampai 23 menambahkannya sebagai langkah penghubung untuk butir c.
  - TC-AC-LA-248 butir e: requester menerima notifikasi `License allocation rejected`, tetapi akun requester tidak ada pada Precondition TC-AC-LA-248; spec memakai Dewi Anggraini (Pre-setup #4) sebagai requester seed (pengamat pada langkah 52 sampai 55).
  - TC-AC-LA-248 butir c dan TC-AC-LA-262 butir a menyebut saldo kantong, kuota, dan waktu entri Allocation Log tanpa menyebut cara membacanya; spec memakai kemampuan baca state BE dari tim FE/BE.
  - TC-AC-LA-259 butir b ("Keputusan hanya dapat diambil dari Approvals") adalah pernyataan; langkah 10 dan 11 mengamatinya lewat `[Review]` pada Approvals.
  - TC-AC-LA-262 butir a menyebut "kedua baris" tampil pada List tanpa menyebut tab; baris yang di-Reject berada di tab History (langkah 45 sampai 47).
