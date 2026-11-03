---
id: TC-AC-LA-E2E-067-approve-reject-oleh-group-manager
title: "Approve dan Reject oleh Group Manager: Approve-only dan Scope Region Jawa"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-476
  - TC-AC-LA-477
  - TC-AC-LA-478
coverage:
  web: automated
---

# Approve dan Reject oleh Group Manager: Approve-only dan Scope Region Jawa

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Rian Hartono (akun pertama tabel "Role yang diuji"); halaman License Allocation dibuka hook `beforeEach` suite (tab Current), dan spec ini berpindah ke Approvals sebagai langkah pertama. Ganti akun ke Hadi Setiawan (langkah 31 dan 32) dan ke Dewi Anggraini sebagai pengamat requester (langkah 45 dan 46) dilakukan eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji:

| Role | Pre-setup | Email | Env password | Blok TC |
|---|---|---|---|---|
| Group Manager approve-only (Rian Hartono, tanpa Manage allocation, Distributor PT Maju Bersama) | #8 | `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_GM_APPROVE_PASSWORD` | TC-AC-LA-476, TC-AC-LA-477 |
| Group Manager + Manage allocation (Hadi Setiawan, scope Region Jawa) | #9 | `gmAllocLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_GM_ALLOC_PASSWORD` | TC-AC-LA-478 |
| Requester pengamat notifikasi (Dewi Anggraini, Distributor Create+Read+Update) | #4 | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` | TC-AC-LA-477 butir e |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: PT Sejahtera (Pre-setup #19) berada dalam scope group `Rian Hartono`; Hierarki group Region Jawa > Cabang Bandung > Gudang Cimahi dengan Client Gudang Cimahi Retail (FAMS Professional Paid Active) di level ke-3 dan Group Manager `gmAllocLic` di-assign pada Region Jawa (Pre-setup #32); kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33); Product Price Concurrent User $365 per unit per tahun (Pre-setup #34); Require Approval ON (Pre-setup #38), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before` oleh requester Dewi Anggraini, status `Waiting for Approval`; tidak memakai baris Pre-setup #41, #42, dan #64 bersama): `{idRH1}` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, Cost $150.00 di-Reserve; `{idRH2}` Concurrent User +10 ke `SUBS-20260101-A1B2C` PT Sejahtera, Cost $300.00 di-Reserve; `{idHS}` Concurrent User +2 ke term Active FAMS Professional Gudang Cimahi Retail, Cost $60.00 di-Reserve.
- Data uji: Approval Note `OK`; Rejection Reason `Kuota tidak sesuai`.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, kemampuan membaca saldo kantong (Balance, Reserved), kuota term, dan jumlah entri Changelog modul (baseline dicatat di hook `before`).
- State global: saldo kantong dan kuota berubah akibat Approve dan Reject; dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Rian Hartono (Group Manager approve-only): Approve

1. Buka Approvals > License Allocation
2. Klik `[Review]` pada alokasi Concurrent User PT Sejahtera `{idRH1}`
3. Pilih Approve
4. Isi Approval Note `OK`
5. Klik Submit
6. Verifikasi toast sukses: "Success, transaction has been approved."
7. Verifikasi alokasi `{idRH1}` `Completed` berstatus lisensi `Active`
8. Verifikasi kuota term bertambah 5
9. Verifikasi Reserve `$150.00` di-Capture tanpa hitung ulang: Balance berkurang `$150.00`
10. Buka Allocation > License Allocation
11. Ketik Search `{idRH1}`, tekan Enter
12. Klik row action `Allocation Log`
13. Verifikasi Allocation Log memuat entri `Allocation approved by Rian H` dengan `Approval Note: OK`
14. Tutup modal Allocation Log
15. Verifikasi Changelog modul tidak bertambah: jumlah entri sama dengan baseline

### Rian Hartono: Reject

16. Buka Approvals > License Allocation
17. Klik `[Review]` pada alokasi Concurrent User +10 PT Sejahtera `{idRH2}`
18. Pilih Reject
19. Isi Rejection Reason `Kuota tidak sesuai`
20. Klik Submit
21. Verifikasi toast sukses: "Success, transaction has been rejected."
22. Verifikasi Status `{idRH2}` menjadi `Rejected`
23. Verifikasi kuota term tidak berubah
24. Verifikasi Reserve alokasi dilepas: Reserved turun dan Balance tidak berubah
25. Buka Allocation > License Allocation
26. Klik tab `History`
27. Ketik Search `{idRH2}`, tekan Enter
28. Klik row action `Allocation Log`
29. Verifikasi Allocation Log memuat entri `Allocation rejected by Rian H` dengan `Rejection Reason: Kuota tidak sesuai`
30. Tutup modal Allocation Log

### Hadi Setiawan (Group Manager Region Jawa): Approve Client descendant level ke-3

31. Ganti akun: Logout dari Rian Hartono
32. Login sebagai Hadi Setiawan (`gmAllocLic`, password `Spectra.env.AC_LA_GM_ALLOC_PASSWORD`)
33. Buka Approvals > License Allocation
34. Klik `[Review]` pada alokasi Concurrent User Gudang Cimahi Retail `{idHS}`
35. Pilih Approve
36. Klik Submit
37. Verifikasi toast sukses: "Success, transaction has been approved."
38. Verifikasi alokasi `{idHS}` `Completed` berstatus lisensi `Active`
39. Verifikasi Client Gudang Cimahi Retail pada level ke-3 di bawah Region Jawa tercakup scope Group Manager beserta seluruh descendant-nya (alokasinya tampil di Approvals dan Approve berhasil)
40. Buka Allocation > License Allocation
41. Ketik Search `{idHS}`, tekan Enter
42. Klik row action `Allocation Log`
43. Verifikasi Allocation Log memuat entri `Allocation approved by Hadi S`
44. Tutup modal Allocation Log

### Pengamat requester untuk Reject

45. Ganti akun: Logout dari Hadi Setiawan
46. Login sebagai Dewi Anggraini (`dewiFullLic`, password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`)
47. Buka daftar notifikasi in-app
48. Verifikasi requester `Dewi Anggraini` menerima notifikasi `License allocation rejected` untuk `{idRH2}`

## Notes

- Alasan di atas sekitar 35 langkah: ketiga TC satu topik (keputusan Approve dan Reject oleh Group Manager), kelas harness Role Matrix (3a), tiap blok role memakai record seed sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); langkah tiap role berbeda (Approve dan Reject untuk Rian Hartono, Approve pada Client descendant untuk Hadi Setiawan).
- Langkah penghubung (S-03, R-16): langkah 1, 10, 16, 25, 33, dan 40 (berpindah halaman), langkah 11, 27, dan 41 (Search untuk menemukan baris seed), langkah 14, 30, dan 44 (menutup modal Allocation Log), langkah 26 (pindah tab), langkah 45 sampai 47 (ganti akun dan membuka notifikasi).
- Ganti akun ke Dewi Anggraini pada langkah 45 sampai 47 dijalankan terakhir untuk TC-AC-LA-477 butir e supaya ganti akun hanya dua kali.
- Temuan untuk QA:
  - TC-AC-LA-476 dan TC-AC-LA-477 memakai Pre-setup #8 yang didefinisikan "Group Manager Distributor PT Maju Bersama tanpa Manage allocation", tetapi langkah TC membuka Allocation > License Allocation dan row action `Allocation Log`; akses menu List untuk akun tanpa Manage allocation tidak dijelaskan di TC. Spec mengikuti TC.
  - TC-AC-LA-477 butir e menyebut requester `Dewi Anggraini` menerima notifikasi tetapi akun requester tidak ada di Precondition; spec memakai Pre-setup #4 sebagai pengamat (langkah 45 sampai 48).
  - TC-AC-LA-476 butir c, TC-AC-LA-477 butir c, dan TC-AC-LA-476 butir b menyebut saldo kantong dan kuota tanpa menyebut cara membacanya; spec memakai kemampuan baca state BE dari tim FE/BE.
  - TC-AC-LA-478 butir b adalah pernyataan scope tanpa langkah observasi; langkah 39 mengasersinya lewat tampilnya alokasi di Approvals dan keberhasilan Approve.
  - TC-AC-LA-477 langkah 3 membuka tab History "dan klik row action Allocation Log"; spec menulis tab History sebagai langkah penghubung.
