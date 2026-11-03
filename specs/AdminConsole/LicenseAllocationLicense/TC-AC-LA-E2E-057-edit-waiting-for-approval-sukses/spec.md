---
id: TC-AC-LA-E2E-057-edit-waiting-for-approval-sukses
title: "Edit Allocation Waiting for Approval: Quantity, Snapshot Harga, Ganti Target, dan Klik Ganda Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-190
  - TC-AC-LA-191
  - TC-AC-LA-192
  - TC-AC-LA-193
  - TC-AC-LA-487
coverage:
  web: automated
---

# Edit Allocation Waiting for Approval: Quantity, Snapshot Harga, Ganti Target, dan Klik Ganda Save

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (Pre-setup #4, Distributor PT Maju Bersama, Manage allocation Create+Read+Update); halaman dibuka hook `beforeEach` suite (tab Current).
- Akun: `dewiFullLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), Toko Serba Ada (Pre-setup #21; term Active `SUBS-20250201-J7K8L` dan term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34), Approval Timeout 3 hari (Pre-setup #40).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`, semuanya requester Dewi Anggraini, Concurrent User +5, Cost $150.00 di-Reserve, status `Waiting for Approval`; tidak memakai baris Pre-setup #41 bersama):
  - `{idA}` pada `SUBS-20260101-A1B2C` PT Sejahtera, tanggal submit pertama diatur 2 hari sebelum hari uji (fixture waktu) supaya SLA sudah berjalan;
  - `{idB}` pada `SUBS-20260101-A1B2C` PT Sejahtera;
  - `{idC}` pada `SUBS-20260101-A1B2C` PT Sejahtera, dibuat dengan harga $365;
  - `{idD}` pada term Active `SUBS-20250201-J7K8L` Toko Serba Ada (bentuk Pre-setup #61);
  - `{idE}` pada `SUBS-20260101-A1B2C` PT Sejahtera.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture waktu untuk tanggal submit pertama, fixture harga untuk mengubah dan memulihkan Product Price Concurrent User, kemampuan membaca saldo kantong (Balance, Reserved, Available) Distributor PT Maju Bersama, kemampuan membaca batas SLA timeout alokasi, serta intercept jaringan (`Spectra.intercept()`) untuk menahan respons Save 5 detik.
- State global: Product Price Concurrent User diubah dari $365 menjadi $730 pada langkah 18 dan dipulihkan ke $365 pada langkah 24 serta di hook `after` sebagai cadangan; intercept dilepas pada langkah 39. Saldo kantong dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit Quantity: status tetap, SLA tidak di-reset, Reserve disesuaikan

1. Ketik Search `{idA}`, tekan Enter
2. Klik row action `Edit`
3. Ubah Additional Quantity dari `5` menjadi `10`
4. Klik `[Save]`
5. Verifikasi toast sukses: "Success, license allocation has been updated."
6. Verifikasi Status tetap `Waiting for Approval`
7. Verifikasi Cost pada List naik dari `$150.00` menjadi `$300.00` (harga snapshot transaksi pertama dan faktor hari dari tanggal Submit pertama)
8. Verifikasi Reserve kantong naik dari `$150.00` menjadi `$300.00` dan Available berkurang sebesar selisih
9. Verifikasi batas SLA timeout alokasi tidak berubah (tetap dihitung dari Submit pertama)

### Edit menurunkan Quantity

10. Ganti isi kotak search dengan `{idB}`, tekan Enter
11. Klik row action `Edit`
12. Ubah Additional Quantity dari `5` menjadi `2`
13. Klik `[Save]`
14. Verifikasi toast sukses: "Success, license allocation has been updated."
15. Verifikasi Reserve kantong turun dari `$150.00` menjadi `$60.00`
16. Verifikasi Available pulih sebesar selisih

### Snapshot harga transaksi pertama

17. Ganti isi kotak search dengan `{idC}`, tekan Enter
18. Naikkan harga Concurrent User dari `$365` menjadi `$730` (fixture harga)
19. Klik row action `Edit`
20. Ubah Additional Quantity dari `5` menjadi `10`
21. Klik `[Save]`
22. Verifikasi toast sukses: "Success, license allocation has been updated."
23. Verifikasi Cost pada List dan Reserve kantong sama-sama `$300.00` (harga snapshot `$365`, bukan `$730`)
24. Pulihkan harga Concurrent User ke `$365` (fixture harga)

### Ganti Target ke term Pending

25. Ganti isi kotak search dengan `{idD}`, tekan Enter
26. Klik row action `Edit` pada baris milik Toko Serba Ada pada term Active
27. Ganti Target ke term Pending `SUBS-20260819-00001`
28. Pilih ulang Type `Concurrent User`
29. Klik `[Save]`
30. Verifikasi toast sukses: "Success, license allocation has been updated."
31. Verifikasi tanggal kedaluwarsa alokasi mengikuti End Date term Target baru (31 Dec 2027)
32. Verifikasi Cost pada List dan Reserve kantong sama-sama disesuaikan dari `$150.00` menjadi `$1,825.00` (5 × $365 × 365 ÷ 365, hari dihitung dari Start Date term baru)

### Klik ganda Save

33. Ganti isi kotak search dengan `{idE}`, tekan Enter
34. Klik row action `Edit`
35. Ubah Additional Quantity dari `5` menjadi `6`
36. Tahan respons Save selama 5 detik (intercept)
37. Klik ganda cepat `[Save]`
38. Verifikasi `[Save]` loading dan disabled setelah klik pertama
39. Lepas tahanan respons
40. Verifikasi toast sukses "Success, license allocation has been updated." tampil sekali
41. Buka modal Changelog dari ikon Changelog pada Table Tools
42. Verifikasi Changelog memuat tepat satu baris `Edit` untuk `{idE}` dengan Field `Additional Quantity` Old `5` New `6`
43. Verifikasi Reserve kantong disesuaikan sekali dari `$150.00` menjadi `$180.00`
44. Tutup modal Changelog

## Notes

- Alasan di atas sekitar 35 langkah: kelima blok satu topik (Edit alokasi `Waiting for Approval` yang berhasil disimpan), memakai kelas harness fungsional yang sama (Edit pada form yang sama, seed `Waiting for Approval` milik Dewi Anggraini), tiap blok memakai record seed sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 17, 25, dan 33 (Search untuk menemukan baris seed), langkah 18 dan 24 (mengubah dan memulihkan harga), langkah 41 dan 44 (membuka dan menutup modal Changelog).
- Langkah 36 sampai 39: respons ditahan sehingga toast belum muncul; toast diasersi sesudah respons dilepas (8b butir 11).
- TC-AC-LA-190 langkah 3 ("Amati selisih Reserve di section Payment") tidak punya Expected sendiri; diamati sebagai bagian langkah 3 sampai 4 tanpa `Verifikasi`.
- Temuan untuk QA:
  - TC-AC-LA-190 butir d ("Batas SLA timeout tidak berubah") tidak menyebut tempat membaca batas SLA; langkah 9 memakai kemampuan baca state BE yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-AC-LA-190, 191, 192, 193, dan 487 menyebut Reserve dan Available kantong tanpa menyebut halaman atau cara membacanya; langkah 8, 15, 16, 23, 32, dan 43 memakai kemampuan baca saldo kantong yang disediakan tim FE/BE.
  - TC-AC-LA-193 butir b ("Tanggal kedaluwarsa mengikuti End Date term Target baru") tidak menyebut kolom atau permukaan tempat tanggal kedaluwarsa dibaca; langkah 31 mengasersi nilai tanggal tanpa menyebut kolom.
  - TC-AC-LA-193 butir c menyebut Cost `$1,825.00` memakai hari dari Start Date term baru (365 hari) sedangkan Pre-setup #21 menyatakan term Pending 1 Jan 2027 sampai 31 Dec 2027 (365 hari); konsisten, dicatat sebagai asumsi harga $365 per unit per tahun.
  - TC-AC-LA-487 butir b menyebut "satu baris `Edit` Field `Additional Quantity`" di Changelog tanpa menyebut cara menyaring baris; spec mengidentifikasi baris lewat Allocation ID `{idE}` (baseline nol karena record milik spec).
