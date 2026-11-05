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
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture waktu untuk tanggal submit pertama, fixture harga untuk mengubah dan memulihkan Product Price Concurrent User, kemampuan membaca saldo kantong (Balance, Reserved, Available) Distributor PT Maju Bersama, menampilkan kolom Cost pada List lewat Setup Column (pemulihan preferensi kolom di hook `after`), kemampuan membaca batas SLA timeout alokasi, serta intercept jaringan (`Spectra.intercept()`) untuk menahan respons Save 5 detik.
- State global: Product Price Concurrent User diubah dari $365 menjadi $730 pada langkah 21 dan dipulihkan ke $365 pada langkah 29 serta di hook `after` sebagai cadangan; intercept dilepas pada langkah 48. Saldo kantong dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit Quantity: status tetap, SLA tidak di-reset, Reserve disesuaikan

1. Pastikan kolom Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Cost, lalu klik `[Save]`
2. Ketik Search `{idA}`, tekan Enter
3. Klik row action `Edit`
4. Ubah Additional Quantity dari `5` menjadi `10`
5. Catat baseline saldo Available dan Reserved kantong Distributor PT Maju Bersama
6. Klik `[Save]`
7. Verifikasi toast sukses: "Success, license allocation has been updated."
8. Verifikasi Status tetap `Waiting for Approval`
9. Verifikasi Cost pada List naik dari `$150.00` menjadi `$300.00` (harga snapshot transaksi pertama dan faktor hari dari tanggal Submit pertama)
10. Verifikasi Reserved kantong naik `$150.00` terhadap baseline langkah 5 (Reserve alokasi `{idA}` dari `$150.00` menjadi `$300.00`)
11. Verifikasi batas SLA timeout alokasi tidak berubah (tetap dihitung dari Submit pertama)

### Edit menurunkan Quantity

12. Ganti isi kotak search dengan `{idB}`, tekan Enter
13. Klik row action `Edit`
14. Ubah Additional Quantity dari `5` menjadi `2`
15. Catat baseline saldo Available dan Reserved kantong Distributor PT Maju Bersama
16. Klik `[Save]`
17. Verifikasi toast sukses: "Success, license allocation has been updated."
18. Verifikasi Reserved kantong turun `$90.00` terhadap baseline langkah 15 (Reserve alokasi `{idB}` dari `$150.00` menjadi `$60.00`)
19. Verifikasi Available pulih sebesar selisih (naik `$90.00` terhadap baseline langkah 15)

### Snapshot harga transaksi pertama

20. Ganti isi kotak search dengan `{idC}`, tekan Enter
21. Naikkan harga Concurrent User dari `$365` menjadi `$730` (fixture harga)
22. Klik row action `Edit`
23. Ubah Additional Quantity dari `5` menjadi `10`
24. Catat baseline saldo Available dan Reserved kantong Distributor PT Maju Bersama
25. Klik `[Save]`
26. Verifikasi toast sukses: "Success, license allocation has been updated."
27. Verifikasi Cost pada List `$300.00` (harga snapshot `$365`, bukan `$730`)
28. Verifikasi Reserved kantong naik `$150.00` terhadap baseline langkah 24 (Reserve alokasi `{idC}` `$300.00`, harga snapshot `$365`, bukan `$730`)
29. Pulihkan harga Concurrent User ke `$365` (fixture harga)

### Ganti Target ke term Pending

30. Ganti isi kotak search dengan `{idD}`, tekan Enter
31. Klik row action `Edit` pada baris milik Toko Serba Ada pada term Active
32. Ganti Target ke term Pending `SUBS-20260819-00001`
33. Pilih ulang Type `Concurrent User`
34. Catat baseline saldo Available dan Reserved kantong Distributor PT Maju Bersama
35. Klik `[Save]`
36. Verifikasi toast sukses: "Success, license allocation has been updated."
37. Verifikasi tanggal kedaluwarsa alokasi mengikuti End Date term Target baru (31 Dec 2027)
38. Verifikasi Cost pada List disesuaikan dari `$150.00` menjadi `$1,825.00` (5 × $365 × 365 ÷ 365, hari dihitung dari Start Date term baru)
39. Verifikasi Reserved kantong naik `$1,675.00` terhadap baseline langkah 34 (Reserve alokasi `{idD}` disesuaikan dari `$150.00` menjadi `$1,825.00`)

### Klik ganda Save

40. Ganti isi kotak search dengan `{idE}`, tekan Enter
41. Klik row action `Edit`
42. Ubah Additional Quantity dari `5` menjadi `6`
43. Catat baseline saldo Available dan Reserved kantong Distributor PT Maju Bersama
44. Tahan respons Save selama 5 detik (intercept)
45. Klik ganda cepat `[Save]`
46. Verifikasi `[Save]` loading setelah klik pertama
47. Verifikasi `[Save]` disabled setelah klik pertama
48. Lepas tahanan respons
49. Verifikasi toast sukses "Success, license allocation has been updated." tampil sekali
50. Buka modal Changelog dari ikon Changelog pada Table Tools
51. Verifikasi Changelog memuat tepat satu baris `Edit` untuk `{idE}` dengan Field `Additional Quantity` Old `5` New `6`
52. Verifikasi Reserved kantong naik `$30.00` sekali saja terhadap baseline langkah 43 (Reserve alokasi `{idE}` disesuaikan dari `$150.00` menjadi `$180.00`)
53. Tutup modal Changelog

## Notes

- Alasan di atas sekitar 35 langkah: kelima blok satu topik (Edit alokasi `Waiting for Approval` yang berhasil disimpan), memakai kelas harness fungsional yang sama (Edit pada form yang sama, seed `Waiting for Approval` milik Dewi Anggraini), tiap blok memakai record seed sendiri sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): langkah 1 (menampilkan kolom Cost lewat Setup Column, tanpa `Verifikasi`; kolom Cost tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 5, 15, 24, 34, 43 (baseline saldo kantong per blok), langkah 2, 12, 20, 30, dan 40 (Search untuk menemukan baris seed), langkah 21 dan 29 (mengubah dan memulihkan harga), langkah 50 dan 53 (membuka dan menutup modal Changelog).
- Langkah 44 sampai 48: respons ditahan sehingga toast belum muncul; toast diasersi sesudah respons dilepas (8b butir 11).
- TC-AC-LA-190 langkah 3 ("Amati selisih Reserve di section Payment") tidak punya Expected sendiri; diamati sebagai bagian langkah 4 sampai 6 tanpa `Verifikasi`.
- Temuan untuk QA:
  - TC-AC-LA-190 Post Condition ("Available berkurang sebesar selisih") tidak punya langkah observasi di TC; tidak diasersi (S-01, S-15).
  - TC-AC-LA-190, 191, 192, 193, 211, 214, dan 487 menulis "Reserve naik dari $150.00 menjadi $300.00" seolah satu reservasi di kantong; kantong yang sama menahan Reserve beberapa alokasi seed sehingga spec mengasersi selisih Reserved kantong terhadap baseline sebelum Save (Reserve alokasi disebut dalam kurung).
  - TC-AC-LA-190 butir d ("Batas SLA timeout tidak berubah") tidak menyebut tempat membaca batas SLA; langkah 11 memakai kemampuan baca state BE yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-AC-LA-190, 191, 192, 193, dan 487 menyebut Reserve dan Available kantong tanpa menyebut halaman atau cara membacanya; langkah 10, 18, 19, 28, 39, dan 52 memakai kemampuan baca saldo kantong yang disediakan tim FE/BE.
  - TC-AC-LA-193 butir b ("Tanggal kedaluwarsa mengikuti End Date term Target baru") tidak menyebut kolom atau permukaan tempat tanggal kedaluwarsa dibaca; langkah 37 mengasersi nilai tanggal tanpa menyebut kolom.
  - TC-AC-LA-193 butir c menyebut Cost `$1,825.00` memakai hari dari Start Date term baru (365 hari) sedangkan Pre-setup #21 menyatakan term Pending 1 Jan 2027 sampai 31 Dec 2027 (365 hari); konsisten, dicatat sebagai asumsi harga $365 per unit per tahun.
  - TC-AC-LA-487 butir b menyebut "satu baris `Edit` Field `Additional Quantity`" di Changelog tanpa menyebut cara menyaring baris; spec mengidentifikasi baris lewat Allocation ID `{idE}` (baseline nol karena record milik spec).
