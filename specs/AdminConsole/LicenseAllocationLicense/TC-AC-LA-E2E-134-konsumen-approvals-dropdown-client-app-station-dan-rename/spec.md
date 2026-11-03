---
id: TC-AC-LA-E2E-134-konsumen-approvals-dropdown-client-app-station-dan-rename
title: "Konsumen Lain: Approvals, Dropdown Client Baru, Asset Control App dan Station, serta Rename Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-429
  - TC-AC-LA-430
  - TC-AC-LA-431
  - TC-AC-LA-528
  - TC-AC-LA-432
coverage:
  web: automated
---

# Konsumen Lain: Approvals, Dropdown Client Baru, Asset Control App dan Station, serta Rename Client

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Ganti akun ke Dewi Anggraini lalu Hendra Wijaya dilakukan eksplisit pada langkah di bawah; hook `after` mengembalikan sesi ke akun default suite. Flag Guided Tooltip diatur hook `before` suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (approver) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Hendra Wijaya | #1 | Total Control Principal | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Kafe Baru (Pre-setup #31; Client Active tanpa data Client Subscription), CV Mitra Sejati (Pre-setup #22; `SUBS-20260105-K2L3M`) dengan alokasi `Active` Asset Control App (Pre-setup #53, hanya dibaca), Klinik Harapan Bunda (Pre-setup #24) dengan alokasi `Active` Asset Control Station +2 dan Storage +50 GB `Client-wide` (Pre-setup #52, hanya dibaca), Require Approval for Allocation ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41 dan #42 bersama): empat alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41): `{idCancelA}` (TC-AC-LA-429), `{idApproveB}` dan `{idRejectC}` (TC-AC-LA-430), `{idRename}` (TC-AC-LA-528).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; pembuatan Subscription Paid untuk Client Kafe Baru oleh aktor admin Client (akun pelaku tidak disebut TC) dan penghapusannya untuk memulihkan Pre-setup #31; fixture backend untuk memulihkan nama Client Pre-setup #19.
- State global: nama Client `PT Sejahtera` (Pre-setup #19) diubah menjadi `PT Sejahtera Makmur` pada blok TC-AC-LA-528 dan dipulihkan lewat fixture backend di akhir blok dan di hook `after`; Subscription Paid Kafe Baru (Pre-setup #31) dibuat pada blok TC-AC-LA-431 dan dihapus di hook `after`; Last Updated dan entri audit trail Client berubah dan dicatat sebagai efek S-06 (pengecualian 2026-10-30, suite serial).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Approvals Tab Active (TC-AC-LA-429)

1. Buka Approvals > License Allocation Tab Active
2. Verifikasi baris alokasi `{idCancelA}` tampil di Tab Active
3. Verifikasi badge count Tab Active menghitung alokasi `{idCancelA}`
4. Catat badge count Tab Active sebagai `{nBadge}`
5. Buka Allocation > License Allocation (tab Current)
6. Ketik Search `{idCancelA}`, tekan Enter
7. Klik row action `Cancel Allocation` pada baris `{idCancelA}`
8. Klik `[Cancel Request]`
9. Verifikasi toast sukses: "Success, license allocation has been canceled."
10. Muat ulang halaman
11. Buka Approvals > License Allocation Tab Active
12. Verifikasi Tab Active tampil dengan sedikitnya satu baris alokasi lain
13. Verifikasi baris `{idCancelA}` tidak ada di Tab Active
14. Verifikasi badge count Tab Active berkurang satu terhadap `{nBadge}`

### Approvals Tab History (TC-AC-LA-430)

15. Klik `[Review]` pada alokasi `{idApproveB}`
16. Pilih Approve
17. Klik Submit
18. Klik `[Review]` pada alokasi `{idRejectC}`
19. Pilih Reject
20. Isi Rejection Reason `Kuota tidak sesuai`
21. Klik Submit
22. Tunggu aksi selesai (tombol Submit aktif kembali atau baris keputusan hilang dari Tab Active)
23. Buka Approvals > License Allocation Tab History
24. Verifikasi baris `{idApproveB}` tampil di Tab History dengan Decision `Approved`
25. Verifikasi baris `{idRejectC}` tampil di Tab History dengan Decision `Rejected`

### Client baru muncul di dropdown Client (TC-AC-LA-431)

26. Ganti akun: Logout dari Fajar Nugroho
27. Login sebagai Dewi Anggraini (`dewiFullLic`, password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`)
28. Buat Subscription Paid untuk Client `Kafe Baru` (kemampuan disediakan tim FE/BE) hingga Client Subscription tersimpan
29. Buka Allocation > License Allocation (tab Current)
30. Klik `[+ Allocation]`
31. Buka dropdown Client dan cari `Kafe Baru`
32. Verifikasi Client `Kafe Baru` muncul sebagai opsi setelah punya data Client Subscription
33. Klik `✕` pada form Allocate

### Rename Client tercermin di dropdown dan kolom Client (TC-AC-LA-528)

34. Buka Client Detail `PT Sejahtera`
35. Ubah nama Client menjadi `PT Sejahtera Makmur`
36. Klik `[Save]`
37. Tunggu aksi selesai (Client Detail kembali ke mode tampil)
38. Buka Allocation > License Allocation (tab Current)
39. Klik `[+ Allocation]`
40. Buka dropdown Client
41. Verifikasi opsi `Toko Serba Ada` tampil di dropdown Client
42. Verifikasi dropdown Client menampilkan opsi `PT Sejahtera Makmur`
43. Verifikasi dropdown Client tidak lagi menampilkan opsi `PT Sejahtera`
44. Klik `✕` pada form Allocate
45. Ketik Search `{idRename}`, tekan Enter
46. Verifikasi kolom Client pada baris `{idRename}` menampilkan `PT Sejahtera Makmur`
47. Pulihkan nama Client menjadi `PT Sejahtera` lewat fixture backend

### Konsumen Asset Control App dan Station (TC-AC-LA-432)

48. Ganti akun: Logout dari Dewi Anggraini
49. Login sebagai Hendra Wijaya (`totalControlLic`, password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`)
50. Buka Allocation > License Allocation (tab Current)
51. Verifikasi baris alokasi `Active` Asset Control App ke `SUBS-20260105-K2L3M` (Pre-setup #53) tampil di List
52. Buka Subscription Detail `SUBS-20260105-K2L3M`
53. Verifikasi status Asset Control App pada Subscription sesuai alokasi `Active` di List
54. Buka Allocation > License Allocation (tab Current)
55. Verifikasi baris alokasi `Active` Asset Control Station +2 `Client-wide` Klinik Harapan Bunda (Pre-setup #52) tampil di List
56. Buka Client Detail `Klinik Harapan Bunda`
57. Verifikasi kuota Station Client sesuai alokasi `Active` Asset Control Station +2 di List

## Notes

- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (fungsional) dengan topik sejenis (sinkronisasi modul ini ke modul konsumen), masing-masing memakai record seed sendiri dan berdiri sendiri. Panjang spec berasal dari lima TC dengan ganti akun dua kali (S-07) dan langkah baca dua modul konsumen.
- Langkah penghubung (S-03, R-16): langkah 5, 29, 38, 50, dan 54 (navigasi ke List), langkah 6 dan 45 (Search baris berdasarkan Allocation ID), langkah 10 (muat ulang), langkah 26 sampai 27 dan 48 sampai 49 (ganti akun), langkah 28 (membuat Subscription Paid), langkah 33 dan 44 (menutup form Allocate yang belum berisi pilihan Client sehingga tidak dirty), langkah 47 (memulihkan nama Client), langkah 22 dan 37 (menunggu aksi selesai, 8b.8).
- Langkah 43 dan 13 adalah asersi absence. Langkah 43 didahului anchor positif opsi pembanding pada dropdown yang sama (langkah 41 dan 42); langkah 13 didahului anchor toast sukses (langkah 9) dan Tab Active yang tampil dengan baris lain (langkah 12).
- TC-AC-LA-432 butir b ("Perilaku modul konsumen diuji pada TC modul pemiliknya") adalah pernyataan cakupan dan tidak diasersi; label Automation TC-AC-LA-432 adalah "Manual Only" dan spec tetap menuliskannya (hambatan teknis bukan alasan mengeluarkan TC).
- Temuan untuk QA:
  - TC-AC-LA-429 langkah 2 ("Cancel alokasi lalu muat ulang") tidak menyebut tempat atau akun pembatalan; spec membatalkan dari List dengan akun approver Fajar Nugroho.
  - TC-AC-LA-429 butir a ("badge count menghitungnya") tidak menyebut nilai badge; spec membandingkan badge sebelum dan sesudah pembatalan.
  - TC-AC-LA-431 tidak menyebut akun pelaku pembuatan Subscription (aktor admin Client), jenis Subscription Paid yang dibuat, maupun cara mencari Client di dropdown; spec memakai kemampuan "disediakan tim FE/BE" dan pencarian teks pada dropdown. Precondition TC mensyaratkan Client tanpa data Client Subscription; spec tidak mengasersi ketiadaan sebelum pembuatan karena tidak ada di Expected.
  - TC-AC-LA-528 tidak menyebut akun pelaku rename Client selain Pre-setup #4; spec memakai Dewi Anggraini.
  - TC-AC-LA-432 tidak menyebut halaman tempat status App dan kuota Station dibaca, nilai awal kuota, dan akun Principal yang membaca selain Pre-setup #1; Langkah Uji "Bandingkan dengan Allocation Log dan List" tidak memiliki Expected tentang Allocation Log sehingga Allocation Log tidak diasersi. Spec memakai Subscription Detail untuk status App dan Client Detail untuk kuota Station.
  - Pre-setup #52 dan #53 dipakai hanya dibaca; Pre-setup #53 (Active Asset Control App pada `SUBS-20260105-K2L3M`) juga menjadi pemblokir App kedua pada TC-AC-LA-520 (spec 128).
