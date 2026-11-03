---
id: TC-AC-LA-E2E-071-edit-record-pending-toggle-off
title: "Edit Allocation Pending dengan Require Approval OFF: Tetap Pending atau Active dengan Capture"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-213
  - TC-AC-LA-215
  - TC-AC-LA-216
coverage:
  web: automated
---

# Edit Allocation Pending dengan Require Approval OFF: Tetap Pending atau Active dengan Capture

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Toko Serba Ada (Pre-setup #21; term Active `SUBS-20250201-J7K8L` End Date 31 Dec 2026 dan term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).
- Konfigurasi: Require Approval for Allocation OFF pada group Client uji (Pre-setup #39), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #46 bersama): tiga alokasi `Completed` berstatus lisensi `Pending`, Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini, Cost $3,650.00 di-Reserve (10 × $365 × 365 hari ÷ 365): `{idP4}` (TC-AC-LA-213), `{idP5}` (TC-AC-LA-215), `{idP6}` (TC-AC-LA-216). Tanggal submit pertama `{idP4}` diatur 25 Dec 2026 lewat fixture waktu.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture toggle Require Approval, fixture waktu untuk tanggal submit pertama, kemampuan membaca saldo kantong (Balance, Reserved, Available), ledger term, dan notifikasi Plan Owner (baseline jumlah notifikasi `License allocated` sebelum aksi).
- State global: toggle Require Approval OFF dipulihkan ke nilai awal di hook `after`; saldo kantong dikembalikan oleh pembersihan record seed. Pelaku Capture pada term Active mengubah Last Updated record seed saja, bukan baris Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit Pending (toggle OFF): Target ke term Active menjadi Active dengan Capture

1. Ketik Search `{idP4}`, tekan Enter
2. Klik row action `Edit` pada baris Pending
3. Ganti Target ke term Active `SUBS-20250201-J7K8L`
4. Pilih Type `Concurrent User`
5. Isi Additional Quantity `10`
6. Klik `[Save]`
7. Verifikasi toast sukses: "Success, license allocation has been updated."
8. Verifikasi tidak ada dialog D-04
9. Verifikasi Status menjadi `Active`
10. Verifikasi Reserve disesuaikan dari `$3,650.00` ke `$70.00` lalu di-Capture tepat `$70.00` (10 × $365 × 7 hari ÷ 365 = 70.0000, hari dihitung dari 25 sampai 31 Dec 2026 dengan kedua tanggal dihitung)
11. Verifikasi Balance kantong berkurang `$70.00`
12. Verifikasi Reserved turun total `$3,650.00` sehingga `$3,580.00` kembali ke Available
13. Verifikasi entri ledger pindah ke term Active dalam transaksi yang sama
14. Verifikasi kolom Cost menampilkan `$70.00`
15. Buka modal Changelog dari ikon Changelog pada Table Tools
16. Verifikasi baris Status Old `Pending` New `Active` dicatat pada entri `Edit` yang sama dengan perubahan lain atas `{idP4}`
17. Tutup modal Changelog

### Edit Pending (toggle OFF): hanya Quantity

18. Ganti isi kotak search dengan `{idP5}`, tekan Enter
19. Klik row action `Edit` pada baris Pending
20. Ubah hanya Additional Quantity menjadi `12`
21. Klik `[Save]`
22. Verifikasi Status lisensi tetap `Pending` tanpa kembali ke `Waiting for Approval`
23. Verifikasi Reserve disesuaikan dari `$3,650.00` menjadi `$4,380.00` (12 × $365 × 365 hari ÷ 365)
24. Verifikasi Capture tidak terjadi: Balance kantong tidak berkurang

### Edit Pending ke term yang sudah mulai: requester dari entitas Plan Owner

25. Ganti isi kotak search dengan `{idP6}`, tekan Enter
26. Klik row action `Edit` pada baris Pending
27. Ganti Target ke term Active `SUBS-20250201-J7K8L`
28. Klik `[Save]`
29. Verifikasi Status `Active` dengan Capture
30. Verifikasi tidak ada notifikasi `License allocated` ke Plan Owner karena entitas requester (PT Maju Bersama) sama dengan entitas Plan Owner

## Notes

- Langkah penghubung (S-03, R-16): langkah 1, 18, dan 25 (Search untuk menemukan baris seed), langkah 15 dan 17 (membuka dan menutup modal Changelog).
- Urutan toast sebelum asersi ketiadaan dialog D-04 pada langkah 7 dan 8: toast menjadi anchor bahwa penyimpanan selesai (8b butir 2 dan 11); urutan butir Expected TC-AC-LA-213 (a sebelum b) berubah karena alasan itu. Pada langkah 29 dan 30, Status `Active` menjadi anchor positif sebelum asersi ketiadaan notifikasi, dengan baseline notifikasi `License allocated` Plan Owner dicatat sebelum langkah 28.
- Edit Pending dengan toggle ON (D-04) ada di spec 058.
- Temuan untuk QA:
  - TC-AC-LA-213 menyebut tanggal submit pertama diatur 25 Dec 2026 tetapi tidak menyatakan apakah jam server juga diatur; spec hanya mengatur tanggal submit pertama record `{idP4}` (fixture waktu) karena faktor hari dihitung dari tanggal itu.
  - TC-AC-LA-213 butir c dan e, TC-AC-LA-215 butir b, serta TC-AC-LA-216 butir a menyebut Reserve, Balance, dan ledger tanpa menyebut halaman atau cara membacanya; langkah 10 sampai 13, 23, 24, dan 29 memakai kemampuan baca state BE yang disediakan tim FE/BE.
  - TC-AC-LA-215 menyebut "tanpa D-04" pada judul tetapi Expected hanya memuat butir a dan b; spec mengikuti Expected dan tidak mengasersi ketiadaan D-04 pada blok ini.
  - TC-AC-LA-216 butir b: akun penerima notifikasi Plan Owner tidak disebut; langkah 30 memakai kemampuan baca notifikasi Plan Owner yang disediakan tim FE.
  - TC-AC-LA-213 langkah 2 menyebut Target `SUBS-20250201-J7K8L` dengan End Date 31 Dec 2026 dan alokasi baru tetap masuk akal hanya bila tanggal acuan berada dalam masa term Active; TC tidak menyebut tanggal acuan server selain tanggal submit pertama.
